from sklearn import tree

# Define the features and labels
features = [[140, 1], [130, 1], [150, 0], [170, 0]]  # weight and texture (1 = smooth, 0 = bumpy)
labels = [0, 0, 1, 1]  # 0 = apple, 1 = orange

# Create a decision tree classifier
clf = tree.DecisionTreeClassifier()

# Train the classifier on the features and labels
clf = clf.fit(features, labels)

# Predict the label of a new instance
new_instance = [[160, 0]]  # weight = 160, texture = bumpy
prediction = clf.predict(new_instance)

# Print the predicted label
if prediction == 0:
    print("The new instance is classified as an apple.")
else:
    print("The new instance is classified as an orange.")


#This example code creates a decision tree classifier using Scikit-Learn
#  library to predict the label of an instance based on its features 
# (in this case, weight and texture). The classifier is trained on a
#  set of labeled instances, and then used to predict the label of a
#  new instance based on its features.

#This example is a simple demonstration of how a machine learning 
# algorithm can be used to build an AI, in this case, a decision tree 
# classifier that can classify a fruit as an apple or an orange based
#  on its weight and texture.