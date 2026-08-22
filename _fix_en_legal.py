import re

path = "/Users/tanaygaherwar/Downloads/wolke-ai-website-github/en/legal.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = re.compile(r'<section class="section compact">.*?</section>', re.DOTALL)

new = (
    '<section class="section compact">'
    '<div class="container">'
    '<article class="legal-block reveal" id="impressum">'
    '<p class="eyebrow">Impressum</p>'
    '<h2>Impressum</h2>'
    '<p>Information pursuant to \u00a7 5 DDG</p>'
    '<p><strong>Wolke AI</strong></p>'
    '<p>Tanay Gaherwar Singh</p>'
    '<p>Sickingenstrasse 4</p>'
    '<p>Berlin 10553</p>'
    '<p>Deutschland</p>'
    '<h3>Contact</h3>'
    '<p>Email: <a href="mailto:singh@wolke-ai.de">singh@wolke-ai.de</a></p>'
    '<h3>VAT</h3>'
    '<p>VAT identification number pursuant to \u00a7 27a UStG: DE457795131</p>'
    '<h3>Responsible for content pursuant to \u00a7 18 Abs. 2 MStV</h3>'
    '<p>Tanay Gaherwar Singh, c/o Wolke AI, Sickingenstrasse 4, Berlin 10553</p>'
    '</article>'
    '<article class="legal-block reveal" id="privacy">'
    '<p class="eyebrow">Privacy</p>'
    '<h2>Privacy policy</h2>'
    '<p>This website does not use third-party analytics, marketing pixels, or tracking scripts. '
    'No Google Analytics, Hotjar, Meta Pixel, LinkedIn Insight Tag or comparable scripts are loaded.</p>'
    '<p>The site is delivered via Cloudflare Pages (Cloudflare, Inc., 101 Townsend St., '
    'San Francisco, CA 94107, USA). Cloudflare may process technical access data including '
    'IP addresses as a data processor for delivery, security, and performance purposes.</p>'
    '<p>Email is handled via Zoho Mail. When you contact us by email, we process your name, '
    'email address, company, message content, and communication metadata to handle your '
    'enquiry and prepare a possible engagement.</p>'
    '<p>For questions about data processing or to exercise your rights under GDPR, '
    'contact: <a href="mailto:singh@wolke-ai.de">singh@wolke-ai.de</a></p>'
    '</article>'
    '<article class="legal-block reveal" id="terms">'
    '<p class="eyebrow">Terms</p>'
    '<h2>Terms of use</h2>'
    '<p>The website content explains Wolke AI\'s services at a high level. It does not '
    'create a binding offer, guarantee a specific commercial outcome, or replace a signed '
    'service agreement.</p>'
    '<p>Service scope, data access, deployment model, responsibilities, pricing, support, '
    'and security requirements must be agreed in writing before any implementation work begins.</p>'
    '<p>German law applies. In case of conflict between the German and English versions of '
    'these legal pages, the German version takes precedence.</p>'
    '</article>'
    '</div>'
    '</section>'
)

result, count = old.subn(new, content, count=1)
if count == 0:
    print("ERROR: pattern not matched")
else:
    with open(path, "w", encoding="utf-8") as f:
        f.write(result)
    print("OK: replaced {} section(s)".format(count))
