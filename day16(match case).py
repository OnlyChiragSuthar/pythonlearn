x = int(input("Enter The Day(1-7):"))

match x:
      
      case 1:
            print("1 Likha Hai Na Tune?")
      case 2:
            print("2 likha hai na?")
      case _:
             if x==3:
                  print("kya Pata?")
             elif x==4:
                  print("4 hai na!")
             else :
                  print("Mereko Kya Kuch Bhi Ho!")

                
                        


            # it is Just Like Switch in C/C++ Language Where We Check Linearly And Execute True statement and 
            #  also include the break statement to stop the next line code
            # but in python we dont write break;
            # if any statement satisfied then the next case will not be executed