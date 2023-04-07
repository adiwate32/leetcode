# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all the given tasks.

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.

# Example 2:
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]

# https://leetcode.com/problems/task-scheduler/description/

from typing import List


def leastInterval(tasks: List[str], n: int) -> int:
    # Initialize a list to keep track of the frequency of each task
    freqs = [0] * 26

    # Iterate through each task in the list of tasks and increment its frequency in the list of frequencies
    for task in tasks:
        freqs[ord(task) - ord("A")] += 1

    # Sort the list of frequencies in ascending order
    freqs.sort()

    # Get the maximum frequency and calculate the total idle time
    f_max = freqs.pop()
    idle_time = (f_max - 1) * n

    # While there are still frequencies left and there is idle time left, decrement the idle time by the minimum of the maximum frequency and the next highest frequency
    while freqs and idle_time > 0:
        idle_time -= min(f_max - 1, freqs.pop())

    # If there is still idle time left, set it to 0
    idle_time = max(0, idle_time)

    # Return the total number of tasks plus the idle time
    return len(tasks) + idle_time
