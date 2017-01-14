# ICS 32, Project 3 - this module interacts with the Open MapQuest APIs.
# This is where I should do things like build URLs, make HTTP requests, and
# parsing JSON responses

import urllib.request
import urllib.parse
import json

### NECESSARY VARIABLES #####
api_ck = 'YOUR API CONSUMER KEY' # this is my api consumer key            
                                                                      
mapquest_url = 'http://open.mapquestapi.com/directions/v2/route?key='
                                                        
elevation_url = 'http://open.mapquestapi.com/elevation/v1/profile?key='                
                                                                                    
elevation_parameters = 'outFormat=json&shapeFormat=raw&unit=f&'
                                                                         
#####################################################################################
### These set of functions CONSTRUCT A URL, beginning with opening the web page,
### opening the page and decoding the bytes, and encoding them to become a string
### and then a JSON OBJECT

def construct_url(location: ['locations'])-> str:
    '''This function takes the list of locations and constrcts url parameters
    describing the mapquest location GPS, taking each location from the list and implementing
    the location into constructing the parameters'''

    url_parameters = []

    try:
        for every in location:
            if every == location[0]:
                url_parameters.append(('from', every))
            else:
                url_parameters.append(('to', every))
                
        return mapquest_url + api_ck + '&' + urllib.parse.urlencode(url_parameters)

    except:
        return 'MAPQUEST ERROR'
    
def open_and_encode(url: str) -> str:
    '''takes the url and encodes into a string'''
    open_page = None

    try:
        open_page = urllib.request.urlopen(url)

        this_page_is_read = open_page.read()

        this_page_is_now_str = this_page_is_read.decode(encoding = 'utf-8')
        
        return this_page_is_now_str
    
    except:
        return 'MAPQUEST ERROR'
        
    finally:
        if open_page != None:
            open_page.close()


def create_elevationURL(lat_tuple: tuple) -> str: 
    '''Takes a tuple and creates the URL from that tuple'''

    try:
        a = str(lat_tuple[0])
        b = str(lat_tuple[1])
           
        str_num = a + ',' + b

        return elevation_url + api_ck + '&' + elevation_parameters + 'latLngCollection=' + str_num

    except:
        return 'MAPQUEST ERROR'
    

def convert_webpage_to_JSON(guts: 'open_and_encode()') -> 'json':
    '''Takes the guts of the web page and converts them into a JSON object (which
    is like a dictionary)'''
    return json.loads(guts)

