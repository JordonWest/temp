my_coffee = ["peruvian", "ethiopian", "columbian", "mexican"]

# print(my_coffee[0])
# print(my_coffee[1])
# print(my_coffee[2])
# print(my_coffee[3])


# print with a for loop
# for coffee in my_coffee:
#     print(coffee)

# print("Done printing coffees")

# sum all of the numbers from 1 to 100
# range(starting_number, ending_number, step)
# sum = 0
# for i in range(0, 101):
#     sum += i
# print(sum)

# sum all of the number from 50 to 100
# for i in range(50, 101):
#     sum += i
# print(sum)

# sum all of the even number from 50 to 100
# for i in range(50, 101, 2):
#     sum += i
# print(sum)

# print("1st time")
# for i in range(len(my_coffee)):
#     if i == 1:
#         my_coffee[i] = "brazilian"
#     print(f"I love {my_coffee[i]} coffee!!")

# print("2nd time")
# for k in my_coffee:
#     if k == "brazilian":
#         k = "ethiopian"
#     print(k)

# print("3rd time")
# for j in my_coffee:
#     print(j)

# enumerate(my_coffee)
# for i, coffee in enumerate(my_coffee):
#     my_coffee[i] = "all"
#     print(f"{i}. {my_coffee[i]}")

# break - don't do anything else in the current execution of the list,

# for coffee in my_coffee:
#     if coffee == "ethiopian":
#         break
#     print(coffee)

# print("Outside the list")

# continue - ends the current iteration of the list
# for coffee in my_coffee:
#     if coffee == "columbian":
#         continue
#     print(coffee)
# print("Outside the list")

# 1
# 2 2
# 3 3 3
# 4 4 4 4

# range(5) - 0, 1, 2, 3, 4
# for i in range(5):
#     for j in range(i):
#         print(i, end=" ")
#     print("\n")

# what if I want to store more information about the coffee?
# dictionary - Key, value

peruvian = {
    "name": "La llama",
    "region": "Villa asuncion",
    "flavor": ["almond", "cherry", "chocolate"]
}

# print(my_coffee)
# print(peruvian["name"])
# peruvian["name"] = "el burro"
# print(peruvian["name"])

# print only the keys
for keys in peruvian.keys():
    print(keys)

# print the key value pairs
for pairs in peruvian.items():
    print(pairs)

# print only the values
for values in peruvian.values():
    print(values)

