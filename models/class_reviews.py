import uuid
from datetime import datetime

class Review:
    def __init__(self, user_name):
        self.__id = str(uuid.uuid4())  # Genera un ID único
        self.__user_name = user_name
        self.__review_text = ""
        self.__created = datetime.now().strftime("%b/%d/%y %I:%M %p")
        self.__updated = self.__created

    # Getters
    @property
    def id(self):
        return self.__id
        return self.__id

    @property
    def user_name(self):
        return self.__user_name
        return self.__user_name

    @property
    def review_text(self):
        return self.__review_text
        return self.__review_text

    @property
    def created(self):
        return self.__created
        return self.__created

    @property
    def updated(self):
        return self.__updated
        return self.__updated

    # Setters
    @user_name.setter
    def user_name(self, value):
        self.__user_name = value
        self.__updated = datetime.now().strftime("%b/%d/%y %I:%M %p")

    @review_text.setter
    def review_text(self, value):
        self.__review_text = value
        self.__updated = datetime.now().strftime("%b/%d/%y %I:%M %p")

    # Métodos para escribir y editar reseñas
    def write_review(self, text):
        self.review_text = text
        self.__updated = datetime.now().strftime("%b/%d/%y %I:%M %p")

    def edit_review(self, new_text):
        self.review_text = new_text
        self.__updated = datetime.now().strftime("%b/%d/%y %I:%M %p")
