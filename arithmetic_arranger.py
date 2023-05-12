errors = {
	"wrong_operator": "Error: Operator must be '+' or '-'.",
	"wrong_length": "Error: Numbers cannot be more than four digits.",
	"wrong_digit": "Error: Numbers must only contain digits."
};

def has_wrong_operator(operator):
	if(operator != '+' and operator != '-'):
		return True;
	return False;

def digit_has_wrong_length(operator, operand):
	if((len(operator) > 4) or (len(operand) > 4)):
			return True;
	return False;

def values_are_numbers(operator, operand):
	try:
		if ((isinstance(int(operator), int) == True) and (isinstance(int(operand), int) == True)):
			return False;
	except:
		return True;
		

def manage_problems(problems):
	
	solutions = {
		"operators1": [],
		"operators2": [],
		"identations": [],
		"answers": []
	};
	
	for problem in problems:
	
		splitted = problem.split();

		#Verify if operators are correct
		if(has_wrong_operator(splitted[1])):
			return "wrong_operator";

		#Verify if values have more than 4 digits
		if(digit_has_wrong_length(splitted[0], splitted[2])):
			return "wrong_length";
			
		#Verify if values are numbers
		if (values_are_numbers(splitted[0], splitted[2])):
			return "wrong_digit";
		
		### Solve Problem ###
		
		if(len(splitted[0]) > len(splitted[2])):
			identation = len(str(splitted[0]));
		else:
			identation = len(str(splitted[2]));

		solutions["operators1"].append(("{:{}d}".format(int(splitted[0]),identation+2)));
		solutions["operators2"].append("{} {:{}d}".format(splitted[1], int(splitted[2]), identation));
		solutions["identations"].append("{}".format(("-"*(identation+2))));
		solutions["answers"].append("{:{}d}".format(eval(f"{splitted[0]} {splitted[1]} {splitted[2]}"),identation+2))

	return solutions;
	
def arithmetic_arranger(problems, show_solutions = False):

	if(len(problems) > 5):
		return "Error: Too many problems.";
	
	response = manage_problems(problems);
	
	if(isinstance(response, str) == True):
		return (errors[response]);
	
	arranged_problems = "";
	
	if(show_solutions == True):
		arranged_problems = ('{}\n{}\n{}\n{}'.format(("    ".join(response["operators1"])), ("    ".join(response["operators2"])),("    ".join(response["identations"])), ("    ".join(response["answers"])))
	);
	else:
		arranged_problems = ('{}\n{}\n{}'.format(("    ".join(response["operators1"])), ("    ".join(response["operators2"])),("    ".join(response["identations"]))));

		
	return arranged_problems;