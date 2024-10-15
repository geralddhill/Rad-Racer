# Names: Gerald Hill, Hoang Do
# Date: 10/14/24
# Desc: Plays a racing game in the console


from random import randint
from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from truck import Truck
from check_input import get_int_range

def generate_map():
    '''Generates a random map with obstacles
    
    Returns: the map as three lists (one for each lane)
    '''
    map = [['-'] * 100,['-'] * 100,['-'] * 100]

    for i in range(3):
        map[i][0] = '*'
        for j in range(2):
            obstacle_loc = randint(1, 98)
            map[i][obstacle_loc] = 'O'

    return map


def display_map(map, vehicles, user_vehicle):
    '''Displays vehicles and map (three lists)
    
    Args:
        - map: the map to display (as list of 3 lists)
        - vehicles: a list of 3 vehicle obejcts
        - user_vehicle: the index of the user's vehicle choice
    '''
    for vehicle in vehicles:
        print(vehicle)
    for i, lane in enumerate(map):
        for j, object in enumerate(lane):
            if j == 99 and vehicles[i].position >= 99:
                if i == user_vehicle:
                    print("P",end='')
                    continue
                print(vehicles[i].initial,end='')
                continue
            elif vehicles[i].position == j:
                if i == user_vehicle:
                    print("P",end='')
                    continue
                print(vehicles[i].initial,end='')
                continue
            print(object,end='')
        print()


def main():
    # Inits variables
    map = generate_map()
    vehicles = [Car(), Motorcycle(), Truck()]
    winners = []

    # Prints intro
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash!")

    # Prints descriptions
    for i, vehicle in enumerate(vehicles):
        print(f"{i + 1}. {vehicle.description_string()}")

    # Lets user choose their vehicle and stores it as an int (index in vehicles[])
    user_vehicle = get_int_range("Choose your vehicle (1-3): ", 1, 3) - 1
    print()

    # Runs until vehicles are finished
    while(vehicles[0].position < 99 or vehicles[1].position < 99 or vehicles[2].position < 99):
        display_map(map, vehicles, user_vehicle)
        actions = {}
        for i in range(3):
            # Continues if vehicle has already finished
            if vehicles[i].position >= 99:
                continue
            # Selects user's action
            if i == user_vehicle:
                actions[i] = get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3)
            else:
                # Randomly selects opponents' actions
                action_rand = randint(1, 10)
                if action_rand in range(1, 4) and vehicles[i].energy >= 5:
                    actions[i] = 1
                elif action_rand in range(4, 7) and vehicles[i].energy >= 15:
                    actions[i] = 3
                else:
                    actions[i] = 2
        print()

        # Takes actions
        for i in range(3):
            result = ""
            try:
                if actions[i] == 1:
                    try:
                        result = vehicles[i].fast(map[i].index('O', vehicles[i].position) - vehicles[i].position)
                    except ValueError:
                        result = vehicles[i].fast(999)
                elif actions[i] == 2:
                    try:
                        result = vehicles[i].slow(map[i].index('O', vehicles[i].position) - vehicles[i].position)
                    except ValueError:
                        result = vehicles[i].slow(999)
                elif actions[i] == 3:
                    try:
                        result = vehicles[i].special_move(map[i].index('O', vehicles[i].position) - vehicles[i].position)
                    except ValueError:
                        result = vehicles[i].special_move(999)
            except KeyError:
                pass

            print(result)

            if vehicles[i].position >= 99:
                map[i][99] = '*'
            else:
                map[i][vehicles[i].position] = '*'
            
            if vehicles[i].position >= 99  and vehicles[i] not in winners:
                winners.append(vehicles[i])
        print()
    
    # Prints final map and winners
    print()
    display_map(map, vehicles, user_vehicle)
    for i, winner in enumerate(winners):
        print(f"{i + 1}st place: {winner}")


main()