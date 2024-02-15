from urllib.request import urlopen
from bs4 import BeautifulSoup

# Note: this may change in the future as Culver's updates their web site.
base_url = "https://www.culvers.com/restaurants/"

def fetch_flavors(location: str) -> dict:
    """ Given a single location string, this will get the flavors and dates for that location.
    Returns a dictionary of flavors for the five dates: { "date1": "flavor", "date2": "flavor", ... }
    """
    return_flavors = {}
    url = f"{base_url}{location}"
    try:
        response_html = urlopen(url).read().decode("utf-8")
    except:
        print("Invalid location : ", location, "\n")
        return None
    response_soup = BeautifulSoup(response_html, "html.parser")

    # Soup selections are typically a list of matches, but class lookup here is specific enough that only the zero index is needed.
    results = response_soup.select('div[class*="RestaurantCalendarPanel_containerCalendar"]')[0]
    days = results.select('div[class*="_containerItem_"]')
    for day in days:
        date = day.select("h3")[0].contents[0]
        flavor = day.select('a[class*="FlavorLink__Kvd0e"]')[0].contents[0]
        return_flavors[date] = flavor
    return return_flavors

def output_flavor_data(collected_flavor_data: dict) -> None:
    """ Given the final collection of location and flavor data, as a dictionary, this will
    output the data to the command-line. This may be modified in the future to output to a CSV, email, front-end, etc.
    """
    for location, value in collected_flavor_data.items():
        print(location.upper())
        for date, flavor in value.items():
            print(date, flavor)
        print("\n")

def flavor_finder() -> None:
    """ Gathers flavor data for each chosen location and then outputs that data.
    Update the location list with your favorite Culvers restaurant locations.
    Locations are typically all lower-case and the city names have hyphens, not spaces. This project assumes that users know
    their locations and enter them correctly. It will simply skip over a returned 404.
    To know your location: go to the flavor of the day page for your restaurant and it should be at the end of the URL.
    """
    culvers_locations = ["verona", "west-allis", "appleton", "this is totally not a location", "arlington-heights"]
    valid_locations = []
    collected_flavor_data = {}
    for location in culvers_locations:
        fetched_flavors = fetch_flavors(location)
        if fetched_flavors is not None:
            valid_locations.append(location)
            collected_flavor_data[location] = fetched_flavors
    # Creates a list of days - dynamic, but reliant on the date keys of the first location.
    output_flavor_data(collected_flavor_data)

flavor_finder()