# PS: best time to buy and sell the stocks

# functionality
def findProfit(price):
    minPrice = float('inf')
    maxProfit = 0
    for i in range(len(price)):
        if minPrice > price[i]:
            minPrice = price[i]
        elif price[i]-minPrice > maxProfit:
            maxProfit = price[i]-minPrice
    return maxProfit


# Driver code
price = [7, 1, 5, 3, 6, 4]
maximumProfit = findProfit(price)
print("Maximum profit is: ",maximumProfit)