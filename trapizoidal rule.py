import math
#this calculator is imperfect
n = float(input('n: '))
upperBnd = float(input('upper limit: '))
lowerBnd = float(input('lower limit: '))
def deltaD ( n, upperBnd, lowerBnd):
	delt = (upperBnd - lowerBnd)/n 
	#print(delt)
	return(abs(delt))
delta = deltaD( n, upperBnd, lowerBnd)
def inputValues(delta, upperBnd, lowerBnd):
	inputValues = []
	i=lowerBnd
	while i < upperBnd:
		inputValues.append(float(i))
		i=float(i+delta)
	return inputValues
def functionOfValues(list,delta):
	i=0
	outputList = []
	newDelt = 0.5*delta
	while i <= len(list,)-1:
		if i == 0 or i == len(list)-1:
			value =list[i]*list[i] 
			outputList.append(value)
		else:
			value =2*(list[i]*list[i]) 
			outputList.append(value)
		
		
		i = i+1
	#print(outputList)
	summation = sum(outputList)
	totalAnswer = summation * newDelt
	return totalAnswer
numbers = inputValues(delta,upperBnd,lowerBnd)
#print(numbers)
print(functionOfValues(numbers,delta))
