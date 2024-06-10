from models.base_model import BaseModel


class Country(BaseModel):
    """
    Country class that inherits from BaseModel.
    """

    def __init__(self, name):
        """
        Initialize a new Country instance.
        """
        super().__init__()
        self.name = name

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        the instance's __dict__.
        """
        country_dict = super().to_dict()
        country_dict.update({
            'name': self.name
        })
        return country_dict
