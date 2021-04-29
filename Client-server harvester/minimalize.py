def minimalize_email_set(test):
    new=[]

    for x in range(len(test)):
        temp = list(set(test[x]))

        for z in range(len(temp)):
            new.append(temp[z])

    new = list(set(new))

    return new


    
