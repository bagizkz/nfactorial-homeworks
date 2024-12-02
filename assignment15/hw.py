import math #c 14
import random # 17



"""
Exercise 1:
Create a Pizza class that could have ingredients added to it. Raise an error if an attempt is made to add a duplicate ingredient.
"""



class Pizza:
    def __init__(self):
        self.ingredients = set()
    
    def add_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            raise ValueError("ingredient уже существует!")
        self.ingredients.add(ingredient)


"""
Exercise 2:
Create an Elevator class with methods to go up, go down, and get the current floor. The elevator should not be able to go below the ground floor (floor 0).
"""

class Elevator:
    def __init__(self):
        self.current_floor = 0

    def go_up(self):
        self.current_floor += 1

    def go_down(self):
        if self.current_floor > 0:
            self.current_floor -= 1

    def get_current_floor(self):
        return self.current_floor


"""
Exercise 3:
Create a class Stack with methods to push, pop, and check if the stack is empty. Raise an exception if a pop is attempted on an empty stack.
"""



class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack пуст")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    
"""
Exercise 4:
Design a BankAccount class with methods to deposit, withdraw, and check balance. Ensure that an account cannot go into a negative balance.
"""



class BankAccount:
    def __init__(self, initial_balance):
        if initial_balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Сумма вклада не может быть отрицательной")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Сумма вывода не может быть отрицательной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount

    def check_balance(self):
        return self.balance



"""
Exercise 5:
Create a class Person with attributes for name and age. Implement a method birthday that increases the person's age by one. Raise an exception if an age less than 0 is entered.
"""


class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

        
"""
Exercise 6:
Create an Animal base class and a Dog and Cat derived classes. Each animal should have a sound method which returns the sound they make.
"""

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"


"""
Exercise 7:
Design a class Calculator with static methods for addition, subtraction, multiplication, and division. Division method should raise a ZeroDivisionError when trying to divide by zero.
"""


class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError("Нельзя разделить на ноль")
        return x / y





"""
Exercise 8:
Create a class `Car` with attributes for speed and mileage. Raise a ValueError if a negative value for speed or mileage is entered.
"""


class Car:
    def __init__(self, speed, mileage):
        if speed < 0 or mileage < 0:
            raise ValueError("Скорость и пробег не должны быть отрицательными")
        self.speed = speed
        self.mileage = mileage


"""
Exercise 9:
Create a Student class and a Course class. Each Course can enroll students and print a list of enrolled students.
"""

class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def print_students(self):
        for student in self.students:
            print(student.name)


"""
Exercise 10:
Create a Flight class with a destination, departure time, and a list of passengers. Implement methods to add passengers, change the destination, and delay the flight by a certain amount of time.
"""


class Flight:
    def __init__(self, destination, departure):
        self.destination = destination
        self.departure = departure
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def change_destination(self, new_destination):
        self.destination = new_destination

    def delay(self, delay_time):
        self.departure += delay_time


"""
Exercise 11:
Create a Library class with a list of Book objects. The Book class should have attributes for title and author. The Library class should have methods to add books and find a book by title.
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None




"""
Exercise 12:
Design a class Matrix that represents a 2D matrix with methods for addition, subtraction, and multiplication. Implement error handling for operations that are not allowed (e.g., adding matrices of different sizes).
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Для сложения должны быть одинакового размера.")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)

    def subtract(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Для вычитания должны быть одинакового размера")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)

    def multiply(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Количество столбов в первой матрице должно равняться кол. строк во второй.")
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0]))) for j in range(len(other.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)



"""
Exercise 13:
Create a class Rectangle with attributes for height and width. Implement methods for calculating the area and perimeter of the rectangle. Also, implement a method is_square that returns true if the rectangle is a square and false otherwise.
"""


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def is_square(self):
        return self.height == self.width


"""
Exercise 14:
Design a class Circle with attributes for radius. Implement methods for calculating the area and the circumference of the circle. Handle exceptions for negative radius values.
"""


class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


"""
Exercise 15:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""


class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b <= side_c or side_b + side_c <= side_a or side_c + side_a <= side_b:
            raise ValueError("Стороны не образуют треугольник")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

"""
Exercise 16:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""


class AbstractShape:
    def area(self):
        pass

    def perimeter(self):
        pass



class Circle(AbstractShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius




class Rectangle(AbstractShape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


class Triangle(AbstractShape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))



"""
Exercise 17:
Create a MusicPlayer class that contains a list of songs and methods to add songs, play a song, and skip to the next song. Also implement a method to shuffle the playlist.
"""



class MusicPlayer:
    def __init__(self):
        self.songs = []
        self.current_song_index = 0

    def add_song(self, song):
        self.songs.append(song)

    def play_song(self):
        if not self.songs:
            print("Нет песен в плейлисте!")
            return
        print(f"Сейчас играет: {self.songs[self.current_song_index]}")

    def next_song(self):
        if not self.songs:
            print("Нет песен в плейлисте!")
            return
        self.current_song_index = (self.current_song_index + 1) % len(self.songs)
        self.play_song()

    def shuffle(self):
        if not self.songs:
            print("Нет песен в плейлисте!")
            return
        random.shuffle(self.songs)
        self.current_song_index = 0
        self.play_song()



"""
Exercise 18:
Design a Product class for an online store with attributes for name, price, and quantity. Implement methods to add stock, sell product, and check stock levels. Include error handling for attempting to sell more items than are in stock.
"""




class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        self.quantity += quantity

    def sell(self, quantity):
        if quantity < 0:
            raise ValueError("Количество продажи не может быть отрицательным")
        if quantity > self.quantity:
            raise ValueError("Недостаточно товара на складе")
        self.quantity -= quantity

    def check_stock(self):
        return self.quantity



"""
Exercise 19:
Create a VideoGame class with attributes for title, genre, and rating. Implement methods to change the rating, change the genre, and display game details.
"""


class VideoGame:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def change_rating(self, rating):
        self.rating = rating

    def change_genre(self, genre):
        self.genre = genre

    def display_details(self):
        print(f"Название: {self.title}, Жанр: {self.genre}, Рейтинг: {self.rating}")



"""
Exercise 21:
Design a Card class to represent a playing card with suit and rank. Then design a Deck class that uses the Card class. The Deck class should have methods to shuffle the deck, deal a card, and check the number of remaining cards.
"""


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("Нет карт в колоде")
        return self.cards.pop()

    def count(self):
        return len(self.cards)

