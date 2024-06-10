from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    """

    def __init__(self, name):
        """
        Initialize a new Amenity instance.
        """
        super().__init__()
        self.name = name

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of the instance's __dict__.
        """
        amenity_dict = super().to_dict()
        amenity_dict.update({
            'name': self.name
        })
        return amenity_dict
