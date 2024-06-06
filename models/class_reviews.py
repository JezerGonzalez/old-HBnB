import uuid
from datetime import datetime

class Review:
    def __init__(self, user_name):
        self.__id = str(uuid.uuid4())  # Genera un ID único
        self.__user_name = user_name
        self.__review_text = ""
        self.__created = datetime.now()
        self.__updated = datetime.now()

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def user_name(self):
        return self.__user_name

    @property
    def review_text(self):
        return self.__review_text

    @property
    def created(self):
        return self.__created

    @property
    def updated(self):
        return self.__updated

    # Setters
    @user_name.setter
    def user_name(self, value):
        self.__user_name = value
        self.__updated = datetime.now()

    @review_text.setter
    def review_text(self, value):
        self._review_text = value
        self._updated = datetime.now()

    # Métodos para escribir y editar reseñas
    def write_review(self, text):
        self.review_text = text

    def edit_review(self, new_text):
        self.review_text = new_text