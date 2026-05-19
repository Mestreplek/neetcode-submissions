class Solution:
    def maxArea(self, heights: List[int]) -> int:
        counter = 0
        water_amounts = []
        for height in heights:
            start = counter + 1
            distance_counter = 0
            for second_height in heights[start::] :
                distance_counter += 1
                min_height = min(second_height,height)

                water_amounts.append(min_height * distance_counter)


            counter += 1

        return max(water_amounts)




        

        

        