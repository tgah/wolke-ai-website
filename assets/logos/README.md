# System-Logos (Anbindungs-Sektion)

Aktuell liegen hier **keine** Logodateien. Die Kacheln in der Sektion „Angebunden an
Ihre Warenwirtschaft und Datenquellen" zeigen bis dahin erkennbare Text-Platzhalter in
der Wolke-Hausschrift — bewusst **keine** nachgebauten Fremdlogos.

## Warum kein Logo im Repo

Offizielle Logodateien von Brückner (WinAB), GDI, Xentral und Qlik sind Marken der
jeweiligen Anbieter. Sie gehören von der offiziellen Presse-/Brand-Seite geholt oder
beim Anbieter angefragt — nicht aus einer Website gescraped und nicht nachgezeichnet.
Das ist eine Entscheidung von Wolke, nicht des Codes.

## Erwartete Dateien

| Datei | System |
|---|---|
| `brueckner-winab.svg` | Brückner WinAB |
| `gdi-business-line.svg` | GDI Business-Line |
| `xentral.svg` | Xentral |
| `qlik-sense.svg` | Qlik Sense |

SVG bevorzugt, sonst PNG/WebP mit mindestens 2× Höhe (Anzeigehöhe 22 px).
Helle Variante wählen — die Kacheln stehen auf dunklem Navy.

## Einbau

In `index.html` pro Kachel den Schriftzug durch das Bild ersetzen:

```html
<!-- vorher: fertiger Text-Platzhalter -->
<li class="int-tile">
  <span class="int-mark"><span class="int-brand">Brückner</span><strong>WinAB</strong></span>
  <span class="int-meta">Warenwirtschaft</span>
</li>

<!-- nachher: offizielles SVG -->
<li class="int-tile">
  <span class="int-mark"><img class="int-logo" src="./assets/logos/brueckner-winab.svg" alt="Brückner WinAB"></span>
  <span class="int-meta">Brückner · Warenwirtschaft</span>
</li>
```

`.int-logo` ist bereits gestylt (`max-height: 22px`). Die Stern-Kachel
(„Viele weitere Systeme") ist ein Wolke-eigenes Element und bleibt.

## Wichtig

Die Logos zeigen technische Anbindbarkeit, **keine** offizielle Partnerschaft.
Formulierungen wie „offizieller Partner" nur verwenden, wenn das vertraglich stimmt.
