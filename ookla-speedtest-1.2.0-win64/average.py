with open ('data.txt', 'rt') as myfile:
    with open("average.txt", "w") as f:
        count = 0
        mysum = 0
        for line in myfile:
            mysum += float(line)
            count+=1
        average = mysum/count
        f.write(str(average))

