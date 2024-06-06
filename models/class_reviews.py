import uuid
from datetime import datetime

class Review:
    def __init__(self, user_name):
        self._id = str(uuid.uuid4())  # Genera un ID único
        self._user_name = user_name
        self._review_text = ""
        self._created = datetime.now()
        self._updated = datetime.now()

    # Getters
    @property
    def id(self):
        return self._id

    @property
    def user_name(self):
        return self._user_name

    @property
    def review_text(self):
        return self._review_text

    @property
    def created(self):
        return self._created

    @property
    def updated(self):
        return self._updated

    # Setters
    @user_name.setter
    def user_name(self, value):
        self._user_name = value
        self._updated = datetime.now()

    @review_text.setter
    def review_text(self, value):
        self._review_text = value
        self._updated = datetime.now()

    # Métodos para escribir y editar reseñas
    def write_review(self, text):
        self.review_text = text

    def edit_review(self, new_text):
        self.review_text = new_text