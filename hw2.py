#Kelsey Donahue
#HW 2
#1/25/2025
import numpy
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
#wooo look at me i figured out the csv issue (kinda). it's not as pretty as /data/hw2data.csv but isnt an entire filepath LOL
data = pd.read_csv("hw2-kdo310/data/hw2data.csv", sep = ",")
#mprint to make sure its actually formatted correctly (sanity check)
print(data)

leafLength = data["LeafLengthInches"]
leafWidth = data["LeafWidthInches"]


#get mean, median, variance, and std dev
meanValues = data[['LeafLengthInches', 'LeafWidthInches']].mean()
medianValues = data[['LeafLengthInches', 'LeafWidthInches']].median()
varianceValues = data[['LeafLengthInches', 'LeafWidthInches']].var()
stdValues = data[['LeafLengthInches', 'LeafWidthInches']].std()

#print them
print("Mean values:\n", meanValues)
print("\nMedian values:\n", medianValues)
print("\nVariance values:\n", varianceValues)
print("\nStandard dev values:\n", stdValues)

#graph histograms
plt.figure(figsize=(10, 6))

#leaf length
#1 row, 2 columns, start at 1 because for whatever reason matplotlib wanted to be special ugh
#also i hate commenting using # python had to be special too i guess. why couldnt we all agree on //
#but i digress (no i dont i will probably definitely complain again)
plt.subplot(1, 2, 1)
plt.hist(data['LeafLengthInches'], bins = 10)
plt.title('Leaf Length Distribution')
plt.xlabel('Leaf Length (in)')
plt.ylabel('Frequency')

#leaf width
plt.subplot(1, 2, 2)
plt.hist(data['LeafWidthInches'], bins = 10)
plt.title('Leaf Width Distribution')
plt.xlabel('Leaf Width (in)')
plt.ylabel('Frequency')

plt.show()



#boxplots
plt.figure(figsize=(10, 6))

#both on same page
plt.boxplot([data['LeafLengthInches'], data['LeafWidthInches']])
#y axis label for both
plt.xticks([1, 2], ['Leaf Length (in)', 'Leaf Width (in)'])
plt.title('Boxplots for Leaf Length and Leaf Width')
plt.xlabel('in')
plt.show()


#scatter plot of entire data set with each subset a diff color and a ledger
groups = data.groupby("Species")

for name, group in groups:
    #name = name of species
    #group = all data belonging to that individual species
    plt.scatter(group['LeafLengthInches'], group['LeafWidthInches'], label = name)

plt.title('Scatter Plot Leaf Length vs Width by Species')
plt.xlabel('Leaf Length (in)')
plt.ylabel('Leaf Width (in)')
plt.legend(title='Species')
plt.show()


