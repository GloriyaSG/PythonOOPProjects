from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity > len(self.animals) and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = sum([worker.salary for worker in self.workers])
        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_money = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals = f"You have {len(self.animals)} animals\n"
        lions = [an for an in self.animals if an.__class__.__name__ == "Lion"]
        tigers = [an for an in self.animals if an.__class__.__name__ == "Tiger"]
        cheetahs = [an for an in self.animals if an.__class__.__name__ == "Cheetah"]

        animals += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            animals += f"{lion}\n"

        animals += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            animals += f"{tiger}\n"

        animals += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            animals += f"{cheetah}\n"
        return animals.strip()

    def workers_status(self):
        workers = f"You have {len(self.workers)} workers\n"
        keepers = [kp for kp in self.workers if kp.__class__.__name__ == "Keeper"]
        caretakers = [ct for ct in self.workers if ct.__class__.__name__ == "Caretaker"]
        vets = [vet for vet in self.workers if vet.__class__.__name__ == "Vet"]

        workers += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            workers += f"{keeper}\n"

        workers += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            workers += f"{caretaker}\n"

        workers += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            workers += f"{vet}\n"
        return workers.strip()
