# CLAUDE.md - Project Guidelines

**dkm9_learning**: Visualization-aided learning platform for mathematics (beginner to research level).

## Architecture Decisions

**Technology:** Pure HTML5 + CSS3 + CDN (MathJax for LaTeX, Mermaid for diagrams)
- No frameworks, build tools, or dependencies
- Self-contained HTML pages with inline CSS
- CDN: MathJax 3 and Mermaid for rendering
- Dark mode support via `@media (prefers-color-scheme: dark)`

**Content Structure:** Each topic contains 4 levels:
1. Beginner - Foundational concepts
2. Intermediate - Advanced techniques  
3. Advanced - Theoretical depth
4. Research - Cutting-edge mathematics

**File Organization:**
```
topics/
├── Topics.md              (meta topic index: Math, Physics, Chemistry, CS)
├── TEMPLATE.html          (shared template for all subjects)
├── COMPONENTS.md          (reusable HTML snippets library)
├── new-topic.py           (Python 3 automated topic creator)
├── Math/
│   ├── index.html         (Math hub landing page)
│   ├── Set.html, Logic.html, Functions.html, ...
├── Physics/               (future)
├── Chemistry/             (future)
└── ComputerScience/       (future)
```

**LaTeX Formulas:** Inline using `\(` ... `\)` or display `\[` ... `\]`  
**Diagrams:** Mermaid in `<div class="mermaid">` blocks

## Git Workflow

**CRITICAL RULE: AI agents shall NOT run `git commit` or `git push`.**

1. Agent makes file edits
2. Agent stages changes: `git add <files>`
3. Agent shows what's staged: `git status`
4. **Agent ASKS USER for permission with suggested commit message**
5. User decides: `git commit -m "..."` or rejects changes

Why: Commits are hard to undo; user controls what enters history.

## Adding Content - HARD REQUIREMENTS

**Use TEMPLATE.html for all new topics** (eliminates code duplication):
1. Create new topic with Python helper (recommended):
   ```bash
   cd topics
   python3 new-topic.py Subject "Your Topic Name"
   ```
2. Or manually copy: `cp topics/TEMPLATE.html topics/Subject/YourTopic.html`
3. Replace all `[PLACEHOLDER]` variables with your content
4. Follow 4-level structure: Beginner → Intermediate → Advanced → Research
5. Use components from `topics/COMPONENTS.md` for consistency

**Content Requirements:**
- Use MathJax for formulas: `\(inline\)` or `\[display\]`
- Use Mermaid for key diagrams (not required, but recommended)
- Add navigation links back to `index.html`
- Update `Topics.md` with new topic link

**🔴 REQUIRED: Add "Sources & References" section:**
- Wikipedia link to the topic
- 2-3 academic papers from arxiv.org
- 3-5 textbook references
- Use format: `<strong>Title</strong> - Author (Year)`

**Testing before commit:**
- All 4 browsers: Firefox, Brave, Chrome, LibreWolf
- Both themes: Light and dark mode
- Mobile responsive: 768px breakpoint
- MathJax formulas render correctly
- Mermaid diagrams display properly

## Resources

- MathJax: https://docs.mathjax.org/
- Mermaid: https://mermaid.js.org/
- arXiv: https://arxiv.org/
- Project requirements: See README.md
