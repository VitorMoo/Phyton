#lottery number generator

import random as rnd

start_range=0
final_range=9
lottery_digits=7

def main():
    run_again='y'
    while run_again=='y':
        print()
        print('lottery number generator\n')

        #populating list objects with random values 
        lottery_numbers=[]      #empty list


        for i in range(lottery_digits):
            lottery_numbers.append(rnd.randint(start_range,final_range))
        #end for 
            
        print('Lottery numbers:' ,sep=' ',end='')
        counter=0               #creating a counter

        for i in lottery_numbers:
            if counter == 0:          #first index is == to 0 so the first number wont have -
                print(i,sep="", end="")
            else:   
                print("-", i, sep="",end="")
            counter+=1

        print('\n')

        run_again=input("do you want to generate another set of lottery numbers?(y/n)").lower()
        while run_again != 'y' and run_again != 'n':
            print('Please enter either (y) or (n) ')
            run_again=input("do you want to generate another set of lottery numbers?(y/n)").lower()

# calling main function
main()