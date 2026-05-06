# Wolke AI website

Static HTML/CSS/JS website for Wolke AI, designed for Cloudflare Pages.

## Current design direction

This iteration moves away from the earlier dark template and toward a lighter, roomier B2B product-site feel:

- cream/off-white page background
- large crisp headlines
- clean numbered bubbles
- app-colored cyan/yellow/mint shadows
- operational dashboard mockup without fake customer logos
- no external runtime CDN dependencies
- bilingual German/English structure with German as default
- German copy uses the informal du form

## Pages

German is the default language. English lives under `/en/`.

```text
/
  index.html        German homepage
  product.html      German product page
  pricing.html      German pricing page
  legal.html        German legal page
  404.html          German 404
  en/
    index.html      English homepage
    product.html    English product page
    pricing.html    English pricing page
    legal.html      English legal page
    404.html        English 404
  robots.txt
  sitemap.xml       Includes hreflang alternates
  site.webmanifest
```

## Running locally

```bash
npm run start
```

Then open `http://localhost:8080`.

No build step is required for this static iteration.

## Cloudflare Pages

Recommended settings:

```text
Build command: npm run build
Build output directory: /
```

The build command is a no-op that confirms the static site is ready.

## Before production launch

Founder/legal input still needed:

- final public email address
- final phone number, or remove phone entirely
- legal entity name
- business address
- responsible person
- VAT ID / registration details if applicable
- privacy contact
- hosting/provider details
- final domain decision: `wolke.ai` or `www.wolke.ai`
- whether Google Analytics/Hotjar will be added later

The legal page currently contains launch-structure placeholders and must be reviewed before production use.
