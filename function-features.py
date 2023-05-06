import statistics

# arb_args - Takes in any number of arguments and prints them one at a time.

def arb_args(a, b):
    sum = a + b
    ext = a - b 
    return sum, ext

print(arb_args(1,2))

# inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.

def inner_func(x):

    def mulbyFive(param):
        return param * 5
    
    new_val = mulbyFive(x)
    print(new_val)

inner_func(3)

def lunchLady(StudentName, Lunch=False):
    if Lunch == False:
        Lunch = 'Mystery Meal'
    return f'My Sname is {StudentName} & my favorite meal is {Lunch}'

print(lunchLady('Jose', 'Sushi'))
print(lunchLady('James'))

# sum_n_product - Accepts two integers and returns both the sum and the product.

def sum_n_product(b, c):
    return b + c, b * c

print(sum_n_product(3, 4))

# alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function

# alias_arb_args = arb_args()

# arb_mean - Accepts any number of integers and prints their average.

def arb_mean(*num):
    arrAvg = statistics.mean(num)
    print(arrAvg)

arb_mean(1,2,3,5)

# arb_longest_string - Accepts any number of strings and returns the longest one.

def arb_longest_string(*strings):
    for i in strings:
        higher_one = max(strings, key=len)
    return higher_one

print(arb_longest_string('jose', 'maria', 'adee'))