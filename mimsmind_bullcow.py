def get_bullcow(user_num, random_num):
    bull = 0
    cow = 0
    #calculating individual digits in the number entered by the user and random number and comparing them
    for u in range(len(user_num)) :             # run loop for each digit in user number
        list_of_digits_counted = []
        for r in range(len(random_num)):        # run loop for each digit in random number
#             instance_counted  = False
            if u == r:                          # if index positions are same and digits at these positions are also same, increment bull by one
                if user_num[u] == random_num[r]:
                    bull += 1
#                     instance_counted = True
                    list_of_digits_counted.append(user_num[u]) # List to add occurances of all digits till now
                    
        if  (user_num[u] not in list_of_digits_counted) and  (user_num[u] in random_num):
            cow += 1
            
    values = [bull, cow]
    return values
