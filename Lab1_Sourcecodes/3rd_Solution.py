class Airline:
    def __init__(self, flightNo):
        Airline.source = input('Enter Src : ')
        Airline.destination = input('Enter Dest : ')
        print('Airlines that are available :')
        print('DELTA')
        print('SPICEJET')
        print('INDIGO')
        print('QATAR')
        Airline.airlinesName = input('Name the Airlines that you prefer to travel: ')
        self.flightNo = flightNo
#This method prints the details of the airlines
    def print_details(self):
        print('Airlines : ', Airline.airlinesName)
        print('Flight Number : ', self.flightNo)
        print(Airline.source, '-->', Airline.destination)
#Inheritance
class Employee(Airline):
    def __init__(self, employee_id, employee_name, employee_gender):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.employee_gender = employee_gender
#Method Overriding
    def print_details(self):
        print("Name of employee: ", self.employee_name)
        print('Employee id: ', self.employee_id)
        print('Employee gender: ', self.employee_gender)
#This class inputs all the Traveller details
class Traveller:
    def __init__(self):
        Traveller.traveller_fn = input('Enter first name : ')
        Traveller.traveller_ln = input('Enter last name : ')
        Traveller.traveller_PNo = input('Enter passport number: ')
        Traveller.traveller_gender = input('Enter gender : ')
        Traveller.traveller_class = input('Business or Economy class? : ')
#This class is used to calculate the baggage fare
class Baggage:
    def __init__(self):
        Baggage.numberOfBags = int(input('Number of bags you want to checkin : '))
        Baggage.totalBagFare =0;
        Baggage.numberOfBags = Baggage.numberOfBags
        if(Baggage.numberOfBags > 3):
            for i in range(Baggage.numberOfBags-3):
                Baggage.totalBagFare += 80
        print('You can take two bags for free !!! Total bag fare is for ', Baggage.numberOfBags,'is ',Baggage.totalBagFare)
#This class calculates the ticket cost based on the class, flight and bags
class TicketCost(Baggage, Traveller, Airline):
    def __init__(self):
        TicketCost.baseCost = 250
        TicketCost.baseCost = TicketCost.baseCost + Baggage.totalBagFare
        if(Traveller.traveller_class == 'business'):
            TicketCost.baseCost = TicketCost.baseCost + 250
        print('Total ticket cost is : ',TicketCost.baseCost)
#These details are displayed on the ticket by using this method
    def ticketDisplay(self):
        print('Ticket Details')
        print('****************************************************************')
        print('Traveller Name : ',Traveller.traveller_fn,' ', Traveller.traveller_ln)
        print('Traveller Passport Number : ',Traveller.traveller_PNo)
        print('Gender : ', Traveller.traveller_gender)
        print('Class : ', Traveller.traveller_class)
        print('Total number of bags checked in : ', Baggage.numberOfBags)
        print('Total Fare for the trip is : ',TicketCost.baseCost)
employee = Employee(5555, 'haneesh', 'male')
employee.print_details()
flight = Airline('RX1006')
traveller = Traveller()
bags = Baggage()
ticket = TicketCost()
ticket.ticketDisplay()
flight.print_details()



