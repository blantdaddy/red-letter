# Red Letter Gospels

A study app for the four Gospels in the King James Version, with the words of Jesus in red.

- `index.html` is the complete app in one file (Scripture text included). Open it in any browser.
- Host this folder on any static web host (for example GitHub Pages) and it becomes an installable phone app: open it on your phone and choose "Add to Home Screen". `manifest.webmanifest` and `sw.js` make it work offline once installed.
- `Red-Letter-Study-Guide.pdf` is the printable booklet: all 13 studies with Scripture, writing space, the Life of Christ harmony and the 89-day checklist.
- `source/` holds the build: `template.html` (layout and code), `content.js` (studies, chapter titles, plans, word help) and `build.py`, which merges them with the KJV text.

Scripture text: King James Version, public domain (from the open-bibles OSIS edition, which marks the words of Jesus and the translators' italics).
