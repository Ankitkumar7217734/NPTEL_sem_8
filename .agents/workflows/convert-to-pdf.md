---
description: Convert a markdown file to a styled PDF using Times New Roman font with black and blue colors
---

# Convert Markdown to Styled PDF

## Prerequisites

- Pandoc must be installed (`brew install pandoc`)
- wkhtmltopdf or a LaTeX engine for PDF output

## Steps

1. Identify the markdown file to convert.

2. Convert using Pandoc with the project CSS:

```bash
pandoc "<input_file>.md" -o "<output_file>.pdf" \
  --pdf-engine=wkhtmltopdf \
  --css=".agents/skills/markdown-styling/style.css" \
  --standalone \
  --metadata title="<document_title>"
```

3. Alternatively, convert to styled HTML first, then print to PDF:

```bash
pandoc "<input_file>.md" -o "<output_file>.html" \
  --css=".agents/skills/markdown-styling/style.css" \
  --standalone \
  --metadata title="<document_title>"
```

Then open the HTML in a browser and use Print → Save as PDF.

## Notes

- The CSS enforces **Times New Roman** font and **black + blue** color scheme.
- The CSS is located at `.agents/skills/markdown-styling/style.css`.
- For VS Code markdown preview, add the CSS path to `markdown.styles` in settings.
