import sqlite3

con = sqlite3.connect("app.db")
# converting the image into binary in order to store it. 
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(prodId, prodName, prodPrice, prodImage):
    try:
        con = sqlite3.connect("app.db")
        cursor = con.cursor()
        print("Connected to sqlite")
        sqliteInsert = """INSERT INTO Products
                                  (prodId, prodName, prodPrice, prodImage) VALUES (?, ?, ?, ?)"""
        productImage = convertToBinaryData(prodImage)
        prodTuple = (prodId, prodName, prodPrice, prodImage)
        cursor.execute(sqliteInsert, prodTuple)
        con.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()                                  
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table because", error)
    finally:
        if con:
            con.close()
            print("the sqlite connection is closed")

insertBLOB(1, "Note 10", "1999", r"C:\Users\engan\Downloads/note10.jpg")



