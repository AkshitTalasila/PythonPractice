from Book import Book

class TextBook(Book):

    def __init__(self, name = "Unknown", author = "Unknown", pages = 0, subject = "Unknown", edition = 0 ):

        super().__init__(name,author,pages)
        self.subject = subject
        self.edition = edition

        