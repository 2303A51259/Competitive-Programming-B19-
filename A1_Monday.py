def maxMeetings(meetings):
    # Sort meetings by end time
    meetings.sort(key=lambda x: x[1])

    count = 0
    lastEnd = -1

    for start, end in meetings:
        if start > lastEnd:
            count += 1
            lastEnd = end

    return count


t = int(input())

for i in range(t):
    n = int(input())
    meetings = []

    for i in range(n):
        startTime, endTime = map(int, input().split())
        meetings.append((startTime, endTime))

    print(maxMeetings(meetings))
