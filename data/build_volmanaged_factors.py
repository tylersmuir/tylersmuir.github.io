"""
Build volatility-managed factor returns following Moreira & Muir (JF 2017).

For each factor f, the vol-managed return is:
    r^vm_{t+1} = (sigma^2_full / sigma^2_t) * r_{t+1}

where sigma^2_t is realized variance from daily returns within month t,
and sigma^2_full is the full-sample variance of the factor.

Data source: Ken French's data library (daily and monthly factor returns).
Output:
  - VolManagedFactors.csv: 6 factors (Mkt-RF, SMB, HML, RMW, CMA, Mom), 1963+
  - VolManagedFactors_Long.csv: 4 factors (Mkt-RF, SMB, HML, Mom), 1926+
"""

import pandas as pd
import numpy as np
import pandas_datareader.data as web
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


def build_volmanaged(daily_factors, monthly_factors, monthly_rf, factors, outpath):
    """Build vol-managed returns for a set of factors and save to CSV."""

    # Realized variance = sum of squared daily returns within each month
    ym = daily_factors.index.to_period("M")
    rv = daily_factors[factors].groupby(ym).apply(lambda x: (x**2).sum())
    rv.index = rv.index.to_timestamp()

    # Convert monthly index from PeriodIndex to Timestamp if needed
    if hasattr(monthly_factors.index, "to_timestamp"):
        monthly_factors.index = monthly_factors.index.to_timestamp()
        monthly_rf.index = monthly_rf.index.to_timestamp()

    # Align on common dates
    common_idx = monthly_factors.index.intersection(rv.index)
    mf = monthly_factors[factors].loc[common_idx].copy()
    rf = monthly_rf.loc[common_idx].copy()
    rv = rv[factors].loc[common_idx]

    # Use last month's RV to scale this month's return
    rv_lagged = rv.shift(1)

    # Full-sample variance for rescaling
    full_sample_var = mf.var()

    # Vol-managed return
    vm = (full_sample_var / rv_lagged) * mf

    # Drop first row (no lagged RV)
    vm = vm.dropna()
    mf = mf.loc[vm.index]
    rf = rf.loc[vm.index]

    # Rename and combine: RF, VM factors, then original factors
    vm_cols = {f: f + "_VM" for f in factors}
    vm = vm.rename(columns=vm_cols)

    out = pd.concat([rf, vm, mf], axis=1)
    out.index.name = "Date"
    out.index = out.index.strftime("%Y-%m")

    out.to_csv(outpath, float_format="%.6f")

    print(f"\nSaved {outpath}")
    print(f"  Shape: {out.shape}")
    print(f"  Date range: {out.index[0]} to {out.index[-1]}")
    print(f"  Columns: {list(out.columns)}")
    print(f"  Annualized Sharpe ratios (original → vol-managed):")
    for f in factors:
        sr_orig = out[f].mean() / out[f].std() * np.sqrt(12)
        sr_vm = out[f + "_VM"].mean() / out[f + "_VM"].std() * np.sqrt(12)
        print(f"    {f:6s}:  {sr_orig:.3f}  →  {sr_vm:.3f}")

    return out


# --- Pull data from Ken French's library ---

# 3-factor daily/monthly (back to 1926)
daily_3f = web.DataReader("F-F_Research_Data_Factors_daily", "famafrench", start="1926-07-01")[0]
monthly_3f = web.DataReader("F-F_Research_Data_Factors", "famafrench", start="1926-07-01")[0]

# 5-factor daily/monthly (back to 1963)
daily_5f = web.DataReader("F-F_Research_Data_5_Factors_2x3_daily", "famafrench", start="1963-07-01")[0]
monthly_5f = web.DataReader("F-F_Research_Data_5_Factors_2x3", "famafrench", start="1963-07-01")[0]

# Momentum daily/monthly (back to 1926)
daily_mom = web.DataReader("F-F_Momentum_Factor_daily", "famafrench", start="1926-07-01")[0]
monthly_mom = web.DataReader("F-F_Momentum_Factor", "famafrench", start="1926-07-01")[0]

# Convert from percent to decimal
for df in [daily_3f, monthly_3f, daily_5f, monthly_5f, daily_mom, monthly_mom]:
    df[:] = df / 100

# Rename momentum column
daily_mom = daily_mom.rename(columns={daily_mom.columns[0]: "Mom"})
monthly_mom = monthly_mom.rename(columns={monthly_mom.columns[0]: "Mom"})

# --- Build long-history file: Mkt-RF, SMB, HML, Mom (1926+) ---

daily_long = daily_3f.join(daily_mom[["Mom"]])
monthly_long = monthly_3f.join(monthly_mom[["Mom"]])

long_factors = ["Mkt-RF", "SMB", "HML", "Mom"]
build_volmanaged(daily_long, monthly_long[long_factors], monthly_long[["RF"]],
                 long_factors, "VolManagedFactors_Long.csv")

# --- Build 6-factor file: all six (1963+) ---

daily_6f = daily_5f.join(daily_mom[["Mom"]])
monthly_6f = monthly_5f.join(monthly_mom[["Mom"]])

all_factors = ["Mkt-RF", "SMB", "HML", "RMW", "CMA", "Mom"]
build_volmanaged(daily_6f, monthly_6f[all_factors], monthly_6f[["RF"]],
                 all_factors, "VolManagedFactors.csv")
