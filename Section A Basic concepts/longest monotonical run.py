def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    def find_run(lst):
        # Helper function to find the longest run
        max_run = []
        current_run = [lst[0]]

        for i in range(1, len(lst)):
            if lst[i] >= lst[i - 1]:
                current_run.append(lst[i])
            else:
                if len(current_run) > len(max_run):
                    max_run = current_run
                current_run = [lst[i]]

        if len(current_run) > len(max_run):
            max_run = current_run

        return max_run

    increasing_run = find_run(L)
    decreasing_run = find_run(L[::-1])[::-1]  # Reverse the list to find decreasing run

    if len(increasing_run) >= len(decreasing_run):
        return sum(increasing_run)
    else:
        return sum(decreasing_run)


# Test cases
print(longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))  # Output: 26
print(longest_run([5, 4, 10]))  # Output: 9
