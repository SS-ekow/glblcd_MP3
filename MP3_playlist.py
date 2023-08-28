from collections import defaultdict

class Playlist:
    def __init__ (self, song_title, artist_name, release_year, album, duration, genre):
        self.song_title = song_title
        self.artist_name = artist_name
        self.release_year = release_year
        self.album = album
        self.duration = duration
        self.genre = genre
        
    def load_playlist(self, text_file):
        file1 = open(text_file)
        details = []
        for line in file1:
            details.append(line.split(','))
                
        for i in details:
            self.song_title = i[0]
            self.artist_name = i[1]
            self.release_year = i[2]
            self.album = i[3]
            self.duration = i[4]
            self.genre = i[5]
                    
        
    def display_all():
        pass
        
    def add_song(self, song: str, a_name: str, year: int, album : str, duration: str, genre: str):
        self.song = song_title
        self.a_name = artist_name
        self.year = release_year
        self.album = album
        self.duration = duration
        self.genre = genre
            
            
new_playlist = Playlist('a','b','c','d','e','f')
loaded = new_playlist.load_playlist('songs')
print(loaded.__dict)
    
        
        