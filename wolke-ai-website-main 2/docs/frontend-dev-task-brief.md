# Wolke AI Website - Frontend Developer Task Brief

## Project goal

Build a fast, static, Cloudflare Pages-ready website for Wolke AI. The site should sell one clear promise: **the end of manual reporting** for warehouse-led FMCG wholesalers, importers, distributors, and other ERP-heavy businesses.

The buyer is usually a non-technical owner or operator. The site must feel familiar to warehouse businesses: ERP data, SKUs, batches, stock, expiry dates, purchase orders, customer orders, warehouse transfers, retailer deliveries, price lists, and operational dashboards.

## Brand direction

Use the existing pitch-deck direction as the starting point:

- Dark operational background: `#001020` / near-black navy
- Bright Wolke cyan: `#00C0F0`
- White text: `#FFFFFF`
- Warm alert/accent yellow from the pilot slide: `#FFC818`
- Neutral operational greys: `#D8DDE3`, `#89939E`, `#384850`

The design should feel like an operations dashboard and warehouse intelligence layer, not a generic AI chatbot or neon AI startup.

## Primary message

Preferred homepage headline:

> End manual reporting for your warehouse business.

Supporting line:

> Wolke AI connects to your ERP and operational tools so non-technical owners can ask questions, see risks, and understand their business reality without learning new software.

## Site structure for iteration 1

Required pages:

- `index.html` - homepage / landing page
- `product.html` - how Wolke AI works
- `pricing.html` - packages and what is included
- `legal.html` - Impressum, privacy policy, terms of use
- `404.html` - created, but needs visual review
- `robots.txt` - created, domain placeholder must be replaced
- `sitemap.xml` - created, domain placeholder must be replaced

## Global tasks

### 1. Navigation

Replace current navigation with:

- Home -> `/`
- How it works -> `/product.html`
- Pricing -> `/pricing.html`
- Legal -> `/legal.html`
- Contact -> `#contact` on homepage or a `mailto:` link once confirmed

Quality bar:

- All links work on desktop and mobile.
- Header is readable on dark background.
- Mobile menu opens, closes, and does not cover the whole page awkwardly.
- CTA is visible in the header: `Book an assessment`.

### 2. SEO metadata

Every HTML page needs:

- Unique `<title>`
- Unique `<meta name="description">`
- Canonical URL once domain is confirmed
- Open Graph title, description, URL, and image
- One clear H1
- Proper heading hierarchy: H1 -> H2 -> H3
- Descriptive image alt text

Quality bar:

- No page has empty meta description.
- No template OG tags remain.
- No placeholder URLs remain.
- Page title clearly includes Wolke AI and the target industry.

### 3. Remove template credibility risks

Remove or replace:

- Fake logos: Google, Microsoft, Adobe, Airbnb, Stripe, Reddit
- Lorem ipsum
- Fake testimonials
- Template social links
- Template address
- AI coding screenshots and copy
- Generic newsletter signup unless there is a real newsletter strategy

Quality bar:

- Nothing on the page implies false customers, false press, or false testimonials.
- Every claim is something the business can stand behind.

### 4. Visual language

Replace generic AI/coding visuals with warehouse and operational visuals:

- ERP table transformed into plain-language assistant answer
- SKU/batch movement cards
- Expiry-risk alert examples
- Warehouse transfer flow
- Customer order tracking card
- Owner dashboard summary

Quality bar:

- A warehouse/FMCG owner should recognize the problems visually within 5 seconds.
- No robot/brain/neon imagery unless heavily restrained.
- Icons should be practical: barcode, box, calendar, chart, warehouse, truck, checklist, alert.

## Homepage tasks: `index.html`

### Section 1 - Hero

Replace current generic hero with:

H1:

> End manual reporting for your warehouse business.

Subheadline:

> Wolke AI connects to your ERP and operational tools so non-technical owners can ask questions, see risks, and understand their business reality without learning new software.

Primary CTA:

> Book an AI warehouse assessment

Secondary CTA:

> See how it works

Hero visual:

- Use a mock dashboard/assistant layout.
- Show example question: `Which products need attention this week?`
- Show answer cards: expiry risk, slow-moving stock, order status, pricing pressure.

Quality bar:

- The first screen says who the site is for and what pain it removes.
- No generic AI wording like "AI-powered coding simplified" remains.

### Section 2 - Familiar operations strip

Replace brand-logo carousel with operational vocabulary chips:

- ERP data
- SKUs
- Batches
- Expiry dates
- Purchase orders
- Warehouse transfers
- Retailer deliveries
- Price lists
- Customer orders

Quality bar:

- This section builds familiarity, not fake trust.
- It should be readable and not move too fast if animated.

### Section 3 - Problem

Heading:

> Your ERP has the data. Your team still has to dig for the answer.

Copy direction:

Explain that owners and staff currently read ERP exports, spreadsheets, and predefined reports manually. Important signals are hidden inside tables: expiry risk, stock movement, pricing pressure, demand shifts, delayed deliveries.

Quality bar:

- Concrete warehouse language.
- No vague business-transformation language.

### Section 4 - Services / capabilities

Cards:

