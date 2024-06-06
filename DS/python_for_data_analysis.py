# Introduction - Variables and Types

# (a) Create a variable named my_variable and assign it the value 123456789.
# (b) Create a variable named my_variable_times_2 whose value will be the double of the value of my_variable. Multiplication is carried out with the character *.
# (c) Display both variables.

my_variable = 123456789
my_variable_times_2 = my_variable * 2
print("my_variable: ", my_variable)
print("my_variable_times_2: ", my_variable_times_2)

# (a) Sort the list my_list in ascending order by assigning new values to its elements one by one.
# (b) Display my_list.

my_list = [4, -1, 2, -3, 3]
my_list[0] = -3
my_list[1] = -1
my_list[2] = 2
my_list[3] = 3
my_list[4] = 4
print("my_list: ", my_list)

# Indexation of a list with a string
word = 'tree'
# Displaying the first character
print('first letter', word[0])
# Displaying the last character
print('last letter',word[3])

a_long_list = [-16, 6, -4, -18, 18, 20, 21, -6, 19, 25, 11,
               2, 9, 7, -16, 16, 4, -15, 11, 7, 17, 18, 4,
               25, 17, 28, -6, 17, 1, 14, -20, -15, 20, -15,
               -8, 8, -19, -11, -20, -16, 3, 3, -10, -5, 10,
               24, -1, 1, -10, 6, 10, -6, -14, 25, 8, -11,
               -17, -9, 0, 21, 3, 14, 7, 10, 25, 24, -18, -11,
               2, 29, 17, -6, 6, -11, 2, -18, 20, -15, -11,
               15, -10, 8, -15, 25, -15, 10, 28, -12, 11, 14,
               27, -1, 10, -2, -15, -10, 19, 26, 3, 27]

# (a) Display the first 10 elements of the list a_long_list.
# (b) Display the last 10 elements of the list a_long_list.

print("Display the 10 first elements", a_long_list[0:10])
print("Display the last 10 elements", a_long_list[-10:])

my_list = [1, 5, "Hello", -1.4, "how", 103, "are", "you"]

# (a) Remove the elements "Hello", "how", "are" and "you" from my_list using the pop method. Note that the indices of the elements in the list change once an item has been deleted.
# (b) Display my_list.

my_list.pop(2)
my_list.pop(3)
my_list.pop(-2)
my_list.pop(-1)
print(my_list)

# (c) Create a list composed of the elements [2,3,2,1,4] and delete all of the values equal to 2 which are present in the list and then display the final list.

my_list1 = [2,3,2,1,4]
my_list1.remove(2)
my_list1.remove(2)
print("List after deleting all values equal to 2 :",my_list1)

# (c) Remove all numbers from the my_list list using the pop method.
# (d) Insert in my_list the elements "Bonjour", "comment", "ça" and "va" at the appropriate indices so that printing my_list displays:
# ["Hello", "Bonjour", "how", "comment", "are", "ça", "you", "va"]

my_list = [1, 5, "Hello", -1.4, "how", 103, "are", "you"]
my_list.pop(0)
my_list.pop(0)
my_list.pop(1)
my_list.pop(-3)
my_list.insert(1, "Bonjour")
my_list.insert(3, "comment")
my_list.insert(5, "ça")
my_list.insert(7, "va")
print(my_list)

# (e) Launch the following cell to create a variable x of value 0 and a list whose unique element will be x.

x = 0
a_list = [x]

# (f) Run the following cell several times:
# The value of x is incremented by 1.
# The new value of x is added at the end of the list a_list.

x = x + 1
a_list.append(x)
print(a_list)

### Merging 2 lists with the extend method

list_1 = ["Hello", "how", "are", "you", "?"]
list_2 = ["Fine", "and", "you", "?"]

# Merging the elements of list_2 with list_1
list_1.extend(list_2)

# Display of list_1
print(list_1)

### Merging 2 lists with the + operator

list_1 = ["Hello", "how", "are", "you", "?"]
list_2 = ["Fine", "and", "you", "?"]

# Merging the elements of list_2 with list_1
list_1 = list_1 + list_2
print(list_1)

# (h) Using the function sort, sort in ascending order the list containing the elements [4,-3,7] and then display the sorted list.

l1 = [4,-3,7]
# We sort the list in the ascending order
l1.sort()
# Displaying the list
print(l1)

# (i) Using the function sort, sort the list defined in the previous question (h) in the descending order and then display it.
l1.sort(reverse=True)
print(l1)

# (a) Run the cell below to perform tuple assignment.

a_tuple = "Hello", -1, 133
print(a_tuple)

# Tuple assignment
x, y, z = a_tuple

print(x)
print(y)
print(z)

a = 10
b = 5

a, b = b, a

print(a)
print(b)

# (a) Create and display a dictionary named card_id with the following key-values pairs:
# Key	Value
# "first name"	"Paul"
# "last name"	"Lefebvre"
# "emission"	1978
# (b) Overwrite the value associated with the key "first name" with the value "Guillaume" and display the new dictionary card_id.

