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