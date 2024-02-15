from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint

# Note: this may change in the future as Culver's updates their web site.
base_url = "https://www.culvers.com/restaurants/"

def fetch_flavors(location: str) -> dict:
    """ Given a single location string, this will get the flavors and dates for that location.
    Returns a dictionary of flavors for the five dates: { "date1": "flavor", "date2": "flavor", ... }
    """
    return_flavors = {}
    url = f"{base_url}{location}"
    response_html = urlopen(url).read().decode("utf-8")
    response_soup = BeautifulSoup(response_html, "html.parser")

    # Soup selections are typically a list of matches, but class lookup here is specific enough that only the zero index is needed.
    results = response_soup.select('div[class*="RestaurantCalendarPanel_containerCalendar"]')[0]
    days = results.select('div[class*="_containerItem_"]')
    for day in days:
        date = day.select("h3")[0].contents[0]
        flavor = day.select('a[class*="FlavorLink__Kvd0e"]')[0].contents[0]
        return_flavors[date] = flavor
    return return_flavors

def output_flavor_data(collected_flavor_data: dict):
    """ Given the final collection of location and flavor data, as a dictionary, this will
    output the data to the command-line. This may be modified in the future to output to a CSV, email, front-end, etc.
    """
    pprint(collected_flavor_data)

def flavor_finder() -> None:
    """ Gathers flavor data for each chosen location and then outputs that data.
    Update the location list with your favorite Culvers restaurant locations.
    Locations are typically all lower-case and the city names have hyphens, not spaces. This project assumes that users know
    their locations and enter them correctly. It will simply skip over a returned 404.
    To know your location: go to the flavor of the day page for your restaurant and it should be at the end of the URL.
    """
    # culvers_locations = ["verona", "west-allis", "appleton", "arlington-heights"]
    # collected_flavor_data = {}
    # for location in culvers_locations:
    #     collected_flavor_data[location] = fetch_flavors(location)
    # pprint(collected_flavor_data, sort_dicts=False)
    dummy_flavors = {'verona': {'Today - ': 'Dark Chocolate Decadence',
                                'Tomorrow - ': 'Chocolate Heath Crunch',
                                'Saturday, February 17': 'Lemon Berry Layer Cake',
                                'Sunday, February 18': 'Turtle',
                                'Monday, February 19': 'Mint Explosion'},
                    'west-allis': {'Today - ': 'Blackberry Cobbler',
                                    'Tomorrow - ': 'Turtle',
                                    'Saturday, February 17': 'Raspberry Cheesecake',
                                    'Sunday, February 18': 'Mint Cookie',
                                    'Monday, February 19': 'Dark Chocolate Decadence'},
                    'appleton': {'Today - ': 'Butter Pecan',
                                'Tomorrow - ': 'Chocolate Covered Strawberry',
                                'Saturday, February 17': 'Caramel Pecan',
                                'Sunday, February 18': 'Red Raspberry',
                                'Monday, February 19': 'Chocolate Volcano'},
                    'arlington-heights': {'Today - ': 'Salted Caramel Pecan Pie',
                                        'Tomorrow - ': 'Chocolate Caramel Twist',
                                        'Saturday, February 17': 'Turtle Dove',
                                        'Sunday, February 18': 'Lemon Berry Layer Cake',
                                        'Monday, February 19': 'Dark Chocolate PB Crunch'}}
    output_flavor_data(dummy_flavors)

flavor_finder()