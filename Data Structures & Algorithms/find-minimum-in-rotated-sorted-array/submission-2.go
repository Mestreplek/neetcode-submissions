func findMin(nums []int) int {
	l := 0 
	r := len(nums) - 1
	m := (r+l) / 2

	for true {
		
		if nums[l] > nums[m] {
			l += 1 
			r = m
		} else {
			before := l -1
			if before < 0 {
				before = len(nums) + before
			}
			if nums[before] > nums[l] {
				return nums[l]
			} 
			l = m + 1
		}
		m = (r+l) / 2
		if l >= r {
			return nums[m]
		}

	}
	return -1
}