from collections import deque

class Song:
    def __init__(self, song_title, artist_name, release_year, duration, genre):
        self.song_title = song_title
        self.artist_name = artist_name
        self.release_year = release_year
        self.duration = duration
        self.genre = genre
        
    def __str__(self):
        return f"'{self.song_title}' by {self.artist_name}, {self.release_year} ({self.genre})" 
    
    
    
class MP3Playlist:
    def __init__(self):
        self.playlist = deque()

    def load_playlist(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                song_details = line.strip().split(",")
                if len(song_details) == 5:
                    song = Song(*song_details)
                    self.add_song(song)

    def display_all(self):
        if not self.playlist:
            print("Your Playlist is empty.")
        else:
            print("Your Playlist:")
            for index, song in enumerate(self.playlist, start=1):
                print(f"{index}. {song}")

    def add_song(self, song):
        self.playlist.append(song)
        print(f"Added {song} to the playlist.")
        
    def clear_playlist(self):
        self.playlist.clear()
        print('You have cleared your playlist')
        
    def get_duration(self):
        durations = []
        for song in self.playlist:
            durations.append(song.duration)
            
        x = [int(i.split(':')[0]) for i in durations]
        y = [int(i.split(':')[1]) for i in durations]
        
        total_hours = 0
        total_minutes = sum(x)
        total_seconds = sum(y)
        
        while total_seconds >= 60:
            total_minutes += 1
            total_seconds -= 60
            
        while total_minutes >=60:
            total_hours +=1
            total_minutes -= 60
    
            
        return f'Total duration of playlist: {total_hours} hours,{total_minutes} mins and {total_seconds} seconds'
    
    def save_on_file(self, file_path):
        with open(file_path, 'w') as file:
            for song in self.playlist:
                file.write(f"{song.song_title},{song.artist_name},{song.release_year},{song.duration},{song.genre}\n")
                
        print(f'Playlist saved on {file_path}')
        
#     def remove_song(self, song_title):
#          for song in self.playlist:
#              if song.song_title == song_title:
#                  self.playlist.remove(song)
#                  print(f'{song_title} has been removed from your playlist')
            
        
            
        
            
        
    
        
   
            

# Create an instance of the MP3Playlist class
playlist = MP3Playlist()

# Load playlist from a text file
playlist.load_playlist("playlist.txt")

# Display the playlist
playlist.display_all()

# Enqueue new songs
new_song = Song("Ye", "Burna boy", "2019", "3:30", "Afrobeats")
playlist.add_song(new_song)

# Display the updated playlist
playlist.display_all()

# get the duration of all songs
print(playlist.get_duration())

playlist.save_on_file('pls.txt')



 
# playlist.clear_playlist()

# playlist.display_all()
