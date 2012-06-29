class Zoo:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_injured(self):
        pass
##
####class for animals
####and all of its sub classes
##    
class Animals(Zoo):
    def __init__(self,name,gender,age):
        Zoo.__init__(self,name,gender,age)

    def feed(self):
        pass

    def reproduce(self):
        pass

    def gestation_period(self):
        pass

    def defense_mechanism(self,defense_mechanism):
        pass

##    class for the mode of movement
##    inheriting from animals
    
class Mode_of_movement(Animals):
    def __init__(self,name,gender,age,mode_of_movement):
        Animals.__init__(self,name,gender,age)
        self.mode_of_movement = mode_of_movement
        
    def get_mode_of_movement(self):
        return self.mode_of_movement

##    class for Type of animals
##    inheriting from animals
    
class Type (Animals):
    def __init__(self,name,gender,age,Type):
        Animals.__init__(self,name,gender,age)
        self.type = Type

    def get_type(self):
        return self.type

##this is the class for people
##and all of its subclasses
class People(Zoo):
    def __init__(self,name,gender,age,arrival,departure):
        Zoo.__init__(self,name,gender,age)
        self.phoneNo = ''
        self.address = ''
        self.email = ''
        self.arrival = arrival
        self.departure = departure
        
    def __str__(self):
        print "this is the people"

    def set_phoneNo(self, phoneNo):
        self.phoneNo= phoneNo

    def set_address(self, address):
        self.address = address

    def set_email(self, email):
        self.email = email
        
    def get_phoneNo(self):
        return self.phoneNo

    def get_address(self):
        return self.address

    def get_arrival(self):
        return self.arrival

    def get_departure(self):
        return self.departure

    def get_email(self):
        return self.email

##    This is the class for workers
##    inheriting from people
    
class workers(People):
    def __init__(self,name,gender,age,arrival,departure,year_of_emp):
        People.__init__(self,name,gender,age,arrival,departure)
        self.department = ''
        self.speciality = ''
        self.position = ''
        self.year_of_emp = year_of_emp

    def set_department(self, department):
        self.department = department

    def set_position(self, position):
        self.position = position

    def set_speciality(self, speciality):
        self.speciality = speciality

    def get_position(self):
        return self.position

    def get_department(self):
        return self.department

    def get_specialty(self):
        return self.specialty

    def get_year_of_emp(self):
        return self.year_of_emp

    def no_of_vistors_being_guided(self):
        pass

class Visitors(People):
    def __init__(self,name,gender,age,date,arrival_time,purpose):
        People.__init__(self,name,gender,age,arrival,departure)
        self.purpose = purpose
        self.depart_time = ''

    def set_depart_time(self,depart_time):
        self.depart_time = depart_time
        
    def set_purpose(self, purpose):
        self.purpose = purpose

    def get_purpose(self):
        return self.purpose

    def add_visitor(self):
        pass

    def rem_visitor(self):
        pass
