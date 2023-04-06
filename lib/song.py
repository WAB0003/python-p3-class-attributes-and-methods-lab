import ipdb
class Song:
    artists=[]
    genres=[]
    count = 0
    artist_count = {}
    genre_count = {}
    
       

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.song_count()
        Song.add_artist(artist)
        Song.add_genre(genre)
        Song.add_artist_count(artist)
        Song.add_genre_count(genre)

    
    @classmethod
    def add_artist(cls,artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            
    @classmethod
    def add_genre(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        
    @classmethod  
    def song_count(cls):
        cls.count += 1
      
    @classmethod
    def add_artist_count(cls,artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist]+=1

        else:
            cls.artist_count[artist] = 1
            
    @classmethod
    def add_genre_count(cls,genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre]+=1

        else:
            cls.genre_count[genre] = 1
     
    
# ipdb.set_trace()