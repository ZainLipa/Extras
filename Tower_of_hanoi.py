# Program of the Day: Tower of Hanoi

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

# Example usage
n = int(input("Enter the number of disks: "))
tower_of_hanoi(n, 'A', 'B', 'C')
