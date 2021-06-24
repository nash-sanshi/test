class car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        print((str(self.year) + ' ' + self.make + ' ' + self.model).title())
        #long_name = str(self.year) + '' + self.make + '' + self.model
        #return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, miles):
        self.odometer_reading = miles
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
my_new_car = car('audi' , 'a4', '2016')
#print(my_new_car.get_descriptive_name())
my_new_car.get_descriptive_name()

my_new_car.update_odometer(20000)
my_new_car.read_odometer()

my_new_car.increment_odometer(200)
my_new_car.read_odometer()

class electriccar(car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = battery()

class battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery")    

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
        
        
my_tesla = electriccar('tesla', 'model 3', '2021')
my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()