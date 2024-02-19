# flavor_finder
Scraper to retrieve the current and next four flavors of the day for selected Culver's restaurants.

- Utilizes Python 3
- To allow for automated runtime or binding to a command-line command, this utilizes a string list of restaurant names instead of user input.
- Is run from the command-line using "python flavor_finder.py", or "python3 flavor_finder.py" depending on environment bindings.
- Becasue this is a scraper, it is fragile and subject to the whims of Culvers front-end devs. If any html changes, this will require an update.
