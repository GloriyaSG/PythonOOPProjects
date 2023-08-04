from typing import List
from project.user import User
from project.route import Route
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar

class ManagingApp:

    VALID_VEHICLES = {
        "CargoVan": CargoVan,
        "PassengerCar": PassengerCar
    }

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):

        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name,last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ManagingApp.VALID_VEHICLES.keys():
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        vehicle = ManagingApp.VALID_VEHICLES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True


        route_ = Route(start_point,end_point,length, route_id)
        self.routes.append(route_)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):

        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        route = [r for r in self.routes if r.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()

        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_vehicles = list(sorted(vehicles, key=lambda x: (x.brand, x.model)))

        needed_vehicles = []
        if len(sorted_vehicles) > count:
            needed_vehicles = sorted_vehicles[:count]
        else:
            needed_vehicles = sorted_vehicles

        for vehicle in needed_vehicles:
            vehicle.is_damaged = False
            vehicle.recharge()

        return f"{len(needed_vehicles)} vehicles were successfully repaired!"

    def users_report(self):

        res = ["*** E-Drive-Rent ***"]

        users = list(sorted(self.users, key=lambda x: -x.rating))
        for user in users:
            res.append(str(user))

        return '\n'.join(res)
