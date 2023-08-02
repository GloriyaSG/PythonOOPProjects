from typing import List

from project.concert import Concert
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.band import Band


class ConcertTrackerApp:

    VALID_MUSICIANS = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer,
    }

    def __init__(self):
        self.bands = []
        self.concerts = []
        self.musicians = []

    def create_musician(self, musician_type: str, name: str, age: int):

        if musician_type not in ConcertTrackerApp.VALID_MUSICIANS.keys():
            raise ValueError(f"Invalid musician type!")

        for person in self.musicians:
            if person.name == name:
                raise Exception(f"{name} is already a musician!")

        person = ConcertTrackerApp.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(person)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            person = [p for p in self.musicians if p.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(person)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        try:
            person = [p for p in band.members if p.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(person)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):

        valid_band_count = {
            "Guitarist": 0,
            "Drummer": 0,
            "Singer": 0,
        }

        band = [b for b in self.bands if b.name == band_name][0]
        for person in band.members:
            if person.__class__.__name__ in valid_band_count.keys():
                valid_band_count[person.__class__.__name__] += 1

        if valid_band_count["Guitarist"] < 1 or valid_band_count["Drummer"] < 1 or valid_band_count["Singer"] < 1:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = [c for c in self.concerts if c.place == concert_place][0]

        if concert.genre == "Rock":
            for band_member in band.members:
                if band_member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

                if band_member.__class__.__name__ == "Singer" and "sing high pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to sing at the concert!")

                if band_member.__class__.__name__ == "Guitarist" and "play rock" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Metal":
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play metal" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Jazz":
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' \
                        and "play the drums with drum brushes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' \
                        and ("sing low pitch notes" not in band_member.skills
                             or "sing high pitch notes" not in band_member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play jazz" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

















