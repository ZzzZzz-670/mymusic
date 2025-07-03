class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 0
        self.smart = 0
        self.health = 0
        
    def play(self):
        self.happiness += 10
        self.smart += 2
        self.health += 6
    
    def eat(self):
        self.happiness += 5
        self.smart += 1
        self.health += 10
        
    def sleep(self):
        self.happiness += 3
        self.smart += 1
        self.health += 5

class Person:
    def __init__(self, name, money, number_of_pets):
        self.name = name
        self.money = money
        self.number_of_pets = number_of_pets
        self.pet = []
        self.pet_dict = {}
    
    def play_with_pet(self, pet_name):
        if self.money >= 10:
            self.money -= 10
            if pet_name in self.pet_dict:
                self.pet_dict[pet_name].play()
            
            
    def eat_with_pet(self, pet_name):
        if self.money >= 5:
            self.money -= 5
            if pet_name in self.pet_dict:
                self.pet_dict[pet_name].eat()
        
        
    def sleep_with_pet(self, pet_name):
        if self.money >= 3:
            self.money -= 3
            if pet_name in self.pet_dict:
                self.pet_dict[pet_name].sleep()
                
    def highest_happiness(self):
        return max(pet.happiness for pet in self.pet_dict.values())
    
    def highest_smart(self):
        return max(pet.smart for pet in self.pet_dict.values())
    
    def highest_health(self):
        return max(pet.health for pet in self.pet_dict.values())
    
n = int(input())
person_dict = {}

for _ in range(n):
    line1 = input().split()
    line2 = input().split()
    name = line1[0]
    money = int(line1[1])
    number_of_pets = int(line1[2])
    person = Person(name, money, number_of_pets)

    person_dict[name] = person
    for _ in range(number_of_pets):
        pet_name = line2[_]
        person.pet_dict[pet_name] = Pet(pet_name)
        
m = int(input())
for _ in range(m):
    line = input().split()
    person_name = line[0]
    pet_name = line[1]
    action = line[2]
    if person_name in person_dict:
        person = person_dict[person_name]
        if action == "play":
            person.play_with_pet(pet_name)
        elif action == "eat":
            person.eat_with_pet(pet_name)
        elif action == "sleep":
            person.sleep_with_pet(pet_name)

    
for person in person_dict.values():
    print(f"{person.name} {person.money} {person.highest_happiness()} {person.highest_smart()} {person.highest_health()}")