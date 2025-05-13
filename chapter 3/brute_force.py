
for hypo in range(21):
	for count in range(hypo):
		for count1 in range(count):
			value = count ** 2 + count1 ** 2
			if hypo ** 2 == value:
				print(count1, count, hypo)