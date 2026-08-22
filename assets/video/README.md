# Produktvideos

Aktuell liegt hier **kein** Video. Die Rechnungs-Sektion auf der Startseite läuft
bis auf Weiteres als reine CSS-Animation (`.invoice-loop` in `index.html`).

## Erwartete Dateien

| Datei | Zweck |
|---|---|
| `rechnung-aenderung.webm` | Primärquelle (VP9/AV1) |
| `rechnung-aenderung.mp4`  | Fallback (H.264) |
| `rechnung-aenderung-poster.webp` | Standbild: Ladefallback, Mobile, `prefers-reduced-motion` |

## Aufnahme

- 8–15 Sekunden, stummer Screencast aus der Wolke-Demo
- 1080p oder auf die UI zugeschnitten; Rechnungsbeträge müssen lesbar bleiben
- Ablauf: Abweichung sichtbar → Klick auf Bestätigen → Rechnung angepasst
- sauberer Anfang/Ende, damit der Loop nicht springt
- kein wandernder Mauszeiger, keine Kunden- oder Personendaten, nur Beispieldaten

## Einbau

`assets/video/` befüllen, dann in `index.html` den Block mit dem Kommentar
`VIDEO SLOT` (Sektion „Änderung prüfen. Rechnung sauber anpassen.") durch dieses
Markup ersetzen:

```html
<div class="product-loop reveal">
  <span class="demo-pill loop-pill">Demo mit Beispieldaten</span>
  <video
    class="product-loop-video"
    autoplay muted loop playsinline preload="metadata"
    poster="assets/video/rechnung-aenderung-poster.webp"
    aria-label="Demo: Rechnungsänderung in Wolke bestätigen">
    <source src="assets/video/rechnung-aenderung.webm" type="video/webm">
    <source src="assets/video/rechnung-aenderung.mp4" type="video/mp4">
  </video>
</div>
```

Dazu ans Ende von `css/index.css`:

```css
.product-loop-video { width: 100%; height: auto; border-radius: 22px; object-fit: contain; }
@media (prefers-reduced-motion: reduce) { .product-loop-video { display: none; }
  .product-loop:has(.product-loop-video) { background: var(--paper) url("../assets/video/rechnung-aenderung-poster.webp") center/contain no-repeat; min-height: 320px; } }
```

Die CSS-Animation kann danach entfernt werden (Block „Visual 3: Rechnung anpassen").
