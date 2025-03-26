def calculate_diameter(radius):
	return 2 * radius

if __name__ == "__main__":
	try:
		radius = float(input("Введите радиус окружности"))
		diameter = calculate_diameter(radius)
		print("диаметр окружности равен:", diameter)
	except ValueError:
		print("Ошибка: необходимо ввести числовое значение.") 