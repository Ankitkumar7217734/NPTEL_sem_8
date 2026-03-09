---
name: Markdown Styling
description: Enforces Times New Roman font with black and blue color scheme for all markdown and document outputs
---

# Markdown Styling Skill

## Overview

This skill defines the standard styling rules for all documents created in this workspace. **Every markdown file and document must follow these rules.**

## Rules

### Font

- **Always use Times New Roman** as the primary font family.
- Fallback fonts: `Times New Roman, Times, serif`

### Colors

- **Only two colors are allowed:**
  - **Black** (`#000000`) — used for all body text, headings, table text, and general content
  - **Blue** (`#003399`) — used for headings, links, highlighted keywords, and emphasis accents

### Application

#### When Writing Markdown Files

- Use the companion CSS file located at `.agents/skills/markdown-styling/style.css` for rendering.
- When converting to PDF (via Pandoc, browser print, or any tool), always reference this CSS.

#### When Creating HTML or Web Pages

- Link the CSS or embed the styles directly.

#### CSS File Location

- **CSS file:** `.agents/skills/markdown-styling/style.css`

## CSS File Usage

### With VS Code Markdown Preview

Add to your VS Code `settings.json`:

```json
{
  "markdown.styles": [".agents/skills/markdown-styling/style.css"]
}
```

### With Pandoc (Markdown → PDF/HTML)

```bash
pandoc input.md -o output.pdf --css=.agents/skills/markdown-styling/style.css
pandoc input.md -o output.html --css=.agents/skills/markdown-styling/style.css --standalone
```

### With Browser Print-to-PDF

Convert markdown to HTML with the CSS linked, then open in browser and print to PDF.
