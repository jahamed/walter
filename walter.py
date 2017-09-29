from keras.models import Sequential
from keras.layers import Dense
import numpy
import pdb
import os

# Fix random seed for reproducibility
# numpy.random.seed(1337)

# if os.path.isfile("model.json"):
	# print("Precomputed model file detected, using it.")
	
# Load initial seed dataset
print("Loading seed data, this might take a while...")
dataset = numpy.loadtxt("query_result.csv", skiprows=1, delimiter=",")

# pdb.set_trace()

# Split seed data into input (X) and output (Y) variables
num_arguments = dataset.shape[1] - 1 # numpy array size
print("# rows in seed dataset: {}").format(dataset.shape[0])
X = dataset[:,0:num_arguments]
Y = dataset[:,num_arguments]

# Dataset to predict on
print("Loading data to predict, this might take a while...")
dataset_to_predict = numpy.loadtxt("to_check.csv", delimiter=",")

print("# rows in prediction dataset: {}").format(dataset_to_predict.shape[0])
X_to_predict = dataset_to_predict[:,0:num_arguments]
Y_to_predict = dataset_to_predict[:,num_arguments]
num_rows_to_predict = dataset_to_predict.shape[0];
print(num_rows_to_predict)

# Create model
model = Sequential()
model.add(Dense(12, input_dim=num_arguments, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X, Y, epochs=1, batch_size=10000)

# Evaluate the model
# scores = model.evaluate(X, Y)
# print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# --- Save Model and Weights for future use ---
# serialize model to JSON
# model_json = model.to_json()
# with open("model.json", "w") as json_file:
# 	json_file.write(model_json)
# # serialize weights to HDF5
# model.save_weights("model.hd5")
# print("Saved model & weights to disk")


print("Time to calculate predictions :D")
# Calculate predictions
predictions = model.predict(X_to_predict)
# pdb.set_trace()
# Round predictions
rounded = [round(x[0]) for x in predictions]
# print(rounded)

correct = 0
num_claimed_predicted = 0
num_not_claimed_predicted = 0
num_actually_claimed = 0
for i in range(0, len(rounded)):
	# print("predicted: " + str(rounded[i]) + "  actual: " + str(Y_predict[i]))
	if rounded[i] == Y_to_predict[i]:
		correct = correct + 1

	# pdb.set_trace()
	if rounded[i] == 1:
		num_claimed_predicted += 1
		if Y_to_predict[i] == 1:
			num_actually_claimed += 1
	else:
		num_not_claimed_predicted += 1

if len(rounded) != num_rows_to_predict:
	print("# Arguments don't match up" + "len(rounded): " + str(len(rounded)) + "num args: " + str(num_rows_to_predict))

print("Right: " + str(correct))
print("Wrong: " + str(len(Y_to_predict) - correct))
print("Accuracy: " + str(float(correct) / len(Y_to_predict)))
print("# people who advertise predicted: {}").format(num_claimed_predicted)
print("# people who actually advertise: {}").format(num_actually_claimed)
print("# people who don't advertise predicted: {}").format(num_not_claimed_predicted)



