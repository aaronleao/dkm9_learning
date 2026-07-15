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
topics/Math/
├── index.html           (landing page)
├── Set.html, Logic.html, Functions.html
├── Equations.html, Inequations.html, Geomery.html
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

1. Create HTML file with 4 learning levels (see existing topics as template)
2. Use MathJax for formulas: `\(inline\)` or `\[display\]`
3. Use Mermaid for key diagrams only
4. Add navigation links back to `index.html`
5. Update `Topics.md` with new topic link
6. **🔴 REQUIRED: Add "Sources & References" section at end of each topic:**
   - Wikipedia link to the topic
   - 2-3 academic papers from arxiv.org (use: `https://arxiv.org/search/?query=topic+name`)
   - Textbook references or bibliography entries
   - Follow format: Title, Author, Year, URL
7. Test in browser before staging

## Resources

- MathJax: https://docs.mathjax.org/
- Mermaid: https://mermaid.js.org/
- arXiv: https://arxiv.org/
- Project requirements: See README.md
