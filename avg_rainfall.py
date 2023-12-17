months = {
    1:"January",
    2:"Febuaray",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}

num_years = int(input("Input the number of years (Must be greater than 0, ex. 10, 15, 30): \n"))

total_rainfall = 0
total_month = 0

if num_years > 0:
    for year in range(1, num_years + 1):
        print("\nYear {}".format(year))
        for month in range(1, 13):
            rainfall = float(input("Enter the rainfall (inches) for {} (Must be greater than 0, ex. 4, 7, 5): ".format(months[month])))
            if rainfall >= 0:
                total_rainfall += rainfall
                total_month += 1
            else:
                print("Invalid input -- rainfall must be positive")
                exit()

    average_rainfall = total_rainfall / total_month

    print("\nThe total number of months is: {}".format(total_month))
    print("The total rainfall is: {} inches".format(total_rainfall))
    print("The average rainfall per month is: {:.2f} inches".format(average_rainfall))
else:
    print("Invalid input -- years must be positive")
