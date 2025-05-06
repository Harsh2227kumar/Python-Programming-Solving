class Car:
	def __init__(self, brand, price, model,color):
		self.brand=brand
		self.price=price
		self.model=model 
		self.color=color 

	def display_details(self):
		print(self.brand)
		print(self.price)
		print(self.model)
		print(self.color)

class Car1(Car):
	def display_details(self):
		super().display_details()

class Car2(Car):
	def display_details(self):
		super().display_details()

def get_car_details():
	brand = input("brand: ")
	price = float(input("price: "))
	model = input("model: ")
	color = input("color: ")
	return brand, price, model, color

print("Details for Car 1:")
car1_brand, car1_price, car1_model, car1_color = get_car_details()
Car1=Car1(car1_brand,car1_price,car1_model,car1_color)
# create an object car1


print("Details for Car 2:")
car2_brand, car2_price, car2_model, car2_color = get_car_details()
Car2=Car2(car2_brand, car2_price, car2_model, car2_color)
# Create the second car object


print("Car 1 Details:")
# Display details of the car1
Car1.display_details()



print("Car 2 Details:")
# Display details of the car1
Car2.display_details()