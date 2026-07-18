# AGENTS.md

## What This Is

**dkm9_learning** — Visualization-aided math learning platform. Pure HTML5 + CSS3 pages served via CDN (MathJax for LaTeX, Mermaid for diagrams). No build tools, no frameworks, no `node_modules`.

## Critical Constraints

- **NEVER run `git commit` or `git push`.** Stage changes (`git add`), show `git status`, suggest a commit message, then stop. The user controls the git history.
- **Every HTML page is fully self-contained.** All CSS, JS, and widget code is inlined. No shared JS files. Copy snippets from `topics/COMPONENTS.md` into each page.
- **All math via MathJax:** inline `\( ... \)`, display `\[ ... \]`. JS never injects LaTeX — no `MathJax.typesetPromise` calls.
- **Diagrams via Mermaid:** `<div class="mermaid">` blocks.
- **Theme system:** CSS variables (`--primary`, `--secondary`, `--dark`, `--bg`, `--card`, `--border`, `--code`) + `data-theme` attribute + localStorage + system preference detection. Never hard-code colors.
- **Canvas widgets:** Read theme colors at draw time via `getComputedStyle` and a `MutationObserver` on `data-theme`.

## Creating a New Topic

```bash
cd topics
python3 new-topic.py Math "Your Topic Name"    # Python 3 (recommended)
# OR
fish new-topic.fish Math "Your Topic Name"     # Fish shell (your terminal)
```

This copies `TEMPLATE.html` → `Math/YourTopic.html` with `[TOPIC_TITLE]`, `[TOPIC_NAME]`, `[TOPIC_URL_SLUG]`, `[TOPIC_KEYWORD]` pre-filled. You still need to replace `[SUBTOPIC_NAME]` and `[SPECIALIZED_TOPIC]` placeholders manually.

After creating the file:
1. Add content in all 4 level sections (Beginner → Intermediate → Advanced → Research)
2. Add interactive widgets from `topics/COMPONENTS.md` (VIZ-0 family for plots, QUIZ-1/2 for exercises, VENN-1 for logic)
3. Add **Sources & References** section (Wikipedia, 2-3 arXiv links, 3-5 textbooks)
4. Update `topics/Topics.md` if this is the first topic in the subject
5. Test in Firefox, Brave, Chrome, LibreWolf — both light and dark themes — at 768px mobile breakpoint

## Structure

```
topics/
├── TEMPLATE.html          ← single source of truth for page structure
├── COMPONENTS.md          ← copy-paste HTML/JS snippets (VIZ-0..6, QUIZ, VENN, PROOF, CIRCUIT)
├── new-topic.py           ← Python 3 topic creator
├── new-topic.fish         ← Fish shell topic creator
├── Topics.md              ← master topic index
├── Math/                  ← 13 topic pages + index.html
├── Physics/               ← 1 topic page + index.html (early stage)
└── features/              ← REFACTOR_PLAN.md (widget directives, Appendix GEO)
```

## Key Files

| File | Purpose |
|------|---------|
| `topics/TEMPLATE.html` | Page skeleton — CSS, theme system, nav, 4-level structure |
| `topics/COMPONENTS.md` | Reusable snippet library — copy into pages, never import |
| `features/REFACTOR_PLAN.md` | Widget architecture decisions, pedagogy patterns (G1-G9), Appendix GEO |
| `CLAUDE.md` | Extended project guidelines (architecture, testing, git workflow) |
| `README.md` | Requirements spec (4 browsers, 4 levels, Mermaid/LaTeX mandatory) |

## Content Pedagogy Pattern (Every Subtopic)

1. **Intuition** — plain-language paragraph, everyday analogy
2. **Formal definition** — MathJax display formulas, every symbol explained
3. **Worked example** — `<div class="example">` with numbered `<strong>Step N:</strong>` blocks
4. **Interactive visualization** — Canvas widget from COMPONENTS.md where applicable
5. **Real applications** — 3-5 concrete uses in `<div class="example">`
6. **Exercises with solutions** — hidden in `<details><summary>Solution</summary>...</details>`

## Widget System

Widgets are copy-pasted inline into pages (not imported). All follow the VIZ-0 skeleton pattern:

- **VIZ-0**: Core parametric plotter (theme-aware canvas, sliders, range bars)
- **VIZ-1**: Function families with parameter knobs
- **VIZ-2**: Animation loop (play/pause)
- **VIZ-3**: Epsilon-delta visualizer
- **VIZ-4**: Secant/tangent visualizer
- **VIZ-5**: 2D vector field / flow animation
- **VIZ-6**: Iteration animator (step-by-step algorithms)
- **QUIZ-1**: Multiple-choice quiz
- **QUIZ-2**: Fill-in truth table
- **VENN-1**: Theme-aware inline SVG Venn diagrams
- **PROOF-1**: Write-and-evaluate proof exercises
- **CIRCUIT-1**: Drag-and-drop logic-gate board

Every widget id must be prefixed with the widget name (e.g., `linWidget-canvas`) since pages host multiple widgets.

## Styling

- Use CSS variables from COMPONENTS.md. Never hard-code hex colors in component CSS.
- Canvas widgets read colors at draw time via `getComputedStyle(document.documentElement)` and redraw on `MutationObserver` for `data-theme`.
- All pages share the same CSS structure from TEMPLATE.html. To update all pages, update TEMPLATE.html and propagate.

## Development Environment

- **OS:** Arch Linux
- **Shell:** Fish
- **Browsers for testing:** Firefox, Brave, Chrome, LibreWolf
- **No build step.** Open `.html` files directly in a browser.
