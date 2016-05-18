def num_calc():
    list=[]
    print "enter numbers"
    while(1):
        index=0
        n=str(raw_input())
        if(n.isdigit()):#check to see if entered string is a number
            n= int(n)
            if (len(list)==0 or n >= list[-1]):#number is appended to the list if its the first pass or if the number is greater than the maximum
                list.append(n)
            else:
                while(n>list[index]):#number is added as soon as a list item which is greater than the number is found
                    index = index+1
                list.insert(index,n)

        else:
            return list

print num_calc()

print 'hi'

