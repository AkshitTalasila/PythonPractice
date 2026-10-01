class Book:

    def __init__(self,title ="Unknown", author = "Unknown", pages =0):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):

        return f"Title: {self.title} "\
            f"Author: {self.author}"\
            f"Pages: {self.pages}"

    
                