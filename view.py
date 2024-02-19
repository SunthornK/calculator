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
        self.keys = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.','mod']
        self.operator = ['C','+', '-', '*', '/', '^','=' ]
        self.total_output = ""
        self.txt_input = "0"
        self.init_components()

    def init_components(self):
        """create all the ui"""
        self.center_window()
        self.minsize(400, 300)
        self.total_display, self.display = self.display_label()
        # Create and configure keypad
        keypad = Keypad(self, keynames=self.keys, columns=3)
        keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        keypad['font'] = ('Monospace', 16)
        keypad.bind("<Button>", self.controller.display_button_click)
        keypad.bind("<Button>", self.controller.display_keypad, '+')

        # Create and configure operator pad
        operators = Keypad(self, keynames=self.operator, columns=1)
        operators.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        operators['font'] = ('Monospace', 16)
        operators.bind("<Button>", self.controller.display_button_click)
        operators.bind("<Button>", self.controller.display_keypad, '+')

        # Bind key press event to display method
        self.bind("<KeyPress>", self.controller.display_keypad)

    def display_label(self):
        total_display = tk.Label(justify='right', anchor=tk.E, text=self.total_output, **SMALL_FONT)
        total_display.pack(expand=True, fill=tk.BOTH, padx=5)
        display = tk.Label(justify='right', anchor=tk.E, text=self.txt_input, **BIG_FONT)
        display.pack(expand=True, fill=tk.BOTH, padx=5)
        return total_display, display

    def update_label(self, update_text):
        if self.txt_input == "":
            self.txt_input = "0"
        elif self.txt_input == "0":
            self.txt_input = ""
        self.txt_input += update_text
        self.display.config(text=self.txt_input)
        self.total_display.config(text=self.total_output)

    def replace_label(self, update_text):
        self.txt_input = update_text
        if self.txt_input == "":
            self.txt_input = "0"
        elif self.txt_input == "0":
            self.txt_input = ""
        self.display.config(text=self.txt_input)
        self.total_display.config(text=self.total_output)

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2
        self.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

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
