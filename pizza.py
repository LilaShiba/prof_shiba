def michael_pays(costs):
    if (costs <= 5):
        return costs
    elif (costs <= 30):
        new_cost = costs/.66
        print("%.2f" %new_cost)
        return costs/(2/3)
    else:
        new_cost = costs - 10
        print(new_cost)
        return costs - 10

michael_pays(45)
