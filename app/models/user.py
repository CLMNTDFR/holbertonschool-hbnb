import uuid
from datetime import datetime
from app.persistence.data_manager import DataManager

storage = DataManager()


class User:
    """
    A class to represent a User.
    """

    def __init__(self, email, first_name, last_name, password=None):
        """
        Initialize a new User instance.

        Args:
            email (str): The email of the user.
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            password (str, optional): The password of the user.
            Defaults to None.
        """
        self.id = str(uuid.uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Save the user to the storage.
        """
        if not self.is_email_unique():
            raise ValueError("Email already exists.")
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def delete(self):
        """
        Delete the user from the storage.
        """
        storage.delete(self.id, 'User')

    def to_dict(self):
        """
        Convert the User instance to a dictionary.

        Returns:
            dict: The dictionary representation of the user.
        """
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def is_email_unique(self):
        """
        Check if the email is unique.

        Returns:
            bool: True if the email is unique, False otherwise.
        """
        users = User.get_all()
        for user in users:
            if user.email == self.email and user.id != self.id:
                return False
        return True

    @staticmethod
    def get(user_id):
        """
        Retrieve a user by its ID.

        Args:
            user_id (str): The ID of the user.

        Returns:
            User: The user instance if found, None otherwise.
        """
        data = storage.get(user_id, 'User')
        if data:
            user = User(
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password=data.get('password')
            )
            user.id = data['id']
            user.created_at = datetime.fromisoformat(data['created_at'])
            user.updated_at = datetime.fromisoformat(data['updated_at'])
            return user
        return None

    @staticmethod
    def get_all():
        """
        Retrieve all users from the storage.

        Returns:
            list: A list of User instances.
        """
        data = storage.get_all('User')
        users = []
        for item in data:
            user = User(
                email=item['email'],
                first_name=item['first_name'],
                last_name=item['last_name'],
                password=item.get('password')
            )
            user.id = item['id']
            user.created_at = datetime.fromisoformat(item['created_at'])
            user.updated_at = datetime.fromisoformat(item['updated_at'])
            users.append(user)
        return users
