class User():

  def __init__(self, name, email):
 
    self.name = name
    self.email = email
    self.books = {}

  def get_email(self):

    print("user {name} has address {email}".format(name = self.name, email = self.email))


  def change_email(self, address):
    if address != self.email:
      print("updated email of {name} is {email}".format(name = self.name, email = address))
    else:
      return "Email address of user has not changed"

  def __repr__(self):
    print("email address of {name} is {email}. Books read: {books}".format(name = self.name, email = self.email, books = self.books))


  def __eq__(self, other_user):
    if (self.name == other_user.name) and (self.email == other_user.email):
      return "Same user"
    else:
      return "Different users"

  def read_book(book,rating=None):
    self.books[book] = rating
    return self.books

  total = 0
  def get_average_rating(self):
    for ratings in self.books.values():
      total+=ratings
    average_rating = total/len(self.books)
    return average_rating
      

#Below is a sample test of the code written so far.
    
#first_user = User("Niraj", "taco.jaco@email.com")
#second_user = User("Evening Glory", "glorify.morning@tmail.com")
#print(first_user.get_email())
#print(first_user.change_email("jaco.whacko@email.com"))
#print(first_user == second_user)
#print(User.read_book("Donkey")



class Book():

  def __init__(self, title, isbn):
    self.title = title
    self.isbn = isbn
    self.rating = []

  def get_title(self):
    return "The title of the book is \"{title}\"".format(title=self.title)

  def get_isbn(self):
    return "Book ISBN - {isbn}".format(isbn=self.isbn)

  def set_isbn(self,new_isbn):
    if new_isbn != self.isbn:
      print("Updated ISBN - {isbn} for \"{title}\"".format(isbn = new_isbn, title = self.title))

  def add_rating(self,rating):
    if rating >= 0 and rating <= 4:
      self.rating.append(rating)
    else:
      print("Invalid Rating")

  def __eq__(self,other_book):
    if (self.title == other_book.title) and (self.isbn == other_book.isbn):
      return "Same Book"
    else:
      return "Different books"

  total = 0
  def get_average_rating(self):
    for ratings in self.rating:
      total+=ratings
    average_rating = total/len(self.rating)
    return average_rating
      
  def __hash__(self):
    return hash((self.title, self,isbn))


class Fiction(Book):

  def __init__(self,title,isbn):
    super().__init__(title,isbn)
    self.author = "Niraj Apocryphal"

  def get_author(self):
    return self.author

  def __repr__(self):
    return "\"{title}\" by {author}".format(title = self.title, author = self.author)



class Non_Fiction(Book):
  def __init__(self,title,isbn):
    super().__init__(title,isbn)
    self.subject = "Superhero animals"
    self.level = "Advance"

  def get_subject(self):
    return self.subject

  def get_level(self):
    return self.level

  def __repr__(self):
    return "\"{title}\" is a {level} literature on {subject}".format(title = self.title, level = self.level, subject = self.subject)

#Below is a sample test of the code written so far.
   
#first_book = Book("Journey to the center of the Earth", 12345678)
#second_book = Book("If the pigs could swim and the elephants could fly", 87654321)
#second_book.set_isbn(30405060)
#first_book.add_rating(4)
#print(first_book.rating)
#print(Fiction("Journey to the center of the Earth", 12345678))
#second_book.add_rating(9)
#print(first_book == second_book)
#print(Fiction("If the pigs could swim and the elephants could fly",87654321))
#print(Non_Fiction("If the pigs could swim and the elephants could fly",87654321))



class TomeRater:

  def __init__(self):
    self.users = {}
    self.books = {}

  def create_book(self, title, isbn):
    return "\"{title}\" , {isbn}".format(title = title, isbn = isbn)

  def create_novel(self,title,author,isbn):
    return "\"{title}\" by {author}, {isbn}".format(title = title, author = author, isbn = isbn)

  def add_book_to_user(self,book,email,rating=None):
    for user in self.users.items():
      if user != self.email:
        print("No user with email {email}".format(email = self.email))
      else:
        User.read_book(self,book,rating)
        Book.add_rating(self,rating)
        if book not in self.books:
          self.books[book] = 1
        else:
          self.books[book] = 1+1

  def add_user(self,name,email,books = None):
    user = User(name,email)
    for book in books:
      user.add_book_to_user(book)
    return self.users

  def print_catalogue(self):
    for item in self.books.items():
      print(item.keys())

  def print_users(self):
    for item in self.users.items():
      print(item.values())

  def most_read_book(self):
    read_value = []
    for item in self.books.items():
      read_value.append(item.values())
    return read_value
    most_read = sorted(read_value)
    return most_read[-1]

  def highest_rated_book(self):
    highest_average_rating = []
    rated_book = []
    for item in self.books.keys():
      highest_average_rating.append(item.get_average_rating())
      rated_book.append(item)
    rating_to_book = {highest_average_rating:rated_book for highest_average_rating, rated_book in zip(highest_average_rating, rated_book)}
    book_with_highest_rating = sorted(rating_to_book.items())
    return book_with_highest_rating[-1]
    best = book_with_highest_rating[-1]
    return best[1]

  def most_positive_user(self):
    highest_average_rating = []
    rated_user = []
    for user in self.users.values():
      highest_average_rating.append(user.get_average_rating())
      rated_user = []
    rating_to_user = {highest_average_rating:rated_user for highest_average_rating, rated_user in zip(highest_average_rating, rated_user)}
    user_with_highest_rating = sorted(rating_to_user.items())
    return user_with_highest_rating[-1]
    best = user_with_highest_rating[-1]
    return best[1]
    
      
      
      
    
      
    










 
