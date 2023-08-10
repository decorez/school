class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f'this restaurant called {self.restaurant_name}, {self.cuisine_type}')

    def open_restaurant():
        print('The restaurant is open.')

    def set_number_served(self, cus):
        self.number_served = cus
    def increment_number_served(self, cus = 1):
        self.number_served += cus

def main():
    
    restaurant1 = Restaurant('mcd', 'chicken')
    #restaurant2 = Restaurant('mixue', 'ice cream')
    #restaurant3 = Restaurant('kfc', 'chicken')
    #restaurant4 = Restaurant('pecel lele', 'seafood')

    restaurant1.describe_restaurant()
    restaurant1.set_number_served(10)
    print(restaurant1.number_served)
    restaurant1.increment_number_served(12)
    print(restaurant1.number_served)
    #restaurant2.describe_restaurant()
    #restaurant3.describe_restaurant()
    #restaurant4.describe_restaurant()

if __name__ == '__main__':
    main()