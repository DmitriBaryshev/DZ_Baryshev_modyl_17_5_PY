# Задание 1
import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE Artists (
                    ArtistID INTEGER PRIMARY KEY,
                    ArtistName TEXT
                );''')

cursor.execute("INSERT INTO Artists (ArtistName) VALUES ('The Beatles');")
cursor.execute("INSERT INTO Artists (ArtistName) VALUES ('Queen');")
cursor.execute("INSERT INTO Artists (ArtistName) VALUES ('Led Zeppelin');")
cursor.execute('''CREATE TABLE Songs (
                    SongID INTEGER PRIMARY KEY,
                    SongTitle TEXT,
                    AlbumTitle TEXT,
                    Duration INTEGER,
                    Genre TEXT,
                    ArtistID INTEGER,
                    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID)
                );''')
cursor.execute("INSERT INTO Songs (SongTitle, AlbumTitle, Duration, Genre, ArtistID) VALUES "
               "('Song1', 'Album1', 200, 'Rock', 1);")
cursor.execute("INSERT INTO Songs (SongTitle, AlbumTitle, Duration, Genre, ArtistID) VALUES "
               "('Song2', 'Album1', 180, 'Rock', 1);")
cursor.execute("INSERT INTO Songs (SongTitle, AlbumTitle, Duration, Genre, ArtistID) VALUES "
               "('Song3', 'Album2', 220, 'Pop', 2);")
cursor.execute('''CREATE VIEW AllArtists AS
                    SELECT ArtistName FROM Artists;''')
cursor.execute('''CREATE VIEW AllSongsInfo AS
                    SELECT SongTitle, AlbumTitle, Duration, Genre, Artists.ArtistName
                    FROM Songs
                    JOIN Artists ON Songs.ArtistID = Artists.ArtistID;''')
cursor.execute('''CREATE VIEW BeatlesAlbums AS
                    SELECT SongTitle, AlbumTitle, Duration, Genre, Artists.ArtistName
                    FROM Songs
                    JOIN Artists ON Songs.ArtistID = Artists.ArtistID
                    WHERE Artists.ArtistName = 'The Beatles';''')
cursor.execute("SELECT * FROM AllArtists;")
print("All Artists:")
artists = cursor.fetchall()
for artist in artists:
    print(artist[0])

print("\n")

cursor.execute("SELECT * FROM AllSongsInfo;")
print("All Songs Info:")
songs_info = cursor.fetchall()
for song_info in songs_info:
    print(song_info)

print("\n")

cursor.execute("SELECT * FROM BeatlesAlbums;")
print("The Beatles Albums:")
beatles_albums = cursor.fetchall()
for album in beatles_albums:
    print(album)
conn.close()


# Задание 2
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE Styles (
        StyleID INTEGER PRIMARY KEY,
        StyleName TEXT
    )
''')

cursor.execute('''
    CREATE TABLE Songs (
        SongID INTEGER PRIMARY KEY,
        SongName TEXT,
        StyleID INTEGER,
        ArtistID INTEGER,
        PublisherID INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE Publishers (
        PublisherID INTEGER PRIMARY KEY,
        PublisherName TEXT
    )
''')

cursor.execute('''
    CREATE TABLE Artists (
        ArtistID INTEGER PRIMARY KEY,
        ArtistName TEXT
    )
''')
cursor.execute('INSERT INTO Styles (StyleName) VALUES ("Rock")')
cursor.execute('INSERT INTO Styles (StyleName) VALUES ("Pop")')

cursor.execute('INSERT INTO Publishers (PublisherName) VALUES ("Sony")')
cursor.execute('INSERT INTO Publishers (PublisherName) VALUES ("Universal")')

cursor.execute('INSERT INTO Artists (ArtistName) VALUES ("Muse")')
cursor.execute('INSERT INTO Artists (ArtistName) VALUES ("Coldplay")')
cursor.execute('''
    CREATE VIEW InsertNewStyle AS
    SELECT * FROM Styles
''')

cursor.execute('''
    CREATE VIEW InsertNewSong AS
    SELECT * FROM Songs
''')

