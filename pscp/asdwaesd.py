link = "https://ijudge.it.kmitl.ac.th/problems/"
word = input("Enter the problem code: ")

if word[0:39] != link:
    print("Invalid link")
else:
    if len(word) == 43 or len(word) == 44:
        if(word[39]== '0'):
            print("0 STAR")
        elif(word[39]== '1'):
            print("1 STAR")
        elif(word[39]== '2'):
            print("2 STAR")
        elif(word[39]== '3'):
            print("3 STAR")
    else:
        print("Invalid link")