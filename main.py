# Project 3 - this module is the only one the executes the whole program
# This is where this reads the input and constructs the objects that will
# generate the output

import handle_mq_api
from printing_outputs import *



### NECESSARY VARIABLES #####
location_list = []              # used to gather user inputs of their locations

legit_stats = {"STEPS": steps(), "TOTALDISTANCE": totaldist(),
               "TOTALTIME": totaltime(), "LATLONG": latlongs(),
               "ELEVATION": elevation()}

user_input_stats = []           # used to gather user inputs of their statistics

jason_object = ''

#############################


###TEST LOCATIONS###

####################


################################################################################
### The following functions help with USER INPUT. They do not provide any info
### to the user, as they expect the user to know what to put.

def take_number() -> int:   # should be the first line of input from the user
    '''specifies how many locations the trip will consist of'''
    return int(input())

def input_locations(num: int) -> None:
    '''This function determines the number of lines that will prompt the user to 
    describe the location(s) of their choice'''
    
    for i in range(num):
        a = input()
        location_list.append(a)


def input_stats(num: int) -> None:
    '''This function determines the number of lines that will prompt the user to
    describe the statistics they want. The statistics MUST match the
    input_stats list'''

    for i in range(num):
        a = input().strip().upper()
        user_input_stats.append(a)


#######################################################################################
##### These next set of functions help with the STATISTICS portion of the program #####

def _is_statistic(choice: str, stats_list: list) -> bool:
    '''This function takes the choice from a previous user input function, and determines if
    it belongs to the list of statistics'''
    return choice in stats_list


#######################################################################
##### These functions combine other functions to make the 'if __name...' block
##### look neat and organized

def behind_the_url() -> str:
    map_url = project3_mapquest.construct_url(location_list)
    print(map_url)
    jason_object = project3_mapquest.open_and_encode(map_url)
    jason_to_json = str(jason_object)

    return jason_to_json


def main_input()-> 'json':
    location_num = take_number()
    input_locations(location_num)
    stats_num = take_number()

    input_stats(stats_num)

def main_output(stat: str, legit: dict, jason: str):
    if stat == legit[stat]:
        print(legit[stat].display(str))


if __name__ == '__main__':
    main_input()
    jason = behind_the_url()
    for stat in user_input_stats:
        main_output(stat, legit_stats, jason)
    print('the key')
