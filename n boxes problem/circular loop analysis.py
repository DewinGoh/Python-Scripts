import random

#inputs
players = 100
iteration = 50000

#Sets up playing field
def boxes(players):
    game_arena = {}
    box_numbers = []
    for number in xrange(1,players+1):
        box_numbers.append(number)
        
    for box in xrange(1,players+1):
        box_number = random.choice(box_numbers)
        game_arena[box] = box_number
        box_numbers.remove(box_number)
        
    return game_arena

#loop length counter
def loopcount(boxes):
    tracker = [x for x in range(1,len(boxes)+1)]
    datastore = []
    while len(tracker)>0:
        startpt = tracker[0]
        number = tracker[0]
        tracker.remove(number)
        number = boxes[number]
        counter = 1
        while number != startpt:
            tracker.remove(number)
            number = boxes[number]
            counter += 1
        datastore.append(counter)    
    return datastore

#percentage return
def percentage(datalist):
    total = sum(datalist)
    length = len(datalist)
    datalist2 = []
    for count in datalist:
        percent = str(round(float(count)/total*100,2)) + '%'
        datalist2.append(percent)
    return datalist2

#main
distribution_table = [0 for x in xrange(players)]

for i in xrange(iteration):
    datastore = loopcount(boxes(players))
    for looplen in datastore:
        distribution_table[looplen-1] += 1
print percentage(distribution_table)
