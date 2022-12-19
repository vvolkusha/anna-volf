from complex_number import ComplexNumber

print("What do you want to calculate?")
print("+ - * /")
s = input()
if s not in ["+", "-", "*", "/"]:
    raise ValueError
print("Enter the first real part:")
x_1 = float(input())
print("Enter the first image part:")
y_1 = float(input())
print("Enter the second real part:")
x_2 = float(input())
print("Enter the second image part:")
y_2 = float(input())
z_1 = ComplexNumber(x_1, y_1)
z_2 = ComplexNumber(x_2, y_2)
if s == "+":
    res = z_1 + z_2
elif s == "-":
    res = z_1 - z_2
elif s == "*":
    res = z_1 * z_2
else:
    res = z_1 / z_2
print(res)