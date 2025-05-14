current_world_population = 8_220_000_000
annual_growth_rate = 0.84

years = 2025

for year in range(100):
	for future in range(1):
		years += 1
		result = current_world_population * annual_growth_rate
		current_world_population = result + current_world_population
		print(f"year {years:<7} => {current_world_population:<20} => {result:<30}")

		