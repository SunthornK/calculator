from math import *
class Model:
    def __init__(self):
        self.history = []
        self.total_output = ""
        self.txt_input = "0"

    def calculate(self, expression):
        try:
            result = eval(expression)
            self.history.append(expression + " = " + str(result))
            return str(result)
        except ValueError as e:
            # Return error message if expression is invalid
            return "Error: " + str(e)

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
