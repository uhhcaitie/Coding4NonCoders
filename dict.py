dict_example = {"A":1,"B":2,"C":3}
#print(dict_example["A"]

dict_example["D"]=4
#print(dict_example)

user_input=input("Prints all even numbers from 0 to... \nA: 10, B: 20, C:30, D:40: ")
user_input=user_input.upper()
max_number = {"A":10, "B":20, "C":30, "D":40}
for x in range(0, max_number[user_input]):
    if x%2==0:
        print(x)
