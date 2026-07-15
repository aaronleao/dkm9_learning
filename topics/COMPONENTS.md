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

## Interactive Canvas Widgets

Reusable **Pure Canvas 2D** widget snippets for interactive plots and animations.
Copy them inline into each page (pages stay self-contained — no shared JS files).
All widgets are theme-aware (colors read from CSS variables at draw time) and
follow the id-prefix rule: every element id starts with the widget name
(e.g. `linWidget-canvas`), so multiple widgets can coexist on one page.

See `features/REFACTOR_PLAN.md` for the full task directives, and **Appendix GEO**
there for the geometric-explanation catalog each widget supports.

### Widget CSS (copy ONCE into each page's `<style>` block)

```css
.viz-widget {background:var(--code); border:1px solid var(--border); border-radius:8px; padding:20px; margin:20px 0;}
.viz-widget canvas {width:100%; height:auto; background:var(--card); border-radius:6px; display:block;}
.viz-controls {display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:12px; margin-bottom:15px;}
.viz-controls label {font-size:0.9em; color:var(--dark);}
.viz-controls input[type=range] {width:100%; accent-color:var(--primary);}
.viz-controls span {color:var(--primary); font-weight:600;}
.viz-readout {font-family:monospace; color:var(--light); margin-top:10px;}
.viz-btn {background:var(--primary); color:#fff; border:none; padding:8px 16px; border-radius:6px; cursor:pointer; font-weight:600;}
.viz-btn:hover {background:var(--secondary);}
details {background:var(--code); border-radius:6px; padding:10px 15px; margin:10px 0;}
details summary {color:var(--primary); font-weight:600; cursor:pointer;}
```

### VIZ-0 — Core widget skeleton (every widget builds on this)

Replace `[WIDGET_ID]`, `[param]`, the slider bounds, and the marked `[REPLACE: ...]`
block. Keep everything else verbatim.

```html
<!-- Widget: [WIDGET_ID] — [DESCRIPTION] -->
<div class="viz-widget" id="[WIDGET_ID]">
    <div class="viz-controls">
        <!-- one block per knob: -->
        <label>[PARAM_LABEL]: <span id="[WIDGET_ID]-[param]Val"></span>
            <input type="range" id="[WIDGET_ID]-[param]" min="[MIN]" max="[MAX]" step="[STEP]" value="[INIT]">
        </label>
        <!-- range bars (x-window of the plot): -->
        <label>x-min: <span id="[WIDGET_ID]-xminVal"></span>
            <input type="range" id="[WIDGET_ID]-xmin" min="-20" max="0" step="0.5" value="-10">
        </label>
        <label>x-max: <span id="[WIDGET_ID]-xmaxVal"></span>
            <input type="range" id="[WIDGET_ID]-xmax" min="0" max="20" step="0.5" value="10">
        </label>
    </div>
    <canvas id="[WIDGET_ID]-canvas" width="820" height="420"></canvas>
    <p class="viz-readout" id="[WIDGET_ID]-readout"></p>
</div>
<script>
(function () {
    const W = document.getElementById('[WIDGET_ID]-canvas');
    const ctx = W.getContext('2d');
    // Theme-aware colors: read CSS variables at draw time
    function themeColors() {
        const cs = getComputedStyle(document.documentElement);
        return {
            axis:  cs.getPropertyValue('--light').trim() || '#888',
            curve: cs.getPropertyValue('--primary').trim() || '#2196F3',
            accent: cs.getPropertyValue('--secondary').trim() || '#4CAF50',
            text:  cs.getPropertyValue('--dark').trim() || '#333',
            grid:  cs.getPropertyValue('--border').trim() || '#ccc'
        };
    }
    const $ = id => document.getElementById('[WIDGET_ID]-' + id);
    // ---- math <-> pixel mapping ----
    let xmin = -10, xmax = 10, ymin = -10, ymax = 10;
    const px = x => (x - xmin) / (xmax - xmin) * W.width;
    const py = y => W.height - (y - ymin) / (ymax - ymin) * W.height;
    function drawAxes(c) {
        ctx.strokeStyle = c.grid; ctx.lineWidth = 1;
        for (let gx = Math.ceil(xmin); gx <= xmax; gx++) {
            ctx.beginPath(); ctx.moveTo(px(gx), 0); ctx.lineTo(px(gx), W.height); ctx.stroke();
        }
        for (let gy = Math.ceil(ymin); gy <= ymax; gy++) {
            ctx.beginPath(); ctx.moveTo(0, py(gy)); ctx.lineTo(W.width, py(gy)); ctx.stroke();
        }
        ctx.strokeStyle = c.axis; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(px(0), 0); ctx.lineTo(px(0), W.height); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(0, py(0)); ctx.lineTo(W.width, py(0)); ctx.stroke();
    }
    function plot(f, c, color) {
        ctx.strokeStyle = color; ctx.lineWidth = 2.5; ctx.beginPath();
        let started = false;
        for (let i = 0; i <= W.width; i++) {
            const x = xmin + (xmax - xmin) * i / W.width;
            const y = f(x);
            if (!isFinite(y) || Math.abs(y) > 1e4) { started = false; continue; }
            if (!started) { ctx.moveTo(px(x), py(y)); started = true; }
            else ctx.lineTo(px(x), py(y));
        }
        ctx.stroke();
    }
    function draw() {
        const c = themeColors();
        ctx.clearRect(0, 0, W.width, W.height);
        xmin = parseFloat($('xmin').value); xmax = parseFloat($('xmax').value);
        $('xminVal').textContent = xmin; $('xmaxVal').textContent = xmax;
        drawAxes(c);
        // [REPLACE: read param sliders, define f(x), call plot(f, c, c.curve),
        //  update $('readout').textContent with the current formula/values]
    }
    ['[param]', 'xmin', 'xmax'].forEach(id => $(id).addEventListener('input', draw));
    // Redraw when the theme toggles (canvas colors are baked at draw time)
    new MutationObserver(draw).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
    draw();
})();
</script>
```

