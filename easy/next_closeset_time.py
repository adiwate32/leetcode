# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

# Example1

# Input: time = "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
# It is not 19:33, because this occurs 23 hours and 59 minutes later.

# Example2

# Input: time = "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.


def closest_time(time: str) -> str:
    digits = set(time)
    hour, minute = time.split(":")
    hour, minute = int(hour), int(minute)
    while True:
        minute += 1
        if minute == 60:
            minute = 0
            hour = (hour + 1) % 24
        time = "{:02d}:{:02d}".format(hour, minute)
        if set(time) <= digits:
            return time


print(closest_time("23:59"))
