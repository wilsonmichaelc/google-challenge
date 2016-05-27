#!/usr/bin/python

#intervals = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20], [30, 31], [32, 33], [19, 22]]
intervals = [[1, 3], [2, 3], [5, 7], [5, 6], [7, 10], [11, 12]]

def answer(intervals):
    # Sort the list so we know where to start
    intervals.sort(key=lambda x: x[0])
    print intervals
    # Save the starting point
    start = intervals[0][0]
    end = intervals[0][1]
    # Keep track of the time
    time = 0
    i=0
    # Loop over sorted intervals
    while i < len(intervals)-1:
        #print "Current", intervals[i]
        #print "Next", intervals[i+1]
        if intervals[i+1][0] < end and intervals[i+1][1] <= end: # If the next interval is a subset of the current interval
            #print "start: ", start, "end: ", end
            #print "next is subset of current"
            i+=1
            continue
        elif intervals[i+1][0] <= end and intervals[i+1][1] > end: # If next interval is overlaping current
            #print "start: ", start, "end: ", end
            #print "next overlaps current"
            end = intervals[i+1][1]
        else:
            time += end-start
            start = intervals[i+1][0]
            end = intervals[i+1][1]
            #print "start: ", start, "end: ", end
            #print "Adding time: ", time
            #i+=1
        i+=1

    time += end-start
    return time

print answer(intervals)
