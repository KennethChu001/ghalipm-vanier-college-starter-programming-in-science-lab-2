# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    # TODO: Implement this function
    h0=float(input("Enter initial height: "))
    time=float(input("Enter time: "))
    g=9.8
    h=h0-0.5*g*time**2
    print("Height of the ball at time", time, "second = ", h)

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    time=float(input("Enter time for car (in seconds): "))
    speed=20
    distance=time*speed
    print("The car will travel", distance, "meters in", time, "second.")
    time2=float(input("Enter time for car (in seconds): "))
    distance=time2*speed
    print("The car will travel", distance, "meters in", time2, "second.")
    time3=float(input("Enter time for car (in seconds): "))
    distance=time3*speed
    print("The car will travel", distance, "meters in", time3, "second.")
