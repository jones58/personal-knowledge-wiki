from connect import *

# create a subroutine 
def insert_song():
    #SongID field is auto increment (no data input is required)
    
    # ask for user input for Title, Artist and Genre
    songTitle = input("Enter song Title: ")
    songArtist = input("Enter song Artist: ")
    songGenre = input("Enter Song Genre: ")

    #data from Title, Artist and Genre variables and save it into the database.
    dbCursor.execute("INSERT INTO songs(Title, Artist, Genre) VALUES(?,?,?)", (songTitle, songArtist, songGenre))
    # Permanently save the record in the songstable in the database
    dbCon.commit()

    print(f"{songTitle} inserted in the songs table. ")

if __name__ == "__main__":
    insert_song()

