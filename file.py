"""
classwork

create a simple class names Pet.
This class should have features name, species and age.
Include a function to display the class information.
Write a function to celebarate the pet's birthday
"""

class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
def display_info(pet_obj):
    print(f"Pet informations")
    print(f"Pet name: {pet_obj.name}")
    print(f"Pet specie: {pet_obj.species}")
    print(f"Pet age: {pet_obj.age}")
    
def pet_birth(birth):
    print(f"Happy birthday, {birth.name} \n Wishing you a long life")
    
pet1 = Pet('Spyrol', 'German Shepherd', '8' )

display_info(pet1)
pet_birth(pet1)
