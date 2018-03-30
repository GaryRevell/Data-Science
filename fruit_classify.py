#
# Very simple "Hello World" type machine learning intro program that uses a decision tree classifier
#
from sklearn import tree
#
print("Features = [Weight, skin-type] e.g.[140 gms, 'smooth' = 1] , [180 gms, 'bumpy' = 0 ]")
features = [[140,1],[130,1],[150,1],[170,0],[190,0]]
print("Raw data = ",features)
#
print("For each label => apple (0) , orange (1)")
#
labels = [0,0,1,1,1]
print("Labels" , labels)
#
# Create the Decision Tree Classifier
#
clf = tree.DecisionTreeClassifier()
#
# Train the classifier using the features we're know and their associated labels
#
clf = clf.fit(features, labels)
#
# Now we're going to predict what a 160gm bumpy fruit is : The answer here is 1,
# which is an orange as we would've predicted ourselves.
#
test = [[160,0]]
lbl = clf.predict(test)
print("Feature",test,"was predicted to be",lbl)
#
# Now go through the list of features and predict what fruit they are
#
for a in features:
    print("Feature",a,"label =",clf.predict([a]))
#
# Loop around and predict weight/skin combinations
#
while 1:
    wt = input("Enter weight: ")
    skin = input("Skin: ")
    test = [int(wt),int(skin)]
    print(test,"is a",clf.predict([test]))

