from datetime import date
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np

def read_sales_data(file_path):
	sales = list()
	with open(file_path, 'r') as file:
		for line in file:
			product, quantity, price, datestr = line.strip().split(', ')
			sales.append({'product_name': product, 
						  'quantity': int(quantity), 
						  'price': float(price), 
						  'date': date.fromisoformat(datestr)})
	return sales


def total_sales_per_product(sales_data):
	total_sales = dict()
	for item in sales_data:
		if item["product_name"] not in total_sales:
			total_sales[item["product_name"]] = item["quantity"] * item["price"]
		else:
			total_sales[item["product_name"]] += item["quantity"] * item["price"]
	return total_sales


def sales_over_time(sales_data):
	sales_by_date = dict()
	for item in sales_data:
		date_str = item["date"].strftime("%Y-%m-%d")
		if date_str not in sales_by_date:
			sales_by_date[date_str] = item["quantity"] * item["price"]
		else:
			sales_by_date[date_str] += item["quantity"] * item["price"]
	return OrderedDict(sorted(sales_by_date.items()))


def product_with_max_sales(sales_data):
	data = total_sales_per_product(sales_data)
	draw_bar_chart(data)
	return find_max(data)


def max_sales_date(sales_data):
	data = sales_over_time(sales_data)
	draw_bar_chart(data)
	return find_max(data)


def find_max(data):
	max_value = max(data.values())
	for k, v in data.items():
		if v == max_value:
			return k


def draw_bar_chart(data):
	x = np.array(list(data.keys()))
	y = np.array(list(data.values()))

	plt.bar(x, y)
	plt.xticks(x, list(data.keys()), rotation='vertical')
	plt.show()


def main():
	file_path = "goods.txt" # generated too many random product lines, let's use the first 15 entries
	sales_data = read_sales_data(file_path)
	product = product_with_max_sales(sales_data[:15])
	sales_date = max_sales_date(sales_data[:15])
	print(f"Продукт, принёсший наибольшую выручку: {product}")
	print(f"День, в который была получена наибольшая сумма продаж: {sales_date}")


if __name__ == "__main__":
	main()
