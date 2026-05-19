func maxProfit(prices []int) int {

	var profit int 
	best_buy, max_profit := prices[0], 0 
	for i:=0; i < len(prices); i++ {
		if best_buy > prices[i] {
			best_buy = prices[i]
		}
		
		profit = prices[i] - best_buy 
		if profit > max_profit {
			max_profit = profit
		}

		
	}
	return max_profit
}
