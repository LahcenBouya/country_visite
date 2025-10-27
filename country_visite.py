travel_list = input("please type the name of the countries separated by comma :").split(", ")

for country in travel_list:
    print("\n", country, "\n")
    visited = input(f"have you visited {country} before? (yes, no): \n").lower()
    if visited == "yes":
        print("i hope you had a wonderful time \n")
    else:
        print("i hope you get to visit it soon \n")
    print("------------")
input("press enter to exit")