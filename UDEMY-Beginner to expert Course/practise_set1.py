price_product1 = input("what is the price of the product1 ")
Quanitity_product1 = input("What will be the Quanitity_product1")
price_product2 = input("what is the price of the product2 ")
Quanitity_product2 = input("What will be the Quanitity_product2")
price_product3 = input("what is the price of the product3 ")
Quanitity_product3 = input("What will be the Quanitity_product3")

result_product1 = float(price_product1) * float(Quanitity_product1)
result_product2 = float(price_product2) * float(Quanitity_product2)
result_product3 = float(price_product3) * float(Quanitity_product3)

result = result_product1 + result_product2 + result_product3

print(f"Your final prize of 3 product is {result}")