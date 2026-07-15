# dkm9_learning

Visualization Aided Learning

## Requirements

This project shall have the following requirements.


1. Mermaid diagrams shall be used always.
2. Latex for mathematical forumalas shall be used always.
3. Latex version supported by Github shall be used always.
4. This project shall be compatible with Firefox, Brave, Chrome and LibreWolf browsers.
5. All topics shall be explained in multiple levels from begining to academis research.


## Topics

- [Topics](topics/Topics.md)

> !IMPORTANT
> DESIGN


## Development

### Source & Bibliography Requirement

Every topic page **MUST** include a "Sources & References" section with:

1. **Wikipedia Link** - Link to related Wikipedia article
2. **Academic Papers** - 2-3 papers from [arxiv.org](https://arxiv.org/)
   - Search format: `https://arxiv.org/search/?query=topic+name`
   - Include: Title, Authors, Year, arXiv URL
3. **Textbooks & Bibliography** - Key textbook references or bibliography entries

**Example format:**
```
## Sources & References

- **Wikipedia:** https://en.wikipedia.org/wiki/Set_theory
- **Academic Papers:**
  - "Axiomatic Set Theory" - Paul Cohen (1966) - https://arxiv.org/search/?query=axiomatic+set+theory
  - "Set Theory: An Introduction" - Kunen (2009) - https://arxiv.org/search/?query=set+theory+introduction
- **Textbooks:**
  - Naive Set Theory by Paul Halmos (1960)
  - Set Theory by Kenneth Kunen (2011)
```

### Content Standards

- All mathematics content must be accurate and verifiable
- Formulas must render correctly in MathJax
- Diagrams must display properly in Mermaid
- Browser compatibility: Firefox, Brave, Chrome, LibreWolf
- Responsive design for mobile devices
- **REQUIRED: Dark mode support with toggle button** in header
  - Light/dark theme toggle button in top-right corner
  - Theme preference saved to localStorage
  - System preference auto-detected on first visit
- **Use modular components** for reusability (theme toggle, navigation, etc.)

### Development Environment

During development, all commands shall be compatible with:
- Arch Linux operating system
- Fish shell

- [Features](features/Features.md)
