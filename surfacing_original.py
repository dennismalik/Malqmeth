from fractions import Fraction
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import itertools
from collections import Counter

#Modulo calculation
def Modulo_1():

    x = input("in a form of (x%y): ")
    x = int(eval(x))
    result = "Applicable" if x == (10%3) else "Not applicable"
    print(f"x: {x}, {result}")


#calculating leftover surface area of a square/rectangle inhibited by circle
def calculate_surface_2():

    constant = math.pi                    # circle area calc
    radius = int(input("r: "))
    circle_area = round(constant * (radius ** 2))

    surface_shape = input("rectangle or a square? ")

    if surface_shape == "rectangle":                 #surface area calc
        length_rectangle = int(input("x: "))
        height_rectangle = int(input("y: "))
        shape_area = length_rectangle * height_rectangle

        text = f"(CA,RA): {circle_area}, {shape_area}"

    elif surface_shape == "square":
        side_square = int(input("x: "))
        shape_area = side_square ** 2

        text = f"(CA,SA): {circle_area}, {shape_area}"

    leftover_area = shape_area - circle_area
    return text, circle_area, shape_area, leftover_area


#arithmetic sequence of odd numbers
def arithmetic_sequence_odd_num_3():

    x = int(input("Submit a: "))
    a = (2 * x) + 1
    b = int(input("Submit difference: "))
    c = int(input("Submit nth term: "))
    print("a sequence generated: ")
    for i in list(range(a, a + b*c, b)):
        print(i)
    sequence = list(range(a, a + b*c, b))

    Sn = int(c * (2 * a + (c-1) *b)) // 2         #Sn calculation
    print("Sum of sequence: ", Sn)

    d = input("Figure out Un?: yes/no ").strip().lower() #Un calculation
    if d == "yes":
        Un_yes = int((input("Un: ")))
        print(f"U{Un_yes}: {a + (Un_yes-1)*b}")
    else:
        print("Skipping Un")

    e = input("Need to find index of Un value?: yes/no").strip().lower() #nth order of Un value
    if e == "yes":
        Un_value = int(input("Un value: "))
        try:
            i_n = sequence.index(Un_value)
            print(f"The value is placed at: {i_n + 1}th position")
        except ValueError:
            print("Value not found in sequence")
    elif e == "no":
        print("Skipping index of Un value")
    else:
        print("Invalid input")


#random rectangle coordinates
def rectangle_coordinates_4():

    x = int(input("Input limit of x: "))
    y = int(input("Input limit of y: "))
    if x * y < 4:
        print("Error: Not enough points to generate 4 unique coordinates")
    else:
        x_coordinates = []
        y_coordinates = []
        for i in range(x):
            for j in range(y):
                print(" Possible co-ordinates combinations: ")
                print(f"(results :{i}, {j})")
                x_coordinates.append(i)
                y_coordinates.append(j)

        random_coordinates = random.sample(list(zip(x_coordinates, y_coordinates)), 4)
        if len(random_coordinates) < 4:
            print("Error: Not enough unique coordinates to sample 4 points")
        else:
            plt.plot(*zip(*random_coordinates), marker='o', linestyle='-')
            plt.show()


#even number count
def even_number_count_5():

    count = 0
    end_term = int(input("Input end term: "))
    for x in range(1, end_term + 1):
        if x % 2 == 0:
            count += 1
            print(x)
    print(f"we have {count} even numbers between 1 and {end_term}")


#Integral calculation and graph display using matplotlib
def calculate_integral(a, power):
    if power.startswith("(") and power.endswith(")"):
        y = int(power[1:-1].split("/")[0])      #exponent being fractional
        j = int(power[1:-1].split("/")[1])
        if j == 0:                                       #exponent zero or division by zero
            return "Error: Division by zero in fraction"
        new_exponent = Fraction(y, j) + 1
        if new_exponent == 0:
            return "Error: Power rule doesn't apply (ln case)"
        coefficient = Fraction(a) / new_exponent
        return coefficient, new_exponent, f"integrated result: {coefficient}x^{new_exponent} + C"
    elif power.startswith("("):           #exponent being fractional and coefficient also fractional
        close = power.index(")")
        inside = power[1:close]
        y = int(inside.split("/")[0])
        j = int(inside.split("/")[1])
        leftover = power[close + 1:]
        z = int(leftover.split("/")[1]) if "/" in leftover else 1
        if j == 0 or z == 0:
            return "Error: Division by zero in fraction"
        new_exponent = Fraction(y, j) + 1
        if new_exponent == 0:
            return "Error: Power rule doesn't apply (ln case)"
        coefficient = Fraction(a, z) / new_exponent
        return coefficient, new_exponent, f"integrated result: {coefficient}x^{new_exponent} + C"
    else:                                           # coefficient being fractional
        y = int(power.split("/")[0])
        z = int(power.split("/")[1]) if "/" in power else 1
        if z == 0 or (y+1) == 0:
            return "Error: Power rule doesn't apply to ln or division by zero"
        coefficient = Fraction(a, z * (y + 1))
        new_exponent = y + 1
        return coefficient, new_exponent, f"integrated result: {coefficient}x^{new_exponent} + C"


