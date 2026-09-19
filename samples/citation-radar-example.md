# Citation Radar - Worked Example

Pairs with the `citation-radar` skill. Fictional product: **ACME Insight Studio**.

## CLEAR scorecard

Weights: Claim density 0.25 · Liftability 0.15 · Evidence 0.20 · Answer match 0.25 · Rarity 0.15

| Page | C | L | E | A | R | CLEAR | Band |
|---|:-:|:-:|:-:|:-:|:-:|:-:|---|
| /pricing | 8 | 7 | 6 | 9 | 8 | **77** | Citable |
| /compare/acme-vs-legacy-bi | 6 | 4 | 5 | 7 | 5 | **56** | Fixable |
| /blog/what-is-insight-studio | 4 | 6 | 4 | 6 | 2 | **45** | Invisible |

Example: /pricing = 10 × (0.25·8 + 0.15·7 + 0.20·6 + 0.25·9 + 0.15·8) = 10 × 7.7 = 77.

## Fix queue

Priority = monthly question volume × (75 − CLEAR), floored at 0.

| Page | Buyer question | Volume | Priority | Fix |
|---|---|:-:|:-:|---|
| /compare/acme-vs-legacy-bi | "Is ACME faster than legacy BI for weekly reporting?" | 20 | 380 | Add a dated benchmark table in the first screen; move the answer above the fold |
| /blog/what-is-insight-studio | "What does ACME Insight Studio do?" | 12 | 360 | Open with a one-sentence definition; add two named customer outcomes with numbers |
| /pricing | "How much does ACME cost per seat?" | 30 | 0 | Already citable; refresh the date quarterly |

**Reading the result:** the comparison page is the fastest win: assistants already quote a competitor's table for that question, and one dated benchmark closes the gap.
