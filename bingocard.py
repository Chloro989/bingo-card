import random
#prepare a list that has numbers from 1 to 75 in it
nums = list(range(1,75+1))
#shuffle
random.shuffle(nums)
nums[12] = "*" #appointig a wildcard
#show cards
for y in range(0,5):
    for x in range(0,5):
        print("{:>3},".format(nums[y*5+x]),end = "")
    print("")
