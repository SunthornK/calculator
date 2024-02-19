from math import *


class Model:
    def __init__(self):
        self.expression = []
        self.total_expression = []
        self.history = []

    def set_total_expression(self, expression):
        self.total_expression = expression

    def add_to_expression(self, value):
        self.expression.append(str(value))

    def evaluate_expression(self):
        try:
            result = eval("".join(self.expression))
            self.history.append(f'{"".join(self.expression)} = {result}')
            self.expression = [str(result)]
        except Exception as e:
            self.expression = ["Error"]

    def clear_expression(self):
        self.expression = []

    def delete_last(self):
        if self.expression:
            self.expression.pop()

    def get_expression(self):
        return "".join(self.expression)

# if event == "C":
#     self.view.total_output = ""
#     self.view.update_label("0", "+")
# elif event in self.view.operator:
#     self.view.update_label(event.char)
#     self.view.total_output += self.view.txt_input
#     self.view.update_label("0", "+")
# else:
#     self.view.update_label(event)
# == del
#     if self.view.txt_input:
#         self.view.update_label(self.view.txt_input[:-1], "+")
#     else:
#         self.view.update_label(self.view.total_output, "+")
#         self.view.total_output = ""
#         self.view.total_display.config(text=self.view.total_output)
