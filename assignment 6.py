#Assignment 6
#Name: Rajat Singh Bishth
#SID : 21107047
#Branch: Mechanical
print("Q1")
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))

print("Q2")
user = input("Enter a word, phrase or sequence to see if it is a palindrome:")
if user == user[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

print("Q3")
from math import factorial

n = 5   # number of rows
for i in range(n):
    for j in range(n - i + 1):
        # for left spacing
        print(end=" ")

    for j in range(i + 1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

    # for new line
    print()

print("Q4")

def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

    return True

string = input("Enter a string to check if it is a pangram: ")
if ispangram(string) == True:
    print("It is a pangram.")
else:
    print("It is not a pangram.")

print("Q5")
items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))

print("Q6")

def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")

    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: {kwargs['student_name']}")
            print(f"Student Class: {kwargs['student_class']}")


student_data(student_id='21107221', student_name='Matthew')

student_data(student_id='21101201', student_name='Henry', student_class ='12')

print("Q7")

class Student:
    pass
Rajat = Student()
Rajat.name = "Rajat"
print(Rajat)
print(Rajat.name)

class Marks:
    pass
mark = Marks()
mark.a = 70
mark.b = 82
print(mark)
print(mark.a)
print(mark.b)

print("class Student:",type(Student),"class Marks:",type(Marks))

print("Q8")

class Zero:
    def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(Zero().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

print("Q9")
class Brackets:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(Brackets().is_valid_parenthese("(){}[]"))
print(Brackets().is_valid_parenthese("()[{]}("))
print(Brackets().is_valid_parenthese("()"))

'''

OUTPUT OF THE CODE
Q1
True
Q2
Enter a word, phrase or sequence to see if it is a palindrome:madam
It is a palindrome.
Q3
      1 
     1 1 
    1 2 1 
   1 3 3 1 
  1 4 6 4 1 
Q4
Enter a string to check if it is a pangram: The quick brown fox jumps over the lazy dog
It is a pangram.
Q5
green-red-yellow-black-white
black-green-red-white-yellow
Q6

Student ID: 21107221
Student Name: Matthew

Student ID: 21101201
Student Name: Henry

Student Name: Henry
Student Class: 12
Q7
<__main__.Student object at 0x000001E7E891FFD0>
Rajat
<__main__.Marks object at 0x000001E7E891FE20>
70
82
class Student: <class 'type'> class Marks: <class 'type'>
Q8
[[-10, 2, 8], [-7, -3, 10]]
Q9
True
False
True

'''