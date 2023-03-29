name = input('what is your name? ')

print(f"Hello, {name}")

file = open('saved-properties.txt','a')  #a- append w- write r-read 
file.write(f'{name}\n')
file.close()

"""
Here, also is one way, if you  don't want to use 
close() command
"""