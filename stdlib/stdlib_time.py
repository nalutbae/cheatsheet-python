# time: time access, conversions, and process timing

import time

print("=" * 5, "Current time and timestamps", "=" * 5)

# Unix timestamp (seconds since 1970-01-01 00:00:00 UTC)
ts = time.time()
print(f"Timestamp: {ts:.6f}")  # e.g., 1722400000.123456

# High-resolution performance counter
perf = time.perf_counter()
print(f"Perf counter: {perf:.6f}")

# Monotonic clock (never goes backward)
mono = time.monotonic()
print(f"Monotonic: {mono:.6f}")

# Process time (CPU time for current process)
proc = time.process_time()
print(f"Process time: {proc:.6f}")

# Thread time (CPU time for current thread)
thread = time.thread_time()
print(f"Thread time: {thread:.6f}")

print("=" * 5, "struct_time: time as named tuple", "=" * 5)

# Get local time as struct_time
local = time.localtime()
print(f"Local time: {local}")
print(f"Year: {local.tm_year}, Month: {local.tm_mon}, Day: {local.tm_mday}")
print(f"Hour: {local.tm_hour}, Minute: {local.tm_min}, Second: {local.tm_sec}")
print(f"Weekday (Mon=0): {local.tm_wday}")  # 0=Monday
print(f"Yearday: {local.tm_yday}")  # day number within year
print(f"Is DST: {local.tm_isdst}")  # daylight saving flag

# Get UTC time as struct_time
utc = time.gmtime()
print(f"UTC time: year={utc.tm_year}, hour={utc.tm_hour}")

# Create struct_time from timestamp
specific = time.localtime(1722400000)
print(f"Specific: {specific.tm_year}-{specific.tm_mon:02d}-{specific.tm_mday:02d}")

print("=" * 5, "Time formatting and parsing", "=" * 5)

# Format time as string
now_struct = time.localtime()

# Common format codes
formats = {
    "%Y-%m-%d": "Date (2025-07-31)",
    "%H:%M:%S": "Time (14:30:00)",
    "%Y-%m-%d %H:%M:%S": "DateTime (2025-07-31 14:30:00)",
    "%A, %B %d, %Y": "Long date (Thursday, July 31, 2025)",
    "%I:%M %p": "12-hour time (02:30 PM)",
    "%Y-%m-%d %H:%M:%S %Z": "With timezone",
}

for fmt, desc in formats.items():
    result = time.strftime(fmt, now_struct)
    print(f"  {desc}: {result}")

# Parse string to struct_time
date_string = "2025-07-31 14:30:00"
parsed = time.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed: year={parsed.tm_year}, mon={parsed.tm_mon}, day={parsed.tm_mday}")
print(f"       hour={parsed.tm_hour}, min={parsed.tm_min}, sec={parsed.tm_sec}")

# Quick format shortcuts
print(f"asctime: {time.asctime()}")  # Thu Jul 31 14:30:00 2025
print(f"ctime: {time.ctime()}")  # Thu Jul 31 14:30:00 2025
print(f"ctime(0): {time.ctime(0)}")  # Thu Jan 01 00:00:00 1970

print("=" * 5, "Timestamp conversions", "=" * 5)

# struct_time → timestamp
st = time.localtime()
ts_from_struct = time.mktime(st)
print(f"struct → timestamp: {ts_from_struct:.6f}")

# timestamp → struct_time (local)
struct_from_ts = time.localtime(ts_from_struct)
print(f"timestamp → struct (local): {time.asctime(struct_from_ts)}")

# timestamp → struct_time (UTC)
struct_utc = time.gmtime(ts_from_struct)
print(f"timestamp → struct (UTC): {time.asctime(struct_utc)}")

# Round-trip: string → struct → timestamp → struct → string
original = "2025-07-31 14:30:00"
parsed = time.strptime(original, "%Y-%m-%d %H:%M:%S")
timestamp = time.mktime(parsed)
back_struct = time.localtime(timestamp)
back_string = time.strftime("%Y-%m-%d %H:%M:%S", back_struct)
print(f"Round-trip: {original} → {back_string}")

print("=" * 5, "Sleep and timing", "=" * 5)

# time.sleep: pause execution
start = time.time()
time.sleep(0.01)  # sleep for 10ms
elapsed = time.time() - start
print(f"Slept for ~{elapsed * 1000:.1f}ms")

# Performance timing with perf_counter (recommended for benchmarks)
start = time.perf_counter()
total = sum(range(1000000))
end = time.perf_counter()
print(f"Sum computed in {(end - start) * 1000:.3f}ms")

# Process time (CPU time, not wall clock)
start_proc = time.process_time()
total = sum(range(1000000))
end_proc = time.process_time()
print(f"CPU time: {(end_proc - start_proc) * 1000:.3f}ms")

# Context manager for timing
class Timer:
    def __init__(self, label=""):
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"{self.label}: {self.elapsed * 1000:.3f}ms")

with Timer("List comprehension"):
    result = [x ** 2 for x in range(100000)]

with Timer("Map function"):
    result = list(map(lambda x: x ** 2, range(100000)))

print("=" * 5, "Timezone information", "=" * 5)

# Timezone offset
local = time.localtime()
if local.tm_isdst == 1:
    tz_name = time.tzname[1]  # DST timezone name
    tz_offset = -time.daylight * 3600
elif local.tm_isdst == 0:
    tz_name = time.tzname[0]  # Standard timezone name
    tz_offset = -time.timezone
else:
    tz_name = "Unknown"
    tz_offset = 0

print(f"Timezone: {tz_name}")
print(f"UTC offset: {tz_offset // 3600} hours")
print(f"DST active: {local.tm_isdst}")
print(f"timezone: {time.timezone}s, daylight: {time.daylight}s")
print(f"tzname: {time.tzname}")

print("=" * 5, "Practical examples", "=" * 5)

# Rate limiter: execute at most N operations per second
def rate_limit(min_interval=0.1):
    """Yield with minimum interval between calls."""
    last_call = [0.0]
    def wait():
        now = time.time()
        elapsed = now - last_call[0]
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)
        last_call[0] = time.time()
    return wait

limiter = rate_limit(0.05)
for i in range(3):
    limiter()
    print(f"  Call {i} at {time.time():.3f}")

# Countdown timer
def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        print(f"  {mins:02d}:{secs:02d}", end="\r", flush=True)
        time.sleep(0.01)  # shortened for demo
    print("  Done!           ")

print("Countdown (3s demo):")
countdown(3)

# Execution timer decorator
def timed(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"  {func.__name__} took {(end - start) * 1000:.3f}ms")
        return result
    return wrapper

@timed
def slow_function():
    return sum(i ** 2 for i in range(100000))

result = slow_function()

# Timestamp-based unique ID
def unique_id():
    ts = int(time.time() * 1e6)  # microsecond precision
    return f"ID-{ts}"

print(f"Unique ID: {unique_id()}")
time.sleep(0.001)
print(f"Unique ID: {unique_id()}")