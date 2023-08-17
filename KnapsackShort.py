def knapsack_max_profit(weights, costs, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            dp[i][j] = max(costs[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j]) if weights[i - 1] <= j else dp[i - 1][j]
    
    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1
    
    selected_items.reverse()
    return dp[n][capacity], selected_items

weights = list(map(int, input("Enter the weights of the items: ").split()))
costs = list(map(int, input("Enter the costs of the items: ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))
profit, selected_items = knapsack_max_profit(weights, costs, capacity)
print("Maximum profit:", profit)
print("Selected items (index):", selected_items)
print("Selected items (weights):", [weights[i] for i in selected_items])
print("Selected items (costs):", [costs[i] for i in selected_items])
