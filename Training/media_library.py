class Media:
    def __init__(self, title):
        self.title = title
    
    def toString(self):
        return f"Welcome to the {self.title} library."

class Book(Media):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def toString(self):
        return f"Book: {self.title} by {self.author}"
    
class DVD(Media):
    def __init__(self, title, director):
        self.title = title
        self.director = director

    def toString(self):
        return f"DVD {self.title} by {self.director}"
    
class MediaLibrary:
    def __init__(self, name):
        self.name = name
        self.media = []

    def addMedia(self, media_name):
        self.media.append(media_name)

    def listMedia(self):
        for med in self.media:
            print(med.toString())

    def listBooks(self):
        for med in self.media:
            if isinstance(med, Book):
                print(med.toString())

    def listDVDs(self):
        for med in self.media:
            if isinstance(med, DVD):
                print(med.toString())


library = MediaLibrary("Navon")
book1 = Book("Breaking Bad", "Walter White")
dvd1 = DVD("Young Sheldon", "Sheldon Cooper")
library.addMedia(book1)
library.addMedia(dvd1)

library.listMedia()
library.listBooks()
library.listDVDs()