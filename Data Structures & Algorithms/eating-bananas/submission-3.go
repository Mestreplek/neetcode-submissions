func minEatingSpeed(piles []int, h int) int {

	
	max_pile := 0 
	for i:=0;i<len(piles);i++ {
		if max_pile < piles[i] {
			max_pile = piles[i]
		}
	}
	r := max_pile
	l := 1
	m := (l+r) / 2

	for l < r {
		// piles[i] = 7 m = 5
		time_spend := 0
		for i:=0;i<len(piles);i++ {
			time_spend += (piles[i] + m - 1) / m
		}
		
		if time_spend <= h {
			r = m 
		} else {
			l = m + 1
		}
		m = (l+r)/2
	}
	return m


}