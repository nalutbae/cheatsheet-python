# datetime: date and time manipulation

from datetime import date, time, datetime, timedelta, timezone

print("=" * 5, "date: calendar dates", "=" * 5)

# Create dates
today = date.today()
print(f"Today: {today}")  # e.g., 2025-07-31
print(f"Year: {today.year}, Month: {today.month}, Day: {today.day}")

specific = date(2025, 12, 25)
print(f"Christmas: {specific}")  # 2025-12-25

from_iso = date.fromisoformat("2025-03-15")
print(f"From ISO: {from_iso}")  # 2025-03-15

from_ordinal = date.fromordinal(739000)
print(f"From ordinal: {from_ordinal}")  # 2024-05-14

# Date properties
print(f"Weekday (Mon=0): {today.weekday()}")  # 0=Mon ... 6=Sun
print(f"ISO weekday (Mon=1): {today.isoweekday()}")  # 1=Mon ... 7=Sun
print(f"ISO calendar: {today.isocalendar()}")  # (year, week, weekday)

# Date formatting
print(f"ISO: {today.isoformat()}")  # 2025-07-31
print(f"Custom: {today.strftime('%Y/%m/%d')}")  # 2025/07/31
print(f"Long: {today.strftime('%B %d, %Y')}")  # July 31, 2025
print(f"Short: {today.strftime('%a, %b %d')}")  # Thu, Jul 31

# Date arithmetic
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)
diff = specific - today
print(f"Tomorrow: {tomorrow}")
print(f"Last week: {last_week}")
print(f"Days until Christmas: {diff.days}")

# Replace parts
first_of_month = today.replace(day=1)
print(f"First of month: {first_of_month}")

print("=" * 5, "time: clock times without dates", "=" * 5)

# Create time objects
noon = time(12, 0, 0)
morning = time(9, 30, 15)
precise = time(14, 30, 0, 500000)  # with microseconds
tz_time = time(9, 0, 0, tzinfo=timezone(timedelta(hours=9)))

print(f"Noon: {noon}")  # 12:00:00
print(f"Morning: {morning}")  # 09:30:15
print(f"Precise: {precise}")  # 14:30:00.500000
print(f"With timezone: {tz_time}")  # 09:00:00+09:00

# Time components
print(f"Hour: {morning.hour}, Minute: {morning.minute}, Second: {morning.second}")
print(f"Microsecond: {precise.microsecond}")

# Time formatting
print(f"ISO: {morning.isoformat()}")  # 09:30:15
print(f"12-hour: {morning.strftime('%I:%M %p')}")  # 09:30 AM
print(f"24-hour: {morning.strftime('%H:%M:%S')}")  # 09:30:15

# Comparison
print(f"Noon > morning: {noon > morning}")  # True
print(f"Noon == time(12, 0): {noon == time(12, 0)}")  # True

print("=" * 5, "datetime: combined date and time", "=" * 5)

# Create datetime objects
now = datetime.now()
utc_now = datetime.now(timezone.utc)
specific_dt = datetime(2025, 7, 31, 14, 30, 0)

print(f"Now: {now}")
print(f"UTC now: {utc_now}")
print(f"Specific: {specific_dt}")  # 2025-07-31 14:30:00

# From ISO format
dt_iso = datetime.fromisoformat("2025-07-31T14:30:00+09:00")
print(f"From ISO: {dt_iso}")  # 2025-07-31 14:30:00+09:00

# From timestamp
dt_ts = datetime.fromtimestamp(1722400000)
print(f"From timestamp: {dt_ts}")

# Components
print(f"Date part: {specific_dt.date()}")  # 2025-07-31
print(f"Time part: {specific_dt.time()}")  # 14:30:00

# Formatting
print(f"ISO: {specific_dt.isoformat()}")
print(f"Custom: {specific_dt.strftime('%Y-%m-%d %H:%M:%S')}")  # 2025-07-31 14:30:00
print(f"Readable: {specific_dt.strftime('%A, %B %d, %Y at %I:%M %p')}")

# Parsing strings
parsed = datetime.strptime("2025/03/15 10:30", "%Y/%m/%d %H:%M")
print(f"Parsed: {parsed}")  # 2025-03-15 10:30:00

# Datetime arithmetic
later = specific_dt + timedelta(hours=3, minutes=30)
earlier = specific_dt - timedelta(days=2)
print(f"+3h30m: {later}")
print(f"-2 days: {earlier}")

# Difference between datetimes
dt1 = datetime(2025, 7, 31, 14, 0, 0)
dt2 = datetime(2025, 8, 1, 17, 30, 0)
delta = dt2 - dt1
print(f"Difference: {delta}")  # 1 day, 3:30:00
print(f"Total seconds: {delta.total_seconds()}")  # 99000.0
print(f"Total hours: {delta.total_seconds() / 3600}")  # 27.5

