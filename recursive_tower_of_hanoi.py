# Program of the Day: Towers of Hanoi (Recursive Solution)

def towers_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    towers_of_hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    towers_of_hanoi(n-1, auxiliary, source, destination)

# Example usage
n_disks = 3
towers_of_hanoi(n_disks, 'A', 'B', 'C')

