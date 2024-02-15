# Imports here

# Note: this may change in the future as Culver's updates their web site.
base_url = "https://www.culvers.com/restaurants/"

def fetch_flavors(location: str) -> dict:
    """ Given a single location string, this will get the flavors and dates for that location.
    Returns a dictionary of flavors for the five dates: { "date1": "flavor", "date2": "flavor", ... }
    """
    print(location)

def output_flavor_data(collected_flavor_data: dict):
    """ Given the final collection of location and flavor data, as a dictionary, this will
    output the data to the command-line. This may be modified in the future to output to a CSV, email, front-end, etc.
    """
    pass

def flavor_finder() -> None:
    """ Gathers flavor data for each chosen location and then outputs that data.
    Update the location list with your favorite Culvers restaurant locations.
    Locations are typically all lower-case and the city names have hyphens, not spaces. This project assumes that users know
    their locations and enter them correctly. It will simply skip over a returned 404.
    To know your location: go to the flavor of the day page for your restaurant and it should be at the end of the URL.
    """
    culvers_locations = ["verona", "west-allis", "appleton", "arlington-heights"]
    fetch_flavors(culvers_locations[0])

flavor_finder()