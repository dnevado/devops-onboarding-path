# STYLE_GUIDE — Visual & Markdown Standards

This repo uses a consistent, professional look for module docs: badges, icons, short metadata, and accessible diagrams.

Quick rules
- Icons: store in `assets/icons/` as SVG files (kebab-case).
- Badges: use Shields.io for status indicators and place them on top of `README.md` or module headers.
- Header metadata: show **Estimated**, **Points**, **Difficulty** under the title.

Header template (copy to module READMEs):

```markdown
![CI](https://img.shields.io/badge/CI-ready-blue) ![Grade](https://img.shields.io/badge/Grader-ready-brightgreen)

# Week X — Title

![Topic icon](../../assets/icons/git.svg)

- **Estimated:** 3–5 hours
- **Points:** 10
- **Difficulty:** Beginner

## Overview

...
```

Accessibility
- Provide useful `alt` text for images.
- Avoid color-only cues; pair with icons or text.

Color tokens (for diagrams)
- Primary: #0F62FE (blue)
- Accent/Success: #00B894 (green)
- Error: #E11D48 (red)

Additions
- Place SVG icons in `assets/icons/` and reference with relative paths from module files.
