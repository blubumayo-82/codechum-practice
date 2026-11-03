a_mb, a_s = input("Enter Server A size (MB) and time (s): ").split()
b_mb, b_s = input("Enter Server B size (MB) and time (s): ").split()

time_a = float(a_s)
time_b = float(b_s)

if a_s == 0 and b_s == 0:
    print("Invalid time input")
else:
    a_speed = float(a_mb) / time_a
    b_speed = float(b_mb) / time_b

    if a_speed > b_speed:
        diff = a_speed - b_speed
        print(f"Server A is faster by {diff:.2f} MB/s")
    elif b_speed > a_speed:
        diff = b_speed - a_speed
        print(f"Server B is faster by {diff:.2f} MB/s") 
    if abs(a_speed - b_speed) < 1e-9:
        print("Both servers have the same speed")
