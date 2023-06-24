def print_row(size_, star_counter):
    for row in range(size_ - star_counter):
        print(" ", end="")
    for row in range(1, star_counter):
        print("*", end=" ")

    print("*")


size = int(input())

for star_count in range(1, size):
    print_row(size, star_count)
for star_count in range(size, 0, -1):
    print_row(size, star_count)