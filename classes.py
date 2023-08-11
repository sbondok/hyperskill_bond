list_str = ['upper()','lower()','title()','casefold()']

my_string = 'this is test'



for i in list_str:
    print(eval(f'my_string.{i}'))