### VIZ-1 — Parametric function plotter (worked instance: linear function)

VIZ-0 specialized with parameter sliders. Full worked instance for
`f(x) = m·x + b` — adapt by changing parameters, the function body, and the
readout only. The knob blocks replacing the `[param]` placeholder:

```html
<label>Slope m: <span id="linWidget-mVal"></span>
    <input type="range" id="linWidget-m" min="-5" max="5" step="0.1" value="2">
</label>
<label>Intercept b: <span id="linWidget-bVal"></span>
    <input type="range" id="linWidget-b" min="-10" max="10" step="0.5" value="3">
</label>
```

And the `draw()` replacement block:

```js
const m = parseFloat($('m').value), b = parseFloat($('b').value);
$('mVal').textContent = m.toFixed(1); $('bVal').textContent = b.toFixed(1);
const f = x => m * x + b;
plot(f, c, c.curve);
$('readout').textContent = `f(x) = ${m.toFixed(1)}x + ${b.toFixed(1)}`;
```

Remember to update the listener list: `['m', 'b', 'xmin', 'xmax'].forEach(...)`.

### VIZ-2 — Animation loop add-on (play/pause)

Add a button next to the sliders and this pattern inside the IIFE. `draw()` must
use the global `t` for its animated quantity.

```html
<button class="viz-btn" id="[WIDGET_ID]-play">▶ Play</button>
```

```js
let t = 0, running = false, lastTs = null;
function tick(ts) {
    if (!running) return;
    if (lastTs !== null) t += (ts - lastTs) / 1000;  // dt in seconds
    lastTs = ts;
    draw();
    requestAnimationFrame(tick);
}
$('play').addEventListener('click', () => {
    running = !running;
    $('play').textContent = running ? '⏸ Pause' : '▶ Play';
    lastTs = null;
    if (running) requestAnimationFrame(tick);
});
```

### VIZ-3 — Epsilon-delta visualizer (continuity / limits)

VIZ-0 plus sliders `eps ∈ [0.05, 2]` (step 0.05) and `cpt` (the point c).
In `draw()`, after plotting f:

```js
const eps = parseFloat($('eps').value), cp = parseFloat($('cpt').value);
const fc = f(cp);
// horizontal epsilon-band f(c) ± eps
ctx.globalAlpha = 0.15; ctx.fillStyle = c.accent;
ctx.fillRect(0, py(fc + eps), W.width, py(fc - eps) - py(fc + eps));
ctx.globalAlpha = 1;
// find largest delta numerically: scan outward until |f(x)-f(c)| >= eps
let delta = 0;
for (let d = 0.001; d < (xmax - xmin); d += 0.001) {
    if (Math.abs(f(cp + d) - fc) >= eps || Math.abs(f(cp - d) - fc) >= eps) break;
    delta = d;
}
if (delta > 0.001) {
    ctx.globalAlpha = 0.15; ctx.fillStyle = c.curve;
    ctx.fillRect(px(cp - delta), 0, px(cp + delta) - px(cp - delta), W.height);
    ctx.globalAlpha = 1;
    $('readout').textContent = `ε = ${eps.toFixed(2)} → δ = ${delta.toFixed(3)}`;
} else {
    $('readout').innerHTML = `ε = ${eps.toFixed(2)} → <span style="color:#ef4444">no δ works!</span>`;
}
// dashed guides through (c, f(c))
ctx.setLineDash([5, 5]); ctx.strokeStyle = c.axis;
ctx.beginPath(); ctx.moveTo(px(cp), py(fc)); ctx.lineTo(px(cp), py(ymin)); ctx.stroke();
ctx.beginPath(); ctx.moveTo(px(cp), py(fc)); ctx.lineTo(px(xmin), py(fc)); ctx.stroke();
ctx.setLineDash([]);
```