1. ERP-connected AI assistant
2. Inventory and expiry intelligence
3. SKU and batch movement tracking
4. Pricing and seasonal demand insight
5. B2B customer order visibility
6. AI integration and team enablement

Quality bar:

- Each card has a one-sentence explanation.
- Each card uses a practical icon.
- The copy makes clear that Wolke sits on top of existing systems, not replacing ERP.

### Section 5 - What we have achieved

Use concrete achievement cards:

- Natural-language questions over ERP data
- AI assistant for owner-level business querying
- SKU movement tracking
- Faster ERP/customer order visibility

Quality bar:

- No inflated numbers unless supplied and verified.
- Avoid saying "case study" unless there is a named case and permission.

### Section 6 - Use cases

Split into:

Current capabilities:

- Natural-language ERP querying
- SKU movement tracking
- Business intelligence summaries
- Customer order visibility

High-value use cases explored during assessment:

- Inventory expiry management
- Seasonal demand prediction
- Optimal pricing support
- Stock movement alerts

Quality bar:

- Be honest about what is current vs exploratory.
- Do not imply a feature is production-ready if it is only a promising wedge.

### Section 7 - How we work

Steps:

1. Map your workflow
2. Review ERP and data sources
3. Pick the first high-value reporting pain
4. Connect through APIs or safe exports
5. Build the assistant/tracking layer
6. Train your team and improve it

Quality bar:

- Must reassure users: `Your ERP remains the source of truth.`
- Must make the process feel low-friction for non-technical owners.

### Section 8 - Pricing teaser

Cards:

- AI Assessment
- Implementation Sprint
- Ongoing AI Partner

CTA to `/pricing.html`.

Quality bar:

- Do not use cheap SaaS monthly pricing unless pricing is confirmed.
- Sell business outcomes and scope, not seats.

### Section 9 - Contact

Create `id="contact"` section.

Needs confirmed content:

- Phone number
- Email address
- Optional appointment booking link
- City/service region

Quality bar:

- Contact options are visible without hunting.
- Use `tel:` and `mailto:` links once confirmed.

## Product page tasks: `product.html`

Content requires founder feedback before final build.

Recommended structure:

1. Hero: `How Wolke AI works`
2. The problem with manual reporting
3. Existing ERP remains the source of truth
4. Connection layer: APIs, exports, permissions
5. Intelligence layer: assistant, BI, alerts, summaries
6. Example workflows:
   - Expiry risk
   - SKU movement
   - Pricing pressure
   - Customer order visibility
7. Security and data handling
8. CTA: book assessment

Quality bar:

- This page should explain the product clearly to a non-technical business owner.
- Avoid technical jargon unless explained.
- Include at least one visual workflow diagram.

## Pricing page tasks: `pricing.html`

Content requires founder feedback before final build.

Recommended packages:

1. AI Assessment
2. Implementation Sprint
3. Ongoing AI Partner

Quality bar:

- Each package should say who it is for, what is included, typical timeline, and what the client receives.
- Prices can be `Custom quote` until actual numbers are approved.
- Include a clear note that pilots or first-partner discounts can be discussed if the founder wants to keep that pitch-deck idea.

## Legal page tasks: `legal.html`

Content requires founder/legal feedback before final build.

Required sections:

- Impressum
- Privacy Policy
- Terms of Use
- Contact
- Responsible party / legal entity
- Analytics and tracking note once Google Analytics and Hotjar are added

Quality bar:

- Do not invent legal entity, address, VAT ID, or responsible person.
- Use placeholders until confirmed.
- Once Google Analytics and Hotjar are added, update privacy/cookie wording and consent flow.

## Technical cleanup tasks

### Tailwind scripts

Current `package.json` scripts reference `tailwind.css` and `tailwind-build.css` in root, but the files are in `/css`. Confirm whether builds work. If not, update scripts to:

```json
"start:tailwind": "cross-env NODE_ENV=development tailwindcss --postcss -i ./css/tailwind.css -o ./css/tailwind-runtime.css -w",
"build:tailwind": "cross-env NODE_ENV=production tailwindcss --postcss -i ./css/tailwind.css -o ./css/tailwind-build.css --minify"
```

Quality bar:

- `npm install` works.
- `npm run build:tailwind` generates `/css/tailwind-build.css`.
- Cloudflare Pages build command is documented.

### External dependencies

Current page loads Bootstrap Icons and GSAP from CDN.

Quality bar:

- Keep if acceptable for iteration 1.
- Consider self-hosting later if privacy/performance policy requires it.
- No broken CDN integrity hashes.

### Performance

Quality bar:

- Images are optimized.
- No giant unused brand logos remain.
- Lighthouse should be strong on Performance, Accessibility, Best Practices, and SEO.

## Iteration 1 acceptance checklist

The website is ready for first launch when:

- All pages load on local server.
- All navigation links work.
- No Lorem ipsum remains.
- No fake logos/testimonials remain.
- Homepage clearly says: `the end of manual reporting`.
- Warehouse/FMCG/ERP audience is obvious.
- Basic SEO tags are present.
- `robots.txt` and `sitemap.xml` have the final domain.
- 404 page works.
- Contact details are correct.
- Cloudflare Pages deployment succeeds.
