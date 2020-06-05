#Write a Python program to calculate the popularity of programming languages at a computer school. The program should receive a keystroke named by the person and the programming language that program. The program must provide an option menu between the three languages taught in the course: (1) C + +(2) Javaand (3) Python. Create a dictionary to store each person and the value of their vote. At the end, print out how many votes each language got.


# 2- Use data entry via the keyboard to ask the user to enter two numbers (int or decimal). Your program should perform the addition, subtraction, multiplication, division and square root operations first number entered and then display the result on the screen.

num1 = float(input("Choose one number:"))
num2 = float(input("Choose another number: "))
print("\nSoma:" + str(num1 + num2), end= " ")
print("\nSubtraction:" + str(num1 - num2), end=" ")
print("\nMultiplication:" + str(num1 * num2), end=" ")
print("\nSquare root of" + " "+  str(num1) +" "+ "is: "+ str((num1)**2), end=" ")

# 3- Develop a Python program that should use a material list for a particular student. Now perform the following operations:
#Print the list on the screen;
materials = ['pen', 'notebook', 'book', 'pencil']
print (materials)
#Add a new material;
materials.append("laptop")
print(materials)
#Print the position in which the new material was added;
print(materials.index("laptop"))
# Sort the list in an ascending manner and print it again; • Show on the screen the size of the list 
print(materials.sort())
print (len(materials))

#Make a program to print on the screen the sum of 10 int numbers provided by the keyboard.
 
numeros = []
number = (int(input("Choose a number: ")))

for number in range(0, 10):
    numeros.append(number)
    print(sum(numeros))