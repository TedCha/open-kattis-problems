#setting test case variable
testCase = input()

#creating for loop in range of test case 
for i in range(int(testCase)):
    
    #get line 1 from user and then print
    line1 = input()
    print(line1)
    #get line 2 from user and then print
    line2 = input()
    print(line2)

    #make list from both lines in order to test each character
    line1 = list(line1)
    
    line2 = list(line2)

    #create a difference list
    diff = []

    #for in in range of line 1 (doesn't matter because each line is same length)
    for i in range(0, len(line1)):
        #if line 1 [i] is equal to line 2 [i], append the diff list with "."
        if line1[i] == line2[i]:
          diff.append(".")

        #else, append the diff list with "*"
        else:
          diff.append("*")
        
    #print the list after joining each character in list as a string
    print("".join([str(i) for i in diff]))
