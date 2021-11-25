def hill(n) :
    k = n - 1 #k = spaces

    for i in range(0, n) :
        for j in range(0, k) : #printing the spaces
            print(end = " ")

        k = k - 1 #decreasing spaces each row

        for j in range(0, i + 1) : #adding star each row
            print("*", end = " ")

        print("\r") #going to next line

hill(5) #function(number of rows)