print("=" * 5, "timedelta: durations", "=" * 5)

# Creating timedeltas
td1 = timedelta(days=7)
td2 = timedelta(weeks=2)
td3 = timedelta(days=3, hours=5, minutes=30, seconds=15)
td4 = timedelta(seconds=3600)

print(f"7 days: {td1}")  # 7 days, 0:00:00
print(f"2 weeks: {td2}")  # 14 days, 0:00:00
print(f"3d 5h 30m 15s: {td3}")  # 3 days, 5:30:15
print(f"1 hour: {td4}")  # 1:00:00

# Total seconds
print(f"Total seconds: {td3.total_seconds()}")  # 277815.0

# Timedelta arithmetic
combined = td1 + td2
print(f"7d + 14d = {combined}")  # 21 days, 0:00:00
doubled = td1 * 2
print(f"7d * 2 = {doubled}")  # 14 days, 0:00:00

# Comparing timedeltas
print(f"td1 < td2: {td1 < td2}")  # True
print(f"td1 == timedelta(weeks=1): {td1 == timedelta(weeks=1)}")  # True

print("=" * 5, "timezone handling", "=" * 5)

# Creating timezones
kst = timezone(timedelta(hours=9))   # Korea Standard Time
jst = timezone(timedelta(hours=9))   # Japan Standard Time (same offset)
est = timezone(timedelta(hours=-5))  # Eastern Standard Time
utc = timezone.utc

# Timezone-aware datetimes
dt_kst = datetime(2025, 8, 1, 10, 0, tzinfo=kst)
dt_utc = dt_kst.astimezone(utc)
dt_est = dt_kst.astimezone(est)

print(f"KST: {dt_kst}")  # 2025-08-01 10:00:00+09:00
print(f"UTC: {dt_utc}")  # 2025-08-01 01:00:00+00:00
print(f"EST: {dt_est}")  # 2025-07-31 21:00:00-05:00

# Make naive datetime timezone-aware
naive = datetime(2025, 8, 1, 10, 0)
aware = naive.replace(tzinfo=kst)
print(f"Naive: {naive}")  # 2025-08-01 10:00:00
print(f"Aware: {aware}")  # 2025-08-01 10:00:00+09:00

# Current time in different timezones
now_utc = datetime.now(timezone.utc)
now_kst = now_utc.astimezone(kst)
now_est = now_utc.astimezone(est)
print(f"Now UTC: {now_utc.strftime('%Y-%m-%d %H:%M %Z')}")
print(f"Now KST: {now_kst.strftime('%Y-%m-%d %H:%M %Z')}")
print(f"Now EST: {now_est.strftime('%Y-%m-%d %H:%M %Z')}")

# Timezone conversion helper
def convert_tz(dt, from_tz, to_tz):
    """Convert a naive datetime from one timezone to another."""
    aware = dt.replace(tzinfo=from_tz)
    return aware.astimezone(to_tz)

meeting = datetime(2025, 8, 1, 10, 0)
print(f"KST 10:00 → UTC: {convert_tz(meeting, kst, utc).strftime('%H:%M')}")  # 01:00
print(f"KST 10:00 → EST: {convert_tz(meeting, kst, est).strftime('%H:%M')}")  # 20:00 (prev day)

print("=" * 5, "Practical patterns", "=" * 5)

# Age calculation
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

birth = date(1995, 3, 15)
print(f"Age: {calculate_age(birth)}")

# Date range generator
def date_range(start, end, step=timedelta(days=1)):
    current = start
    while current < end:
        yield current
        current += step

for d in date_range(date(2025, 7, 28), date(2025, 8, 2)):
    print(f"  {d.strftime('%A, %B %d')}")

# Day of week check
def is_weekend(dt):
    return dt.weekday() >= 5  # Sat=5, Sun=6

def is_business_day(dt):
    return dt.weekday() < 5

test_date = date(2025, 8, 2)  # Saturday
print(f"{test_date.strftime('%A')} is weekend: {is_weekend(test_date)}")  # True

# Next business day
def next_business_day(from_date):
    next_day = from_date + timedelta(days=1)
    while is_weekend(next_day):
        next_day += timedelta(days=1)
    return next_day

print(f"Next business day after Friday: {next_business_day(date(2025, 8, 1))}")

# Time elapsed since a moment
start = datetime(2025, 1, 1, 0, 0, 0)
elapsed = datetime.now() - start
print(f"Days since 2025-01-01: {elapsed.days}")