def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


f_temp = float(input())

c_temp = fahrenheit_to_celsius(f_temp)

print(f"{f_temp} F = {c_temp:.2f} C")
