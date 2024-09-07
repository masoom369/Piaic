name = "hello world"

# Basic attributes
print(name.__class__)          # <class 'str'> this will tell u type of your variable like str or int
print(name.__doc__)            # The docstring for the str class
# String methods
print(name.capitalize())      # 'Hello world' this is making your first letter capital
print(name.casefold())        # 'hello world'
print(name.center(20, '*'))   # '****hello world****'
print(name.count('o'))        # 2 words number
print(name.encode())          # b'hello world'
print(name.endswith('world')) # True last word is world 
print(name.expandtabs(4))     # 'hello world' (no change as there are no tabs) if are change value of a variable it will show is all old  values
print(name.find('world'))     # 6
print(name.format())          # 'hello world'
print(name.format_map({}))    # 'hello world'
print(name.index('world'))    # 6 number of letters
print(name.isalnum())         # False if it has numbers 
print(name.isalpha())         # False
print(name.isascii())        # True
print(name.isdecimal())       # False
print(name.isdigit())         # False
print(name.isidentifier())    # False
print(name.islower())         # False
print(name.isnumeric())       # False
print(name.isprintable())     # True
print(name.isspace())         # False
print(name.istitle())         # False
print(name.isupper())         # False
print(name.join(['Hi', 'there'])) # 'Hihello worldthere'
print(name.ljust(20, '*'))    # 'hello world********'
print(name.lower())          # 'hello world'
print(name.lstrip())         # 'hello world'
print(name.maketrans('hello', 'HELLO'))  # Translation map
print(name.partition(' '))   # ('hello', ' ', 'world')
print(name.removeprefix('hello '))  # 'world'
print(name.removesuffix(' world'))  # 'hello'
print(name.replace('world', 'there')) # 'hello there'
print(name.rfind('o'))        # 7
print(name.rindex('o'))       # 7
print(name.rjust(20, '*'))    # '********hello world'
print(name.rpartition(' '))   # ('hello', ' ', 'world')
print(name.rsplit(' ', 1))    # ['hello', 'world']
print(name.rstrip())         # 'hello world'
print(name.split())          # ['hello', 'world']
print(name.splitlines())     # ['hello world'] (not split as no newline)
print(name.startswith('hello')) # True
print(name.strip())          # 'hello world'
print(name.swapcase())       # 'HELLO WORLD'
print(name.title())          # 'Hello World'
print(name.translate(str.maketrans('', '', ' '))) # 'helloworld'
print(name.upper())          # 'HELLO WORLD'
print(name.zfill(20))        # '00000000000hello world'
