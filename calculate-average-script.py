noteA = float (input ("Write the first note: "))
noteB = float (input ("Write the second note: "))

#calculate average
finalaverage = (noteA + noteB)/ 2

#verification
if finalaverage >= 7.0:
    print("Average: %.1f - Approved "% finalaverage)
else:
    print("Average: %.1f - Not Approved "% finalaverage)