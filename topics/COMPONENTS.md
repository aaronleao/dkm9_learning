# HTML Components Library

Reusable HTML snippets for consistent styling across all topic pages.

## Quick Components

### Example Box
```html
<div class="example">
    <strong>Example:</strong> [Your example text here]
</div>
```

### Subsection Divider (for merged topics)
```html
<div class="subsection-title">Topic Name</div>
```

### Horizontal Divider
```html
<hr style="height:2px; background:linear-gradient(to right, var(--primary), var(--secondary)); margin:40px 0; border:none;">
```

### Mermaid Diagram
```html
<div class="mermaid">
    graph TD
        A["Topic"] --> B["Subtopic 1"]
        A --> C["Subtopic 2"]
</div>
```

### LaTeX Inline Formula
```html
<p>The equation is: \(E = mc^2\)</p>
```

### LaTeX Display Formula
```html
<p>\[f(x) = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\]</p>
```

### Definition List
```html
<h4>Key Concepts</h4>
<ul>
    <li><strong>Term 1:</strong> Definition of term 1</li>
    <li><strong>Term 2:</strong> Definition of term 2</li>
</ul>
```

### Basic Table
```html
<table>
    <tr><th>Column 1</th><th>Column 2</th></tr>
    <tr><td>Data 1</td><td>Data 2</td></tr>
</table>
```

### Source Links Section
```html
<h3>Wikipedia</h3>
<ul>
    <li><a href="https://en.wikipedia.org/wiki/[TOPIC]" target="_blank">[TOPIC_NAME] - Wikipedia</a></li>
</ul>

<h3>Academic Papers (arXiv)</h3>
<ul>
    <li><a href="https://arxiv.org/search/?query=[KEYWORD]&searchtype=all" target="_blank">[KEYWORD] - arXiv Search</a></li>
</ul>

<h3>Textbooks & Bibliography</h3>
<ul>
    <li><strong>Book Title</strong> - Author Name (Year)</li>
</ul>
```

## CSS Variables (Auto-Theming)

All components automatically respond to light/dark theme:

```css
--primary: #2196F3       /* Primary blue button/accent color */
--secondary: #4CAF50     /* Secondary green accent color */
--dark: #333             /* Text color (light mode) / #e0e0e0 (dark) */
--light: #666            /* Secondary text (light mode) / #b0b0b0 (dark) */
--bg: #f5f5f5            /* Background (light mode) / #1a1a1a (dark) */
--card: #fff             /* Card background (light) / #2d2d2d (dark) */
--border: #e0e0e0        /* Border color (light) / #404040 (dark) */
--code: #f0f0f0          /* Code/example background (light) / #3a3a3a (dark) */
```

No need to manually set colors—use CSS variables and the theme system handles light/dark automatically.

## How to Use the Template

### Option 1: Automated (Recommended)
```bash
cd topics
python3 new-topic.py Math "Your Topic Name"
# Creates: Math/YourTopic.html with all placeholders pre-filled
```

### Option 2: Manual
```bash
cp TEMPLATE.html Math/YourTopic.html
# Then find-replace [PLACEHOLDERS] in your editor
```

### Placeholders to Replace
- `[TOPIC_TITLE]` → Your topic name with capitals
- `[TOPIC_NAME]` → Lowercase topic name
- `[SUBTOPIC_NAME]` → Specific subtopic
- `[TOPIC_URL_SLUG]` → Wikipedia slug (e.g., `Set_theory`)
- `[TOPIC_KEYWORD]` → Search keyword for arXiv (e.g., `set+theory`)

### Then Fill In Your Content

1. **Add content** in each level section
   - Keep structure: h3 headings, paragraphs, examples
   - Use components above for consistency

2. **Add sources** at the bottom
   - Wikipedia link
   - 2-3 arXiv searches
   - 3-5 textbook references

3. **Test in browser**
   - All browsers: Firefox, Chrome, Brave, LibreWolf
   - Dark and light themes
   - Mobile responsive (check at 768px breakpoint)

## Sections Structure

Each topic follows 4 levels:

### Level 1: Beginner
- Start with basics
- Use simple language
- Include intuitive examples
- Visual diagrams recommended

### Level 2: Intermediate
- Build on fundamentals
- Introduce properties and methods
- Include formulas and applications
- Worked examples essential

### Level 3: Advanced
- Theoretical depth
- Specialized applications
- Proofs and formal definitions
- Research connections

### Level 4: Research
- Cutting-edge topics
- Open problems
- Recent papers
- Active research areas

## CSS Class Reference

| Class | Purpose | Auto-Themes |
|-------|---------|------------|
| `.example` | Highlight important examples | Yes, uses --code, --secondary |
| `.mermaid` | Diagram container | Yes, uses --code |
| `.toc` | Table of contents box | Yes, uses --card, --primary |
| `.theme-toggle` | Theme switch button | Yes, uses --primary |
| `.subsection-title` | Section divider in merged topics | Yes, uses --primary, --secondary |
| All semantic HTML | Headings, text, links | Yes, all use CSS variables |

## Best Practices

✓ **DO:**
- Use CSS variables for colors
- Keep markup semantic and simple
- Use LaTeX for math formulas
- Add examples in `.example` boxes
- Test theme switching
- Include sources section
- Use descriptive heading hierarchy

✗ **DON'T:**
- Hard-code colors (use CSS variables)
- Add inline styles (use shared CSS)
- Mix markdown and HTML
- Forget theme toggle button
- Skip responsive testing
- Add content without examples
- Forget sources/bibliography

## Template Maintenance

The template is the single source of truth for:
- HTML structure
- CSS styling
- Theme system
- JavaScript components

To update all pages at once:
1. Update TEMPLATE.html
2. Document changes in COMPONENTS.md
3. Use Fish shell scripts to propagate to all files

## Questions?

Refer to:
- CLAUDE.md - Project guidelines
- README.md - Requirements
- Existing topic files - Real examples (Set.html, Logic.html, etc.)