# Definition of the dictionnary
card_id = {"first name": "Paul",
           "last name" : "Lefebvre",
           "emission"  : 1978}
print(card_id)

# Overwriting a field of the dictionnary
card_id["first name"] = "Guillaume"
print(card_id)

# (c) Add a new key "expiration" to the card_id dictionary by assigning it the value 1993 and display it.
# (d) How long was this ID card valid for?

card_id["expiration"] = 1993
print(card_id)
validity_duration = card_id["expiration"] - card_id["emission"]
print("This ID card was valid for", validity_duration, "years.")

# Operators and Control Structures

# (a) Create the variable distance and assign it the value 750 (distance between Paris and Marseille in km).
# (b) Create the variable speed and assign it the value 4.8 (average speed of a walker in km/h).
# (c) Create a new variable time which contains the value of distance divided by speed. The variable time should give us the time in hours that it would take for a walker to travel from Paris to Marseille without stopping.
# (d) How many days and hours would it take to go from Paris to Marseille without stopping? Your response should be displayed in the form "You would need __ days and __ hours to walk from Paris to Marseille.".

distance = 750
speed = 4.8
time = distance/speed
print("You would need",time//24,"days and",time%24,"hours to walk from Paris to Marseille.")

# (a) A magician claims that if we take a prime number that is not 2 or 3 and perform the following operations:
# square that number,
# add 17 to it,
# then divide it by 12,
# That we can expect the remainder to be 6. Is he right?
# Remember that a prime number is a number that is only divisible by 1 or itself. The 10 smallest prime numbers other than 2 and 3 are 5, 7, 11, 13, 17, 19, 23, 29, 31, 37.

prime_numbers = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
x = prime_numbers[0]
y=(x**2+17)%12
print(y)

# (a) In a single line of code, determine with a boolean value if  7 divides  3^7+2^14
# As on a calculator, you can use parentheses to set operation priorities.
# (b) Now determine if  7 divides  3^(2n+1)+2(4𝑛+2)for  𝑛=4,5 and  10

print((3**7+2**14)%7==0)
n=4
print((3**(2*n+1)+2**(4*n+2))%7==0)
n=5
print((3**(2*n+1)+2**(4*n+2))%7==0)
n=10
print((3**(2*n+1)+2**(4*n+2))%7==0)

# (a) Launch the following cell to instantiate the variable excerpt.

excerpt = ['The', '21', 'World', 'Cup', 'tournaments', 'have', 'been', 'won', 'by', 'eight',
           'national', 'teams.', 'Brazil', 'have', 'won', 'five', 'times', ',', 'and',
           'they', 'are', 'the', 'only', 'team', 'to', 'have', 'played', 'in', 'every',
           'tournament', '.', 'The', 'other', 'World', 'Cup', 'winners', 'are', 'Germany',
           'and', 'Italy', ',', 'with', 'four', 'titles', 'each', ';', 'Argentina', ',',
           'France', ',', 'and', 'inaugural', 'winner', 'Uruguay,', 'with', 'two', 'titles',
           'each', ';and', 'England', 'and', 'Spain', ',', 'with', 'one', 'title', 'each', '.']

print("France"in excerpt)
print("Croatia"not in excerpt)

# (a) Using the same logical expressions, determine whom between Bernadette and Marc can earn this bonus. For this you can:
# Create two variables seniority and salary.
# Evaluate the 3 decision criteria from the variables seniority and salary.
# Check if at least one of the criteria is satisfied.
# To test whether a value x is between two values a and b, you can either:

# Make two comparisons in two expressions and use a logical AND: x > a and x < b
# Make two comparisons in a single expression: a < x < b

#Bernadette
seniority=12
salary=2400

c1=seniority<5 and salary<1500
c2=(5<=seniority<=10) and (1500<=salary<=2300)
c3=seniority>10 and (salary>2300 or salary<1500)

print("Can Bernadette receive thte bonus?",c1 or c2 or c3)

#Marc
seniority=6
salary=1490

c1=seniority<5 and salary<1500
c2=(5<=seniority<=10) and (1500<=salary<=2300)
c3=seniority>10 and (salary>2300 or salary<1500)

print("Can Marc receive thte bonus?",c1 or c2 or c3)

# (a) Rewrite the following code using only an if statement, an elif statement and an else statement.
# if number >= 0:
#     if number == 0:
#         print("This number is 0.")
#     else:
#         print("This number is positive.")
# else:
#     print("This number is negative.")

number = -100
if number == 0:
    print ("This number is 0.")
elif number > 0:
    print ("This number is positive.")
else:
    print ("This number is negative.")

# (b) Is the syntax of the following code correct? If not, suggest a correction.
# if size < 160:
#   print("This person is small.")
# else if 160 <= size < 180:
#   print("This person is of medium height.")
# else 180 <= size < 200:
#   print("This person is very tall")
# else:
#   print("This person is very, very tall")

size = 205
if size < 160:
  print("This person is small.")
elif 160 <= size < 180:
  print("This person is of medium height.")
elif 180 <= size < 200:
  print("This person is very tall")
else:
  print("This person is very, very tall")

# Loops




















