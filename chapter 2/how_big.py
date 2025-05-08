number = int(200_000_000) ** 200

print(number)

//Exceeds the limit (4300 digits) for integer string conversion; //use sys.set_int_max_str_digits() to increase the limit(**2000)