import csv
import os
import sys
from datetime import timedelta
from pathlib import Path
from uuid import uuid4

import dateparser

import re

from ical.calendar import Calendar
from ical.calendar_stream import IcsCalendarStream
from ical.event import Event

if __name__ == "__main__":
    csv_file_input = sys.argv[1]
    base_name = csv_file_input[:-4]

    cal = Calendar()
    with open(csv_file_input, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count >= 0:
                start, end = (
                    dateparser.parse(row["start"]).date(),
                    dateparser.parse(row["end"]).date(),
                )
                print(f"{row['description']}:  {start} ➡️ {end}")
                if row["description"].lower() == "Y":
                    transparency = "TRANSPARENT"  # outlook calls this Free
                else:
                    transparency = "OPAQUE"
                cal.events.append(
                    Event(
                        summary=row["description"],
                        start=start,
                        end=end,
                        transparency=transparency,
                    )
                )
            line_count += 1
    print(f"Processed {line_count} lines.")

    # filename = Path(f"{base_name}.ics")
    # with filename.open("w") as ics_file:
    #    ics_file.write(IcsCalendarStream.calendar_to_ics(cal))

    # FIXME Hack to add X-MICROSOFT-CDO-ALLDAYEVENT:TRUE
    #   so outlook makes it all day instead of 12am-12am
    ics_string = IcsCalendarStream.calendar_to_ics(cal)
    regex = r"^END:VEVENT"
    subst = "X-MICROSOFT-CDO-ALLDAYEVENT:TRUE\\nEND:VEVENT"
    ics_string = re.sub(regex, subst, ics_string, 0, re.MULTILINE)

    filename = Path(f"{base_name}.ics")
    with filename.open("w") as ics_file:
        ics_file.write(ics_string)
