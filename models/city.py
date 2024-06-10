from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    """

    def __init__(self, name, country_id):
        """
        Initialize a new City instance.
        """
        super().__init__()
        self.name = name
        self.country_id = country_id

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        the instance's __dict__.
        """
        city_dict = super().to_dict()
        city_dict.update({
            'name': self.name,
            'country_id': self.country_id
        })
        return city_dict