cursor.execute('''
    CREATE VIEW UpdatePublisherInfo AS
    SELECT * FROM Publishers
''')

cursor.execute('''
    CREATE VIEW DeleteArtist AS
    SELECT * FROM Artists
''')

cursor.execute('''
    CREATE VIEW UpdateArtistInfo AS
    SELECT * FROM Artists WHERE ArtistName = "Muse"
''')
cursor.execute('SELECT * FROM Styles')
print("Styles:")
print(cursor.fetchall())

cursor.execute('SELECT * FROM Songs')
print("\nSongs:")
print(cursor.fetchall())

cursor.execute('SELECT * FROM Publishers')
print("\nPublishers:")
print(cursor.fetchall())

cursor.execute('SELECT * FROM Artists')
print("\nArtists:")
print(cursor.fetchall())
conn.close()

# Задание 3
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE Sellers (
        SellerID INTEGER PRIMARY KEY,
        SellerName TEXT,
        TotalSales INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE Buyers (
        BuyerID INTEGER PRIMARY KEY,
        BuyerName TEXT,
        TotalPurchases INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE Sales (
        SaleID INTEGER PRIMARY KEY,
        SellerID INTEGER,
        BuyerID INTEGER,
        ProductName TEXT,
        SaleAmount INTEGER
    )
''')

cursor.execute('INSERT INTO Sellers (SellerName, TotalSales) VALUES ("John", 500)')
cursor.execute('INSERT INTO Sellers (SellerName, TotalSales) VALUES ("Alice", 700)')

cursor.execute('INSERT INTO Buyers (BuyerName, TotalPurchases) VALUES ("Bob", 800)')
cursor.execute('INSERT INTO Buyers (BuyerName, TotalPurchases) VALUES ("Emma", 600)')

cursor.execute('INSERT INTO Sales (SellerID, BuyerID, ProductName, SaleAmount) VALUES (1, 1, "Apples", 100)')
cursor.execute('INSERT INTO Sales (SellerID, BuyerID, ProductName, SaleAmount) VALUES (2, 2, "Oranges", 200)')
cursor.execute('INSERT INTO Sales (SellerID, BuyerID, ProductName, SaleAmount) VALUES (1, 2, "Bananas", 150)')
cursor.execute('INSERT INTO Sales (SellerID, BuyerID, ProductName, SaleAmount) VALUES (2, 1, "Grapes", 300)')
cursor.execute('''
    CREATE VIEW AllSellers AS
    SELECT * FROM Sellers
''')

cursor.execute('''
    CREATE VIEW AllBuyers AS
    SELECT * FROM Buyers
''')

cursor.execute('''
    CREATE VIEW SalesByProduct AS
    SELECT * FROM Sales WHERE ProductName = "Apples"
''')

cursor.execute('''
    CREATE VIEW AllSales AS
    SELECT * FROM Sales
''')

cursor.execute('''
    CREATE VIEW MostActiveSeller AS
    SELECT * FROM Sellers WHERE TotalSales = (SELECT MAX(TotalSales) FROM Sellers)
''')

cursor.execute('''
    CREATE VIEW MostActiveBuyer AS
    SELECT * FROM Buyers WHERE TotalPurchases = (SELECT MAX(TotalPurchases) FROM Buyers)
''')
cursor.execute('SELECT * FROM Sellers')
print("Sellers:")
print(cursor.fetchall())

cursor.execute('SELECT * FROM Buyers')
print("\nBuyers:")
print(cursor.fetchall())

cursor.execute('SELECT * FROM Sales WHERE ProductName = "Apples"')
print("\nSales of Apples:")
print(cursor.fetchall())

cursor.execute('SELECT * FROM Sales')
print("\nAll Sales:")
print(cursor.fetchall())

cursor.execute('SELECT * FROM Sellers WHERE TotalSales = (SELECT MAX(TotalSales) FROM Sellers)')
print("\nMost Active Seller:")
print(cursor.fetchall())

cursor.execute('SELECT * FROM Buyers WHERE TotalPurchases = (SELECT MAX(TotalPurchases) FROM Buyers)')
print("\nMost Active Buyer:")
print(cursor.fetchall())
conn.close()

