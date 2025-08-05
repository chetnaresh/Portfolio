from collections import Counter
import heapq

def rearrange_string(s):
    freq = Counter(s)
    max_heap = [(-count, char) for char, count in freq.items()]
    heapq.heapify(max_heap)

    prev = (0, "")
    result = []

    while max_heap:
        count, char = heapq.heappop(max_heap)
        result.append(char)

        if prev[0] < 0:
            heapq.heappush(max_heap, prev)

        count += 1 
        prev = (count, char)

    rearranged = ''.join(result)
    if len(rearranged) == len(s):
        return rearranged  
    else:
        ""

print(rearrange_string("aaabbc")) 
