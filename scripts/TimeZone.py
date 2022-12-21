# @author Melina Dimitrova

from datetime import datetime
import pytz

# current Datetime
current = datetime.now()
print('Current Timezone :', current)

# Standard UTC timezone
standard = datetime.now(pytz.utc)
print('Standard Timezone :', standard)

# Paris timezone datetime
dt_paris = datetime.now(pytz.timezone('Europe/Paris'))
print('Paris DateTime', dt_paris)
# US/Pacific timezone datetime
dt_us_pacific = datetime.now(pytz.timezone('US/Pacific'))
print('US Pacific DateTime', dt_us_pacific)
# US/Pacific timezone datetime
dt_aus = datetime.now(pytz.timezone('Australia/Sydney'))
print('Australia Oceanic DateTime', dt_aus)

print(pytz.all_timezones[0:10])

# Get current TimeZone name
print("Timezone name: " + dt_aus.tzname())

# Get UTC Offset
print(dt_aus.utcoffset())

# Get the daylight saving time (DST offset) adjustment
print(dt_aus.dst())

dt_us_central = datetime.now(pytz.timezone('US/Central'))
print('US Central DateTime', dt_us_central)
# Convert US Central to US Eastern timezone
dt_us_eastern = dt_us_central.astimezone(pytz.timezone('America/New_York'))
print('US Eastern DateTime', dt_us_eastern)

# Get timezone by user input
timezone = input("Enter a UTC timezone ")
dt = datetime.now(pytz.timezone(timezone))
print('Current time in your timezone: ', dt)
print("Timezone name: " + dt.tzname())
