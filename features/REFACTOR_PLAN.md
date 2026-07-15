# Math Topics Refactor — Master Directives Document

## Context

**Why:** The `topics/Math/` pages (especially `Functions.html`) are currently formula-dense but shallow: definitions with one-line examples, no real-world applications, no interactivity, and no visual/geometric intuition. The goal is to turn them into a visualization-aided learning experience where every function family has an **interactive canvas plot with parameter knobs (sliders) and range bars**, every subtopic is explained **step-by-step**, and four new subject pages (Calculus, Linear Algebra, Numerical Methods & Analysis, Real Analysis) are created with **step-by-step algorithms and canvas animations** for their core theorems (e.g., Green/Gauss/Stokes).

**Who executes this:** Less-capable agents working one task at a time. Every task below is self-contained: it states its inputs, exact steps, the snippet to copy, and acceptance criteria. **Agents must not improvise architecture — copy the snippets from Module 0 verbatim and only change the marked parts.**

**Decisions already made by the user (do not re-ask):**
1. **Code reuse = inline copy-paste snippets.** No shared JS file. Canonical snippets live in `topics/COMPONENTS.md`; each page gets its own inline copy. Pages stay fully self-contained.
2. **New subjects = separate pages** (`Calculus.html`, `LinearAlgebra.html`, `NumericalMethods.html`, `RealAnalysis.html`), created from `topics/TEMPLATE.html`, linked from `topics/Math/index.html` and `topics/Topics.md`.
3. **Plot technology = both documented, Canvas 2D used in pages.** COMPONENTS.md documents a Pure Canvas 2D snippet family AND a JSXGraph CDN variant for reference — but all `.html` pages embed the **Pure Canvas 2D** versions only.

**Reference example for canvas style:** `/home/aaron/dkm9_learning/euv_beam_collision.html` — sliders driving a live canvas redraw with computed values displayed. Use it as guidance for interaction patterns, NOT for styling (it uses Tailwind + dark-only colors; our pages must use the project CSS variables and be theme-aware).

---

## Global Rules (apply to EVERY task)

**G1 — Git:** NEVER run `git commit` or `git push`. After finishing a task: `git add <files>`, `git status`, then STOP and show the user a suggested commit message.

**G2 — Styling:** Use only the project CSS variables (`--primary`, `--secondary`, `--dark`, `--light`, `--bg`, `--card`, `--border`, `--code`). Never hard-code colors in CSS. Canvas code reads colors at draw time via `getComputedStyle` (see snippet VIZ-0) so plots follow the light/dark theme.

**G3 — Math notation:** MathJax only: `\( ... \)` inline, `\[ ... \]` display. Formal notation required (∀, ∃, ε-δ, limits with proper subscripts).

**G4 — Structure:** Every page keeps the 4 levels: Beginner → Intermediate → Advanced → Research. Every new page comes from `topics/TEMPLATE.html` (or `python3 new-topic.py Math "Name"` run from `topics/`).

**G5 — Pedagogy pattern for EVERY subtopic** (this is the "extensive step-by-step" requirement):
1. **Intuition** — 1–2 plain-language paragraphs, everyday analogy.
2. **Formal definition** — MathJax display formula(s), every symbol explained.
3. **Step-by-step worked example** — numbered `<strong>Step N: ...</strong>` blocks inside `<div class="example">`, each step stating *why* (copy the style already used in `EquationsAndInequalities.html` lines 125–165).
4. **Interactive visualization** — a canvas widget from Module 0 where applicable.
5. **Real applications** — a `<div class="example">` titled "Real-World Applications" listing 3–5 concrete uses (physics, engineering, economics, CS…), at least one worked numerically.
6. **Exercises with solutions** — at least 2 exercises; solutions hidden in `<details><summary>Solution</summary>...</details>`.

**G6 — Sources:** Every page ends with a "Sources & References" section: Wikipedia links, 2–3 arXiv links, 3–5 textbooks (`<strong>Title</strong> - Author (Year)` format). Additionally, per user preference, put source links **directly inline in explanations** where a concept is introduced (e.g., `<a href="https://en.wikipedia.org/wiki/Green%27s_theorem" target="_blank" style="color: var(--primary);">Green's Theorem</a>`).

**G7 — Testing before handing back:** Open the page in a browser (or at minimum validate: no duplicated `<script>` blocks, balanced tags, MathJax delimiters closed, every `canvas` id unique on the page, every slider wired to a redraw). Check both themes and 768px responsiveness.

**G8 — Unique IDs:** All canvas/slider/label element ids on a page must be prefixed with the widget name (e.g., `linWidget-canvas`, `linWidget-slopeSlider`) because pages contain many widgets.

**G9 — Every algorithm gets a geometric explanation.** Whenever a task includes a numbered algorithm box (Gaussian elimination, bisection, Newton, Euler/RK4, u-substitution, ratio test, …), the agent MUST add, right after the algorithm box, a paragraph titled `<h4>Geometric Picture</h4>` explaining what each step *does geometrically*, and — where the Appendix below provides one — the matching canvas directive. Rule of thumb: an algorithm is a sequence of geometric moves; name the move for every step ("this row operation rotates a line about the solution point", "this Newton step slides down the tangent"). Consult **Appendix GEO** at the end of this document: it catalogs the geometric interpretation + animation directive for every algorithm in this plan. If an algorithm has no entry in Appendix GEO, the agent writes the geometric paragraph anyway (text only, no widget required).

---

## Module 0 — Reusable Visualization Snippet Library (DO THIS FIRST)

**Task 0.1 — Add snippet library to `topics/COMPONENTS.md`.**
Append a new section `## Interactive Canvas Widgets` to `topics/COMPONENTS.md` containing the snippets below (VIZ-0 … VIZ-6) exactly, plus the JSXGraph reference variant (VIZ-JSX). All later tasks copy from here. Files: `topics/COMPONENTS.md` only.

### VIZ-0 — Core widget skeleton (theme-aware, every widget builds on this)

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
        // grid lines every integer, axes darker through (0,0)
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

