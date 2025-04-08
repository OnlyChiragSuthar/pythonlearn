def Code(char):
    for i in range(0,len(words)):
        if len(words[i])>2:
            # print(type(word))
            r1 = "Dkg"
            r2 = "smg"
            newchar1 = r1 + words[i][1:] + words[i][0] + r2
            # if (len(word)>=2):
            #     newchar2 = r1 + word[i][1:] + word[i][0] + r2
            #     print(newchar1+" "+newchar2)
            # print(newchar1)
            print(newchar1,end=" ")
        else:
            for j in range(1,len(words[i])+1):
                print(words[i][-j],end="")

            print(end=" ")

def Decode(char):
    for word in words:
        if len(word)>2:
            # print(type(word))
            
            newchar1 =  word[-4] + word[3:len(word)-4] 
            # if (len(word)>=2):
            #     newchar2 = r1 + word[i][1:] + word[i][0] + r2
            #     print(newchar1+" "+newchar2)
            # print(newchar1)
            print(newchar1,end=" ")
        else:
            for j in range(1,len(word)+1):
                print(word[-j],end="")

            print(end=" ")



char = input("Enter The Word:")
print("For Coding Press 1 And For Decoding Press 2:")
Option = int(input())
words = char.split(" ") 

match Option:
    case 1:
        Code(char)

    case 2:
        Decode(char)

    case _:
        print("Invalid Option")



