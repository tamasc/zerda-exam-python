# Create a Rocket class.
# It should take 3 parameters in its constructor
# 1st parameter: the type of the rocket as a string, "falcon1" or "falcon9".
# 2nd parameter: the starting fuel level as a number, defaults to 0.
# 3rd parameter: number of launches as a number, defaults to 0.
#
# It should have 3 methods:
#
# launch()
# it should use 1 fuel if it's a falcon1 and 9 fuels if it's a falcon9.
# it should increment the launches by one if it had enough fuel for the launch.
#
# refill()
# it should refill the rocket's fuel level to 5 if falcon1 and to 20 if falcon9.
# it should return the amount of fuel used for the refill.
# example: if the rocket is a falcon1 and has fuel level 3, then it should return 2.
#
# getStats()
# it should return its stats as a string like: "name: falcon9, fuel: 11, launches: 1"

################################################

# The following code should work with the class:

class Rocket():

    def __init__(self, name, fuel=0, number_of_launches=0):
        self.name = name
        self.fuel = fuel
        self.number_of_launches = number_of_launches

    def launch(self):
        if self.name == "falcon1" and self.fuel >= 1:
            self.number_of_launches += 1
            self.fuel -= 1
        elif self.name == "falcon9" and self.fuel >= 9:
            self.number_of_launches += 1
            self.fuel -= 9

    def refill(self):
        if self.name == "falcon1":
            refilled_fuel = 5 - self.fuel
            self.fuel = self.fuel + refilled_fuel   #that is identical self.fuel = 5
            return refilled_fuel                    #can be a negative number
        elif self.name == "falcon9":
            refilled_fuel = 20 - self.fuel
            self.fuel = self.fuel + refilled_fuel   #that is identical self.fuel = 9
            return refilled_fuel                    #can be a negative number

    def getStats(self):
        stats = "name: " + self.name + ", fuel: " + str(
            self.fuel) + ", launches: " + str(self.number_of_launches)
        return stats


falcon1 = Rocket('falcon1')
returned_falcon9 = Rocket('falcon9', 11, 1)

falcon1.refill() # 5
falcon1.launch()

print(falcon1.getStats()) # name: falcon1, fuel: 4, launches: 1
print(returned_falcon9.getStats()) # name: falcon9, fuel: 11, launches: 1
