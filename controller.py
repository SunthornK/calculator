from model import Model
from view import View
from math import *


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def bind_keys(self):
        self.view.bind("<Key>", self.key_pressed)

    def key_pressed(self, event):
        key = event.char
        sym_key = event.keysym
        if key.isdigit() or key in ['+', '-', '*', '/', '^', '(', ')', '.', 'π', '!']:
            self.process_input(key)
        elif sym_key == "Return":
            self.update_total_display()
            self.model.evaluate_expression()
            self.update_display()
        elif sym_key == "BackSpace":
            self.model.delete_last()
        elif sym_key == "Escape":
            self.model.clear_expression()
        self.update_display()

    def process_input(self, value):
        if value.isdigit() or value in ['+', '-', '*', '/', '^', '(', ')', '.']:
            self.model.add_to_expression(value)
        elif value == '=':
            self.update_total_display()
            self.model.evaluate_expression()
        elif value == '!':
            # Call the factorial function on the last number in the expression
            expression = self.model.get_expression()
            last_number = int(expression.split()[-1])
            result = factorial(last_number)
            self.model.delete_last()
            self.model.add_to_expression(f'{result}')
        elif value == 'π':
            result = pi
            self.model.add_to_expression(f'{result:.2f}')
        elif value == 'DEL':
            self.model.delete_last()
        elif value == 'CLR':
            self.model.clear_expression()
        elif value in ['exp', 'ln', 'log10', 'log2', 'sqrt']:
            self.model.add_to_expression(f'{value}(')
        self.update_display()
        self.update_view()

    def display_selected_item(self, selected_item):
        self.model.expression = selected_item
    def update_display(self):
        expression = self.model.get_expression()
        self.view.update_display(expression)

    def update_view(self):
        self.view.update_history_combobox(self.model.history)

    def update_total_display(self):
        expression = self.model.get_expression()
        self.view.update_total_display(expression)

    def run(self):
        self.bind_keys()
        self.view.mainloop()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
