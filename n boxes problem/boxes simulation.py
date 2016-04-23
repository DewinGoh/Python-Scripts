#Game Simulation
import random

players = 13
picking_percentage = 10.0/13
iterations = 50000

def boxes(players):
    game_arena = {}
    box_numbers = []
    for number in range(1,players+1):
        box_numbers.append(number)
        
    for box in xrange(1,players+1):
        box_number = random.choice(box_numbers)
        game_arena[box] = box_number
        box_numbers.remove(box_number)
        
    return game_arena

#choose the boxes randomly
def strategy1(players,game_arena,percentage):
    for player in xrange(1,players+1):
        chosen = random.sample(game_arena.values(),int(percentage*len(game_arena)))
        if player in chosen:
            continue
        else:
            return False
    return True

#choose boxes non-randomly: follow the directions of piece of paper in box
def strategy2(players,game_arena,percentage):
    for player in xrange(1,players+1):
        box_number = player
        boxes_opened = 0
        while boxes_opened < int(len(game_arena)*percentage):
            
            if game_arena[box_number] == player:
                break
            else:
                box_number = game_arena[box_number]            
                boxes_opened += 1
                continue
        if boxes_opened >= int(len(game_arena)*percentage):
            return False       
    return True

#choose boxes non-randomly: select consecutive boxes
def strategy3(players,game_arena,percentage):
    playercounter = players
    for player in xrange(1,players+1):
        box_number = player
        boxes_opened = 0
        while boxes_opened < int(len(game_arena)*percentage):
            
            if game_arena[box_number] == player:
                break
            else:
                print box_number
                box_number = (box_number % playercounter) + 1
                boxes_opened += 1
                continue
        if boxes_opened >= int(len(game_arena)*percentage):
            return False       
    return True

def success_rate(players,picking_percentage,iterations):
    success = 0
    for i in xrange(iterations):
        result = strategy1(players,boxes(players),picking_percentage)
        if result:
            success += 1
    percentage = success/float(i+1)*100
    print str(percentage) + '%'
    return 0

success_rate(players,picking_percentage,iterations)