#probability calculation using combinatorics in a secluded environment
def probability_calculation_7():
    user_probability = input("Do you want to calculate probability? (yes,C/P /yes with multiple cases/no): ").lower().strip()
    if user_probability == "yes, C":
        detail_required = int(input("input different variations if exist in a form of (group,members): ")).strip() #group as n(a) with C and universe as n(s)
        group = int(detail_required.split(",")[0])
        members = int(detail_required.split(",")[1])
        possible_outcomes = list(itertools.combinations(range(group), members))
        probability = Fraction(len(possible_outcomes), math.comb(group, members))
        print(f"Probability of this case: {probability}")

    elif user_probability == "yes, P":
        detail_required = int(input("input different variations if exist in a form of (group,members): ")).strip() #group as n(a) with P and universe as n(s)
        group = int(detail_required.split(",")[0])
        members = int(detail_required.split(",")[1])
        possible_outcomes = list(itertools.permutations(range(group), members))
        probability = Fraction(len(possible_outcomes), math.comb(group, members))
        print(f"Probability of this case: {probability}")

    elif user_probability == "yes with multiple cases":
        all_cases = []
        detail_required = int(input("input different variation if exist in a form of (group,members): ")).strip() #multiple groups, no order, universe as n(s)
        while True:
            detail_required = input("input different variation if exist in a form of (group,members) or type 'done' to finish: ").strip()
            if detail_required.lower() == "done":
                break
            group = int(detail_required.split(",")[0])
            members = int(detail_required.split(",")[1])
            possible_outcomes = list(itertools.combinations(range(group), members))
            all_cases.append(len(possible_outcomes))
            print(f"{group}C{members} = {len(possible_outcomes)}")
            print(f"All cases collected: {all_cases}")
            #PROBABILITY COUNT
            probability = Fraction(len(possible_outcomes), sum(all_cases))
            print(f"Probability of this case: {probability}")
    elif user_probability == "no":                                     #no variations, only n(s)
        print("Skipping variations, 0 variations")
        user_specific = input("Combinations or Permutations? (aCb/aPb): ").strip().upper()
        if user_specific == "C":
            a = int(input("value of a: "))
            b = int(input("value of b: "))
        if b > a:
            print("B cannot be greater than a")
        else:
            universe = list(itertools.combinations(range(a), b))
            print(f"Result of {a}C{b}: {len(universe)}")
            return a, b, len(universe)
    elif user_specific == "P":
        a = int(input("value of a: "))
        b = int(input("value of b: "))
        if b > a:
            print("B cannot be greater than a")
        else:
            result = math.perm(a,b)
        return a, b, result, print(f"Result of {a}P{b}: {result}")

# ---------------- MENU ----------------
while True:
    choice = input("Choose a calculation type: 1. Modulo, 2. CRS calculation surface, 3. Arithmetic Sequence, 4. Rectangle Coordinates, 5. Even Number Count, 6. Integral Calculation, 7. Probability Calculation: ")

    if choice == "1":
        Modulo_1()

    elif choice == "2":
        text, circle_area, shape_area, leftover_area = calculate_surface_2()
        if leftover_area < 0:
            print(f"your calculated area: {text}, with the leftover area: {leftover_area} (Error: Circle area exceeds shape area)")
        else:
            print(f"your calculated area: {text}, with the leftover area: {leftover_area}")
    elif choice == "3":
        arithmetic_sequence_odd_num_3()

    elif choice == "4":
        rectangle_coordinates_4()

    elif choice == "5":
        even_number_count_5()

    elif choice == "6":
        integral_values = input("Integral values in form of (ax^y/z) or (ax^(y/j)) or (ax^(y/j)/z): ").split("x^")
        a = int(integral_values[0])
        power = integral_values[1]

        output = calculate_integral(a, power)
        if isinstance(output, str):
            print(output)
        else:
            coefficient, new_exponent, result = output
            print(f"After integrated: {result}")

            x_values = np.linspace(0.1, 10, 100)
            y_values = float(coefficient) * (x_values ** float(new_exponent))
            plt.plot(x_values, y_values)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title(f'Graph of Integrated Function: {result}')
            plt.axhline(0, color="gray", linewidth=0.5)
            plt.axvline(0, color="gray", linewidth=0.5)
            plt.show()

    elif choice == "7":
        probability_calculation_7()

    else:
        print("Invalid choice")