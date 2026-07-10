import math
import tkinter as tk
from tkinter import font

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


BG = "#1e1e2e"
DISPLAY_BG = "#11111b"
DISPLAY_FG = "#cdd6f4"
RENDER_FG = "#f5c2e7"
NUM_BG = "#313244"
NUM_FG = "#cdd6f4"
OP_BG = "#f9e2af"
OP_FG = "#1e1e2e"
ACCENT_BG = "#f38ba8"
ACCENT_FG = "#1e1e2e"
EQ_BG = "#a6e3a1"
EQ_FG = "#1e1e2e"
SCI_BG = "#89b4fa"
SCI_FG = "#1e1e2e"
TOGGLE_OFF_BG = "#45475a"
TOGGLE_OFF_FG = "#cdd6f4"
HOVER = "#585b70"

FUNCTIONS = ("sin", "cos", "tan", "log", "ln")


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dennis")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar(value="0")
        self.history_var = tk.StringVar(value="")
        self.sci_visible = False
        self.deg_mode = True

        self._build_ui()
        self._bind_keys()
        self._render_math("")

    def _build_ui(self):
        container = tk.Frame(self.root, bg=BG, padx=16, pady=16)
        container.pack()

        history_font = font.Font(family="Helvetica", size=14)
        display_font = font.Font(family="Helvetica", size=34, weight="bold")
        toggle_font = font.Font(family="Helvetica", size=11, weight="bold")

        toolbar = tk.Frame(container, bg=BG)
        toolbar.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 6))

        self.sci_btn = tk.Button(
            toolbar,
            text="SCI",
            bg=TOGGLE_OFF_BG,
            fg=TOGGLE_OFF_FG,
            font=toggle_font,
            bd=0,
            relief="flat",
            padx=10,
            pady=3,
            cursor="hand2",
            command=self._toggle_sci,
        )
        self.sci_btn.pack(side="left", padx=(0, 6))

        self.angle_btn = tk.Button(
            toolbar,
            text="DEG",
            bg=SCI_BG,
            fg=SCI_FG,
            font=toggle_font,
            bd=0,
            relief="flat",
            padx=10,
            pady=3,
            cursor="hand2",
            command=self._toggle_angle,
        )
        self.angle_btn.pack(side="left")

        self.plot_btn = tk.Button(
            toolbar,
            text="PLOT",
            bg=EQ_BG,
            fg=EQ_FG,
            font=toggle_font,
            bd=0,
            relief="flat",
            padx=10,
            pady=3,
            cursor="hand2",
            command=self._open_plot,
        )
        self.plot_btn.pack(side="left", padx=(6, 0))

        tk.Label(
            container,
            textvariable=self.history_var,
            anchor="e",
            bg=DISPLAY_BG,
            fg="#6c7086",
            font=history_font,
            padx=14,
            pady=6,
            width=14,
        ).grid(row=1, column=0, columnspan=4, sticky="ew")

        tk.Label(
            container,
            textvariable=self.display_var,
            anchor="e",
            bg=DISPLAY_BG,
            fg=DISPLAY_FG,
            font=display_font,
            padx=14,
            pady=14,
            width=10,
        ).grid(row=2, column=0, columnspan=4, sticky="ew", pady=(0, 6))

        self.render_fig = Figure(figsize=(4.2, 0.9), facecolor=DISPLAY_BG)
        self.render_ax = self.render_fig.add_subplot(111)
        self.render_ax.set_facecolor(DISPLAY_BG)
        self.render_ax.axis("off")
        self.render_fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
        self.render_canvas = FigureCanvasTkAgg(self.render_fig, master=container)
        render_widget = self.render_canvas.get_tk_widget()
        render_widget.configure(bg=DISPLAY_BG, highlightthickness=0)
        render_widget.grid(row=3, column=0, columnspan=4, sticky="ew", pady=(0, 12))

        btn_font = font.Font(family="Helvetica", size=18, weight="bold")
        sci_font = font.Font(family="Helvetica", size=14, weight="bold")

        sci_buttons = [
            ("sin", 4, 0, 1), ("cos", 4, 1, 1), ("tan", 4, 2, 1), ("π", 4, 3, 1),
            ("log", 5, 0, 1), ("ln", 5, 1, 1), ("√", 5, 2, 1), ("ℯ", 5, 3, 1),
            ("x²", 6, 0, 1), ("xʸ", 6, 1, 1), ("(", 6, 2, 1), (")", 6, 3, 1),
            ("x", 7, 0, 4),
        ]

        self.sci_widgets = []
        for (text, row, col, span) in sci_buttons:
            btn = self._make_button(container, text, SCI_BG, SCI_FG, sci_font)
            btn.grid(row=row, column=col, columnspan=span, padx=4, pady=4, sticky="nsew")
            btn.grid_remove()
            self.sci_widgets.append(btn)

        main_buttons = [
            ("C", 8, 0, ACCENT_BG, ACCENT_FG),
            ("⌫", 8, 1, ACCENT_BG, ACCENT_FG),
            ("%", 8, 2, OP_BG, OP_FG),
            ("/", 8, 3, OP_BG, OP_FG),
            ("7", 9, 0, NUM_BG, NUM_FG),
            ("8", 9, 1, NUM_BG, NUM_FG),
            ("9", 9, 2, NUM_BG, NUM_FG),
            ("*", 9, 3, OP_BG, OP_FG),
            ("4", 10, 0, NUM_BG, NUM_FG),
            ("5", 10, 1, NUM_BG, NUM_FG),
            ("6", 10, 2, NUM_BG, NUM_FG),
            ("-", 10, 3, OP_BG, OP_FG),
            ("1", 11, 0, NUM_BG, NUM_FG),
            ("2", 11, 1, NUM_BG, NUM_FG),
            ("3", 11, 2, NUM_BG, NUM_FG),
            ("+", 11, 3, OP_BG, OP_FG),
            ("0", 12, 0, NUM_BG, NUM_FG),
            (".", 12, 2, NUM_BG, NUM_FG),
            ("=", 12, 3, EQ_BG, EQ_FG),
        ]

        for (text, row, col, bg, fg) in main_buttons:
            colspan = 2 if text == "0" else 1
            btn = self._make_button(container, text, bg, fg, btn_font)
            btn.grid(row=row, column=col, columnspan=colspan, padx=4, pady=4, sticky="nsew")

    def _make_button(self, parent, text, bg, fg, btn_font):
        btn = tk.Button(
            parent,
            text=text,
            bg=bg,
            fg=fg,
            font=btn_font,
            activebackground=HOVER,
            activeforeground=DISPLAY_FG,
            bd=0,
            relief="flat",
            width=4,
            height=2,
            cursor="hand2",
            command=lambda t=text: self._on_press(t),
        )
        btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=HOVER))
        btn.bind("<Leave>", lambda e, b=btn, c=bg: b.configure(bg=c))
        return btn

    def _bind_keys(self):
        for ch in "0123456789.+-*/%()x":
            self.root.bind(ch, lambda e, c=ch: self._on_press(c))
        self.root.bind("<Return>", lambda e: self._on_press("="))
        self.root.bind("<KP_Enter>", lambda e: self._on_press("="))
        self.root.bind("<BackSpace>", lambda e: self._on_press("⌫"))
        self.root.bind("<Escape>", lambda e: self._on_press("C"))

    def _toggle_sci(self):
        self.sci_visible = not self.sci_visible
        if self.sci_visible:
            for w in self.sci_widgets:
                w.grid()
            self.sci_btn.configure(bg=SCI_BG, fg=SCI_FG)
        else:
            for w in self.sci_widgets:
                w.grid_remove()
            self.sci_btn.configure(bg=TOGGLE_OFF_BG, fg=TOGGLE_OFF_FG)

    def _toggle_angle(self):
        self.deg_mode = not self.deg_mode
        self.angle_btn.configure(text="DEG" if self.deg_mode else "RAD")

    def _on_press(self, key):
        if key == "C":
            self.expression = ""
            self.history_var.set("")
            self.display_var.set("0")
            self._render_math("")
            return

        if key == "⌫":
            for token in ("sin(", "cos(", "tan(", "log(", "ln(", "√("):
                if self.expression.endswith(token):
                    self.expression = self.expression[: -len(token)]
                    self.display_var.set(self.expression or "0")
                    self._render_math(self.expression)
                    return
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression or "0")
            self._render_math(self.expression)
            return

        if key == "=":
            self._evaluate()
            return

        if self.display_var.get() in ("Error", "∞"):
            self.expression = ""

        if key in FUNCTIONS or key == "√":
            self.expression += f"{key}("
        elif key == "x²":
            self.expression += "**2"
        elif key == "xʸ":
            self.expression += "**"
        else:
            self.expression += key

        self.display_var.set(self.expression)
        self._render_math(self.expression)

    def _evaluate(self):
        if not self.expression:
            return

        expr = (
            self.expression
            .replace("π", "PI")
            .replace("ℯ", "E_CONST")
            .replace("√", "sqrt")
        )

        if self.deg_mode:
            trig = {
                "sin": lambda x: math.sin(math.radians(x)),
                "cos": lambda x: math.cos(math.radians(x)),
                "tan": lambda x: math.tan(math.radians(x)),
            }
        else:
            trig = {"sin": math.sin, "cos": math.cos, "tan": math.tan}

        safe_ns = {
            "PI": math.pi,
            "E_CONST": math.e,
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            **trig,
        }

        try:
            result = eval(expr, {"__builtins__": {}}, safe_ns)
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)
            self.history_var.set(f"{self.expression} =")
            self.display_var.set(str(result))
            self._render_math(f"{self.expression}={result}")
            self.expression = str(result)
        except ZeroDivisionError:
            self.history_var.set(self.expression)
            self.display_var.set("∞")
            self._render_math(self.expression)
            self.expression = ""
        except Exception:
            self.history_var.set(self.expression)
            self.display_var.set("Error")
            self._render_math(self.expression)
            self.expression = ""

    def _open_plot(self):
        if not self.expression:
            return

        win = tk.Toplevel(self.root)
        win.title(f"Plot — {self.expression}")
        win.configure(bg=BG)

        controls = tk.Frame(win, bg=BG)
        controls.pack(fill="x", padx=10, pady=8)

        label_font = font.Font(family="Helvetica", size=11)
        tk.Label(controls, text="x min", bg=BG, fg=DISPLAY_FG, font=label_font).pack(side="left")
        xmin_var = tk.StringVar(value="-10")
        tk.Entry(controls, textvariable=xmin_var, width=6, bg=DISPLAY_BG, fg=DISPLAY_FG,
                 insertbackground=DISPLAY_FG, bd=0, relief="flat").pack(side="left", padx=(4, 12))

        tk.Label(controls, text="x max", bg=BG, fg=DISPLAY_FG, font=label_font).pack(side="left")
        xmax_var = tk.StringVar(value="10")
        tk.Entry(controls, textvariable=xmax_var, width=6, bg=DISPLAY_BG, fg=DISPLAY_FG,
                 insertbackground=DISPLAY_FG, bd=0, relief="flat").pack(side="left", padx=(4, 12))

        fig = Figure(figsize=(6.5, 4.5), facecolor=BG)
        ax = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master=win)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.configure(bg=BG, highlightthickness=0)
        canvas_widget.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        def draw():
            try:
                xmin = float(xmin_var.get())
                xmax = float(xmax_var.get())
                if xmax <= xmin:
                    raise ValueError("x max must exceed x min")
                x = np.linspace(xmin, xmax, 800)
                with np.errstate(all="ignore"):
                    y = self._eval_for_x(self.expression, x)
                y = np.asarray(y, dtype=float)
                if y.ndim == 0:
                    y = np.full_like(x, float(y))
                y = np.where(np.abs(y) > 1e6, np.nan, y)
            except Exception as e:
                ax.clear()
                ax.set_facecolor(DISPLAY_BG)
                ax.text(0.5, 0.5, f"Plot error:\n{e}", ha="center", va="center",
                        color="#f38ba8", fontsize=14, transform=ax.transAxes)
                ax.axis("off")
                canvas.draw()
                return

            ax.clear()
            ax.set_facecolor(DISPLAY_BG)
            ax.plot(x, y, color=RENDER_FG, linewidth=2)
            ax.axhline(0, color="#45475a", linewidth=0.8)
            ax.axvline(0, color="#45475a", linewidth=0.8)
            ax.tick_params(colors=DISPLAY_FG)
            for spine in ax.spines.values():
                spine.set_color("#45475a")
            ax.grid(True, color="#313244", linewidth=0.5)
            mt = self._to_mathtext(self.expression)
            try:
                ax.set_title(f"$y = {mt}$", color=RENDER_FG, fontsize=15, pad=10)
            except Exception:
                ax.set_title(f"y = {self.expression}", color=RENDER_FG, fontsize=13, pad=10)
            fig.tight_layout()
            canvas.draw()

        tk.Button(controls, text="Replot", bg=EQ_BG, fg=EQ_FG, bd=0,
                  padx=12, pady=4, cursor="hand2", command=draw).pack(side="left", padx=(4, 0))

        draw()

    def _eval_for_x(self, expression, x):
        expr = (
            expression
            .replace("π", "PI")
            .replace("ℯ", "E_CONST")
            .replace("√", "sqrt")
        )
        if self.deg_mode:
            trig = {
                "sin": lambda v: np.sin(np.radians(v)),
                "cos": lambda v: np.cos(np.radians(v)),
                "tan": lambda v: np.tan(np.radians(v)),
            }
        else:
            trig = {"sin": np.sin, "cos": np.cos, "tan": np.tan}

        ns = {
            "PI": np.pi,
            "E_CONST": np.e,
            "sqrt": np.sqrt,
            "log": np.log10,
            "ln": np.log,
            "x": x,
            **trig,
        }
        return eval(expr, {"__builtins__": {}}, ns)

    def _render_math(self, expression):
        self.render_ax.clear()
        self.render_ax.set_facecolor(DISPLAY_BG)
        self.render_ax.axis("off")
        if expression:
            mathtext = self._to_mathtext(expression)
            try:
                self.render_ax.text(
                    0.5, 0.5, f"${mathtext}$",
                    fontsize=22, color=RENDER_FG,
                    ha="center", va="center",
                )
                self.render_canvas.draw()
            except Exception:
                self.render_ax.clear()
                self.render_ax.set_facecolor(DISPLAY_BG)
                self.render_ax.axis("off")
                self.render_ax.text(
                    0.5, 0.5, expression,
                    fontsize=16, color="#6c7086",
                    ha="center", va="center",
                )
                self.render_canvas.draw()
        else:
            self.render_canvas.draw()

    def _to_mathtext(self, expr):
        s = self._wrap_sqrt(expr)
        s = self._wrap_powers(s)
        for fn in FUNCTIONS:
            s = s.replace(fn, rf"\{fn} ")
        s = s.replace("π", r"\pi ")
        s = s.replace("ℯ", "e")
        s = s.replace("*", r"\cdot ")
        s = s.replace("%", r"\,\%\,")
        return s

    def _wrap_sqrt(self, s):
        i = 0
        while True:
            idx = s.find("√", i)
            if idx == -1:
                return s
            if idx + 1 >= len(s) or s[idx + 1] != "(":
                i = idx + 1
                continue
            depth = 0
            j = idx + 1
            while j < len(s):
                if s[j] == "(":
                    depth += 1
                elif s[j] == ")":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            if j >= len(s):
                return s
            inner = s[idx + 2:j]
            replacement = r"\sqrt{" + inner + "}"
            s = s[:idx] + replacement + s[j + 1:]
            i = idx + len(replacement)

    def _wrap_powers(self, s):
        i = 0
        while True:
            idx = s.find("**", i)
            if idx == -1:
                return s
            start = idx + 2
            if start >= len(s):
                return s
            if s[start] == "(":
                depth = 0
                j = start
                while j < len(s):
                    if s[j] == "(":
                        depth += 1
                    elif s[j] == ")":
                        depth -= 1
                        if depth == 0:
                            j += 1
                            break
                    j += 1
                operand = s[start + 1:j - 1]
            else:
                j = start
                if j < len(s) and s[j] in "+-":
                    j += 1
                if j < len(s) and (s[j].isdigit() or s[j] == "."):
                    while j < len(s) and (s[j].isdigit() or s[j] == "."):
                        j += 1
                elif j < len(s) and s[j] not in "+-*/%()":
                    j += 1
                operand = s[start:j]
                if not operand:
                    i = idx + 2
                    continue
            replacement = "^{" + operand + "}"
            s = s[:idx] + replacement + s[j:]
            i = idx + len(replacement)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
