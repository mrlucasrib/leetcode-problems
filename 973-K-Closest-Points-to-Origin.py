import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        identifier = {}
        for x, y in points:
            dist = x**2+y**2
            heapq.heappush(hp, dist)
            if (v := identifier.get(dist, None)) is None:
                identifier[dist] = [[x,y]]
            else:
                v.append([x,y])
                

            
        ans = []
        for dist in heapq.nsmallest(k, hp):
            ans.append(identifier[dist].pop())

        return ans
