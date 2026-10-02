class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        track = [(0, 101)]
        i = 0

        while i < len(temperatures):
            _, temp_to_compare = track[-1]
            if temperatures[i] <= temp_to_compare:
                track.append((i, temperatures[i]))
            else: 
                ind_smaller_temp, _ = track.pop()
                result[ind_smaller_temp] = i - ind_smaller_temp
                i -= 1
            i += 1

        return result                