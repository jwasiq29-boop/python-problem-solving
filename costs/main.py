account_blance = 5000

def costs():
    x = []
    while True:
        cos = input("Enter your daily costs (or type 'done' to finish): ")
        if cos == 'done':
            break
        cos = float(cos)
        x.append(cos)
    return sum(x)


def after_costs():
    total_costs = costs()
    remaining_balance = account_blance - total_costs
    return remaining_balance

print("all of your costs are: " , costs())
print("Your remaining balance is: " , after_costs())


