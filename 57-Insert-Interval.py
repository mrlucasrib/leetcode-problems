class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        curr = [None, None]
        new_start, new_end = newInterval
        if not intervals:
            return [newInterval]
        for [start_i, end_i] in intervals:
            if None not in curr:
                ans.append([start_i, end_i])
                continue
            if new_start > end_i:
                ans.append([start_i, end_i])
            else:
                if curr[0] is None:
                    if new_start < start_i:
                        curr[0] = new_start
                    else:    
                        curr[0] = start_i
                    if new_end < start_i:
                        curr[1] = new_end
                        ans.append(curr)
                        ans.append([start_i, end_i])
                        continue
                    elif new_end <= end_i:
                        curr[1] = end_i
                        ans.append(curr)
                        continue
                    else:
                        continue
                if curr[1] is None:
                    if new_end < start_i:
                        curr[1] = new_end
                        ans.append(curr)
                        ans.append([start_i,end_i])
                        continue
                    else:
                        if new_end <= end_i:
                            curr[1] = end_i
                            ans.append(curr)
        if curr[0] is None:
            ans.append(newInterval)
        elif curr[1] is None:
            ans.append([curr[0], max(intervals[-1][1], newInterval[1])])
        return ans