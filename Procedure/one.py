sum = 0
with open("text_sum.txt") as number:
    for num in number:
        sum += int(num)
print (sum)
