import os
import picDetect


# Detect multiple images and return average percentage
# images should be in the dataset folder to be detected and obtain their average waste percentage

def avgPercPerimgs():

    count = 0
    totalPerc = 0
    perc = 0

    imgsList = os.listdir("dataset")
    print(imgsList)
    for i in range(len(imgsList)):
        perc = picDetect.detection(imgsList[i])
        count = count + 1

        if perc < 5:
            print("not real value")
        else:
            totalPerc = totalPerc + perc

    print(count)
    print(totalPerc)

    averagePercentage = totalPerc // count
    return averagePercentage
avgPerc = avgPercPerimgs()
print("Average Waste Percentage = ",avgPerc, "%")

