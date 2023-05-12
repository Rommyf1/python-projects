import copy
import random
# Consider using the modules imported above.

class Hat:
	def __init__(self, **kwargs):
		self.contents = [];
		for color, value in kwargs.items():
			for i in range(value):
				self.contents.append(color);
		
	def draw(self, number_of_draws):
		if(number_of_draws >= len(self.contents)):
			return self.contents;
		balls_drawn = [];
		for i in range(number_of_draws):
			balls_drawn.append(self.contents.pop(random.randrange(len(self.contents))));
		return balls_drawn;

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	#hat_to_test = copy.deepcopy(hat);
	number_of_successes = 0;
	for experiment in range(num_experiments):
		partial_success = True;
		hat_to_test = copy.deepcopy(hat);
		balls_drawns = hat_to_test.draw(num_balls_drawn);
		for color_expected, number_of_balls_expected in expected_balls.items():
			if(balls_drawns.count(color_expected) < number_of_balls_expected):
				partial_success = False;
				break;
		if(partial_success):
			number_of_successes += 1;
	
	probability = (number_of_successes / num_experiments);
	return probability;
	