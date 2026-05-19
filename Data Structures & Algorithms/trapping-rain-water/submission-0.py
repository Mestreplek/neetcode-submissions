class Solution:
    def trap(self, height: List[int]) -> int:
        
        total_water = 0 # OUTPUT

        height_iteration = height

        while height_iteration.count(0) != len(height):

            current_water_amount = 0
            block_to_left = False

            for block in height_iteration:


                if block > 0 and not block_to_left:
                    block_to_left = True
                elif block == 0 and not block_to_left:
                    continue


                if block > 0:
                    total_water += current_water_amount
                    current_water_amount = 0
                else:
                    current_water_amount += 1
                    # ?


            height_iteration = [x - 1 if x != 0 else x for x in height_iteration]
            distance_counter = 0
            first_block = False





            distance_counter = 0
        return total_water
