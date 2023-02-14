class Animals:
    def __init__(self, name):
        self.name = name


    def display_info(self):
        print("Animals in Zoo:", self.__class__.__name__,"-", self.name , ":", 
        self.happy,"% happy,", self.energy, "% energy")
        return self


class Lion(Animals):
    def __init__(self, name):
        self.name = name
        self.happy = 60
        self.energy = 30


class Tiger(Animals):
    def __init__(self, name):
        self.name = name
        self.happy = 50
        self.energy = 70
        

class Bear(Animals):
    def __init__(self, name):
        self.name = name
        self.happy = 80
        self.energy = 20

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        # self.happy = happy
        # self.energy = energy

    def add_lion(self, name):
        self.animals.append( Lion(name) )
        return self

    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
        return self

    def add_bear(self, name):
        self.animals.append( Bear(name) )
        return self

    """This part doesn't work, i will finish it later   """
    # def feed(self, name):  
        # self.animals.happy += 10
        # # self.animals.energy += 10
        # return self

    def print_all_info(self):
        print("-"*20, self.name, "-"*20)
        for animal in self.animals:
            animal.display_info()


zoo1 = Zoo("John's Zoo")

zoo1.add_lion("Nala").add_lion("Simba")
zoo1.add_tiger("Rajah").add_tiger("Shere Khan")
zoo1.add_bear("Browny")
zoo1.print_all_info()


# zoo1.feed("Nala")
# zoo1.print_all_info()
