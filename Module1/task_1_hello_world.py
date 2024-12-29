print("1) For loop")
for i in range(1, 11):
    print(f"Hello World! {i}")

print("-------------------------------------------------")



print("2) While loop")
i=0
while i < 11:
    print(f"Hello World! {i}")
    i+=1

print("-------------------------------------------------")



print("3) Recursion")
def print_hello_world(count, current=1):
    if current > count:
        return
    print(f"Hello World {current}")
    print_hello_world(count, current + 1)

print_hello_world(10)

print("-------------------------------------------------")