from math import ceil
from typing import List

class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = self.__photo_matrix()
        self.current_index = 0


    def __photo_matrix(self):
        matrix = []
        for _ in range(self.pages):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label:str):
        if len(self.photos[self.current_index]) == 4:
            self.current_index += 1
        try:
            self.photos[self.current_index].append(label)
            return f"{label} photo added successfully on page {self.current_index + 1} slot" \
                   f" {len(self.photos[self.current_index])}"
        except IndexError:
            return "No more free slots"

    def display(self):
        result = "-" * 11 + "\n"
        for p in self.photos:
            result += ' '.join(["[]" for photo_name in p]) + "\n"
            result += "-" * 11 + "\n"

        return result
