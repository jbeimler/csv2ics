# csv2ics

take semi unstructured data from a csv file and create an ics calendar

## Description

MVP, created for full day and multi day events.

## Getting Started

### Dependencies

* requires python 3 installed
* uses external packages
  * [dateparser](https://pypi.org/project/dateparser/)
  * [ical](https://pypi.org/project/ical/)

### Installing

* download and uncompress source package
* ```python -m pip install -r requirements.txt```

### Executing program

* requires a csv with the following rows, order not required
  * description -- event title
  * start -- start date, most formats supportedd
  * end -- end date, most formats supportedd
  * transparency -- contains free/busy, Y is free, anything else is busy
* run `python csv2ics.py <events.csv>`
* it will create ```events.ics```
* import calendar into your favorite calendar application

## Help

### To create a new calendar in Outlook to add your new calendar items

1. Open Microsoft Outlook.
2. In the lower left corner, click on the Calendar icon.
3. In the Calendar Navigation Pane along the left side of the screen, look for the section entitled My Calendars. Within the My Calendars section, right-click on your current calendar and select New Folder from the pop-up menu.
4. In the provided field, type in the name for your new calendar and press return.
5. The new calendar appears in the Calendar Navigation Pane along the left side of the screen.
6. To view the new calendar, select the circle next to the calendar name.

## Authors

[John Beimler](mailto:jbeimler@radiomind.com)

## Version History

* 0.1
  * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
