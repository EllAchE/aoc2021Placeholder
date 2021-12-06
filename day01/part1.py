data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

# This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.
# The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.
# To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

# 199 (N/A - no previous measurement)
# 200 (increased)
# 208 (increased)
# 210 (increased)
# 200 (decreased)
# 207 (increased)
# 240 (increased)
# 269 (increased)
# 260 (decreased)
# 263 (increased)
#
# In this example, there are 7 measurements that are larger than the previous measurement.

def countIncreases():
    intlst = list(map(lambda a : int(a), lst))
    total = 0
    oldItem = intlst.pop(0)
    print(len(intlst))
    for item in intlst:
        if item > oldItem:
            total += 1
        print("total {} oldItem {} Item {}".format(total, oldItem, item))
        oldItem = item
    return total

print(countIncreases())