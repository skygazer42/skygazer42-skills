# HTML PPT Generator

A Claude Code skill for creating interactive HTML presentations. Simply provide the theme, color scheme, and content to generate professional-looking PPT files.

> **Tip**: For creating more beautiful frontend interfaces, consider also installing the [frontend-design](https://github.com/anthropics/skills/tree/main/skills) skill.

## Features

- **8 Preset Color Schemes** - Cyberpunk, Business Blue, Dark Purple, Forest Green, etc.
- **Custom Colors** - Full control over color configuration
- **Rich Components** - Title slides, card lists, code blocks, timelines, statistics
- **Interactive** - Keyboard navigation, touch swipe, thumbnail view, fullscreen
- **Animations** - Particle effects, glassmorphism, elastic entrance animations
- **Zero Dependencies** - Pure local solution, no external CDN required

## Quick Start

### 1. Install

Copy the `html-ppt` skill folder to your Claude Code skills directory:

```
.claude/skills/html-ppt/
├── SKILL.md                 # Skill documentation
├── README.md                # Chinese documentation
├── README_EN.md             # English documentation
├── templates/
│   ├── base_template.html   # Base template
│   └── color_schemes.json   # Color scheme config
```

### 2. Usage

Invoke this skill in Claude Code:

```
/html-ppt
```

Then provide:
1. **Color Scheme** - Choose from presets or customize
2. **Theme** - Presentation title
3. **Content** - Slide titles, content types, specific content

### 3. Output

The generated PPT is a standalone `.html` file that can be opened directly in any browser.

## Color Schemes

| Scheme | Primary | Secondary | Accent | Background |
|--------|---------|-----------|--------|------------|
| Cyberpunk | #00f5d4 | #7b2cbf | #ff6b35 | #0a0a0f |
| Business Blue | #2563eb | #1e40af | #f59e0b | #ffffff |
| Dark Purple | #8b5cf6 | #ec4899 | #06b6d4 | #1a1a2e |
| Forest Green | #10b981 | #047857 | #f59e0b | #fefce8 |
| Sunset Orange | #f97316 | #ef4444 | #eab308 | #fff7ed |
| Minimal Gray | #000000 | #6b7280 | #dc2626 | #ffffff |
| Corporate Red | #dc2626 | #991b1b | #9ca3af | #1f2937 |
| Ocean Blue | #0ea5e9 | #0369a1 | #22c55e | #f0f9ff |

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| → / Space / Scroll Down | Next slide |
| ← / Scroll Up | Previous slide |
| T | Toggle thumbnail view |
| F | Toggle fullscreen |
| H | Show help |
| ESC | Exit fullscreen/thumbnail |

## Available Components

1. **Title Slide** - Large title + subtitle + dynamic background
2. **Content Slide** - Title + text content
3. **Card List** - Multi-column cards for features
4. **Code Block** - Syntax highlighted code display
5. **Image Display** - Image/screenshot showcase
6. **Comparison Cards** - Left-right comparison layout
7. **Feature List** - Items with icons
8. **Quote Box** - Case study / quote display
9. **Summary Slide** - Summary + contact info
10. **Timeline** - Process/step display
11. **Statistics Cards** - Numbers/stats display

## Technical Constraints

- **Zero Dependencies** - No external CDN links allowed
- **System Fonts** - Uses system pre-installed fonts
- **Single File Output** - All CSS/JS inline in HTML
- **No Scrollbars** - All content must fit within viewport

## License

MIT License

## Contributing

Issues and Pull Requests are welcome!