# Creating A Program like A KBC Where User Answer The Question
# using List data Type

que = ["Q.1. What is the sum of 130+125+191?",
       "Q.2: If we minus 712 from 1500, how much do we get?",
       "Q.3: 50 times of 8 is equal to:"]
ans =  [446,
        788,
        400]
i = 0
Reward = 0
uans = ["","",""]
for x in que:
    
    uans[i]=int(input(x))
    if(uans[i]==ans[i]):
        print()
        Reward = Reward +10000
        i = i+1
    else:
        print("\nBetter luck Next Time")
        break

print("We Glad You Play.")
print("Reward:",Reward)
print(uans)
    
    