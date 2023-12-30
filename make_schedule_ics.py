"""
Create a .ics file from schedule.csv
See https://icalendar.org/RFC-Specifications/iCalendar-RFC-5545/ for reference
See https://icalendar.org/validator.html for validating generated .icsv file

The schedule is present in a CSV file, this code requires the file to follow 
the column naming conventions used here. Other parameters needed for adding content
in the calendar entry (such as location of the meeting) are read from _variables.yml file
"""
import os
import uuid
import yaml
import pandas as pd
from datetime import datetime

SCHEDULE_CSV = os.path.join("data", "schedule.csv")
SCHEDULE_ICS = os.path.join("files", "schedule.ics")
VARIABLES_YML = "_variables.yml"

#def cal_event(group, subgroup, date, title, lecture, lab, assignment, notes, start_hhmmss, end_hhmmss, location, course_url):
def cal_event(group, subgroup, date, title, lecture, lab, notes, start_hhmmss, end_hhmmss, location, course_url):
    date_start = date.replace("-", "") + "T" + start_hhmmss
    date_end = date.replace("-", "") + "T" + end_hhmmss
    uuid_str = str(uuid.uuid4())
    created = datetime.now().replace(microsecond=0).isoformat().replace("-", "").replace(":", "")
    description = f"{course_url}/{lecture}"
    event = f"""
BEGIN:VEVENT
DTSTART:{date_start}
DTEND:{date_end}
DTSTAMP:{date_start}
UID:{uuid_str}
CREATED:{created}
DESCRIPTION:{description}
LAST-MODIFIED:{created}
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:{title}
TRANSP:OPAQUE
LOCATION:{location}
END:VEVENT
"""
    return event

def make_ics():
    # read the schedule from CSV
    schedule = pd.read_csv(SCHEDULE_CSV)

    # read the config yaml file
    with open(VARIABLES_YML, 'r') as yaml_in:
        config = yaml.safe_load(yaml_in)

    # now ready to create icsv file
    print(f"going to write calendar to {SCHEDULE_ICS}")
    with open(SCHEDULE_ICS, "w") as f:
        # calendar header
        cal_header = f"""BEGIN:VCALENDAR
                        PRODID:-//Google Inc//Google Calendar 70.9054//EN
                        VERSION:2.0
                        CALSCALE:GREGORIAN
                        METHOD:PUBLISH
                        X-WR-CALNAME:{config['course']['number']} {config['course']['semester']}
                        X-WR-TIMEZONE:America/New_York
                      """
        f.write(cal_header)

        # calendar event entries
        for k, row in schedule.iterrows():
            row['start_hhmmss'] = config['course']['class_start_hhmmss']
            row['end_hhmmss'] = config['course']['class_end_hhmmss']
            row['location'] = config['course']['location']
            row['course_url'] = config['course']['url']
            f.write(cal_event(**row))

        # calendar trailer        
        cal_trailer = "END:VCALENDAR"
        f.write(cal_trailer)

