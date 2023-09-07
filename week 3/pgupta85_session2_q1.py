"""
Name: Pratik Narendra Gupta
Program: Software Engineering - 3rd year

"""
import heapq

"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example:

Input: intervals = [[7,10],[2,4]]
Output: 1  

"""


# Importing the required libraries
def min_meeting_rooms(intervals):
    if not intervals:
        return 0

        # Sort the intervals by their start times
    intervals.sort(key=lambda x: x[0])

    # Use a priority queue (min heap) to keep track of the end times
    room_end_times = []
    heapq.heappush(room_end_times, intervals[0][1])

    for i in range(1, len(intervals)):
        start_time, end_time = intervals[i]

        # Check if any meeting has ended before the current meeting starts
        if room_end_times[0] <= start_time:
            heapq.heappop(room_end_times)

        # Add the current meeting's end time to the priority queue
        heapq.heappush(room_end_times, end_time)

    return len(room_end_times)


def test_minMeetingRooms():
    # testing case given in the question
    print("Testing case given in the question")
    intervals = [[0, 30], [5, 10], [15, 20]]
    result = min_meeting_rooms(intervals)
    print("Input:", intervals)
    print("Output:", result)
    assert result == 2

    # testing case given in the question
    print("\nTesting case given in the question")
    intervals = [[7, 10], [2, 4]]
    result = min_meeting_rooms(intervals)
    print("Input:", intervals)
    print("Output:", result)
    assert result == 1

    # Test case with no meetings
    print("\nTesting case with no meetings")
    intervals_empty = []
    result_empty = min_meeting_rooms(intervals_empty)
    print("Input:", intervals_empty)
    print("Output:", result_empty)
    assert result_empty == 0

    # Test case with one meeting
    print("\nTesting case with one meeting")
    intervals_one = [[0, 30]]
    result_one = min_meeting_rooms(intervals_one)
    print("Input:", intervals_one)
    print("Output:", result_one)
    assert result_one == 1

    # Test case with two non-overlapping meetings
    print("\nTesting case with two non-overlapping meetings")
    intervals_two_non_overlapping = [[7, 10], [10, 11]]
    result_two_non_overlapping = min_meeting_rooms(intervals_two_non_overlapping)
    print("Input:", intervals_two_non_overlapping)
    print("Output:", result_two_non_overlapping)
    assert result_two_non_overlapping == 1

    # Test case with two overlapping meetings
    print("\nTesting case with two overlapping meetings")
    intervals_two_overlapping = [[1, 5], [4, 10]]
    result_two_overlapping = min_meeting_rooms(intervals_two_overlapping)
    print("Input:", intervals_two_overlapping)
    print("Output:", result_two_overlapping)
    assert result_two_overlapping == 2

    # Test case with three meetings where two meetings can share a room
    print("\nTesting case with three meetings where two meetings can share a room")
    intervals_three_shared_room = [[0, 30], [5, 10], [15, 20]]
    result_two_shared_room = min_meeting_rooms(intervals_three_shared_room)
    print("Input:", intervals_three_shared_room)
    print("Output:", result_two_shared_room)
    assert result_two_shared_room == 2

    # Test case with three meetings where no one can share a room
    print("\nTesting case with three meetings where no meeting can share a room")
    intervals_three_shared_room = [[0, 30], [0, 20], [15, 20]]
    result_three_shared_room = min_meeting_rooms(intervals_three_shared_room)
    print("Input:", intervals_three_shared_room)
    print("Output:", result_three_shared_room)
    assert result_three_shared_room == 3

    # Test case with multiple overlapping meetings
    print("\nTesting case with multiple overlapping meetings")
    intervals_multiple_overlapping = [[1, 5], [2, 6], [5, 10], [9, 12], [11, 15], [13, 18]]
    result_multiple_overlapping = min_meeting_rooms(intervals_multiple_overlapping)
    print("Input:", intervals_multiple_overlapping)
    print("Output:", result_multiple_overlapping)
    assert result_multiple_overlapping == 2

    # Test case with multiple meetings, but no overlapping
    print("\nTesting case with multiple meetings, but no overlapping")
    intervals_no_overlapping = [[1, 5], [6, 10], [11, 15], [16, 20]]
    result_no_overlapping = min_meeting_rooms(intervals_no_overlapping)
    print("Input:", intervals_no_overlapping)
    print("Output:", result_no_overlapping)
    assert result_no_overlapping == 1

    print("\nAll test cases ran successfully")


# Run the test cases


# Main function
if __name__ == "__main__":
    test_minMeetingRooms()

# what is the time complexity of the above solution?
# O(nlogn) is the time complexity of the above solution.
# what is the space complexity of the above solution?
# O(n) is the space complexity of the above solution.
