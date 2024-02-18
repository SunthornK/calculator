from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def run(self):
        self.view.run()
if __name__ == '__main__':
    controller = Controller()
    controller.run()
