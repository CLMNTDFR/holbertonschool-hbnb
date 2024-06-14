import uuid
from datetime import datetime
from app.persistence.data_manager import DataManager

storage = DataManager()

class User:
    def __init__(self, email, first_name, last_name, password=None):
        self.id = str(uuid.uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        if not self.is_email_unique():
            raise ValueError("Email already exists.")
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def delete(self):
        storage.delete(self.id, 'User')

    def to_dict(self):
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
        users = User.get_all()
        for user in users:
            if user.email == self.email and user.id != self.id:
                return False
        return True

    @staticmethod
    def get(user_id):
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
