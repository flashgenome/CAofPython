def tower_of_hanoi(n, source, target, auxiliary):
    """
    Prints the sequence of moves needed to transfer 'n' disks from the 'source' needle to the 'target' needle,
    using the 'auxiliary' needle as an intermediate.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)


# Number of disks
num_disks = 3

# Needle labels
source_needle = "Source"
target_needle = "Target"
auxiliary_needle = "Auxiliary"

# Call the tower_of_hanoi function to print the sequence of moves
tower_of_hanoi(num_disks, source_needle, target_needle, auxiliary_needle)
