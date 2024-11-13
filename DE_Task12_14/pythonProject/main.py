def total_revenue(purchases):
    sum = 0
    for purchase in purchases:
        sum += purchase['price'] * purchase['quantity']
    return sum


def items_by_category(purchases):
    categories = {}
    for purchase in purchases:
        category = purchase['category']
        item = purchase['item']
        if category not in categories:
            categories[category] = []
        if item not in categories[category]:
            categories[category].append(item)
    return categories


def expensive_purchases(purchases, min_price):
    return [purchase for purchase in purchases if purchase['price'] >= min_price]


def average_price_by_category(purchases):
    prices = {}
    for purchase in purchases:
        category = purchase['category']
        if category not in prices:
            prices[category] = []
        prices[category].append(purchase['price'])
    for category, category_prices in prices.items():
        prices[category] = round(sum(category_prices) / len(category_prices), 2)
    return prices


def most_frequent_category(purchases):
    category_totals = {}
    for purchase in purchases:
        category = purchase['category']
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += purchase['quantity']
    return max(category_totals, key=category_totals.get)


purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

print(f"Общая выручка: {total_revenue(purchases)}")
print(f"Товары по категориям: {items_by_category(purchases)}")
print(f"Покупки дороже 1.0: {expensive_purchases(purchases, 1.0)}")
print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")
