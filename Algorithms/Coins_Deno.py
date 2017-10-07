def coinDenominationCombinations(amount,denominations):
    combinations = [0 for x in range(amount+1) ]
    print combinations
    combinations[0] = 1
    print combinations

    for denomination in denominations:
        for j in range(denomination,amount+1):
            #print combinations[j-denomination]
            combinations[j] += combinations[j-denomination]
            print combinations
    #print combinations[amount]
    return combinations[amount]

#Testing the function
print(coinDenominationCombinations(5,[1,2,3]))
#print(coinDenominationCombinations(11,[1,5,6,8]))
