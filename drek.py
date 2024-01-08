# open readings.js and read all lines
with open('readings.js', 'r') as f:
    lines = f.readlines()

lines = lines[1:-1]
lines = [line.strip() for line in lines]

from datetime import datetime, timedelta
start = datetime(2022, 1, 1)
end = datetime(2022, 12, 31)
dates = [start + timedelta(days=i) for i in range((end - start).days + 1)]
dates_str = [f'biblija{date.strftime("%Y%m%d")}' for date in dates]
print("const readingsList = {")
for date_str,line in zip(dates_str, lines):
    print(f'    "{date_str}": {line}')
print("};")
