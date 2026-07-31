# Datetime: date and time manipulation

from datetime import date, time, datetime, timedelta, timezone
import time as time_module

print("=" * 5, "Creating date objects", "=" * 5)

# Current date
today = date.today()
print(f"Today: {today}")  # e.g., 2025-07-31
print(f"Year: {today.year}, Month: {today.month}, Day: {today.day}")

# Create a specific date
birthday = date(2025, 12, 25)
print(f"Birthday: {birthday}")

# Date from ISO format
from_iso = date.fromisoformat("2025-01-15")
print(f"From ISO: {from_iso}")  # 2025-01-15

# Date from timestamp
from_timestamp = date.fromtimestamp(1700000000)
print(f"From timestamp: {from_timestamp}")  # 2023-11-14

# Date properties
print(f"Weekday (Mon=0): {today.weekday()}")  # 0=Mon, 6=Sun
print(f"ISO weekday (Mon=1): {today.isoweekday()}")  # 1=Mon, 7=Sun
print(f"ISO calendar: {today.isocalendar()}")  # (year, week, weekday)

# Date formatting
print(f"ISO format: {today.isoformat()}")  # 2025-07-31
print(f"Custom format: {today.strftime('%Y/%m/%d')}")  # 2025/07/31
print(f"Long format: {today.strftime('%B %d, %Y')}")  # July 31, 2025
print(f"Short format: {today.strftime('%a, %b %d')}")  # Thu, Jul 31

# Parsing dates
parsed = datetime.strptime("2025-03-15", "%Y-%m-%d").date()
print(f"Parsed date: {parsed}")  # 2025-03-15

print("=" * 5, "Creating time objects", "=" * 5)

# Create time objects
t1 = time(14, 30, 0)  # 14:30:00
t2 = time(9, 0, 0, 500000)  # 09:00:00.500000
t3 = time(23, 59, 59)

print(f"Time: {t1}")  # 14:30:00
print(f"Time with microsecond: {t2}")  # 09:00:00.500000
print(f"Hour: {t1.hour}, Minute: {t1.minute}, Second: {t1.second}")

# Time formatting
print(f"ISO format: {t1.isoformat()}")  # 14:30:00
print(f"Custom format: {t1.strftime('%I:%M %p')}")  # 02:30 PM
print(f"24h format: {t1.strftime('%H:%M:%S')}")  # 14:30:00

# Time with timezone
tz = timezone(timedelta(hours=9))
t_tz = time(14, 30, tzinfo=tz)
print(f"Time with TZ: {t_tz}")  # 14:30:00+09:00

# Time comparison
print(f"t1 < t3: {t1 < t3}")  # True (14:30 < 23:59)

print("=" * 5, "Creating datetime objects", "=" * 5)

# Current datetime
now = datetime.now()
utc_now = datetime.now(timezone.utc)
print(f"Now: {now}")
print(f"UTC now: {utc_now}")

# Create specific datetime
dt = datetime(2025, 7, 31, 14, 30, 0)
print(f"Specific datetime: {dt}")  # 2025-07-31 14:30:00

# From ISO format
dt_iso = datetime.fromisoformat("2025-07-31T14:30:00+09:00")
print(f"From ISO: {dt_iso}")  # 2025-07-31 14:30:00+09:00

# From timestamp
dt_ts = datetime.fromtimestamp(1700000000)
print(f"From timestamp: {dt_ts}")

# Datetime components
print(f"Date part: {dt.date()}")  # 2025-07-31
print(f"Time part: {dt.time()}")  # 14:30:00

# Datetime formatting
print(f"ISO format: {dt.isoformat()}")
print(f"Custom: {dt.strftime('%Y-%m-%d %H:%M:%S')}")  # 2025-07-31 14:30:00
print(f"Readable: {dt.strftime('%A, %B %d, %Y at %I:%M %p')}")  # Thursday, July 31, 2025 at 02:30 PM

# Datetime parsing
parsed_dt = datetime.strptime("2025/03/15 10:30", "%Y/%m/%d %H:%M")
print(f"Parsed datetime: {parsed_dt}")  # 2025-03-15 10:30:00

print("=" * 5, "timedelta: date and time arithmetic", "=" * 5)

# Creating timedeltas
delta1 = timedelta(days=7)
delta2 = timedelta(weeks=2)
delta3 = timedelta(days=3, hours=5, minutes=30)
delta4 = timedelta(seconds=3600)  # 1 hour

print(f"7 days: {delta1}")  # 7 days, 0:00:00
print(f"2 weeks: {delta2}")  # 14 days, 0:00:00
print(f"3d 5h 30m: {delta3}")  # 3 days, 5:30:00
print(f"1 hour: {delta4}")  # 1:00:00

# Date arithmetic
today = date.today()
next_week = today + timedelta(days=7)
last_month = today - timedelta(days=30)
print(f"Today: {today}")
print(f"Next week: {next_week}")
print(f"30 days ago: {last_month}")

# Datetime arithmetic
now = datetime.now()
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
in_2_hours = now + timedelta(hours=2)

