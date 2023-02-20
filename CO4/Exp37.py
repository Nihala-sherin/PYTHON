class Publisher:
    def __int__(self, publisher):
        self.publisher=publisher
    def display(self):
        print("Publisher name:",self.publisher)
class Book(Publisher):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print("Title of the book:",self.title)
        print("Author:",self.author)
class Angels(Book):
    def __init__(self, publisher, author, title, price, numb):
        self.price=price
        self.pages=numb
        Book.__init__(self,title,author)
        Publisher.__int__(self, publisher)
    def display(self):
        super().display()
        print("Price of the book:",self.price)
        print("No. of pages in the book:",self.pages)
b1=Angels("Washington Square Press","Dan Brown","Angels and Demons",1570,496)
b1.display()