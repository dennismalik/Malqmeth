# 🐍 Python Debugging Checklist (Beginner)

Built from the bugs I hit while writing the integral calculator in `surfacing_original.py`.
Keep this next to me while coding.

---

## The 5 error messages and what they REALLY mean

| Error | Plain-English meaning | My real example | Fix |
|-------|----------------------|-----------------|-----|
| `SyntaxError` | Python can't even *read* the line — grammar is broken | `for y = ... =>` | A `for` loop needs `in`, not `=`. `=>` isn't Python; "not equal" is `!=` |
| `TypeError` | The value is the *wrong kind* for what I'm doing | `if "/" in a` where `a` is a number | Check the *string* (`integral_values[1]`), not the int |
| `ValueError` | Right kind, but *this* value is impossible | `int("3/4")` | Split off the `/` first, then `int()` each piece |
| `IndexError` | Asked for a list item that isn't there | `"3".split("/")[1]` (no `/` exists) | Give a default: `... if "/" in power else 1` |
| `NameError` | Used a variable before creating it | `return f"{coefficient}..."` but never built `coefficient` | Assign a variable BEFORE using it |

---

## ⚠️ The sneakiest bug: NO error, but WRONG answer

The code runs happily and lies to me. Watch for these:

- [ ] **Printing the wrong variable** — e.g. printed `{a}` (the input) instead of `{coefficient}` (the result). Both exist, so no crash — but wrong.
- [ ] **A branch that never returns** — computed the value but forgot `return`, so it gave back `None`.
- [ ] **Backwards if/else** — returned the answer in the wrong branch.
- [ ] **Right formula, wrong meaning** — the same formula was correct for `(a/z)·xʸ` but wrong for `a·x^(y/j)`.

👉 **Rule: "No error" does NOT mean "correct." Always hand-check one example with a known answer.**

---

## ✅ My pre-flight checklist (run through this before trusting code)

1. [ ] **Does every variable exist before I use it?** (no `NameError`)
2. [ ] **Is each variable the right *kind*?** (string vs int — no `TypeError`)
3. [ ] **Could any `int()` get a value it can't convert?** (no `ValueError`)
4. [ ] **Could any `[index]` be out of range?** (no `IndexError` — add a default)
5. [ ] **Does EVERY branch of an if/else actually `return`?** (no surprise `None`)
6. [ ] **Am I printing the *computed* result, not the raw input?**
7. [ ] **Did I hand-check one example by hand?** (the most important step)

---

## Things I did WELL (keep doing these) 👏

- Caught the fractional-exponent math problem myself — real mathematical thinking.
- Used separate names `j` (exponent denominator) vs `z` (coefficient denominator) so two similar things don't get confused.
- Used a parentheses convention `(y/j)` vs `y/z` to make ambiguous input clear.

---

## Quick reference: comparison symbols

| Meaning | Symbol |
|---------|--------|
| equal to | `==` |
| **not equal to** | `!=` |
| greater than / or equal | `>` / `>=` |
| less than / or equal | `<` / `<=` |

⚠️ It's `>=` and `<=` — the `=` goes **after**. `=>` does not exist in Python.