print(f"Now: {now.strftime('%Y-%m-%d %H:%M')}")
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d %H:%M')}")
print(f"In 2 hours: {in_2_hours.strftime('%Y-%m-%d %H:%M')}")

# Difference between two dates
date1 = date(2025, 12, 25)
date2 = date(2025, 7, 31)
diff = date1 - date2
print(f"Days until Christmas: {diff.days}")  # number of days

# Difference between two datetimes
dt1 = datetime(2025, 7, 31, 14, 0, 0)
dt2 = datetime(2025, 7, 31, 17, 30, 0)
diff = dt2 - dt1
print(f"Time diff: {diff}")  # 3:30:00
print(f"Total seconds: {diff.total_seconds()}")  # 12600.0
print(f"Hours: {diff.total_seconds() / 3600}")  # 3.5

# Timedelta operations
delta = timedelta(days=1, hours=6)
print(f"Total seconds: {delta.total_seconds()}")  # 108000.0
print(f"Total hours: {delta.total_seconds() / 3600}")  # 30.0

print("=" * 5, "Timezone handling", "=" * 5)

# UTC timezone
utc = timezone.utc
now_utc = datetime.now(utc)
print(f"UTC now: {now_utc}")

# Creating timezones
kst = timezone(timedelta(hours=9))  # Korea Standard Time
est = timezone(timedelta(hours=-5))  # Eastern Standard Time

print(f"KST: {datetime.now(kst)}")
print(f"EST: {datetime.now(est)}")

# Converting between timezones
utc_time = datetime.now(timezone.utc)
kst_time = utc_time.astimezone(kst)
print(f"UTC: {utc_time.strftime('%Y-%m-%d %H:%M %Z')}")
print(f"KST: {kst_time.strftime('%Y-%m-%d %H:%M %Z')}")

# Timezone-aware vs timezone-naive
naive = datetime(2025, 7, 31, 14, 0)
aware = datetime(2025, 7, 31, 14, 0, tzinfo=kst)
print(f"Naive: {naive}")  # 2025-07-31 14:00:00
print(f"Aware: {aware}")  # 2025-07-31 14:00:00+09:00
print(f"TZ info: {aware.tzname()}")  # UTC+09:00

print("=" * 5, "time module: timestamps and sleeping", "=" * 5)

# Unix timestamp (seconds since 1970-01-01)
ts = time_module.time()
print(f"Timestamp: {ts}")  # e.g., 1722400000.123456

# Convert timestamp to datetime
dt_from_ts = datetime.fromtimestamp(ts)
print(f"From timestamp: {dt_from_ts}")

# Convert datetime to timestamp
back_to_ts = dt_from_ts.timestamp()
print(f"Back to timestamp: {back_to_ts}")

# Sleep (pause execution)
start = time_module.time()
time_module.sleep(0.01)  # sleep for 10ms
elapsed = time_module.time() - start
print(f"Slept for ~{elapsed:.4f} seconds")

# Performance timing
start = time_module.perf_counter()
total = sum(range(1000000))
end = time_module.perf_counter()
print(f"Sum computed in {end - start:.6f} seconds")

# time.struct_time
local = time_module.localtime()
print(f"Local time struct: year={local.tm_year}, mon={local.tm_mon}, day={local.tm_mday}")

# Format time as string
time_str = time_module.strftime("%Y-%m-%d %H:%M:%S", local)
print(f"Formatted: {time_str}")

# Parse time string
parsed_time = time_module.strptime("2025-07-31 14:30:00", "%Y-%m-%d %H:%M:%S")
print(f"Parsed: year={parsed_time.tm_year}, hour={parsed_time.tm_hour}")

print("=" * 5, "Practical datetime patterns", "=" * 5)

# Date range generator
def date_range(start, end, step=timedelta(days=1)):
    """Generate dates from start to end (exclusive)."""
    current = start
    while current < end:
        yield current
        current += step

start_date = date(2025, 7, 28)
end_date = date(2025, 8, 3)
for d in date_range(start_date, end_date):
    print(f"  {d.strftime('%A, %B %d')}")
# Monday, July 28
# Tuesday, July 29
# ...

# Age calculation
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

birth = date(1995, 3, 15)
print(f"Age: {calculate_age(birth)}")

# Timezone conversion helper
def convert_timezone(dt, from_tz, to_tz):
    """Convert a naive datetime from one timezone to another."""
    dt_aware = dt.replace(tzinfo=from_tz)
    return dt_aware.astimezone(to_tz)

meeting_time = datetime(2025, 8, 1, 10, 0)  # 10:00 AM
kst = timezone(timedelta(hours=9))
utc = timezone.utc
est = timezone(timedelta(hours=-5))

print(f"Meeting in KST: {convert_timezone(meeting_time, kst, kst).strftime('%H:%M')}")
print(f"Meeting in UTC: {convert_timezone(meeting_time, kst, utc).strftime('%H:%M')}")
print(f"Meeting in EST: {convert_timezone(meeting_time, kst, est).strftime('%H:%M')}")