# mini project: Banking System-(Online)

user_name_list = ["Lijesh", "Amal", "Kiran", "Fathima"]
pass_dict = {'Lijesh': 'L123456#', 'Amal': 'Amal12#', 'Kiran': 'Admin@123', 'Fathima': 'Applemango#'}
acc_list = [112233123, 112233124, 112233125, 112233126]
balance = {"Lijesh": 54367.34, "Amal": 15890.11, "Kiran": 2790.45, "Fathima": 129870.75}

print("Choose the option '0' if you are a New User.")
print("Choose the option '#' if you are a Existing User.")

info=input("Select:")

if info=='0':
    new_user=input("Please enter your new banking name:")
    new_password=input("Please enter your new password:")
    new_acc_no=int(input("Please enter your new Account number:"))

    if new_acc_no not in acc_list:
        user_name_list.append(new_user.capitalize())
        pass_dict[new_user.capitalize()]=new_password
        acc_list.append(new_acc_no)
        balance[new_user.capitalize()]=0
        print("Your account has been successfully created.")

        user = input("Please enter your banking name:")
        user_name = user.capitalize()
        password = input("Please enter your password:")
        acc_no = int(input("Please enter your Account number:"))

        if user_name in user_name_list:
            if password == pass_dict[user_name]:
                if acc_no in acc_list:
                    print("Hi,", user_name)
                    print("Welcome to Kerala Gramin Bank")
                    print("""Choose options,
                  1 for Deposit.
                  2 for withdrawal
                  3 for check balance
                  """)
                    choice = int(input("Enter your choice:"))

                    if choice == 1:
                        deposit_amnt = float(input("Enter the amount to deposit:"))
                        if deposit_amnt > 0:
                            balance[user_name] += deposit_amnt
                            print("Deposit successful.")
                            print("Your updated balance is:", balance[user_name])
                        else:
                            print("Invalid amount entered. Please enter a positive value.")
                        print("***Thank you for Banking with us***")
                        print("***Have a Nice day***")

                    elif choice == 2:
                        withdraw_amnt = float(input("Enter the amount to withdraw:"))
                        if withdraw_amnt > 0:
                            if withdraw_amnt <= balance[user_name]:
                                balance[user_name] -= withdraw_amnt
                                print("Withdrawal successful.")
                                print("Your updated balance is:", balance[user_name])
                            else:
                                print("Insufficient balance. Please try again.")
                        else:
                            print("Invalid amount entered. Please enter a positive value.")
                        print("***Thank you for Banking with us***")
                        print("***Have a Nice day***")

                    elif choice == 3:
                        print("Your balance is:", balance[user_name])
                        print("***Thank you for Banking with us***")
                        print("***Have a Nice day***")

                    else:
                        print("Invalid choice entered. Please try again.")

                else:
                    print("Invalid account number entered. Please try again.")
            else:
                print("Invalid password entered. Please try again.")
        else:
            print("Invalid username entered. Please try again.")

    else:
        print("Account already exists. Please Log in ")

elif info =='#':
    user = input("Please enter your banking name:")
    user_name = user.capitalize()
    password = input("Please enter your password:")
    acc_no = int(input("Please enter your Account number:"))

    if user_name in user_name_list:
        if password == pass_dict[user_name]:
            if acc_no in acc_list:
                print("Hi,", user_name)
                print("Welcome to Kerala Gramin Bank")
                print("""Choose options,
          1 for Deposit.
          2 for withdrawal
          3 for check balance
          """)
                choice = int(input("Enter your choice:"))

                if choice == 1:
                    deposit_amnt = float(input("Enter the amount to deposit:"))
                    if deposit_amnt > 0:
                        balance[user_name] += deposit_amnt
                        print("Deposit successful.")
                        print("Your updated balance is:", balance[user_name])
                    else:
                        print("Invalid amount entered. Please enter a positive value.")
                    print("***Thank you for Banking with us***")
                    print("***Have a Nice day***")

                elif choice == 2:
                    withdraw_amnt = float(input("Enter the amount to withdraw:"))
                    if withdraw_amnt > 0:
                        if withdraw_amnt <= balance[user_name]:
                            balance[user_name] -= withdraw_amnt
                            print("Withdrawal successful.")
                            print("Your updated balance is:", balance[user_name])
                        else:
                            print("Insufficient balance. Please try again.")
                    else:
                        print("Invalid amount entered. Please enter a positive value.")
                    print("***Thank you for Banking with us***")
                    print("***Have a Nice day***")

                elif choice == 3:
                    print("Your balance is:", balance[user_name])
                    print("***Thank you for Banking with us***")
                    print("***Have a Nice day***")

                else:
                    print("Invalid choice entered. Please try again.")

            else:
                print("Invalid account number entered. Please try again.")
        else:
            print("Invalid password entered. Please try again.")
    else:
        print("Invalid username entered. Please try again.")

