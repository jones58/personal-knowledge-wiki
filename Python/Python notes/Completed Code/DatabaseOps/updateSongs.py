from connect import * 

# create subroutine
def update_song():
    # ask for the SongID
    idfield = input("Enter SongID for the record to be updated:")

    # ask for the field/column to be updated
    fieldName = input("Enter Title, Artist or Genre as field name: ").title()

    # ask for the field/column value(new value)
    fieldValue = input(f"Enter the value for the field {fieldName} field")

    # add single quotes to the new value 
    fieldValue = "'"+fieldValue+"'"

    # update a specific field for a particula record
    dbCursor.execute(f"UPDATE songs SET {fieldName} = {fieldValue} WHERE SongID = {idfield}")

    dbCon.commit()

    print(f"Record {idfield} update in the songs table")

if __name__ == "__main__":
    update_song()
        



