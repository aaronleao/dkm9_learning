# Mathematical Logic

## Beginner Level

### What is Logic?

**Mathematical logic** is the study of reasoning and proof. It provides the foundation for all mathematics by formalizing the rules of valid reasoning.

### Propositions and Truth Values

A **proposition** (or **statement**) is a declarative sentence that is either true or false (not both).

**Examples:**
- "2 + 2 = 4" is a proposition (true)
- "3 > 7" is a proposition (false)
- "Is it raining?" is not a proposition (it's a question)

#### Truth Tables

Truth values are denoted:
- $T$ or $1$ for true
- $F$ or $0$ for false

### Logical Operators

#### Negation (NOT)
The **negation** of proposition $P$, denoted $\neg P$ or $\overline{P}$, is true when $P$ is false and vice versa.

| $P$ | $\neg P$ |
|-----|----------|
| T   | F        |
| F   | T        |

#### Conjunction (AND)
The **conjunction** of propositions $P$ and $Q$, denoted $P \land Q$, is true only when both $P$ and $Q$ are true.

| $P$ | $Q$ | $P \land Q$ |
|-----|-----|------------|
| T   | T   | T          |
| T   | F   | F          |
| F   | T   | F          |
| F   | F   | F          |

#### Disjunction (OR)
The **disjunction** of propositions $P$ and $Q$, denoted $P \lor Q$, is true when at least one of $P$ or $Q$ is true.

| $P$ | $Q$ | $P \lor Q$ |
|-----|-----|-----------|
| T   | T   | T         |
| T   | F   | T         |
| F   | T   | T         |
| F   | F   | F         |

#### Conditional (Implication)
The **conditional** or **implication** $P \rightarrow Q$ (read "if $P$ then $Q$") is false only when $P$ is true and $Q$ is false.

| $P$ | $Q$ | $P \rightarrow Q$ |
|-----|-----|-----------------|
| T   | T   | T               |
| T   | F   | F               |
| F   | T   | T               |
| F   | F   | T               |

Key insight: A conditional with false premise is always true.

#### Biconditional
The **biconditional** $P \leftrightarrow Q$ (read "$P$ if and only if $Q$") is true when $P$ and $Q$ have the same truth value.

| $P$ | $Q$ | $P \leftrightarrow Q$ |
|-----|-----|------------------|
| T   | T   | T                |
| T   | F   | F                |
| F   | T   | F                |
| F   | F   | T                |

### Logical Equivalence

Two propositions are **logically equivalent**, denoted $\equiv$, if they have the same truth value in all cases.

**Example:** $\neg(P \land Q) \equiv (\neg P \lor \neg Q)$ (De Morgan's Law)

---

## Intermediate Level

### Quantifiers

#### Universal Quantifier
The **universal quantifier** $\forall$ (read "for all") denotes that a property holds for all elements in a domain.

$$\forall x \in D: P(x)$$

reads as "for all $x$ in domain $D$, property $P(x)$ holds."

**Example:** $\forall x \in \mathbb{R}: x^2 \geq 0$ (all real numbers squared are non-negative)

#### Existential Quantifier
The **existential quantifier** $\exists$ (read "there exists") denotes that a property holds for at least one element.

$$\exists x \in D: P(x)$$

reads as "there exists an $x$ in domain $D$ such that property $P(x)$ holds."

**Example:** $\exists x \in \mathbb{R}: x^2 = 4$ (there exists a real number whose square is 4)

#### Negation of Quantified Statements

$$\neg(\forall x: P(x)) \equiv \exists x: \neg P(x)$$
$$\neg(\exists x: P(x)) \equiv \forall x: \neg P(x)$$

### Logical Laws and Tautologies

A **tautology** is a proposition that is always true regardless of the truth values of its components.

#### Commutative Laws
$$P \land Q \equiv Q \land P$$
$$P \lor Q \equiv Q \lor P$$

#### Associative Laws
$$(P \land Q) \land R \equiv P \land (Q \land R)$$
$$(P \lor Q) \lor R \equiv P \lor (Q \lor R)$$

#### Distributive Laws
$$P \land (Q \lor R) \equiv (P \land Q) \lor (P \land R)$$
$$P \lor (Q \land R) \equiv (P \lor Q) \land (P \lor R)$$

#### De Morgan's Laws
$$\neg(P \land Q) \equiv \neg P \lor \neg Q$$
$$\neg(P \lor Q) \equiv \neg P \land \neg Q$$

#### Absorption Laws
$$P \lor (P \land Q) \equiv P$$
$$P \land (P \lor Q) \equiv P$$

### Implication and Contrapositive

For an implication $P \rightarrow Q$:
- **Contrapositive**: $\neg Q \rightarrow \neg P$ is logically equivalent to $P \rightarrow Q$
- **Converse**: $Q \rightarrow P$ is not necessarily equivalent
- **Inverse**: $\neg P \rightarrow \neg Q$ is not necessarily equivalent

$$P \rightarrow Q \equiv \neg Q \rightarrow \neg P$$

---

## Advanced Level

### Predicate Logic

**Predicate logic** extends propositional logic with predicates and quantifiers, allowing more expressive statements.

A **predicate** is a function $P: D \rightarrow \{T, F\}$ that assigns truth values to elements of a domain.

#### First-Order Logic (FOL)

First-order logic includes:
- Variables: $x, y, z, ...$
- Constants: $a, b, c, ...$
- Predicates: $P(x), Q(x, y), ...$
- Functions: $f(x), g(x, y), ...$
- Quantifiers: $\forall$, $\exists$
- Logical operators: $\neg$, $\land$, $\lor$, $\rightarrow$, $\leftrightarrow$

**Example:** The statement "all humans are mortal" can be expressed as:
$$\forall x: \text{Human}(x) \rightarrow \text{Mortal}(x)$$

#### Logical Consequence

A set of propositions $\Gamma$ **logically entails** a proposition $\phi$, denoted $\Gamma \vDash \phi$, if whenever all propositions in $\Gamma$ are true, $\phi$ must be true.

### Proof Techniques

#### Direct Proof
To prove $P \rightarrow Q$, assume $P$ is true and show $Q$ must be true.

#### Proof by Contradiction
To prove $P$, assume $\neg P$ and derive a contradiction, concluding $P$ must be true.

#### Proof by Contrapositive
To prove $P \rightarrow Q$, prove $\neg Q \rightarrow \neg P$ instead.

#### Mathematical Induction
To prove $P(n)$ for all $n \in \mathbb{N}$:
1. **Base case**: Show $P(1)$ is true
2. **Inductive step**: Assume $P(k)$ is true, show $P(k+1)$ must be true

---

## Research Level

### Gödel's Incompleteness Theorems

**Gödel's First Incompleteness Theorem**: In any consistent formal system $\mathcal{S}$ that is powerful enough to express arithmetic, there exists a true proposition that cannot be proven within $\mathcal{S}$.

**Gödel's Second Incompleteness Theorem**: A consistent formal system $\mathcal{S}$ cannot prove its own consistency.

These theorems have profound implications for the foundations of mathematics and show fundamental limits to formal mathematical systems.

### Gödel Numbers and Self-Reference

Gödel introduced a method of encoding logical formulas as natural numbers (Gödel numbering), enabling formulas to refer to themselves and proving the incompleteness theorems.

### Model Theory

**Model theory** studies the relationship between formal languages and mathematical structures:
- A **model** is a structure that interprets a formal language
- **Semantics** defines how formulas are evaluated in models
- **Completeness**: A formal system is complete if every true statement is provable

**Gödel's Completeness Theorem**: For first-order logic, a proposition is true in all models if and only if it is provable.
