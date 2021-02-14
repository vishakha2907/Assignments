def frequencyDigits(n, d): 
      
    # Counter variable to  
    # store the frequency 
    c = 0; 
      
    # iterate till number 
    # reduces to zero 
    while (n > 0):  
          
        # check for equality 
        if (n % 10 == d): 
            c += 1; 
        # reduce the number 
        n = int(n / 10); 
  
    return c; 

print("frequency of 1 in number 11175 is : % d" % (frequencyDigits(11175,1)))
