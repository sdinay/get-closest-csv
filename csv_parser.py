import math
import csv


def distance(lat1, lng1, lat2, lng2):
  manhattan = abs(lat1 - lat2) + abs(lng1 - lng2)
  return manhattan

def get_closest(csv_text, lat, lng):
    min_distance = 999
    location = ""

    reader = csv.reader(csv_text, delimiter=',', quotechar='"', skipinitialspace=True)
    for row in reader:

        if not row:
            continue
        this_distance = distance(int(lat), int(lng), int(row[1]), int(row[2]))

        if location == "":
            location = row[0]
            min_distance = this_distance

        if this_distance < min_distance:
            location = row[0]
            min_distance = this_distance

    return location
