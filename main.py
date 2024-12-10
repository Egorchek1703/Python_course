# Functions

def say_hello():
    print("Hello")

say_hello()



a = int(input('a = '))
b = int(input('b = '))
def sum():
    return a + b

result = sum()
print(result)



def multiply_by_2(num):
    return(num * 2)

print( multiply_by_2(5) ) # 10



def calc_factorial(n):
    """Calculate factorial of numbers"""
    if (n == 1):
        return 1
    else:
        return n * calc_factorial(n - 1)

factorial_num = int( input("What number do you want to calculate factorial of? ") )
print( calc_factorial(factorial_num) )


print('==================================')
def safe_user_data(*arguments):
    user = []
    for piece_of_data in arguments:
        user.append(piece_of_data)
    return user
print( safe_user_data('Egor', '24', 'DevOps', 'Hachapuri') )
print('==================================')

print('==================================')
def safe_user_data(**arguments):
    user = arguments
    return user
print( safe_user_data(name='Egor', age='24', work='DevOps', dishes='Hachapuri') )
print('==================================')

def create_list_and_dict(static_arg, static_arg2, *unnamed_args, **named_args):
    print(static_arg)
    print(static_arg2)
    print(unnamed_args)
    print(named_args)

create_list_and_dict(1, 2, 'I', 'am', 'a', 'big', 'lover', 'of', 'python', '!', name='Egor', age=24, phone='8(800)555-35-35')