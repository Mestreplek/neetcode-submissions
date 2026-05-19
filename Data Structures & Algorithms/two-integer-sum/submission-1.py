class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_counter = 0 
        index_list = []
        while i_counter < len(nums): 
            j_counter = i_counter + 1 
            while j_counter < len(nums): 
                if (nums[i_counter] + nums[j_counter]) == target:
                    index_list.append(i_counter)
                    index_list.append(j_counter) 
                j_counter += 1 
            i_counter += 1 
        return index_list 