### DECLARATIONS ###
def check_input(user_input, num_of_choices):
    while True:
        if user_input == 'exit':
            exit()
        try:
            user_input = int(user_input)
            while not (1 <= user_input <= num_of_choices):
                choice = int(input(f'\nInvalid choice. Please select a number between 1 and {num_of_choices}: '))
            return user_input
        except ValueError:
            print(f'Invalid input. Please enter a valid number between 1 and {num_of_choices}.')



categories = ['small', 'big', 'eco', 'suv']
cars = [{'#': 1, 'category': categories[0], 'model': 'toyota yaris', 'costPD': 50, 'cc': 1200, 'seats': 4},
        {'#': 2, 'category': categories[1], 'model': 'mazda 6', 'costPD': 80, 'cc': 1800, 'seats': 5},
        {'#': 3, 'category': categories[2], 'model': 'toyota prius', 'costPD': 100, 'cc': 2000, 'seats': 5},
        {'#': 4, 'category': categories[3], 'model': 'jeep cherokee', 'costPD': 120, 'cc': 2200, 'seats': 5},
        {'#': 5, 'category': categories[0], 'model': 'opel corsa', 'costPD': 50, 'cc': 1400, 'seats': 4}]

customers = [{'name': 'Kostas', 'surname': 'Papadopoulos', 'address': 'Pou8ena 7', 'mail': 'user@user.com',
              'phone': '0987654321'},
             {'name': 'Klean8is', 'surname': 'Koumarianos', 'address': 'Spiti mou 2', 'mail': 'axl3@gmail.com',
              'phone': '1234567890'},
             {'name': 'Stathis', 'surname': 'Matsas', 'address': 'menw sto grafeio 1', 'mail': 'gstathis@hotmail.gr',
              'phone': '6989142390'}]

rentals = [{'car': cars[0], 'customer': customers[0], 'days': 3},
           {'car': cars[2], 'customer': customers[1], 'days': 4}]
flag = True


### PROGRAM START ###
while flag:
    prompt = input('Welcome! do you want to rent a car? (y/n/exit): ')
    if prompt == 'y':
        print('''Here are the available cars:
        a/a, size, model, costPD, cc, seats
        ''')
        for car in cars:
            print(f'{car['#']}, {car['category']}, {car['model']}, {car['costPD']}, {car['cc']}, {car['seats']}')
    
        # while True:
            # try:
            #     choice = input('\nWhich car do you want to rent?: (pick a number) ')
            #     if choice == 'exit':
            #         # print('Thank you for using our service!')
            #         exit()
            #     choice = int(choice)
            #     while not (1 <= choice <= 5):
            #         choice = int(input('\nInvalid choice. Please select a number between 1 and 5: '))
            #     break
            # except ValueError:
            #     print('Invalid choice. Please select a number between 1 and 5.')
        print('Which car do you want to rent?: (pick a number)')
        choice = check_input(input(), 5)
        print(f'You have chosen {cars[choice - 1]['model']}\n')

        name = input('please give your name: ')
        surname = input('please give your surname: ')
        address = input('please give your address: ')
        mail = input('please give your mail: ')
        phone = input('please give your phone: ')
        days = input('how many days do you want to rent the car?: ')

        customers.append({'name': name, 'surname': surname, 'address': address, 'mail': mail, 'phone': phone})
        rentals.append({'car': cars[choice - 1], 'customer': customers[len(customers) - 1], 'days': days})


        print(f'\nYou have successfully rented {cars[choice - 1]['model']} for {days} days.\n')

    elif prompt == 'n':
        # while True:
        #     try:
        #         choice = input('''Do you want to:
        #                        1. see the currently rented cars?
        #                        2. find a customer's rentals?
        #                        3. find a specific model's rentals?
        #                        exit?\n''')
        #         if choice == 'exit':
        #             # print('Thank you for using our service!')
        #             exit()
        #         choice = int(choice)
        #         while not (1 <= choice <= 3):
        #             choice = int(input('\nInvalid choice. Please select a number between 1 and 3: '))
        #         break
        #     except ValueError:
        #         print('Invalid choice. Please select a number between 1 and 3.')

        print('''Do you want to:
                                       1. see the currently rented cars?
                                       2. find a customer's rentals?
                                       3. find a specific model's rentals?
                                       exit?\n''')
        choice = check_input(input(), 3)

        if choice == 1:
            print('\nCurrently rented cars:')
            for rental in rentals:
                print({rental['car']['model']},rental['days'],'days')
    
        elif choice == 2:
            name = input('please give your name: ')
            surname = input('please give your surname: ')
            for customer in customers:
                if customer['name'] == name and customer['surname'] == surname:
                    print(f'\n{customer["name"]} {customer["surname"]}\'s rentals:')
                    for rental in rentals:
                        if rental['customer'] == customer:
                            print({rental['car']['model']}, rental['days'], 'days')
    
        elif choice == 3:
            model = input('please give the model of the car you want to find: ')
            for car in cars:
                if car['model'] == model:
                    print(f'\n{car["model"]}\'s rentals:')
                    for rental in rentals:
                        if rental['car'] == car:
                            print({rental['customer']['name']}, {rental['customer']['surname']})
        
        choice = input('can we do anything else for you? (y/n):')
        if choice == 'n':
            flag = False
    
print('\nThank you for using our service!')