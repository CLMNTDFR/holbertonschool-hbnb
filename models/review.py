from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    """
    def __init__(self, user_id, place_id, text):
        """
        Initialize a new Review instance.
        """
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.text = text

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        the instance's __dict__.
        """
        review_dict = super().to_dict()
        review_dict.update({
            'user_id': self.user_id,
            'place_id': self.place_id,
            'text': self.text
        })
        return review_dict
