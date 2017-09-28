from keras.models import Sequential
from keras.layers import Dense
import numpy
import pdb

# fix random seed for reproducibility
numpy.random.seed(1337)

# load pima indians dataset
dataset = numpy.loadtxt("query_result.csv", skiprows=1, delimiter=",")

# split into input (X) and output (Y) variables
pdb.set_trace()
num_arguments = dataset[0].size - 1

X = dataset[:,0:num_arguments]
Y = dataset[:,num_arguments]

# create model
model = Sequential()
model.add(Dense(12, input_dim=num_arguments, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X, Y, epochs=5, batch_size=1000)

# evaluate the model
# scores = model.evaluate(X, Y)
# print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# calculate predictions
predictions = model.predict(X)
# round predictions
rounded = [round(x[0]) for x in predictions]
# print(rounded)

correct = 0
for i in range(0, len(rounded)):
	print("predicted: " + str(rounded[i]) + "  actual: " + str(Y[i]))
	if rounded[i] == Y[i]:
		correct = correct + 1

print("Right: " + str(correct))
print("Wrong: " + str(len(Y) - correct))
print("Accuracy: " + str(float(correct) / len(Y)))


