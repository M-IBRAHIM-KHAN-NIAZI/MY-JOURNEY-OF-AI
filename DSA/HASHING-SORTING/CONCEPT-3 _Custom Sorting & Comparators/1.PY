# Concept 4: Custom Sorting & Comparators
# Unsorted intervals: [start_time, end_time]
intervals = [[8, 10], [1, 3], [2, 6], [15, 18]]

# Custom sort using lambda function based on the starting time (x[0])
intervals.sort(key=lambda x: x[0])

print("Sorted Intervals:", intervals)
# Output: [[1, 3], [2, 6], [8, 10], [15, 18]]