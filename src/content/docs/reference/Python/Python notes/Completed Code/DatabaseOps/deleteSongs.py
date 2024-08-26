from connect import * 

# create a subroutine
def delete_song():
    idfield = input("Enter SongID for the record to be deleted:")


    #    delete the record with the song id entered 
    dbCursor.execute(f"DELETE FROM songs WHERE SongID = {idfield}")

    dbCon.commit()

    print(f"Record {idfield} deleted from the songs table")

if __name__ == "__main__":
    delete_song()