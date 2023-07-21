class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.id

    @staticmethod
    def get_next_id():
        next_eq = Equipment.id
        Equipment.id += 1
        return next_eq

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"


