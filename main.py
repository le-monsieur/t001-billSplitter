
import random
num_of_peeps = int(input('Enter the number of people joining (including you):\n'))
print()
if num_of_peeps <= 0:
    print("No one is joining for the party")
else:
    print('Enter the name of every friend (including you), each on a new line:')
    friends = {}
    for _ in range(num_of_peeps):
        names = input()

        friends[names] = 0

    total_bill = float(input('Enter the total bill value:\n'))
    lucky_feature = input('Do you want to use the "Who is lucky" feature? Write Yes/No:\n')
    if lucky_feature == 'Yes':
        
        lucky_one = random.choice(list(friends))
        print(lucky_one,'is the lucky one!')
        
        ind_bill = round(total_bill/(num_of_peeps-1), 2)  
        for val in friends:
            friends[val] = ind_bill
            friends[lucky_one] = 0   
        print(friends)   
        
    elif lucky_feature == 'No':
        print('No one is going to be lucky') 
        ind_bill = round(total_bill/num_of_peeps, 2)  
        for val in friends:
            friends[val] = ind_bill   
        print(friends)    
  
