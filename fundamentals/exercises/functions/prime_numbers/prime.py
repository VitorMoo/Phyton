#1

def is_prime(value):
    if value< 2:
        return False
    else:
        for i in range(2,value):
            if value % i ==0:           #example 1: 6 % 5 = 1
                return False            #           6 % 4 = 2
                                        #           6 % 3 = 0 so its not prime!
        return True