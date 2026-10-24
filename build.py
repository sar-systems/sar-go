"""Builds tlv/index.html and invest/index.html from one template (run from the repo root)."""
WA = "https://wa.me/972584441005?text=Hi%20Sharon%2C%20we%20met%20at%20the%20Tel%20Aviv%20defense%20salon"
CAL = "https://calendly.com/sharon-sarsystem/30min"
MAIL = "sharon.sarsystem@gmail.com"
LJ = "https://www.linkedin.com/in/l%C3%A9a-jane-krief-2a06301b6/"

ICONS = {
  "call": '<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/>',
  "wa": '<path d="M12 2a10 10 0 0 0-8.6 15l-1.3 4.8 4.9-1.3A10 10 0 1 0 12 2zm5.2 13.8c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2.1 1-2.4c.3-.3.6-.3.8-.3h.6c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .6l-.4.6-.4.5c-.1.2-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.7-.1l2 1c.3.1.5.2.5.3.1.2.1.7-.1 1.2z"/>',
  "mail": '<path d="M3 5h18c.6 0 1 .4 1 1v12c0 .6-.4 1-1 1H3a1 1 0 0 1-1-1V6c0-.6.4-1 1-1zm9 7.2L4 7.3V17h16V7.3l-8 4.9zM4.6 7l7.4 4.6L19.4 7H4.6z"/>',
  "add": '<path d="M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zm0 2c-3.3 0-7 1.6-7 4v2h11.1A6 6 0 0 1 13 13.4 11 11 0 0 0 9 13zm9-1v3h3v2h-3v3h-2v-3h-3v-2h3v-3h2z"/>',
}
def icon(k): return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[k]}</svg>'

def page(title, eyebrow, primary2, docs):
    doc_rows = "".join(
        f'<a class="doc" href="../docs/{f}" target="_blank" rel="noopener"><span class="pdf">PDF</span><span class="dt">{n}</span><span class="dm">{m}</span></a>'
        for n, m, f in docs)
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="robots" content="noindex">
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<main>
  <div class="brand">SAR System</div>
  <p class="eyebrow">{eyebrow}</p>
  <h1>Vertical AI for systems engineering.</h1>
  <p class="lead">Multiplies the capacity of the engineers you already have. Runs fully air-gapped.</p>

  <section class="me">
    <div class="who">
      <div class="avatar" aria-hidden="true">SZ</div>
      <div><div class="name">Sharon Zerbib</div><div class="role">Co-founder &amp; CTO</div></div>
    </div>
    <div class="lines">
      <a href="tel:+972584441005">+972 58-444-1005</a>
      <a href="mailto:{MAIL}">{MAIL}</a>
    </div>
    <nav class="acts">
      <a href="tel:+972584441005">{icon("call")}<span>Call</span></a>
      <a href="{WA}" target="_blank" rel="noopener">{icon("wa")}<span>WhatsApp</span></a>
      <a href="mailto:{MAIL}?subject=SAR%20System">{icon("mail")}<span>Email</span></a>
      <a href="../sharon-zerbib.vcf">{icon("add")}<span>Save</span></a>
    </nav>
  </section>

  <a class="cta" href="{CAL}" target="_blank" rel="noopener">Book a 30-minute call</a>
  {primary2}

  <section class="block">
    <h2>Documents</h2>
    {doc_rows}
  </section>

  <section class="block">
    <h2>Team</h2>
    <a class="row" href="{LJ}" target="_blank" rel="noopener"><span>Léa-Jane Krief</span><span class="rm">CEO · LinkedIn</span></a>
    <a class="row" href="https://sar-system.com/?lang=en" target="_blank" rel="noopener"><span>sar-system.com</span><span class="rm">Website</span></a>
  </section>

  <footer>© SAR System</footer>
</main>
</body>
</html>
'''

ONE = ("One-pager", "1 page", "SAR-one-pager-public-v7-2026-10-23.pdf")
DECK = ("Introduction deck", "10 slides", "SAR_System_Introduction_v3_2026-10-23.pdf")

open("tlv/index.html", "w").write(page(
    "SAR System", "Defense · Aerospace · Complex systems",
    f'<a class="cta2" href="mailto:{MAIL}?subject=SAR%20System%20%E2%80%94%20Demo%20request">Request a demo</a>',
    [ONE, DECK]))
open("invest/index.html", "w").write(page(
    "SAR System — Investors", "For investors",
    '<a class="cta2" target="_blank" rel="noopener" href="https://wa.me/972584441005?text=Hi%20Sharon%2C%20could%20you%20send%20me%20the%20SAR%20System%20investor%20deck%3F">Ask for the investor deck</a>',
    [ONE]))
print("built")
