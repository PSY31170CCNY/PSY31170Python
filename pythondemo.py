#pythondemo.py
x1 = """fundamental components of python include:
- variables : names for stored information
- data types: numbers (integers, floating point, complex)
            characters (represented internally as binary codes e.g. ASCII)
            text strings: sequences of characters delimeted by matching
                single or double quotes)
- commands : tells python to do something eg. print ('xxx')
- assignment statements: variable = value eg: x=5
- expressions: combinations of variables and values and operations that
    python has to figure out
- conditional expressions: if (condition is True) : do something
- relational expressions: Boolean values: True and False, comparison operators > (greater than,
        < less than, == equal to
        see: https://www.tutorialspoint.com/python3/python_basic_operators.htm
loops:
for variable = expression that evaluates to a list:
    do something with the next item in the list
eg:
>>> for N in range(3): print ("loop number ",N)

while condition is True:
    do something
eg:
while n > 0:
	n= n-1
	print('loop number',n)
-user interactions:
    input( "prompt in quotes", variable_to_store_user_response)
        eg: input('What's your name, username)
        then you can use the variable: print('Hello,',username)

- lists: items separated by , enclosed in square brackets:
    eg: [1,2,'Dave','0', ['nested list', 'second part'] ]
    slice the list to get a specific part: mylist[index1:indexn]

- dictionary: Dick={label1=value1, label2=value2, ... labeln=valuen}
        print(Dick[label3])

- set, is an immutable list in parentheses: e.g.: x = ('a', 3, 'z', 1)
    can't be changed but runs faster
    

    

    
    
    
