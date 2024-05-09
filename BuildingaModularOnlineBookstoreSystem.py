class Book: 
    books = {}

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @classmethod
    def add_new(cls):
        title = input("\nPlease input the name of the book: ")
        author = input("Please input the name of the author: ")
        price = input("Please input the price: $")
        try:
            price = float(price)
        except ValueError:
            print("price must be entered as a number.")
            return
        cls.books[title] = cls(title, author, price)
        print(f"\nBook: {title}\nAuthor: {author}\nPrice: ${price}\n")

    @classmethod
    def check_stock(cls, title):
        if title in cls.books:
            print("\nthe book is available.\n")
        else:
            print("\nthe book is not available.\n")
    
    @classmethod
    def check_out_book(cls):
        title = input("Please enter the name of the book you want to check out: ").strip()
        if title in cls.books:
            del cls.books[title]
            print(f"\nYou have checked out the book {title}.\n")
    
    @classmethod
    def view_stock(cls):
        for  title, book in cls.books.items():
            print (f"\n Title: {title}\n Author: {book.author}, Price: {book.price}\n")


def main():
    while True:
        print('''Menu
1. Add a new book
2. Check stock of book
3. Check out a book
4. View Stock
5. quit''')
        selection = input("Please select a number: ")

        if selection == '1':
            Book.add_new()
        elif selection == '2':
            title = input("Please input the title of the book: ")
            Book.check_stock(title)
        elif selection == '3':
            Book.check_out_book()
        elif selection == '4':
            Book.view_stock() 
        elif selection == '5':
            break
        
if __name__ == "__main__":
    main()
    

        

   
