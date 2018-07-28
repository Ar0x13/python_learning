#
# Python math expression calculator
#

from py_expression_eval import Parser
parser = Parser()

try:
# Math expression initialization

	expression = input('Enter math expression: \n')
	print('Your expression is: \n', expression)

# Number of variables in math expression
	number = int(input('Enter number of variables: \n'))

# Variables initialization
	variables = list(parser.parse(expression).variables())
	print('You have such variables; ', variables)

# Add values to variables
	var_values = []
	for i in range(number):
		print("Enter variable value for {}: ".format(variables[i]) )
		value = int(input())
		var_values.append(value)

# Concatenation variables and their values
	dictionary = dict(zip(variables, var_values))
	print('Your variables and values: ', dictionary)

# Expression execution
	result = parser.evaluate(expression, dictionary)

except Exception as error:
	print(error)

finally:
	print('Result: ', result)
