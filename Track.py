class Media:

    def __init__(self, name, artist):
        self.name = name
        self.artist = artist

    def show(self):
        print(f'Name: {self.name}, Artist: {self.artist}')


class Track(Media):

    def __init__(self, name, artist, duration):
        super().__init__(name, artist)
        self.duration = duration

    def show(self):
        super().show()
        print(f'Duraction: {self.duration}')


class Album(Media):

    def __init__(self, name, artist, tracks):
        super().__init__(name, artist)
        self.tracks = tracks

    def get_tracks(self):
        for track in self.tracks:
            track.show()

    def add_track(self, track):
        self.tracks.append(track)

    def get_duration(self):
        album_duration = 0
        for track in self.tracks:
            album_duration += track.duration
        print('Длительность альбома', album_duration)


violator_tracks = [Track('Personal Jesus', 'Depeche Mode', 5), Track('Enjoy the Silence', 'Depeche Mode', 4),
                   Track('Clean', 'Depeche Mode', 3)]
violator = Album('Violator', 'Depeche Mode', violator_tracks)
violator.get_duration()

smiths_tracks = [Track('Reel Around the Fountain', 'Depeche Mode', 7), Track('Miserable Lie', 'Depeche Mode', 4),
                 Track('Pretty Girls Make Graves', 'Depeche Mode', 3)]
smiths_album = Album('The Smiths', 'The Smiths', smiths_tracks)
smiths_album.get_duration()
