import datetime
import sys
from script.text import *
from script.utils import *

FILE = "pixelArt.txt"

shades_of_green = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353",
]


#git commit -m "add commit" --date="2005-01-01T00:12:00Z"

def generate_template(year):
    first_day = datetime.date(year, 1, 1)
    first_weekday = (first_day.weekday()+1)%7
    number_of_days = 364

    if(year%4 == 0) :
        remaining_days = [(datetime.date(year, 12, 31).weekday()+1)%7, (datetime.date(year, 12, 30).weekday()+1)%7]
    else :
        remaining_days = [(datetime.date(year, 12, 31).weekday()+1)%7]

    with open(FILE, "w") as file:
        file.write("Year: {}\n".format(year))
        for i in range(7):
            if i < first_weekday:
                file.write(" ")
            for j in range(1, int(number_of_days/7)):
                file.write("0")
            if i in remaining_days:
                file.write("0")
            file.write("\n")

def visualize_template():
    with open(FILE, "r") as file:
        for line in file:
            if line.startswith("Year"):
                print(line)
                continue
            for pixel in line:
                if pixel == "\n" or pixel == " ":
                    print("  ", end="")
                else:
                    print_text_with_hex_color(shades_of_green[int(pixel)],"██")
            print()

def main(params):
    if len(params) != 2:
        print(errorAction)
        sys.exit(1)

    if params[1] == "generate":
        if len(params) != 3:
            print(errorAction)
            sys.exit(1)
        year = int(params[2])
        generate_template(year)
        print(generationSuccess.format(year, FILE))
    elif params[1] == "commit":
        print("Commit")
    elif params[1] == "visualize":
        visualize_template()
    else:
        print(errorAction)
        sys.exit(1)