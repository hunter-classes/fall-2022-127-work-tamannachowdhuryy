#problem 2.3

current_time_str = input("What is the time now (in hour): ")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

hours = current_time_int + wait_time_int

totalhours = hours % 24

print(totalhours)