from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):

    PORTION = 250

    def __init__(self, name, price):
        super().__init__(name,Stolen.PORTION, price)

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."