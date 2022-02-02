
from typing import List
def minAvailableDuration(slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    def is_overlapping(ts1,ts2):
        if (ts2[0] <= ts1[0] <ts2[1]) or (ts1[0] <= ts2[0] <ts1[1]):
            return True
        return False
    p1 = p2 = 0
    slots1 = sorted(slots1, key =lambda x: x[0])
    slots2 = sorted(slots2, key=lambda x: x[0])
    while p1 < len(slots1) and p2 < len(slots2):
        time_slot_1 = slots1[p1]
        time_slot_2 = slots2[p2]
        if is_overlapping(time_slot_1,time_slot_2):
            overlap_interval =  min(time_slot_2[1], time_slot_1[1]) - max(time_slot_2[0], time_slot_1[0])
            if duration <= overlap_interval:
                start_time = max(time_slot_2[0], time_slot_1[0])
                return [start_time, start_time + duration]
        if time_slot_1[1] < time_slot_2[1]:
            p1 += 1
        else:
            p2 +=1


    return []

    #I dont need to check for overlapping. If there is no overlap, then the overlpa duration will always be negative,
    # and therefore always smallerthan the duration of the meetingf
def simpler_implementation_of_is_overlapping(slots1, slots2,duration):
    p1 = p2 = 0
    slots1 = sorted(slots1, key=lambda x: x[0])
    slots2 = sorted(slots2, key=lambda x: x[0])
    while p1 < len(slots1) and p2 < len(slots2):
        time_slot_1 = slots1[p1]
        time_slot_2 = slots2[p2]
        overlap_interval = min(time_slot_2[1], time_slot_1[1]) - max(time_slot_2[0], time_slot_1[0])
        if duration <= overlap_interval:
            start_time = max(time_slot_2[0], time_slot_1[0])
            return [start_time, start_time + duration]
        if time_slot_1[1] < time_slot_2[1]:
            p1 += 1
        else:
            p2 +=1
    return []








print(simpler_implementation_of_is_overlapping(
[[10,50],[60,120],[140,210]],
[[0,15],[60,70]],
8))