(Red `#ef4444` is allowed for warnings only — everything else uses theme colors.)

### VIZ-4 — Secant/tangent visualizer (derivatives, convexity)

VIZ-0 plus sliders for two points `a`, `b` on the curve. In `draw()`:

```js
const a = parseFloat($('a').value), b2 = parseFloat($('b').value);
const fa = f(a), fb = f(b2);
// chord (secant line), extended across the view
const slope = (fb - fa) / (b2 - a);
ctx.strokeStyle = c.accent; ctx.lineWidth = 2;
ctx.beginPath();
ctx.moveTo(px(xmin), py(fa + slope * (xmin - a)));
ctx.lineTo(px(xmax), py(fa + slope * (xmax - a)));
ctx.stroke();
// endpoints
[[a, fa], [b2, fb]].forEach(([X, Y]) => {
    ctx.fillStyle = c.accent; ctx.beginPath();
    ctx.arc(px(X), py(Y), 5, 0, 2 * Math.PI); ctx.fill();
});
$('readout').textContent =
    `slope of secant = (f(b)−f(a))/(b−a) = ${slope.toFixed(4)}`;
```

Animated variant (with VIZ-2): drive `b2 = a + (b0 - a) * Math.exp(-t)` so the
secant visibly collapses onto the tangent; readout shows the difference quotient
converging to f′(a).

### VIZ-5 — 2D vector field / flow animation (Green, Gauss, Stokes, linear maps)

VIZ-0 + VIZ-2. Field `F(x,y) = (P(x,y), Q(x,y))`; arrow grid + advected tracer
particles with fading trails.

```js
// field — replace P, Q per topic:
const P = (x, y) => -y, Q = (x, y) => x;
// particles
const parts = Array.from({length: 200}, () => ({
    x: xmin + Math.random() * (xmax - xmin),
    y: ymin + Math.random() * (ymax - ymin)
}));
function drawField(c) {
    for (let gx = xmin + 0.5; gx < xmax; gx += 1)
        for (let gy = ymin + 0.5; gy < ymax; gy += 1) {
            let vx = P(gx, gy), vy = Q(gx, gy);
            const n = Math.hypot(vx, vy) || 1;
            const L = Math.min(n, 2) / n * 0.35;   // capped arrow length
            vx *= L; vy *= L;
            ctx.strokeStyle = c.curve; ctx.lineWidth = 1.5;
            ctx.beginPath(); ctx.moveTo(px(gx), py(gy));
            ctx.lineTo(px(gx + vx), py(gy + vy)); ctx.stroke();
            // arrowhead
            const ang = Math.atan2(-(vy), vx);
            ctx.beginPath(); ctx.moveTo(px(gx + vx), py(gy + vy));
            ctx.lineTo(px(gx + vx) - 6 * Math.cos(ang - 0.4), py(gy + vy) + 6 * Math.sin(ang - 0.4));
            ctx.moveTo(px(gx + vx), py(gy + vy));
            ctx.lineTo(px(gx + vx) - 6 * Math.cos(ang + 0.4), py(gy + vy) + 6 * Math.sin(ang + 0.4));
            ctx.stroke();
        }
}
function stepParticles(dt) {
    parts.forEach(p => {
        p.x += P(p.x, p.y) * dt; p.y += Q(p.x, p.y) * dt;
        if (p.x < xmin || p.x > xmax || p.y < ymin || p.y > ymax) {
            p.x = xmin + Math.random() * (xmax - xmin);
            p.y = ymin + Math.random() * (ymax - ymin);
        }
    });
}
function drawParticles(c) {
    ctx.fillStyle = c.accent; ctx.globalAlpha = 0.8;
    parts.forEach(p => {
        ctx.beginPath(); ctx.arc(px(p.x), py(p.y), 2, 0, 2 * Math.PI); ctx.fill();
    });
    ctx.globalAlpha = 1;
}
```

Fading trails: instead of `clearRect`, at the start of each animated frame draw a
translucent card-colored rectangle over the canvas (`ctx.globalAlpha=0.2;
ctx.fillStyle=cardColor; ctx.fillRect(0,0,W.width,W.height)`), then redraw arrows.

