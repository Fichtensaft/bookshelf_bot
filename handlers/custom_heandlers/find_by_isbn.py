import requests
import json
from loader import bot
from telebot.types import Message


class BookFinderISBN:
    """[MAKING PROCESS] Function to find information about a book by its ISBN-number"""
    google_key = 'AIzaSyBVsiLu0K0vBkDz6uTmiG28b3xdSLV70DY'

    @classmethod
    def find_book(cls, value):
        prms = {'q': value, 'key': cls.google_key}
        response = requests.get('https://www.googleapis.com/books/v1/volumes', params=prms)

        data = json.loads(response.text)
        print(data)

        return data

