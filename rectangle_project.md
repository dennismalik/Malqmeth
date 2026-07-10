# Python Learning Notes — 2026-05-23

Chat with Claude covering `def`, `return`, function calls, and classes.

---

## 1. `def` and `return`

### `def` — defining a function
`def` creates a reusable block of code:
```python
def function_name(parameters):
    # code goes here
```

Defining does NOT run the code. It only runs when you **call** it.

Example from your `surfacing_original.py` line 41:
```python
def calculate_surface():
    ...
```

### `return` — sending a value back
`return` ends the function and hands a value back to the caller.

From your code line 63:
```python
return text, circle_area, shape_area, leftover_area
```
This returns 4 values as a tuple, which you unpack on line 65:
```python
text, circle_area, shape_area, leftover_area = calculate_surface()
```

### `return` vs `print`
- `print` → just displays on screen
- `return` → gives back a value you can store, reuse, or pass into another function

```python
def add(a, b):
    return a + b

result = add(2, 3)   # result is now 5
print(result * 10)   # 50
```

### Key rules
1. A function without `return` returns `None`.
2. Once `return` runs, the function STOPS immediately.
3. You can return multiple values (Python wraps them in a tuple).

---

## 2. Defining vs Calling a function

- **Defining** = writing the recipe (`def` block). Nothing runs yet.
- **Calling** = writing `function_name()` to actually run it.

Calls happen INSIDE your Python file, NOT in the terminal. The terminal just launches the file (`python surfacing_original.py`) and shows input/output.

```python
def say_hello():              # DEFINING
    print("Hello!")

say_hello()                   # CALLING (parentheses = run it now)
```

### Calling with arguments
```python
def greet(name):           # 'name' is a parameter
    print(f"Hi, {name}")

greet("Dennis")            # "Dennis" is the argument
```

---

## 3. The rectangle / cartesian coordinates project

### Building blocks
1. **Custom data type** = `class`
   ```python
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y
   ```
2. **Randomness** → `import random` (`random.sample(list, 4)` picks 4 unique items)
3. **Graph display** → `import matplotlib.pyplot as plt`
   Install once in terminal: `pip install matplotlib`

### Rectangle rule (axis-aligned)
4 points form a rectangle if there are **exactly 2 unique x-values and 2 unique y-values**.

Example: `(1,2), (1,5), (4,2), (4,5)` → xs `{1,4}`, ys `{2,5}` → ✅

### Execution flow
1. Use the nested loop (lines 104–107) to build a list of all possible `Point` objects (append instead of print).
2. Randomly pick 4 points.
3. `is_rectangle(points)` returns `True` / `False`.
4. Store results into `successful = []` and `failed = []`.
5. Plot with matplotlib — green for success, red for fail.
6. `plt.show()` opens the graph.

### Skeleton (to replace lines 104–107)
```python
import random
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def is_rectangle(pts):
    xs = {p.x for p in pts}
    ys = {p.y for p in pts}
    return len(xs) == 2 and len(ys) == 2

# 1. build all possible points
all_points = []
for i in range(x):
    for j in range(y):
        all_points.append(Point(i, j))

# 2. try N random combinations
successful, failed = [], []
for _ in range(20):
    pick = random.sample(all_points, 4)
    if is_rectangle(pick):
        successful.append(pick)
    else:
        failed.append(pick)

# 3. plot
for rect in successful:
    plt.scatter([p.x for p in rect], [p.y for p in rect], color="green")
for rect in failed:
    plt.scatter([p.x for p in rect], [p.y for p in rect], color="red")

plt.show()
```

### How to run
```
pip install matplotlib       # one-time install
python surfacing_original.py
```

---

## 4. `__init__` vs a regular function

| | `__init__` | `is_rectangle` |
|---|---|---|
| What is it? | Method inside `Point` class | Standalone function |
| When does it run? | Automatically when you write `Point(...)` | Only when you explicitly call it |
| What does it do? | Stores x and y on a new object | Checks if 4 points form a rectangle |
| What does it return? | Nothing (None) — just sets attributes | `True` or `False` |

### `__init__` doesn't generate coordinates
It just STORES whatever you hand it:
```python
p = Point(3, 5)
print(p.x)    # 3
print(p.y)    # 5
```
The actual coordinate generation happens in the nested loop using `i` and `j`.

### `is_rectangle` checks points
```python
def is_rectangle(pts):
    xs = {p.x for p in pts}       # collect unique x-values
    ys = {p.y for p in pts}       # collect unique y-values
    return len(xs) == 2 and len(ys) == 2
```

The `return` line is shorthand for:
```python
if len(xs) == 2 and len(ys) == 2:
    return True
else:
    return False
```
Because the expression already evaluates to `True`/`False`, you can return it directly.

---

## Next step
You're going to try building the rectangle project yourself, replacing lines 104–107 in `surfacing_original.py`.
