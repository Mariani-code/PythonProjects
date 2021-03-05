from math import pow

def distinct_powers(low_lim, upp_lim):

	combination_list = []
	amount_combination = 0

	for numb in range(low_lim, upp_lim+1):
		for power in range(low_lim, upp_lim+1):
			combination = pow(numb, power)
			if combination not in combination_list:
				combination_list.append(combination)
				amount_combination += 1

	return amount_combination

lower_limit = 2
upper_limit = 100
print(distinct_powers(lower_limit, upper_limit))
