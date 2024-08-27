def zero_ending(scores):
    total = 0
    for number in scores:
        if number%10 == 0:
            total += number
    return total

scores =  [20, 45, 30, 10, 23, 67]
s = zero_ending(scores)
print("Sum of digits ending with 0 is: ", s)
