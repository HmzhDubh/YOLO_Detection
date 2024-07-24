import os
import picDetect

# Detect multiple images and return average percentage
# images should be in the dataset folder to be detected and obtain their average waste percentage
#
# def avgPercPerimgs():
#
#     count = 0
#     totalPerc = 0
#     perc = 0
#
#     imgsList = os.listdir("dataset/detection-images/")
#     print(imgsList)
#     for i in range(len(imgsList)):
#         perc = picDetect.detection(imgsList[i])
#         print(perc)
#         count = count + 1
#         totalPerc = totalPerc + perc
#
#     print(count)
#     print(totalPerc)
#
#     averagePercentage = totalPerc // count
#     print("Average Waste Percentage = (",averagePercentage, "%)", "For total of", count, " plates")
#     return averagePercentage
# avgPerc = avgPercPerimgs()



def avgPercPerimgsReq(imgsList):

    count = 0
    totalPerc = 0
    perc = 0
    print(imgsList)
    for i in range(len(imgsList)):
        perc = picDetect.detection(imgsList[i])
        print(perc)
        count = count + 1
        totalPerc = totalPerc + perc

    print(count)
    print(totalPerc)

    averagePercentage = totalPerc // count
    #print("Average Waste Percentage = (",averagePercentage, "%)", "For total of", count, " plates")
    return averagePercentage


