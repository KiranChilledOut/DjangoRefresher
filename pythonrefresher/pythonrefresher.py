#string
firstName = "Kiran Raj"
lastName = "Rajendran"
#int
age = 31
#float
test_score = 9.9
#bool
man = True
woman = False

print(f"My name is {firstName} and last name is {lastName}, my age is {age}")

#list
listcheck = ['dog','cat']
print(f"The length of the list is {len(listcheck)} and the item 0 is {listcheck[0]}")

#dict
dictcheck={
    "key1" : "test",
    "key2" : "test1"
}

print(f"{len(dictcheck)} and {dictcheck['key1']}")

#conditional
c=5
if c>3:
    print(f"{c} is greater")
else:
    print("hello world")

listcheck2 = ["cat","dog","fish","pig","what"]
for l in listcheck2:
    print(l)

def squareme(x):
    return x*x 

print(squareme(5))

#classes

class House:
    livingRoom = None
    bathRoom = None
    backyard = None

    def __init__(self,livingRoom,bathRoom,backyard):
        self.livingRoom = livingRoom
        self.bathRoom = bathRoom
        self.backyard = backyard

    def number_of_rooms(self):
        return self.livingRoom + self.bathRoom

kirans_house = House(livingRoom=1,bathRoom=2,backyard=True)
print(kirans_house.backyard)
print(kirans_house.number_of_rooms())
        