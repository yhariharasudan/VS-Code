import calendar

# Create a plain text calendar for May 2024
year = 2024
month = 5
text_calendar = calendar.TextCalendar(calendar.SUNDAY)
print(text_calendar.formatmonth(year, month))