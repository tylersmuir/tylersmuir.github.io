# Tyler Muir - Academic Website

Professional academic website for Tyler Muir, Professor of Finance at UCLA Anderson.

## Hosting on GitHub Pages

### Initial Setup

1. Create a new repository on GitHub named `tylersmuir.github.io` (or any name if using a custom domain)

2. Initialize git and push:
```bash
cd "New Website"
git init
git add .
git commit -m "Initial website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/tylersmuir.github.io.git
git push -u origin main
```

3. Enable GitHub Pages:
   - Go to repository Settings > Pages
   - Set Source to "Deploy from a branch"
   - Select "main" branch and "/ (root)" folder
   - Click Save

### Custom Domain Setup (tylersmuir.com)

1. In your GitHub repository Settings > Pages, add `tylersmuir.com` as the custom domain

2. Add these DNS records at your domain registrar:
   - **A Records** (point to GitHub's IPs):
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```
   - **CNAME Record** (for www):
     ```
     www -> YOUR_USERNAME.github.io
     ```

3. Wait for DNS propagation (can take up to 48 hours, usually faster)

4. Enable "Enforce HTTPS" in GitHub Pages settings once the certificate is issued

## Recent Changes (March 2026)

- **Section reorganization**: Moved Central Banks ahead of Volatility. Moved "Financial Crises and Risk Premia" (QJE 2017) into Intermediaries section.
- **Leverage factor data extended**: Updated AEM_LevFactor.csv through 2025Q3. Fixed data.html labels (Monthly → Quarterly).
- **Slides added for 12 papers** (stored in `/slides/`):
  - Whatever It Takes (MFS Lecture 2025)
  - Do Intermediaries Matter (AFA 2019)
  - Financial Crises and Risk Premia (JMP/NBER AP SI 2014)
  - Hedging Risk Factors (NBER AP 2019)
  - Vol Expectations (Stanford 2021)
  - Long-Term Vol Timing
  - Market Volatility (ASU 2026)
  - Bank Fragility (Haddad-Hartman-Glaser-Muir)
  - Asset Purchase Rules Euro Area (SITE Oct 2025)
  - How Credit Cycles (FRIC 2015)
  - Intermediaries US/UK/Japan (Arrowstreet 2021)
  - Is Risk Mispriced (INET 2019)

## TODO — Papers Still Missing Slides

- Diverging Banking Sector (Kundu-Muir-Zhang) — check SHARE_Shohini_Jinyuan folder
- 1930: First Modern Crisis (Gorton-Laarits-Muir)
- Mobile Collateral vs Immobile Collateral (Gorton-Laarits-Muir)
- Aggregate External Financing (Eisfeldt-Muir)
- Intermediaries and Asset Prices (JEL survey, Haddad-Muir)
- Market Macrostructure (Tyler making slides himself)

## Other Pages Not Yet Built

- Teaching page
- Fun page

## Adding Your Profile Photo

Replace `images/profile.jpg` with your professional photo. Recommended:
- Format: JPG or PNG
- Size: At least 400x500 pixels
- Aspect ratio: Portrait orientation works best

## Updating Content

- Edit `index.html` to add/modify papers
- Edit `data.html` to update data downloads
- CSS styling is in `css/style.css`

## Features

- Expandable abstracts (click [abstract] to show/hide)
- Video presentation badges (pink)
- Press coverage badges (green)
- Slides/data badges (blue)
- Mobile responsive design
- Clean, professional typography
