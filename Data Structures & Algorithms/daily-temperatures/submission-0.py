class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        temp_list = []
        time_list = []
        out = [0 for _ in range(len(temperatures))]
        for time, current_temp in enumerate(temperatures):
            
            j = 0
            while j < len(time_list):
                waiting_t = temp_list[j]
                if current_temp > waiting_t:
                     out[time_list[j]] = time - time_list[j]
                     time_list.pop(j)
                     temp_list.pop(j)
                else:
                    j += 1 
            temp_list.append(current_temp)
            time_list.append(time) 
        return out