Hooks to specialize per topic: the field `P, Q`; an overlay closed curve
(circle/rectangle) with animated dots circulating along it (circulation) or
normal arrows crossing it (flux); a heatmap toggle coloring each grid cell by the
sign of `∂Q/∂x − ∂P/∂y` (curl) or `∂P/∂x + ∂Q/∂y` (divergence) computed by finite
differences — blue negative / red positive at `globalAlpha = 0.2`.

### VIZ-6 — Iteration animator (numerical methods, sequences, Riemann sums)

VIZ-0 + VIZ-2 + a Step button. State array pattern:

```html
<button class="viz-btn" id="[WIDGET_ID]-step">Step</button>
<button class="viz-btn" id="[WIDGET_ID]-reset">Reset</button>
```

```js
let iterates = [];           // full history, redrawn every frame
function stepOnce() {
    // [REPLACE: compute next iterate from the last one, push to iterates]
    draw();
}
function reset() { iterates = []; /* [REPLACE: initial state] */ draw(); }
$('step').addEventListener('click', stepOnce);
$('reset').addEventListener('click', reset);
// in draw(): render ALL iterates (old ones at ctx.globalAlpha = 0.25),
// and set $('readout').innerHTML to a small table of the last 5 iterates + error.
```

### NUM-1 — Small linear solver (Gaussian elimination with partial pivoting)

For widgets that need to solve a small system (e.g. interpolation Vandermonde):

```js
function solveLinear(A, b) {      // A: n×n array of rows, b: length-n array
    const n = b.length, M = A.map((r, i) => [...r, b[i]]);
    for (let col = 0; col < n; col++) {
        let piv = col;                             // partial pivoting
        for (let r = col + 1; r < n; r++)
            if (Math.abs(M[r][col]) > Math.abs(M[piv][col])) piv = r;
        [M[col], M[piv]] = [M[piv], M[col]];
        if (Math.abs(M[col][col]) < 1e-12) return null;   // singular
        for (let r = col + 1; r < n; r++) {
            const k = M[r][col] / M[col][col];
            for (let cc = col; cc <= n; cc++) M[r][cc] -= k * M[col][cc];
        }
    }
    const x = new Array(n);
    for (let r = n - 1; r >= 0; r--) {             // back substitution
        let s = M[r][n];
        for (let cc = r + 1; cc < n; cc++) s -= M[r][cc] * x[cc];
        x[r] = s / M[r][r];
    }
    return x;
}
```

### VIZ-JSX — JSXGraph reference variant (DOCUMENT ONLY — never embed in pages)

**Reference alternative. Project pages use Pure Canvas 2D (VIZ-0 family).**
Kept here so the interactive plots can be ported to JSXGraph if the project ever
chooses a library. CDN includes:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraph.css">
<script src="https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraphcore.js"></script>
```

Equivalent of the VIZ-1 linear plotter:

```html
<div id="jxgbox" style="width:100%; height:420px;"></div>
<script>
    const board = JXG.JSXGraph.initBoard('jxgbox', {
        boundingbox: [-10, 10, 10, -10], axis: true, showCopyright: false
    });
    const m = board.create('slider', [[-8, 8], [-2, 8], [-5, 2, 5]], {name: 'm'});
    const b = board.create('slider', [[-8, 7], [-2, 7], [-10, 3, 10]], {name: 'b'});
    board.create('functiongraph', [x => m.Value() * x + b.Value()], {strokeWidth: 2.5});
</script>
```

### Widget usage table

| Widget | Base | Use for |
|--------|------|---------|
| VIZ-0  | —    | Any static parametric plot (skeleton) |
| VIZ-1  | VIZ-0 | Function families with knobs (linear, quadratic, exp, …) |
| VIZ-2  | add-on | Anything animated (play/pause clock) |
| VIZ-3  | VIZ-0 | Continuity, limits (ε-δ bands) |
| VIZ-4  | VIZ-0(+2) | Derivatives (secant→tangent), convexity (chords) |
| VIZ-5  | VIZ-0+2 | Vector fields: Green/Gauss/Stokes, gradients, linear maps |
| VIZ-6  | VIZ-0+2 | Step-by-step algorithms: bisection, Newton, Riemann, sequences |
| NUM-1  | helper | Solving small linear systems inside widgets |
| VIZ-JSX | —   | Reference only (JSXGraph port) |

## Questions?

Refer to:
- CLAUDE.md - Project guidelines
- README.md - Requirements
- features/REFACTOR_PLAN.md - Math refactor directives (widgets, tasks, Appendix GEO)
- Existing topic files - Real examples (Set.html, Logic.html, etc.)
