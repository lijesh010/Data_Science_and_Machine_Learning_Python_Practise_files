'''
Exercise 6:
Create a Python module named greetings that contains functions to greet the user in different languages.
Write a program to use this module to greet the user in different languages.
'''
#creating the module
def wish(name):
    print('''choose your option
    1.English
    2.Spanish
    3.French
    4.Malayalam
    ''')
    lan=int(input("Enter the choice:"))
    if lan==1:
        print(f"Welcome {name}")
    elif lan==2:
        print(f"Bienvenida {name}")
    elif lan==3:
        print(f"Bienvenue {name}")
    elif lan==4:
        print(f"സ്വാഗതം {name}")
