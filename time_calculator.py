def add_time(start, duration, day=None):
  days =["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

  # calculate seconds on start+duration
  sec = convert_12_to_sec(start)
  sec = sec + convert_dur_to_sec(duration)

  # get time and days
  r = convert_sec_to_12(sec)

  # format output
  day_part = ""
  if r[1]==1:
    day_part = " (next day)"
  elif r[1]>1:
    day_part = " (" + str(r[1]) + " days later)"

  week_day_part = ""
  day_index = get_day_index(day, days)
  if day_index is not None:
    i = (day_index + r[1]) % 7
    week_day_part = ", " + days[i].capitalize()

  new_time = r[0] + week_day_part + day_part
  return new_time

def get_day_index(day, days):
 
  if day is not None:
    day = day.lower()
    for i in range(len(days)):
      if days[i]==day:
        di = i
        break
    return di
  return None

def convert_dur_to_sec(dur):
  
  p = dur.split(':')
  return int(p[0])*60*60 + int(p[1])*60

def convert_12_to_sec(time):

  p1 = time.split(':')
  p2 = p1[1].split(' ')
  if p2[1]=='PM':
    if p1[0] != '12':
      p1[0] = int(p1[0]) + 12
  elif p1[0]=='12': # am
    p1[0] = '00'
  sec = int(p1[0])*60*60
  sec = sec + int(p2[0])*60
  return sec

# sec: 60 
def convert_sec_to_12(sec):

  mode = 'AM'
  h_total = int(sec / 3600)
  rem = sec % 3600
  m = int(rem / 60)
  d = int(h_total / 24)
  h24 = h_total % 24
  h12 = h24
  if h24 >= 12:
    mode = "PM"
    if h24 > 12:
      h12 = h24 - 12 # 13:00 > 01:00 PM
  elif h24==0:
    h12 = h24 + 12 # 00:00 > 12:00 AM
  time = str(int(h12)) + ":" + add_zero(m) + " " + mode
  return [time, int(d)]
  
def add_zero(num):

  z = str(int(num))
  if len(z) == 1:
    z = '0' +  z
  return z