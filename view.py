import tkinter as tk
from tkinter import ttk

GRAY = "#F5F5F5"
NAVY = "#25265E"
BIG_FONT = {"font": ("Arial", 32), "fg": NAVY, "bg": GRAY}
SMALL_FONT = {"font": ("Arial", 16), "fg": NAVY, "bg": GRAY}


class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Calculator")
        self.keys = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', 'mod']
        self.operator = ['CLR', '+', '-', '*', '/', '^', '=']
        self.special_operator = ['(', ')', 'π', '!', 'DEL']
        self.functions = ['exp', 'ln', 'log10', 'log2', 'sqrt']
        self.init_components()

    def init_components(self):
        """create all the ui"""
        self.center_window()
        self.minsize(400, 500)
        history_label = tk.Label(text='History', font=('Arial', 12))
        history_label.pack()
        self.history_combobox = ttk.Combobox(self, font=('Arial', 12), state='readonly')
        self.history_combobox.pack(pady=10, expand=True, fill=tk.X)
        self.history_combobox.bind('<<ComboboxSelected>>', self.history_combobox_selected)
        self.display_label()
        self.function_combobox = ttk.Combobox(self, values=self.functions, font=('Arial', 12))
        self.function_combobox.pack(pady=10)
        self.function_combobox.bind('<<ComboboxSelected>>', self.combobox_selected)

        # Create and configure keypad
        special = Keypad(self, keynames=self.special_operator, columns=5)
        special.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        special['font'] = ('Monospace', 16)
        special.bind("<Button>", self.button_click)

        keypad = Keypad(self, keynames=self.keys, columns=3)
        keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        keypad['font'] = ('Monospace', 16)
        keypad.bind("<Button>", self.button_click)

        # Create and configure operator pad
        operators = Keypad(self, keynames=self.operator, columns=1)
        operators.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        operators['font'] = ('Monospace', 16)
        operators.bind("<Button>", self.button_click)

    def combobox_selected(self, event):
        selected_function = self.function_combobox.get()
        self.controller.process_input(selected_function)

    def history_combobox_selected(self, event):
        selected_item = self.history_combobox.get()
        self.controller.display_selected_item(selected_item)

    def display_label(self):
        self.total_display = tk.Label(self, anchor=tk.E, text="", **SMALL_FONT)
        self.total_display.pack(expand=True, fill=tk.BOTH, padx=10)
        self.display = tk.Entry(self, justify='right', **BIG_FONT)
        self.display.pack(expand=True, fill=tk.BOTH, padx=10)

    def button_click(self, event):
        button_text = event.widget.cget("text")
        self.controller.process_input(button_text)

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2
        self.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

    def update_total_display(self, expression):
        self.total_display.config(text=expression)

    def update_display(self, expression):
        self.display.delete(0, tk.END)
        self.display.insert(0, expression)

    def update_history_combobox(self, history):
        self.history_combobox['values'] = history

    def run(self):
        self.mainloop()


class Keypad(tk.Frame):

    def __init__(self, parent, keynames=[], columns=1, **kwargs):

        # keynames and columns
        super().__init__()
        self.parent = parent
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        options = {'padx': 2, 'pady': 2, 'sticky': tk.NSEW}
        for i in range(columns):
            self.grid_columnconfigure(i, weight=1)
        num_rows = len(self.keynames) // columns + (len(self.keynames) % columns)
        for j in range(num_rows):
            self.grid_rowconfigure(j, weight=1)
        for index, value in enumerate(self.keynames):
            row = index // columns
            col = index % columns
            button = tk.Button(self, text=value)
            button.grid(row=row, column=col, **options)

    def bind(self, key, todo, add=None):
        """Bind an event handler to an event sequence."""
        for i in self.winfo_children():
            i.bind(key, todo, add)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for i in self.winfo_children():
            i[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        return self.winfo_children()[0][key]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        for i in self.winfo_children():
            i.configure(cnf)

    @property
    def frame(self):
        """Returns a reference to the superclass object for this keypad."""
        return super()
