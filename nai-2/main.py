import math


class Perceptron:
    def __init__(self, num_attributes):
        self.weights = [0.0] * num_attributes #random
        self.bias = 0.0 #random

    def predict(self, inputs):
        activation = self.bias
        for i in range(len(inputs)-1):
            activation += float(inputs[i]) * self.weights[i]
        return 1 / (1 + math.exp(-activation))

    def train(self, training_data, learning_rate, num_iterations):
        for _ in range(num_iterations):
            for example in training_data:
                inputs = example[:-1]
                target = 1.0 if example[-1] == 'Iris-setosa' else 0.0
                output = self.predict(inputs)
                error = target - output
                self.bias += learning_rate * error
                for i in range(len(inputs)):
                    self.weights[i] += learning_rate * error * float(inputs[i])


training = open("iris_training.txt")
test = open("iris_test.txt")

trainingSample = []
for line in training:
    temp = " ".join(line.split()).replace(",", ".").split(" ")
    trainingSample.append(temp)

testSample = []
for line in test:
    temp = " ".join(line.split()).replace(",", ".").split(" ")
    testSample.append(temp)
i = 0
num_attributes = len(trainingSample[0]) - 1
perceptron = Perceptron(num_attributes)
iterations = input("How many iterations?\n")
perceptron.train(trainingSample, 0.1, int(iterations))

correct = 0
amountOfSetosa = 0
for sample in testSample:
    inputs = sample[:-1]
    target = sample[-1]
    if target == "Iris-setosa":
        amountOfSetosa+=1
    output = 'Iris-setosa' if perceptron.predict(inputs) >= 0.5 else 'not Iris-setosa'
    print(output)
    if output == target:
        correct += 1

accuracy = correct / amountOfSetosa #len(testSample)
print("Number of correctly classified examples: ", correct)
print("Accuracy: ", accuracy * 100, "%")
while (True):
    print("input your own", num_attributes, "arguments (type @ to stop program)")
    args = []
    for x in range(0, num_attributes):
        arg = input()
        if arg == '@':
            print("Stopping program...")
            exit()
        args.append(arg)
    args.append("unknown")
    output = 'Iris-setosa' if perceptron.predict(args) >= 0.5 else 'not Iris-setosa'
    print(output)

