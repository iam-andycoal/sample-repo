#age = 0

#while age < 18:
#    age = int(input("Enter your age (must be 18 or older): "))

#print("You are old enough to proceed.")

outer_count = 5

while outer_count > 0:
    inner_count = 1
    while inner_count <= outer_count:
        print(inner_count, end="")
        inner_count += 1
    print ()
outer_count -= 1