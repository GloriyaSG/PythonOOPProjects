from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService
from project.services.base_service import BaseService
from project.robots.base_robot import BaseRobot

class RobotsManagingApp:

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):

        services_dict = {"MainService": MainService, "SecondaryService": SecondaryService}

        if service_type not in services_dict.keys():
            raise Exception("Invalid service type!")

        service = services_dict[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        robots_dict = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}
        if robot_type not in robots_dict:
            raise Exception("Invalid robot type!")
        robot = robots_dict[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):

        robot = [rob for rob in self.robots if rob.name == robot_name][0]
        service = [serv for serv in self.services if serv.name == service_name][0]

        if (robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "MainService") \
                or (robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "SecondaryService"):
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):

        service = [serv for serv in self.services if serv.name == service_name][0]

        for robot in service.robots:
            if robot.name == robot_name:
                service.robots.remove(robot)
                self.robots.append(robot)
                return f"Successfully removed {robot_name} from {service_name}."
        raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        fed = 0

        for robot in service.robots:
            robot.eating()
            fed += 1

        return f"Robots fed: {fed}."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        total_price = 0
        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []

        for service in self.services:
            result.append(service.details())

        return "\n".join(result)
    
    
    
