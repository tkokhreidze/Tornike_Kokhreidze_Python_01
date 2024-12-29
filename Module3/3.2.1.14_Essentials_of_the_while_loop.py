blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	

height = 0
blocks_needed = 1

while blocks >= blocks_needed:
    blocks = blocks - blocks_needed
    height += 1
    blocks_needed += 1

print("The height of the pyramid:", height)
