"""Main module.

This module implements the SportShoesStore and Sneakers classes
"""
class SportShoesStore:
    """Sport shoes store. Implements managing the store and printing some analytics.

    There are implemented methods for adding sneakers to shop, sorting them and printing the top
    sneakers by number of sales

    Attributes:
        sneakers_list (Sneakers[]): All sneakers in store are here.
    """

    def __init__(self):
        self.__sneakers_list = []

    def get_sneakers(self):
        return self.__sneakers_list

    def add_sneakers(self, sneakers):
        self.__sneakers_list.append(sneakers)

    def add_sneakers_bulk(self, sneakers):
        for sneaker in sneakers:
            self.add_sneakers(sneaker)

    def __sort_sneakers_by_custom_property(self, get_sort_property):
        """Insertion sort algorithm for specific value.
        Args:
            self
            get_sort_property (str): The property to sort by.

        Returns:
            Sneakers[]: The array of sorted sneakers by get_sort_property()
        """

        result = []
        # add each item to result list and move it to it's correct place
        for item in self.__sneakers_list:
            result.append(item)
            # If current result len is < 2, then we skip
            if len(result) < 2:
                continue
            # Take our new item and move it to right place
            curr_position = len(result) - 1
            while curr_position > 0:
                prev_position = curr_position - 1
                prev_item = result[prev_position]
                # If our value is less than prev value, then we swap them
                if get_sort_property(result[curr_position]) < get_sort_property(prev_item):
                    result[curr_position], result[prev_position] = result[prev_position], result[curr_position]
                # Move to the next iteration
                curr_position -= 1
        return result

    def sort_by_price(self):
        return self.__sort_sneakers_by_custom_property(Sneakers.get_price)

    def sort_by_quantity(self):
        return self.__sort_sneakers_by_custom_property(Sneakers.get_quantity)

    def get_most_popular(self):
        """Prints the top sneakers by number of sales in descending order."""

        sorted_by_sales = self.__sort_sneakers_by_custom_property(Sneakers.get_number_of_sales)
        for idx, item in enumerate(sorted_by_sales[::-1]):
            print(f"{idx + 1}. {item}")

class Sneakers:
    """Sneakers pair class. Implements getters for some attributes of sneakers pair

    Attributes:
        brand (str): brand
        size (int): EU size
        color (str): color
        price (int): price for one pair
        quantity (int): number of available pairs
        number_of_sales (int): number of sales
        material (string): material
    """

    def __init__(self, brand, size, color, price, quantity, number_of_sales, material):
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.number_of_sales = number_of_sales
        self.material = material

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def get_number_of_sales(self):
        return self.number_of_sales

    def __str__(self):
        return f"Brand: {self.brand}, Price: {self.price}, Size: {self.size}, Color: {self.color}, Quantity: {self.quantity}, Number of sales: {self.number_of_sales}, Material: {self.material}"

    def __repr__(self):
        return f"{chr(123)} Brand: {self.brand}; Price: {self.price}; Quantity: {self.quantity}; {chr(125)}"

def main():
    sport_shoes_store = SportShoesStore()

    sport_shoes_store.add_sneakers_bulk([
        Sneakers("Nike", 9, "Red", 100, 50, 1, "Leather"),
        Sneakers("Adidas", 10, "Blue", 80, 40, 8, "Mesh"),
        Sneakers("Reebok", 8, "Black", 90, 60, 6, "Synthetic"),
        Sneakers("Rick Owens", 10, "Blue", 1100, 40, 10, "Mesh"),
        Sneakers("Jordan", 8, "Black", 30, 210, 0, "Synthetic")
    ])

    sorted_by_price = sport_shoes_store.sort_by_price()
    print(sorted_by_price)
    print('-'*100)
    sorted_by_quantity = sport_shoes_store.sort_by_quantity()
    print(sorted_by_quantity)
    print('-'*100)
    sport_shoes_store.get_most_popular()

main()