Also add this CSS to the snippet section (agents copy it once into each page's `<style>` block):

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

### VIZ-1 — Parametric function plotter
VIZ-0 specialized with parameter sliders. Document one full worked instance in COMPONENTS.md: linear function `f(x) = m·x + b` with sliders `m ∈ [-5,5]` step 0.1, `b ∈ [-10,10]` step 0.5, readout showing `f(x) = 2.0x + 3.0`. Agents adapt: change parameters, function body, and readout only.

### VIZ-2 — Animation loop add-on (play/pause)
Adds to VIZ-0: a `<button class="viz-btn" id="[WIDGET_ID]-play">▶ Play</button>`, a `let t = 0; let running = false;` clock, `requestAnimationFrame` loop calling `draw()` with `t += dt`, button toggling `running` and label (▶/⏸). Used by all "animated" widgets (secant→tangent, vector fields, iteration methods). Document the ~15-line pattern.

### VIZ-3 — Epsilon-delta visualizer (for continuity/limits)
VIZ-0 plus: sliders for `ε ∈ [0.05, 2]` and `c` (the point). Draw: the curve; horizontal band `f(c)±ε` (translucent `c.accent`, use `globalAlpha=0.15`); the **largest δ** found numerically (scan outward from `c` until `|f(x)−f(c)| ≥ ε`) as a vertical band `c±δ`; dashed lines connecting `(c, f(c))`. Readout: `ε = 0.50 → δ = 0.24`. For a discontinuous function, the δ band collapses to zero at the jump — show readout "no δ works!" in red (`#ef4444` is allowed for warnings only).

### VIZ-4 — Secant/tangent visualizer (for derivatives, convexity)
VIZ-0 plus: two draggable-by-slider points `a`, `b` on the curve; draws the chord between `(a,f(a))` and `(b,f(b))`; optional animation (VIZ-2) shrinking `b → a` to show the secant becoming the tangent, with readout of the difference quotient `(f(b)−f(a))/(b−a)` converging to `f'(a)`.

### VIZ-5 — 2D vector field / flow animation (for Green, Gauss, Stokes, linear maps)
VIZ-0 plus VIZ-2. Draw a grid of arrows for field `F(x,y) = (P(x,y), Q(x,y))` (arrow length ∝ |F|, capped; color `c.curve`). Animate ~200 tracer particles advected by the field (`x += P·dt; y += Q·dt`, respawn when out of bounds; draw as small dots with fading trails via `globalAlpha`). Optional overlay: a closed curve (circle/rectangle) with animated arrows circulating along it (for circulation) or crossing it (for flux). Document parameter hooks: the field functions `P`, `Q`, the overlay curve, and a "show divergence/curl heatmap" boolean (color cells by sign of `∂Q/∂x − ∂P/∂y` computed by finite differences, blue negative / red positive at `globalAlpha=0.2`).

### VIZ-6 — Iteration animator (for numerical methods, sequences, Riemann sums)
VIZ-0 plus VIZ-2 plus a "Step" button. Maintains an iteration state array; each step appends one iterate and redraws history (e.g., bisection brackets, Newton tangent lines, Riemann rectangles, sequence points `(n, a_n)`). Readout shows a small table of the last 5 iterates and current error.

### VIZ-JSX — JSXGraph reference variant (DOCUMENT ONLY — never embed in pages)
Document in COMPONENTS.md: the CDN includes
`<script src="https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraphcore.js"></script>` + CSS, and one example (`JXG.JSXGraph.initBoard` with a slider and functiongraph reproducing VIZ-1's linear plot). Mark clearly: *"Reference alternative. Project pages use Pure Canvas 2D (VIZ-0 family)."*

**Acceptance for Task 0.1:** COMPONENTS.md contains VIZ-0…VIZ-6 + VIZ-JSX with complete copy-pasteable code, the CSS block, and a usage table mapping widget → use case. No page files touched yet.

---

## Task Group A — Refactor `topics/Math/Functions.html`

> Order matters: A.0 first. A.1–A.12 are independent of each other (parallelizable). Each task edits ONLY its own subtopic block. Every task follows the G5 pedagogy pattern; below only the *specifics* per task are listed (application ideas, widget config, step-by-step content).

**Task A.0 — Bug fix + page prep.**
1. Fix the duplicated line: `Functions.html` has `const ThemeToggle = (() => {` twice (lines 322–323) — delete one. This currently breaks all page JS (syntax error), so it must be first.
2. Copy the `.viz-widget` CSS block (Module 0) into the page `<style>`.
3. Expand the TOC to list the named subtopics (anchors added by A.1–A.12).
**Acceptance:** page loads with no console errors; theme toggle works.

**Task A.1 — Linear functions `f(x)=mx+b`.**
Widget: VIZ-1 instance `linWidget`, sliders `m∈[-5,5]`, `b∈[-10,10]`; draw the y-intercept as a dot and a slope-triangle (run=1, rise=m) in `c.accent`. Step-by-step: interpreting m and b; finding a line through two points (full worked example). Applications: taxi fare (base fare + per km — work the numbers), unit conversion °C→°F, Ohm's law V=RI, linear depreciation. Inline source: Wikipedia "Linear function".

**Task A.2 — Quadratic functions.**
Widget `quadWidget`: sliders `a∈[-3,3]` (step 0.1, note a≠0 → skip 0 in readout), `b`, `c`; mark vertex `(−b/2a, f(−b/2a))` and real roots (dots) when discriminant ≥ 0; readout shows vertex + discriminant. Step-by-step: completing the square (every algebra step), vertex form ↔ standard form. Applications: projectile motion (h(t) = −½gt² + v₀t + h₀, worked: when does the ball land?), profit maximization, parabolic reflectors/satellite dishes. Inline source: Wikipedia "Quadratic function".

**Task A.3 — Polynomial functions.**
Widget `polyWidget`: degree selector (slider 1–6) + coefficient sliders for a cubic default; show end-behavior annotation. Step-by-step: end behavior rules (sign of leading coeff × parity of degree, table of 4 cases), finding roots by factoring a cubic completely. Applications: volume optimization (open box from cardboard — full worked max problem set up, solved at intermediate level by graph reading), Bézier curves in computer graphics, polynomial regression. 

**Task A.4 — Rational functions.**
Widget `ratWidget`: `f(x) = (ax+b)/(cx+d)`, four sliders; draw vertical asymptote `x=−d/c` and horizontal `y=a/c` as dashed lines (plot() already breaks at singularities). Step-by-step: finding all asymptotes of `(x²−1)/(x²−4)` (vertical, horizontal, holes — each substep shown). Applications: average cost per unit C(x)/x, lens equation 1/f = 1/u + 1/v, drug concentration decay, Michaelis–Menten kinetics.

**Task A.5 — Even/odd functions & monotonicity.**
Widget `symWidget`: function picker (slider selecting from x², x³, x²+x, cos x, sin x); draws f(x) solid and f(−x) dashed in `c.accent` so symmetry (or its failure) is visible; readout states "even / odd / neither" by numeric test. Step-by-step: proving x³ is odd, proving x²+x is neither (evaluate f(−x) explicitly). Applications: even/odd decomposition in Fourier analysis, symmetry shortcuts in integration (∫₋ₐᵃ odd = 0).

**Task A.6 — Exponential functions.**
Widget `expWidget`: `f(x)=C·aˣ`, sliders `C∈[0.5,5]`, `a∈[0.2,4]` (highlight a=1 as degenerate); log-scale toggle checkbox (second y-mapping) to show exponentials become lines. Step-by-step: compound interest derivation → limit definition of e (numeric table of (1+1/n)ⁿ). Applications: population growth, radioactive decay (worked half-life problem: carbon-14 dating), compound interest (worked), Moore's law. Inline source: Wikipedia "Exponential function".

**Task A.7 — Logarithmic functions.**
Widget `logWidget`: `f(x)=log_a(x)`, slider `a∈[1.5,10]`; overlay `aˣ` dashed + the line y=x dotted to show reflection/inverse relationship. Step-by-step: solving `3·2^(x+1)=24` with every log rule cited; the three log laws each derived in one line from exponent laws. Applications: pH scale (worked), decibels, Richter scale (worked: energy ratio of magnitude 5 vs 7), binary search complexity O(log n), entropy.

**Task A.8 — Trigonometric functions.**
Widget `trigWidget` (VIZ-2 animated): left half of canvas draws the unit circle with a rotating point (angle θ = t), right half draws sin traced out as θ advances; sliders for amplitude A, frequency ω, phase φ of `A·sin(ωx+φ)`. Step-by-step: reading sin/cos off the unit circle for θ = π/6, π/4, π/3 (exact values, triangle derivations). Applications: sound waves/tuning fork (worked: A440), AC voltage, tides, circular motion, springs (SHM). Inline source: Wikipedia "Trigonometric functions".

**Task A.9 — Inverse functions.**
Widget `invWidget`: plot f (slider-selected from 2x+3, x³, eˣ), its inverse (reflect points across y=x numerically), and dashed y=x. Step-by-step: full algorithm to invert f(x)=2x+3 (swap, solve, verify both compositions); why x² needs domain restriction (horizontal line test, drawn). Applications: decryption as inverse of encryption, converting units back, log as inverse of exp interlink to A.7.

**Task A.10 — Composition & transformations.**
Widget `transWidget`: base function picker + sliders for `a·f(b(x−h))+k` (a, b, h, k); base curve dashed, transformed solid; readout shows the transformed formula. Step-by-step: order of transformations for `−2f(x−3)+1` (why order matters, each intermediate graph described); composition worked both ways (f∘g ≠ g∘f with numbers). Applications: image scaling/translation in graphics, time-shifting signals, currency conversion chains (composition).

**Task A.11 — Continuous functions (geometric, canvas — REQUIRED by user).**
Two widgets:
- `contWidget` = VIZ-3 (ε-δ) on `f(x)=x²` at slider-chosen c. Explain geometrically in the text: *"continuity at c means: whatever ε-tube you draw around f(c), there is a δ-window around c whose image stays inside the tube"* — the widget shows exactly this.
- `jumpWidget` = VIZ-3 on a step function `f(x) = x<1 ? x : x+2` showing δ failing at c=1 for ε<1 (readout "no δ works!").
Step-by-step: verify continuity of f(x)=3x+1 at c=2 with a full ε-δ proof (choose δ=ε/3, every inequality justified); classify the 3 discontinuity types (removable/jump/infinite) with one example each. Applications: why bisection needs continuity (IVT), physical quantities as continuous signals, thermostat/jump discontinuities. Theorems stated: IVT and Extreme Value Theorem with geometric explanation referencing the widget. Inline source: Wikipedia "Continuous function".

**Task A.12 — Differentiable functions (MORE examples + exercises, formal notation — REQUIRED by user).**
Widget `diffWidget` = VIZ-4 animated on x² (secant → tangent, readout shows difference quotient converging to 2a). Second static-per-slider widget on `|x|` showing left/right secants disagreeing at 0.
Content (formal notation mandatory):
- Definition: \(f'(c)=\lim_{h\to 0}\frac{f(c+h)-f(c)}{h}\), and the ε-δ form.
- **Worked examples (min 4, from the limit definition, all steps):** f(x)=x² at general c; f(x)=1/x; f(x)=√x (conjugate trick); f(x)=|x| at 0 fails (one-sided limits computed: +1 vs −1).
- Theorem with proof sketch: differentiable ⇒ continuous (and counterexample |x| for the converse).
- **Exercises (min 5) with `<details>` solutions:** derivative of x³ from definition; differentiability of x·|x| at 0 (it IS differentiable — good surprise); of x·sin(1/x) vs x²·sin(1/x) at 0 (extended by 0); find a,b making a piecewise function differentiable; prove f'(c)=0 at an interior max (Fermat).
Applications: velocity/acceleration, marginal cost, Newton's method preview (link to NumericalMethods.html), gradient descent in ML.

**Task A.13 — Convex & concave functions (plots + canvas — REQUIRED by user).**
Widget `convWidget` = VIZ-4 variant: function picker (x², −ln x, x³, sin x); chord between slider points a,b drawn in `c.accent`; the region between chord and curve shaded (`globalAlpha=0.15`); readout states "chord above curve → convex here" / "below → concave" / "crosses → neither"; a λ-slider moves a point along the chord showing \(f(\lambda a + (1-\lambda)b) \le \lambda f(a)+(1-\lambda)f(b)\) numerically.
Step-by-step: verify convexity of x² directly from the definition (full inequality chain); second-derivative test statement; find inflection points of x³−3x (worked). Applications: convex optimization (why local=global — explained with the widget), Jensen's inequality, economics (diminishing returns = concavity), least squares is convex. Inline source: Wikipedia "Convex function".

**Task A.14 — Functions.html final pass.**
Update TOC anchors for all new subtopics; verify every widget has unique ids (G8); add cross-links to the four new pages in relevant places; extend the Sources section (add: *Calculus* – Spivak (2008), *Convex Optimization* – Boyd & Vandenberghe (2004), Wikipedia links for each subtopic). Run G7 checks.

---

## Task Group B — Create `topics/Math/Calculus.html`

**Task B.0 — Scaffold.** From `topics/`: `python3 new-topic.py Math "Calculus"` (or copy TEMPLATE.html), replace placeholders, add `.viz-widget` CSS. Add page to `Math/index.html` and `Topics.md` (see Group F).

**Task B.1 — Beginner: Limits.**
Widget: VIZ-3 instance on `(x²−1)/(x−1)` showing the hole at x=1 and limit 2. Step-by-step: numeric table approach (x=0.9, 0.99, …), then algebraic (factor & cancel, why allowed for x≠1). Limit laws listed. Applications: instantaneous speed from average speed, 0/0 forms.

**Task B.2 — Beginner/Intermediate: Derivatives.**
Widget: VIZ-4 animated (reuse A.12 config, but plot f and f' together: second pass computing numeric derivative `(f(x+h)−f(x−h))/2h`, drawn in `c.accent`). Step-by-step algorithm boxes for: power rule, product rule, quotient rule, **chain rule (numbered algorithm: identify outer/inner → differentiate outer at inner → multiply)**, each with one fully worked example. Applications: related rates (ladder problem fully worked), optimization (fence problem fully worked with endpoint check).

**Task B.3 — Intermediate: Integrals.**
Widget: VIZ-6 Riemann-sum instance `riemannWidget`: function x², sliders n∈[1,100] and interval; draws n rectangles (left/mid/right selector), readout: sum vs exact 1/3, error shrinking. Step-by-step: computing a Riemann sum by hand for n=4; u-substitution algorithm (numbered steps + worked ∫2x·cos(x²)dx); integration by parts (LIATE, worked ∫x·eˣdx). **FTC** stated both parts, geometric explanation: "the accumulation function's growth rate is the height" — tie to the widget.

**Task B.4 — Advanced: Multivariable — partial derivatives & gradient.**
Widget: VIZ-5 instance `gradWidget` showing the gradient field of f(x,y)=x²+y² (arrows point away from origin, growing) with level-set circles overlaid; slider picks the function (x²+y², x²−y², sin x·cos y). Explain: gradient ⊥ level sets, points uphill (visible in widget). Step-by-step: compute ∇f and the directional derivative for a worked point.

**Task B.5 — Advanced: Green's Theorem (canvas animation directives — REQUIRED by user).**
State: \(\oint_{\partial D}(P\,dx+Q\,dy)=\iint_D\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA\), every symbol explained, inline Wikipedia link.
**Animation directives (widget `greenWidget`, VIZ-5 base):**
1. Draw vector field F=(−y,x) (rotation) as the arrow grid.
2. Overlay a closed square boundary; animate arrow-heads circulating counterclockwise along it (parametrize the boundary, place 20 moving dots, advance with t).
3. "Subdivide" button: split the square into an n×n grid (slider n∈[1,8]); draw a small circulating loop in EVERY cell; adjacent interior edges have arrows in opposite directions — draw shared edges in a "cancel" color and fade them out over ~1s, leaving only the outer boundary highlighted. **This is the proof idea animated: interior circulations cancel, only the boundary survives.**
4. Curl heatmap toggle (VIZ-5 hook): here ∂Q/∂x−∂P/∂y = 2 everywhere → uniform red tint; readout shows "circulation = 2 × Area" verified numerically (line integral computed by sampling vs 2·area).
Step-by-step worked example: verify Green's theorem for F=(−y,x) on the unit square (both sides computed to 2, every integral step shown). Applications: planimeter, area via \(\frac12\oint(x\,dy−y\,dx)\), fluid circulation.

**Task B.6 — Advanced: Divergence (Gauss) Theorem (canvas animation directives).**
State in 2D-flux form for the canvas (\(\oint_{\partial D}\mathbf F\cdot\mathbf n\,ds=\iint_D\nabla\!\cdot\!\mathbf F\,dA\)) and full 3D statement in text.
**Animation directives (widget `gaussWidget`, VIZ-5 base):** field F=(x,y) (source at origin). Particles stream outward; a closed circle boundary with outward normal arrows; particles crossing the boundary flash briefly (detect radius crossing) and a flux counter increments — readout compares counted flux rate with ∬(∇·F)dA = 2·Area. Slider: boundary radius. Divergence heatmap toggle (uniform red = 2). Second field option F=(−y,x): particles circulate, NOTHING crosses, flux counter stays ~0 — divergence-free. Step-by-step worked verification for F=(x,y) on the unit disk. Applications: conservation laws, Maxwell's ∇·E=ρ/ε₀, incompressible flow.

**Task B.7 — Advanced: Stokes' Theorem (canvas animation directives).**
Full 3D statement; explain Green's theorem is its flat special case. Canvas is 2D, so the directive is an **orthographic-projection animation** (widget `stokesWidget`): draw a tilted disk (ellipse) as the surface, its boundary circle with circulating animated arrows, and small curl-loops on the surface tilting with it (project 3D points (x,y,z)→(x + 0.5·z·cosα, y + 0.3·z·sinα) with a tilt slider α); animate the same interior-cancellation idea as B.5 on the surface patches. Readout ties \(\oint_{\partial S}\mathbf F\cdot d\mathbf r = \iint_S(\nabla\times\mathbf F)\cdot d\mathbf S\). Keep the 3D math in text; the canvas conveys the geometric idea only. Applications: Faraday's law, vorticity.

**Task B.8 — Research level + sources.** Differential forms unify the three theorems (generalized Stokes \(\int_M d\omega=\int_{\partial M}\omega\)); de Rham cohomology one paragraph. Sources: Wikipedia (Green's/Divergence/Stokes' theorem, Calculus), arXiv searches (differential forms, geometric integration), textbooks: Spivak *Calculus on Manifolds* (1965), Stewart *Calculus* (2015), Apostol *Calculus* (1967), Marsden & Tromba *Vector Calculus* (2011).

---

## Task Group C — Create `topics/Math/LinearAlgebra.html`

**Task C.0 — Scaffold** (same procedure as B.0).

**Task C.1 — Beginner: Vectors.**
Widget `vecWidget` (VIZ-0): two vectors u, v with angle/length sliders; draw u, v, u+v (parallelogram, dashed construction lines); readout: components, dot product, angle between them. Step-by-step: computing u+v, ‖u‖, u·v by hand; geometric meaning of dot product sign. Applications: forces, velocity composition, dot product in similarity search/recommendations.

**Task C.2 — Beginner/Intermediate: Matrices as transformations (canvas animation).**
Widget `matWidget` (VIZ-2): 4 sliders for entries of A=[[a,b],[c,d]]; draw the unit grid and a shape (letter-F polygon or unit square); animate interpolation from I to A (`M(t)=(1−t)I+tA`), grid deforming; draw images of e₁, e₂ as colored arrows; readout: det A (area scale factor, negative = flip — state it). Step-by-step: matrix–vector multiplication by hand (columns = images of basis vectors); matrix–matrix as composition. Applications: image rotation/scaling, robotics, coordinates changes, computer graphics pipelines.

**Task C.3 — Intermediate: Solving systems — Gaussian elimination (step-by-step algorithm — REQUIRED).**
Numbered algorithm box: (1) forward elimination with row operations, (2) pivoting rule (swap when pivot 0), (3) back substitution. Full 3×3 worked example showing EVERY row operation and the resulting matrix after each. Widget `gaussStepWidget` (VIZ-6): "Step" button applies one row operation at a time to a displayed matrix (render matrix as text on canvas or in a `<pre>` updated by JS — the `<pre>` variant is acceptable here), highlighting the pivot and the row being modified. **Geometric companion widget `gaussGeoWidget`** (2×2 case, see Appendix GEO-1): two lines in the plane whose intersection is the solution; each Step animates one line rotating about the (fixed!) intersection point into axis-aligned position — elimination never moves the solution, it only simplifies the lines. Cross-link `EquationsAndInequalities.html`. Applications: circuits, structural analysis, least squares setup.

**Task C.4 — Advanced: Determinants & eigenvalues (canvas animation).**
Determinant: 2×2 and 3×3 cofactor expansion worked; tie to area (C.2 widget already shows it). Eigen: widget `eigenWidget` (VIZ-2): fixed A (slider-adjustable symmetric default [[2,1],[1,2]]); animate a unit vector x rotating through 360°, drawing Ax simultaneously; when x ∥ Ax (cross product ≈ 0) flash and freeze briefly — those directions are eigenvectors; readout: current x, Ax, and the ratio. Step-by-step: characteristic polynomial for [[2,1],[1,2]] solved completely (λ=1,3 with eigenvectors). Applications: PageRank, principal component analysis, vibration modes, quantum states.

**Task C.5 — Research + sources.** Abstract vector spaces, SVD (statement + applications: compression, pseudo-inverse), random matrix theory paragraph. Sources: Wikipedia (Linear algebra, Gaussian elimination, Eigenvalues), arXiv (randomized numerical linear algebra), textbooks: Strang *Introduction to Linear Algebra* (2016), Axler *Linear Algebra Done Right* (2015), Horn & Johnson *Matrix Analysis* (2012), Trefethen & Bau *Numerical Linear Algebra* (1997).

---

## Task Group D — Create `topics/Math/NumericalMethods.html`

**Task D.0 — Scaffold** (same as B.0).

**Task D.1 — Root finding: bisection (algorithm + canvas — flagship VIZ-6 use).**
Numbered algorithm (with stopping criterion |b−a|<tol, why continuity+sign change guarantees a root → link IVT in Functions.html). Widget `bisectWidget` (VIZ-6): f(x)=x³−x−2 plotted; Step button halves the bracket; brackets drawn as shrinking colored interval, midpoint dot each step; iterate table in readout (n, aₙ, bₙ, mₙ, f(mₙ)). Worked example: 4 iterations by hand in a table. Error bound \((b−a)/2^n\) derived.

**Task D.2 — Root finding: Newton–Raphson (algorithm + canvas).**
Algorithm box: \(x_{n+1}=x_n−f(x_n)/f'(x_n)\), derivation from tangent line (step-by-step). Widget `newtonWidget` (VIZ-6): each Step draws the tangent at xₙ, drops to its x-intercept (animated dot sliding down the tangent), that's xₙ₊₁; slider for x₀ — show divergence for bad x₀ on f(x)=x³−2x+2 (cycles!). Quadratic convergence stated; comparison table bisection vs Newton iterations for same tolerance. Applications: square roots in hardware (worked: √a via x²−a), optimization (Newton on f'), machine learning second-order methods.

**Task D.3 — Interpolation & least squares.**
Lagrange interpolation: formula, worked 3-point example fully expanded. Widget `interpWidget`: slider-placed 4 points, canvas draws the interpolating cubic (solve the 4×4 Vandermonde numerically with the Gaussian elimination routine — include the ~20-line JS `solveLinear(A,b)` helper in the snippet, documented in COMPONENTS.md as `NUM-1`) plus Runge phenomenon note. Least squares line fit: derive normal equations step-by-step; widget option toggling "fit line" through the points — **draw the residuals as literal squares** (see Appendix GEO-4: vertical segment from each point to the line, with an actual square of that side length rendered at `globalAlpha=0.2`; sliders m, b let the student minimize total square area by hand before revealing the optimum). Applications: sensor calibration, trendlines, font rendering.

**Task D.4 — Numerical integration.**
Trapezoid & Simpson rules: geometric derivation, error orders (h², h⁴), worked example ∫₀¹x²dx with n=4 for both, compared with exact. Widget: reuse `riemannWidget` config (B.3) extended with method selector (left/mid/trapezoid/Simpson) — document as one widget with a method dropdown. Applications: distance from GPS speed samples, probability from densities.

**Task D.5 — ODEs: Euler & RK4 (algorithm + canvas animation).**
Euler algorithm box (derivation from tangent line); RK4 stated with the 4 slopes explained (weighted average — geometric description of k₁..k₄). Widget `odeWidget` (VIZ-6 + VIZ-2): y'=y with exact eˣ dashed; Step/Play advances Euler (polyline) and RK4 simultaneously in two colors; slider h; readout: error of each at x=1. Second system option: pendulum θ''=−sin θ as 2D phase animation (particle tracing the phase orbit — Euler visibly spirals out, RK4 stays closed: energy drift made visible). Applications: physics engines, orbital mechanics, epidemiology (SIR), circuit simulation.

**Task D.6 — Linear systems revisited + conditioning; Research + sources.**
LU factorization = recorded Gaussian elimination (worked 3×3); iterative methods (Jacobi: algorithm box + convergence condition, diagonal dominance); condition number intuition (worked ill-conditioned 2×2 — tiny data change, huge solution change, numbers shown). Research: Krylov methods paragraph, randomized NLA. Sources: Wikipedia (Newton's method, Runge–Kutta, Numerical analysis), arXiv (numerical analysis searches), textbooks: Burden & Faires *Numerical Analysis* (2015), Quarteroni *Numerical Mathematics* (2007), Press et al. *Numerical Recipes* (2007), Trefethen & Bau (1997).

---

## Task Group E — Create `topics/Math/RealAnalysis.html`

**Task E.0 — Scaffold** (same as B.0).

**Task E.1 — Sequences & convergence (canvas).**
Formal: \(\lim a_n = L \iff \forall\varepsilon>0\,\exists N\,\forall n\ge N: |a_n−L|<\varepsilon\). Widget `seqWidget` (VIZ-6): plot (n, aₙ) dots for slider-selected sequence (1/n, (−1)ⁿ/n, (1+1/n)ⁿ, (−1)ⁿ); ε-slider draws band L±ε; N computed and marked with vertical line — all dots right of N inside band (or readout "diverges: no single L works" for (−1)ⁿ). Step-by-step ε-N proof that 1/n→0 (find N=⌈1/ε⌉, full chain). Monotone convergence theorem stated with (1+1/n)ⁿ as the widget-visible example.

**Task E.2 — Series.**
Partial sums as a sequence (widget: same `seqWidget` machinery, plot Sₙ for Σ1/n² vs Σ1/n — harmonic visibly crawling to ∞, readout compares). Step-by-step: geometric series sum derivation; harmonic divergence by grouping (the 1/2-blocks argument, every group shown); comparison and ratio tests as algorithm boxes with one worked example each. Applications: decimal expansions, compound annuities, Zeno's paradox resolved.

**Task E.3 — Rigorous limits & continuity.**
Reuse VIZ-3 (`analContWidget`) on new examples: Dirichlet function described (not plottable — explain why!), Thomae's function plotted as dots (continuous at irrationals — statement only, proof sketch). Full ε-δ proofs, step-by-step: lim_{x→2}x²=4 (the classic |x+2| bound trick, δ=min(1, ε/5), every step justified — this is the model proof for students). Uniform vs pointwise continuity: 1/x on (0,1) counterexample with widget showing δ shrinking as c→0 (VIZ-3 readout makes this visible: same ε, smaller δ near 0).

**Task E.4 — Compactness, IVT/EVT, Riemann integral.**
Heine–Borel stated; why [a,b] matters (EVT fails on (0,1) with 1/x — widget optional). IVT proof sketch via bisection (cross-link D.1 — the algorithm IS the proof). Riemann integral: upper/lower sums formal definition; widget `darbouxWidget` (VIZ-6): draws BOTH upper and lower step-rectangles for x² with n-slider, readout shows U(f,P)−L(f,P)→0 — integrability made visible. Step-by-step: compute upper/lower sums for x on [0,1] with n equal parts, take limits.

**Task E.5 — Research + sources.** Lebesgue integration motivation (what Riemann misses — Dirichlet function callback), measure-zero idea; Baire category one paragraph. Sources: Wikipedia (Real analysis, Riemann integral, Uniform continuity), arXiv, textbooks: Rudin *Principles of Mathematical Analysis* (1976), Abbott *Understanding Analysis* (2015), Tao *Analysis I* (2016), Royden *Real Analysis* (2010).

---

## Task Group F — Integration & site wiring

**Task F.1 — `topics/Math/index.html`:** add cards/links for the 4 new pages (match existing link markup for Set.html etc.).
**Task F.2 — `topics/Topics.md`:** add the 4 new topics under Math.
**Task F.3 — Cross-links:** Functions.html §Continuous → RealAnalysis.html & Calculus.html; §Differentiable → Calculus.html & NumericalMethods.html (Newton); EquationsAndInequalities.html §Systems → LinearAlgebra.html (Gaussian elimination).
**Task F.4 — Final QA sweep (one agent, whole site):** run the G7 checklist on all 5 touched/created pages; verify every slider moves something, every Play button animates, no console errors, both themes, 768px layout; verify all internal links resolve (`grep -o 'href="[^"]*\.html"'` against `ls`); verify each page still has exactly ONE ThemeToggle block.

---

## Execution order & task list (checklist)

Dependencies: 0.1 → everything. A.0 → A.1–A.14. B.0 → B.1–B.8. C.0 → C.1–C.5. D.0 → D.1–D.6. E.0 → E.1–E.5. Groups A–E parallelizable across agents after 0.1. F last.

- [ ] 0.1 COMPONENTS.md snippet library (VIZ-0…VIZ-6, VIZ-JSX, NUM-1, CSS)
- [ ] A.0 Functions.html: fix duplicate ThemeToggle bug + widget CSS + TOC
- [ ] A.1 Linear • A.2 Quadratic • A.3 Polynomial • A.4 Rational
- [ ] A.5 Even/odd & monotonicity • A.6 Exponential • A.7 Logarithmic • A.8 Trig
- [ ] A.9 Inverse • A.10 Composition/transformations
- [ ] A.11 Continuous functions (ε-δ canvas ×2)
- [ ] A.12 Differentiable functions (examples + 5 exercises w/ solutions, formal)
- [ ] A.13 Convex/concave (chord canvas + λ-slider)
- [ ] A.14 Functions.html final pass + sources
- [ ] B.0–B.8 Calculus.html (Green B.5 / Gauss B.6 / Stokes B.7 animations)
- [ ] C.0–C.5 LinearAlgebra.html (matrix-transform + eigen animations, Gaussian stepper)
- [ ] D.0–D.6 NumericalMethods.html (bisection/Newton/ODE animators)
- [ ] E.0–E.5 RealAnalysis.html (ε-N sequence widget, Darboux sums)
- [ ] F.1–F.4 index.html, Topics.md, cross-links, full QA
- [ ] Stage all changes (`git add`), show `git status`, propose commit message(s) to user — DO NOT COMMIT

## Verification (end-to-end)

1. `python3 -m http.server` from repo root (or open files directly); load each of the 5 pages.
2. Console must be error-free on load and while dragging every slider / pressing every Play/Step button.
3. Toggle theme on each page: canvas widgets must redraw in new colors (MutationObserver test).
4. Narrow to <768px: controls grid collapses to one column, canvas scales (CSS `width:100%`).
5. Spot-check math: readouts vs hand values (e.g., riemannWidget n=100 ≈ 0.3334; gaussWidget flux ≈ 2·πr²... i.e. 2×area; newtonWidget on x³−x−2 → 1.5214).
6. MathJax: no raw `\(` visible; Mermaid unaffected.

---

## Appendix GEO — Geometric Explanations of Algorithms (canvas directives)

Every algorithm in this plan is explained twice: symbolically (the algorithm box) and geometrically (what each step *does* in the plane). This appendix is the catalog. Each entry gives: **the geometric picture** (text the agent adapts into the `<h4>Geometric Picture</h4>` paragraph) and **the animation directive** (how to show it with the VIZ snippets). Widget bases refer to Module 0.

### GEO-1 — Gaussian elimination (used by C.3, D.6-LU)
**Picture:** In 2D, each equation is a line; the solution is their intersection. A row operation `R2 ← R2 − k·R1` replaces line 2 by a new line **through the same intersection point** (any linear combination of two equations is satisfied by their common solution). Elimination is therefore a sequence of rotations of lines about the fixed solution until each line is axis-parallel (`x = …`, `y = …`) — at which point the solution can be read off. In 3D the same story with planes; pivoting = choosing which plane to rotate.
**Animation (`gaussGeoWidget`, VIZ-2 base):** draw the two lines of a 2×2 system and a dot at the solution. Each "Step" animates one line continuously interpolating from its old slope/intercept to the eliminated version (interpolate the coefficient row `(1−t)·old + t·new`, redraw the line each frame, ~1s). The solution dot NEVER moves — render it pulsing in `c.accent` during the rotation to hammer the invariant. Readout shows the matrix row being replaced.
**LU variant (D.6):** each elimination step is a **shear** of the plane; show the unit grid shearing (reuse C.2 `matWidget` machinery with M = elementary matrix); L simply records the shears.

### GEO-2 — Bisection (used by D.1, E.4-IVT)
**Picture:** The root is an animal trapped in a cage `[a,b]`; the sign change (f(a)·f(b)<0, guaranteed to persist by continuity/IVT) is the proof it's inside. Each step builds a wall at the midpoint and keeps the half that still has the sign change. The cage halves forever, so the animal's position is known to arbitrary precision — the algorithm IS the constructive proof of IVT.
**Animation (`bisectWidget`, VIZ-6):** shade the current bracket as a translucent vertical band; on Step, draw the midpoint wall, flash the discarded half in red fading out, band shrinks. Plot the endpoints' signs as +/− labels. Error bar `(b−a)/2ⁿ` drawn as a shrinking ruler under the axis.

### GEO-3 — Newton–Raphson (used by D.2)
**Picture:** Stand on the curve at (xₙ, f(xₙ)). The tangent line is the best straight-line impersonation of the curve; ride it down to where *it* crosses zero and call that xₙ₊₁. If the curve were exactly its tangent, one step would finish — quadratic convergence measures how good the impersonation is. Divergence happens when the tangent is nearly flat (f'≈0): the slide shoots you far away.
**Animation (`newtonWidget`, VIZ-6):** on Step: draw vertical dashed line up from xₙ to the curve, draw the tangent, animate a dot sliding along the tangent to its x-intercept (~0.7s), drop marker xₙ₊₁. Keep previous tangents at `globalAlpha=0.25`. Add a "basin strip": a 1-px-tall bar under the x-axis coloring each x₀ by which root it converges to (precompute 400 samples) — geometric picture of basins of attraction.

### GEO-4 — Least squares / normal equations (used by D.3)
**Picture:** Each data point pays a penalty: the *actual square* built on its vertical miss. Fitting = tilting/sliding the line until the total square area is smallest. (Advanced remark for the text: in ℝⁿ this is orthogonal projection of the data vector onto the span of the model — the residual is perpendicular to the fit, which is exactly what the normal equations say: "normal" means perpendicular.)
**Animation:** described in Task D.3 — residual squares rendered live while m, b sliders move; running total shown as a number and as a bar that the student tries to minimize; "Solve" button animates to the optimal (m*, b*).

### GEO-5 — Euler's method (used by D.5)
**Picture:** The ODE y'=f(x,y) paints a **slope field**: a tiny compass needle at every point of the plane. Euler walks the field like a hiker who checks the compass only every h kilometers and walks straight between checks — he drifts off the true path on curves, always cutting corners. Shrinking h = checking the compass more often.
**Animation (`odeWidget`):** draw the slope field (grid of short segments, VIZ-5-style but static) behind everything; animate the Euler polyline advancing one segment per Step, each new segment visibly parallel to the field needle at its start point; exact solution dashed for comparison.

### GEO-6 — RK4 (used by D.5)
**Picture:** The smarter hiker: before committing to a step, he scouts — checks the compass at the start (k₁), uses it to peek at the midpoint twice (k₂, k₃), and at the far end (k₄), then walks the *weighted average* direction (k₁+2k₂+2k₃+k₄)/6. Four compass checks per step buy four orders of accuracy.
**Animation:** on Step (slowed mode), draw the four probe arrows k₁..k₄ one by one in distinct alphas at their probe points, then collapse them into the single averaged arrow that the path actually follows; fade probes out. Then the pendulum phase-portrait mode (Task D.5) shows the payoff: Euler's orbit spirals outward (energy gain — corner-cutting made visible), RK4's stays closed.

### GEO-7 — Riemann / Darboux sums, trapezoid, Simpson (used by B.3, D.4, E.4)
**Picture:** Approximating area with ever-better bricks: rectangles (order 0), tilted-roof trapezoids (order 1), parabolic roof tiles (Simpson, order 2). Darboux: build one ceiling (sup) and one floor (inf) staircase; integrability = the gap between ceiling and floor can be squeezed to zero.
**Animation:** `riemannWidget`/`darbouxWidget` as specified in B.3/E.4/D.4; for Simpson, draw the actual parabolic arcs over each pair of subintervals so the "curved roof" is visible; animate n increasing (Play) with the error readout shrinking at visibly different *rates* per method — the geometric meaning of order of accuracy.

### GEO-8 — u-substitution (used by B.3)
**Picture:** A change of variables is a **rubber-sheet re-gridding** of the x-axis: u = g(x) stretches/compresses the axis non-uniformly; the factor du = g'(x)dx is exactly the local stretch factor, so area is preserved — same area, more convenient shape.
**Animation (optional widget `usubWidget`, VIZ-2):** left plot: area under 2x·cos(x²); right plot: area under cos(u); animate vertical strips of the left area sliding/stretching into position on the right, strip widths visibly changing by the factor g'(x) while total area readout stays constant.

### GEO-9 — Integration by parts (used by B.3)
**Picture:** Draw the curve as (x, y=f(x)) in the plane and the rectangle [0,x]×[0,y] around a point on it: the rectangle's area x·y splits into the area under the curve counted horizontally (∫y dx) plus the area counted vertically (∫x dy). The formula ∫u dv = uv − ∫v du is literally this picture.
**Animation:** static canvas figure is enough (no sliders required): shade the two complementary regions in `c.curve`/`c.accent` at alpha 0.25 inside the uv-rectangle, label the three areas.

### GEO-10 — Chain rule (used by B.2)
**Picture:** Composition is a two-stage machine: g stretches the input tape locally by g'(x), then f stretches g's output tape by f'(g(x)). Local stretch factors **multiply** — that's the whole rule.
**Animation (optional, text figure acceptable):** three horizontal number lines (x → u=g(x) → y=f(u)); animate a small interval flowing through both stages, its width multiplying at each stage, readout showing widths: dx → g'·dx → f'·g'·dx.

### GEO-11 — Eigenvector search (used by C.4)
**Picture:** A matrix mostly *turns* vectors; eigenvectors are the directions the matrix refuses to turn — it only stretches them (by λ). Sweeping a unit vector through 360° and watching Ax, the eigendirections are the moments x and Ax line up. Power iteration remark: repeatedly applying A turns every vector toward the dominant eigendirection — animate A applied 5 times to a random vector, each image normalized, visibly converging.
**Animation:** `eigenWidget` as in C.4, plus the optional power-iteration Play mode above.

### GEO-12 — Jacobi iteration (used by D.6)
**Picture:** Cobweb toward the crossing: from a guess, satisfy equation 1 exactly (move horizontally onto line 1), then equation 2 exactly (move vertically onto line 2), repeat. With diagonally dominant systems the staircase spirals *into* the intersection; otherwise it can spiral out — convergence made visible.
**Animation (`jacobiWidget`, VIZ-6, 2×2 case):** two lines + starting dot; each Step draws one segment of the horizontal/vertical staircase; readout: iterate table + distance to solution. Toggle between a dominant and a non-dominant system to show divergence.

### GEO-13 — Condition number (used by D.6)
**Picture:** Nearly parallel lines have a well-defined but *fragile* intersection: wiggle one line a hair and the crossing leaps. Condition number = how many times the leap magnifies the wiggle.
**Animation (`condWidget`):** two nearly parallel lines, a slider adds a tiny perturbation ±ε to one intercept; solution dot leaps; a second well-conditioned (near-perpendicular) pair shown side by side barely reacts; readout: κ and the ratio Δsolution/Δdata.

### GEO-14 — Lagrange interpolation (used by D.3)
**Picture:** Each basis polynomial ℓᵢ is a switch: 1 at its own node, 0 at all others. The interpolant is the superposition Σyᵢℓᵢ — each data point broadcasts its own bump, and at each node all other bumps are silent.
**Animation (`interpWidget` extension):** checkbox "show basis": plot each yᵢ·ℓᵢ(x) as a faint colored curve; animate them summing (stack curves one at a time) into the final interpolant passing exactly through all points. Runge phenomenon: button loading 9 equispaced nodes on 1/(1+25x²) — wild edge oscillations appear; geometric lesson stated: high-degree "switches" ring near the interval ends.

### GEO-15 — Series convergence tests (used by E.2)
**Picture:** A series is a stack of bars of widths 1 and heights aₙ laid along the n-axis; convergence = the total stacked area is finite. Comparison test: your stack fits under a stack already known finite. Ratio test: eventually each bar is at most r<1 times the previous — the stack fits under a geometric staircase. Harmonic divergence by grouping: bundle bars [1/2], [1/3+1/4], [1/5..1/8], … each bundle's area ≥ 1/2 — infinitely many half-bricks.
**Animation (`seriesWidget`, VIZ-6):** bar-stack view of Σ1/n with the grouping brackets drawn and each bundle flashing when its area passes 1/2; toggle to Σ1/n² with an overlaid dominating geometric staircase that visibly contains it.

### GEO-16 — Completing the square (used by A.2)
**Picture:** Algebra tiles, literally: x² is a square, bx is a strip; cut the strip in half, hang the halves on two sides of the square — an L-shape one corner short of a perfect square; the missing corner is (b/2)². The identity x²+bx = (x+b/2)² − (b/2)² is this picture.
**Animation (optional `csqWidget`, VIZ-2; a static two-frame figure is acceptable):** animate the two half-strips sliding from a row layout onto the square's right and bottom edges, then the missing (b/2)² corner blinking in dashed outline.

### GEO-17 — Green/Gauss/Stokes (already specified)
The theorem animations are fully specified in Tasks B.5–B.7; their unifying geometric sentence (use it in all three texts): *"add up a local quantity (curl / divergence) over the inside, and everything cancels except at the boundary — the boundary remembers the sum."*

### Usage table (agent quick reference)

| Algorithm | Appendix | Task(s) | Widget | Base |
|---|---|---|---|---|
| Gaussian elimination | GEO-1 | C.3, D.6 | gaussGeoWidget | VIZ-2 |
| Bisection | GEO-2 | D.1, E.4 | bisectWidget | VIZ-6 |
| Newton–Raphson | GEO-3 | D.2 | newtonWidget | VIZ-6 |
| Least squares | GEO-4 | D.3 | interpWidget(fit) | VIZ-0 |
| Euler | GEO-5 | D.5 | odeWidget | VIZ-6 |
| RK4 | GEO-6 | D.5 | odeWidget | VIZ-6 |
| Riemann/trap/Simpson | GEO-7 | B.3, D.4, E.4 | riemann/darbouxWidget | VIZ-6 |
| u-substitution | GEO-8 | B.3 | usubWidget (opt) | VIZ-2 |
| Integration by parts | GEO-9 | B.3 | static figure | — |
| Chain rule | GEO-10 | B.2 | static/opt | — |
| Eigenvector search | GEO-11 | C.4 | eigenWidget | VIZ-2 |
| Jacobi iteration | GEO-12 | D.6 | jacobiWidget | VIZ-6 |
| Conditioning | GEO-13 | D.6 | condWidget | VIZ-0 |
| Lagrange basis | GEO-14 | D.3 | interpWidget | VIZ-0 |
| Series tests | GEO-15 | E.2 | seriesWidget | VIZ-6 |
| Completing the square | GEO-16 | A.2 | csqWidget (opt) | VIZ-2 |
| Green/Gauss/Stokes | GEO-17 | B.5–B.7 | green/gauss/stokesWidget | VIZ-5 |
