name_1 = input("What is your name?")
name_2 = input("What is your name?")
name_3 = input("What is your name?")

Slice_in_pizza = input("how many slice in pizza?")
Price_of_pizza = input("what is the price of the pizza?")
Percentage_ate_by_persona1 = input(name_1 + " what percentage of the pizza yuv have ate?")
Percentage_ate_by_persona2 = input(name_2 + " what percentage of the pizza yuv have ate?")
Percentage_ate_by_persona3 = input(name_3 + " what percentage of the pizza yuv have ate?")

no_of_slices_ate_person_1 = float(Percentage_ate_by_persona1) * float(Slice_in_pizza)
no_of_slices_ate_person_2 = float(Percentage_ate_by_persona2) * float(Slice_in_pizza)
no_of_slices_ate_person_3 = float(Percentage_ate_by_persona3) * float(Slice_in_pizza)

prize_paid_name_1 = float(Price_of_pizza) / float(no_of_slices_ate_person_1)
prize_paid_name_2 = float(Price_of_pizza) / float(no_of_slices_ate_person_2)
prize_paid_name_3 = float(Price_of_pizza) / float(no_of_slices_ate_person_3)

print(f"{name_1} has paid Rs {prize_paid_name_1}")
print(f"{name_2} has paid Rs {prize_paid_name_2}")
print(f"{name_3} has paid Rs {prize_paid_name_3}")
