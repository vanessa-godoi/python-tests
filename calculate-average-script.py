# SCRIPT 1

noteA = float (input ("Write the first note: "))
noteB = float (input ("Write the second note: "))

#calculate average
finalaverage = (noteA + noteB)/ 2

#verification
if finalaverage >= 7.0:
    print("Average: %.1f - Approved "% finalaverage)
else:
    print("Average: %.1f - Not Approved "% finalaverage)


# SCRIPT 2

quantity = 0
sum = 0
average = 0
value = float (input ("Write a value: "))

while (value > 0.0):
    sum = sum + value
    quantity = quantity + 1
    #values input
    value = float (input ("Write a value: "))

#if a negative value is entered, the loop ends.
average = sum / quantity
print("\n Total sum: ", sum)
print("\n Quantity of values entered: ", quantity)
print("\n Average value: ", average)