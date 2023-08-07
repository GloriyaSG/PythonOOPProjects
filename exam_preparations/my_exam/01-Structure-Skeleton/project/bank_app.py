from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan
from project.clients.student import Student
from project.clients.adult import Adult

class BankApp:

    VALID_LOAN_TYPES = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan,
    }

    VALID_CLIENTS = {
        "Student": Student,
        "Adult": Adult,
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):

        if loan_type not in BankApp.VALID_LOAN_TYPES.keys():
            raise Exception("Invalid loan type!")

        loan = BankApp.VALID_LOAN_TYPES[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):

        if client_type not in BankApp.VALID_CLIENTS.keys():
            raise Exception("Invalid client type!")

        if self.capacity == len(self.clients):
            # Change this == if something goes wrong!
            return "Not enough bank capacity."

        client = BankApp.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = ""

        for person in self.clients:
            if person.client_id == client_id:
                client = person

        if client.__class__.__name__ == "Adult" and loan_type != "MortgageLoan" \
                or client.__class__.__name__ == "Student" and loan_type != "StudentLoan":
            raise Exception("Inappropriate loan type!")

        loan = [loan for loan in self.loans if loan_type == loan.__class__.__name__][0]
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = ""
        try:
            client = [p for p in self.clients if p.client_id == client_id][0]

        except IndexError:
            raise Exception("No such client!")

        if len(client.loans) != 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loans = [loan for loan in self.loans if loan_type == loan.__class__.__name__]
        count = len(loans)

        for loan in loans:
            loan.increase_interest_rate()

        return f"Successfully changed {count} loans."

    def increase_clients_interest(self, min_rate: float):
        clients = [client for client in self.clients if client.interest < min_rate]
        count = len(clients)

        for client in clients:
            client.increase_clients_interest()

        return f"Number of clients affected: {count}."

    def get_statistics(self):
        clients_count = len(self.clients)
        total_clients_income = sum(client.income for client in self.clients)

        loans_granted_to_clients = 0
        for person in self.clients:
            for _ in person.loans:
                loans_granted_to_clients += 1

        loans_not_granted = len(self.loans)
        granted_sum = sum(loan.amount for client in self.clients for loan in client.loans)
        not_granted_sum = sum(loan.amount for loan in self.loans)

        try:
            avg_interest_rate = sum(person.interest for person in self.clients) / len(self.clients)
        except ZeroDivisionError:
            avg_interest_rate = 0

        res = (
            f"Active Clients: {clients_count}\n"
            f"Total Income: {total_clients_income:.2f}\n"
            f"Granted Loans: {loans_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
            f"Available Loans: {loans_not_granted}, Total Sum: {not_granted_sum:.2f}\n"
            f"Average Client Interest Rate: {avg_interest_rate:.2f}"
        )
        return res

