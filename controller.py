from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def display_button_click(self, event):
        """Event handler for button click."""
        button_text = event.widget.cget("text")
        if button_text in self.view.keys or button_text in self.view.operator:
            if button_text == "=":
                self.view.total_output += self.view.txt_input
                result = self.model.calculate(self.view.total_output)
                self.view.replace_label(result)
            elif button_text == "C":
                self.view.total_output = ""
                self.view.replace_label("")
            elif button_text == "^":
                self.view.update_label("**")
                self.view.total_output += self.view.txt_input
                self.view.replace_label("")
            elif button_text == "mod":
                self.view.update_label("//")
                self.view.total_output += self.view.txt_input
                self.view.replace_label("")
            elif button_text in self.view.operator:
                self.view.update_label(button_text)
                self.view.total_output += self.view.txt_input
                self.view.replace_label("")
            else:
                self.view.update_label(button_text)
        elif button_text == "Del":
            if self.view.txt_input:
                self.view.replace_label(self.view.txt_input[:-1])
            else:
                self.view.replace_label(self.view.total_output)
                self.view.total_output = ""
                self.view.total_display.config(text=self.view.total_output)

    def display_keypad(self, event):
        if event.char in self.view.keys or event.char in self.view.operator:
            if event.char == "=":
                self.view.total_output += self.view.txt_input
                result = self.model.calculate(self.view.total_output)
                self.view.replace_label(result)
            elif event.char == "C":
                self.view.total_output = ""
                self.view.replace_label("")
            elif event.char == "^":
                self.view.update_label("**")
                self.view.total_output += self.view.txt_input
                self.view.replace_label("")
            elif event.char == "mod":
                self.view.update_label("//")
                self.view.total_output += self.view.txt_input
                self.view.replace_label("")
            elif event.char in self.view.operator:
                self.view.update_label(event.char)
                self.view.total_output += self.view.txt_input
                self.view.replace_label("")
            else:
                self.view.update_label(event.char)
        elif event.keysym == "BackSpace":
            if self.view.txt_input:
                self.view.replace_label(self.view.txt_input[:-1])
            else:
                self.view.replace_label(self.view.total_output)
                self.view.total_output = ""
                self.view.total_display.config(text=self.view.total_output)

    def select_math_function(self, event):
        function_name = event.widget.get()

    # Handle mathematical functions
    def run(self):
        self.view.run()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
