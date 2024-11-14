from datetime import datetime, timezone
import zoneinfo

# Example epoch timestamp
epoch_timestamp = 1609459200  # This represents 2021-01-01 00:00:00 UTC

# Convert epoch to datetime object in UTC
utc_time = datetime.fromtimestamp(epoch_timestamp, tz=timezone.utc)

# Define IST timezone
ist_timezone = zoneinfo.ZoneInfo('Asia/Kolkata')

# Convert UTC time to IST
ist_time = utc_time.astimezone(ist_timezone)

print("UTC Time:", utc_time)
print("IST Time:", ist_time)
