prices = [100, 180, 260, 310, 40, 535, 695]
profit = 0
i = 0

while i < len(prices) - 1:
    while i < len(prices) - 1 and prices[i + 1] <= prices[i]:
        i += 1
    if i == len(prices) - 1:
        break
    buy = i
    while i < len(prices) and prices[i] >= prices[i - 1]:
        i += 1
    sell = i - 1
    profit += prices[sell] - prices[buy]

print(f"Maximum profit: {profit}")
