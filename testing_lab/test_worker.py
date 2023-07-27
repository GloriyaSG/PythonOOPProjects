class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0


    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1


    def rest(self):
        self.energy += 1


    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main

class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker('Ivan', 1000, 10)

    def test_if_correct_initial(self):
        self.assertEqual(self.worker.name, "Ivan")
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 10)
        self.assertEqual(self.worker.money, 0)

    def test_workers_energy_is_incremented(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)
        self.assertEqual(self.worker.money, 1000)

    def test_if_raise_correct_exception(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception) )

    def test_if_energy_is_incremented(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 11)

    def test_if_info_is_correct(self):
        self.assertEqual(self.worker.get_info(), 'Ivan has saved 0 money.')

if __name__ == '__main__':
    main()