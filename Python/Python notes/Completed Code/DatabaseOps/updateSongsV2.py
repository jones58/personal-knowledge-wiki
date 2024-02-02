from connect import * 

# create subroutine
def update_song():
    # ask for the SongID
    idfield = input("Enter SongID for the record to be updated:")

    # ask for the field/columns value(new value)
    songTitle = input("Enter song Title value : ").title()
    songArtist = input("Enter song Artist value: ").title()
    songGenre = input("Enter Song Genre value: ").title()

    
    # add single quotes to the new value 
    songTitle = "'"+songTitle +"'"
    songArtist ="'"+songArtist+"'"
    songGenre = "'"+songGenre +"'"

    # update a specific field for a particula record
    dbCursor.execute(f"UPDATE songs SET Title = {songTitle}, Artist = {songArtist}, Genre = {songGenre}  WHERE SongID = {idfield}")

    dbCon.commit()

    print(f"Record {idfield} update in the songs table")

if __name__ == "__main__":
    update_song()
        



