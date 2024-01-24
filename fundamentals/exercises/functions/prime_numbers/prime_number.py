#2

import prime

def main():
    print('this program outputs a list of prime numbers that exists in a user specified range')

    start_range=int(input('Start Range: '))
    end_range=int(input('End range: '))

    total_primes=0

    print()
    for i in range(start_range,end_range):
       if  prime.is_prime(i):
           
           total_primes+=1
           
           print(f'.\t {total_primes}', '\t', i)
    print(f'\t there are {total_primes} prime number between {start_range} and {end_range}')

main()
