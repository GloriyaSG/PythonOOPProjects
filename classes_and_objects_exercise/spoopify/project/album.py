from typing import Tuple, List

from person.project import Song


class Album:
    def __init__(self, name, *songs: Tuple[Song]):
        self.name = name
        self.songs: List[Song] = [*songs]
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if song in self.songs:
            return "Song is already in the album."

        if self.published:
            return "Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: Song) -> str:
        try:
            song = next(filter(lambda a: a.name == song_name, self.songs))
        except StopIteration:
            return f"Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        songs = '\n'.join([f"== {Song.get_info(song)}"for song in self.songs])
        return f"Album {self.name}\n" \
               f"{songs}"



