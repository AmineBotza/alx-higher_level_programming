#!/usr/bin/python3
for digits in range(100):
    if digits == 99:
        print(digits)
    else:
        print("{}".format('0' + str(digits) if digits < 10 else digits), end=", ")
