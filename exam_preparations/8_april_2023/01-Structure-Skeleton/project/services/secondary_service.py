from project.services.base_service import BaseService


class SecondaryService(BaseService):

    CAPACITY = 15

    def __init__(self, name):
        super().__init__(name, capacity=SecondaryService.CAPACITY)


    def details(self):
        res = [f"{self.name} Secondary Service:"]
        if self.robots:
            res.append(f"Robots: {' '.join([r.name for r in self.robots])}")
        else:
            res.append("Robots: none")
        return '\n'.join(res)
