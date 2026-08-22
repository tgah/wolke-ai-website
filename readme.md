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
- German copy uses the formal Sie form; `/en/` is still on the V1 copy
- German homepage is product-led (V3, August 2026): every capability is shown as a
  Wolke product screen next to its explanation — integration network, order intake,
  dispatch/route choice, return + invoice, Layer-2 signal cards, MHD item view.
  All animation is CSS; the only JavaScript is the menu and the reveal observer.
- restrained radii (buttons 10px, panels 16px), flat section labels instead of pills,
  headline scale roughly 30% below V2 so the product UI dominates
- system tiles carry text wordmarks until real logo files land — see
  `assets/logos/README.md`; the invoice section can be swapped for a real recording,
  see `assets/video/README.md`
- copy alternatives live in `docs/homepage-v2-copy-options.md`
- `python3 check.py` runs production acceptance checks (dead anchors, forbidden
  strings, contact address, nav, required content)
- `pricing.html` is reachable by direct URL but no longer linked from nav or footer

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
