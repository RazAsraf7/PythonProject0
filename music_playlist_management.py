class Track:
    def __init__(self, title):
        self.title = title
    
    def toString(self):
        return f"You\'re now looking at {self.title} "
    
class Song(Track):
    def __init__(self, title, artist):
        super().__init__(title)
        self.artist = artist
    
    def toString(self):
        return super().toString() + f"by {self.artist}"
    
class Podcast(Track):
    def __init__(self, title, host):
        super().__init__(title)
        self.host = host
    
    def toString(self):
        return super().toString() + f"which hosted by {self.host}"

class Playlist:
    def __init__(self, name):
        self.tracks = []
        self.name = name

    def addTrack(self, track_name):
        self.tracks.append(track_name)
    
    def listTracks(self):
        for tr in self.tracks:
            print(tr.toString())

    def listSongs(self):
        for tr in self.tracks:
            if isinstance(tr, Song):
                print(tr.toString())
    
    def listPodcasts(self):
        for tr in self.tracks:
            if isinstance(tr, Podcast):
                print(tr.toString())


playlist = Playlist("Casual Drive")
song1 = Song("Hurricane", "Eden Golan")
podcast1 = Podcast("Drive", "Boaz Korpel")

playlist.addTrack(song1)
playlist.addTrack(podcast1)

playlist.listPodcasts()
playlist.listSongs()
playlist.listTracks()
