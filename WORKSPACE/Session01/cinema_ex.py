weekday = "Saturday" 
title = "Ferris Bueller's Day Off"
capacity = 200
n_adult = 12
n_child = 0
n_student = 97
price_adult = 9.99
price_child = 4.99
price_student = 5.99

cash_taken = (n_adult * price_adult) + (n_child * price_child) + (n_student * price_student)
total_tickets_sold = n_adult + n_child + n_student
tickets_remaining = capacity - total_tickets_sold

print("Welcome to the University of Exeter cinema!")
print(f"Next {weekday} we will be showing {title}!")
print(f'{total_tickets_sold} of {capacity} tickets were sold, {capacity - total_tickets_sold} tickets remain!')
print(f'£{cash_taken:.2f} worth of tickets were sold!')