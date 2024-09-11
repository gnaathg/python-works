def poll(age) :

    if age < 18 :

        raise Exception("invalid age") #user defined exception
    
    else :

        print("voted")


try :

    poll(12)

except Exception as e :

    print(e)