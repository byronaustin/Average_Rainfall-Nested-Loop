def AvgRain():
    Month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October', 'November', 'December']
    years = input('How many years: ')
    print ("Years = ", years)
    TotalRain = 0
    NumberOfMonths = 0
    for num in range (0,int(years)):
        for index in range(0,12):
            Rainfall = int(input('How many inches in ' + Month[index] + ' of year ' + str(num+1) + ': '))
            TotalRain = TotalRain + Rainfall
            NumberOfMonths = NumberOfMonths + 1
    print ('Number of months', NumberOfMonths)
    print ('Total Rainfall: ',TotalRain)
    print ('Average Rainfall: ', TotalRain/NumberOfMonths)

    
if __name__ == '__main__' :
    AvgRain() 
