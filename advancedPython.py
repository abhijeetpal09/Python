my_dict = {
  "youtube":"true",
  "snapchat":"false",
  "instagram":"true"
}

#.items() returns an array of tuples with each tuple consisting of a key/value pair from the dictionary
#.keys() method returns a list of the dictionary's keys
#.values() method returns a list of the dictionary's values.
#these methods will not return the keys or values from the dictionary in any specific order.
#You can think of a tuple as an immutable (that is, unchangeable) list. Tuples are surrounded by ()s and can contain any data type.
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

#list_comprehension
even_squares = [x ** 2 for x in range(1,12) if x % 2 == 0]
print(even_squares)
cubes_by_four = [x ** 3 for x in range(1,11) if (x ** 3) % 4 == 0]
print(cubes_by_four)

#List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:
#[start:end:stride]
#start-inclusive, stride-exclusive
#he default starting index is 0.The default ending index is the end of the list.The default stride is 1.
my_list = range(1, 11) # List of numbers 1 - 10
print(my_list[::2])

#Reverse a list with negative stride
my_list = range(1, 11)
backwards = my_list[::-1]
print(backwards)
#Lambda functions are defined using the following syntax:
#Python 3 onwards list
my_list = range(16)
print(list(filter(lambda x: x % 3 == 0, my_list)))
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
strn = filter(lambda lang:lang=="Python", languages)
print(list(strn))

squares = [x ** 2 for x in range(1,11)]
print(list(filter(lambda y:y >=30 and y<=70,squares)))

threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print(threes_and_fives)

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x:x!='X',garbled)
print("".join(list(message)))

print(5 >> 4)  # Right Shift
print(5 << 1)  # Left Shift
print(8 & 5)  # Bitwise AND
print(9 | 4)  # Bitwise OR
print(12 ^ 42) # Bitwise XOR
print(~88)     # Bitwise NOT(1's complement)

print(int("1",2))
print(int("10",2))
print(int("111",2))
print(int("0b100",2))
print(int(bin(5),2))
# Print out the decimal equivalent of the binary 11001001.
print(int("11001001",2))

def flip_bit(number,n):
  result = number ^ (0b1 << n)
  return bin(result)

print(flip_bit(32,2))