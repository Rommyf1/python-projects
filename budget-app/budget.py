import math;
from itertools import zip_longest;

class Category:
	global_spent = 0;
	longest_category_name = "";
	
	def __init__(self, category_name):
		self.category = category_name;
		self.ledger = [];
		self.balance = 0;
		self.total_spent = 0;
		if(len(self.category) > len(Category.longest_category_name)):
			Category.longest_category_name = self.category;

	def __str__(self):
		budget_length = 30;
		category_length = len(self.category);
		decorator_size = round((budget_length - category_length) / 2);
		budget_header = "{}{}{}\n".format(("*"*decorator_size),self.category,("*"*decorator_size));
		budget_body = "";
		budget_total = "Total: {}".format(self.balance);
		
		for item in self.ledger:
			budget_body += "{:23}{:7.2f}\n".format(item["description"][:23], float(item["amount"]));
			
		
		return (budget_header + budget_body + budget_total);
	
	def check_funds(self, amount):
		if(amount > self.balance):
			return False;
		return True;
	
	def deposit(self, amount, description=""):
		if(amount < 0):
			return False;
		new_deposit = {
			"amount": amount,
			"description": description
		};
		self.balance += amount; 
		self.ledger.append(new_deposit);
		return True;

	def withdraw(self, amount, description=""):
		if((self.check_funds(amount)) == False):
			return False;

		new_withdraw = {
			"amount": (amount*(-1)),
			"description": description
		};

		Category.global_spent += amount;
		self.total_spent += amount;
		self.balance -= amount;
		self.ledger.append(new_withdraw);
		return True;

	def get_balance(self):
		return self.balance;

	def get_local_percentage(self):
		local_percentage = ((self.total_spent/Category.global_spent) * 100);
		return round_down(local_percentage);

	def transfer(self, amount, budget):
		if(self.check_funds(amount) and isinstance(budget, Category)):
			transfer_description = ("Transfer to {}".format(budget.category));
			deposit_description = ("Transfer from {}".format(self.category));
			withdraw_status = self.withdraw(amount, transfer_description);
			deposit_status = budget.deposit(amount, deposit_description);

			if(withdraw_status and deposit_status):
				return True;
		return False;


def round_down(n):
    multiplier = 10 ** -1;
    return int(math.floor(n * multiplier) / multiplier);


def create_spend_chart(categories):
	chart = "Percentage spent by category\n";
	for i in range(100, -10, -10):
		line = ("{:3}| ".format(i));
		for budget in categories:
			bar = "";
			if(budget.get_local_percentage() >= i):
				bar += ("{:{}} ".format("o", 2));
				line += bar;
			else:
				bar += ("{:{}} ".format(" ", 2));
				line += bar;
		chart += line+"\n";
	chart += "{}{}\n".format(" "*4,("-"*(len(line)-4)));

	new_line = "     ";
	
	for i in range(len(Category.longest_category_name)):
		for category in categories:
			try:
				if(category.category[i]):
					new_line += "{:2} ".format(category.category[i]);
			except:
				new_line += "{:2} ".format("");
		if(i != len(Category.longest_category_name)-1):
			new_line += "\n     ";

	chart += new_line;
	Category.global_spent = 0;
	return chart;