num_books = int(input("Enter the number of books purchased (0, 2, 4, 6, 8 or more): "))

if num_books == 0:
    print("You are awarded 0 points")
elif num_books == 2:
    print("You are awarded 5 points")
elif num_books == 4:
    print("You are awarded 15 points")
elif num_books == 6:
    print("You are awarded 30 points")
elif num_books >= 8:
    print("You are awarded 60 points")
else:
    print("Invalid input")