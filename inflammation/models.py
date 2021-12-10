"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    :returns: An array of mean values of measurements for each day.
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    :returns: An array of maximum values of measurements for each day.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    :returns: An array of minimum values of measurements for each day.
    """
    return np.min(data, axis=0)


def patient_normalise(data):
    """
    Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.

    :param data: 2d array of inflammation data
    :type data: ndarray
    """
    if not isinstance(data, np.ndarray):
        raise TypeError('data input should be ndarray')
    if len(data.shape) != 2:
        raise TypeError('inflammation array should be 2-dimensional')
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')
    max = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised


# TODO(lesson-design) Add Patient class
# TODO(lesson-design) Implement data persistence
# TODO(lesson-design) Add Doctor class


class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.day == other.day and self.value == other.value

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name, observations=None):
        super().__init__(name)

        self.observations = []
        if observations is not None:
            self.observations = observations

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(value, day)

        self.observations.append(new_observation)
        return new_observation

    def __eq__(self, other):
        return self.name == other.name and self.observations == other.observations


class Doctor(Person):
    """A patient in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)
        self.patients = []

    def add_patients(self, name):

        new_patient = Patient(name)

        self.patients.append(new_patient)
        return new_patient


#alice = Patient('Alice')
#print(alice)

#obs = alice.add_observation(3)
#print(obs)

#bob = Person('Bob')
#print(bob)

#obs = bob.add_observation(4)
#print(obs)


# The library:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + ' by ' + self.author

class Library():
    def __init__(self,books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        return self.books

    def __len__(self):
        return len(self.books)

    def __getitem__(self, key):
        return self.books[key]

    def by_author(self, name):
        matches = []
        for book in self.books:
            if book.author == name:
                matches.append(book)

        if not matches:
            raise KeyError('Author does not exist')

        return matches

    @property
    def titles(self):
        titles=[]
        for book in self.books:
            titles.append(book.title)
        return titles

    @property
    def authors(self):
        authors=[]
        for book in self.books:
            if book.author not in authors:
                authors.append(book.author)
        return authors

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def union(self, other):
        books = []
        for book in self.books:
            if book not in books:
                books.append(book)

        for book in other.books:
            if book not in books:
                books.append(book)

        return Library(books)

#library = Library()

#library.add_book('My First Book', 'Alice')
#library.add_book('My Second Book', 'Alice')
#library.add_book('A Different Book', 'Bob')

#print(len(library))

#book = library[2]
#print(book)

#books = library.by_author('Alice')
#for book in books:
    #print(book)

#books = library.by_author('Carol')

#print(library.titles)
#print(library.authors)


#library1 = Library()
#library1.add_book('My First Book', 'Alice')
#library2 = Library()
#library2.add_book('My Second Book', 'Alice')
#library2.add_book('A Different Book', 'Bob')

#library3 = library1.union(library2)

#print(library3.titles)

#Sum

def sum_of_squares(l):
    # Your code here
    from functools import reduce
    integers = [int(x) for x in l if x[0]!='#']
    squares = [x * x for x in integers]
    result = reduce((lambda a, b: a+b), squares)
    return result
