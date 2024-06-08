class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.validate_pet_type()
        Pet.all.append(self)

    def validate_pet_type(self):
        if self.pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {self.pet_type}. Valid types are: {', '.join(Pet.PET_TYPES)}")

class Owner:
    def __init__(self, name) -> None:
        self.name = name 

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)