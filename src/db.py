import sqlite3


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
        print("the product with the {id} inserted successfully as a BLOB into a table", prodId)
        cursor.close()                                  
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table because", error)
    finally:
        if con:
            con.close()
            print("the sqlite connection is closed")

def deleteBLOB(prodId):
    try:
        con = sqlite3.connect("app.db")
        cursor = con.cursor()
        print("Connected to sqlite server successfully")
        exist = cursor.fetchall()
        sqliteDelete = 'DELETE FROM Products where prodId=?'
        cursor.execute(sqliteDelete, (prodId,))
        if not exist:
            print("The Id you entered doesn't exist in our records")
            
        else:
            con.commit()
            print("the product has been deleted successfully from the database")
            cursor.close()
       
    except sqlite3.Error as error:
        print("We can't proceed the deletion process because of:", error)
    finally:
        if con:
            con.close()
            print("The sqlite connection is closed")
