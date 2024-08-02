import datetime
import os
import subprocess
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

def verify_template():
    with open(FILE, "r") as file:
        line = file.readline()
        if not line.startswith("Year"):
            return 1
        year = line.split("Year: ")[1].strip()
        if not year.isdigit():
            return 1
        for line in file:
            if line.startswith("Year"):
                continue
            for pixel in line:
                if pixel != "\n" and pixel != " " and not pixel.isdigit():
                    return 2
                if pixel.isdigit() and (int(pixel) < 0 or int(pixel) > 4):
                    return 2
    return 0



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
    invalid = False
    with open(FILE, "r") as file:
        for line in file:
            if line.startswith("Year"):
                print(line)
                continue
            for pixel in line:
                if pixel == "\n" or pixel == " ":
                    print("  ", end="")
                else:
                    if int(pixel) < 0 or int(pixel) > 4:
                        print("██", end="")
                        invalid = True
                    else:
                        print_colored_text_hex(shades_of_green[int(pixel)],"██")
            print()
    if invalid:
        print(errorVisualize)

def commit(date, message):
    command = ["git", "commit", "--allow-empty", "-m", message, "--date", date]
    result = subprocess.run(command)
    return result.returncode != 0

def commitTemplate():
    with open(FILE, "r") as file:
        year = 0
        linesStarts = [0]
        for line in file:
            if (line.startswith("Year")):
                year = int(line.split("Year: ")[1].strip())
            linesStarts.append(len(line) + linesStarts[-1])

    date = datetime.date(year, 1, 1)

    with open(FILE, "r") as file:
        line = 1
        column = 0
        for i in range(0, 366):
            file.seek(linesStarts[line]+column)
            char = file.read(1)

            if char.isdigit():
                date_str = date.strftime("%Y-%m-%dT%H:%M:%SZ")
                char = int(char)
                if char < 0 or char > 4:
                    print(errorPixelValue.format(line, column+1))
                    return 1
                for j in range(char):
                    if commit(date_str, f'commit n°{j+1} for the {date_str}') :
                        return 1
                date += datetime.timedelta(days=1)

            line += 1
            if line == 8:
                line = 1
                column += 1

def main(params):
    if len(params) < 2:
        print(errorAction)
        return 1

    if params[1] == "template":
        if len(params) != 3:
            print(errorAction)
            return 1
        year = int(params[2])
        if generate_template(year) :
            return 1
        print(generationSuccess.format(year, os.path.abspath(FILE)))
        return 0
    elif params[1] == "commit":
        if verify_template() :
            print(errorTemplate)
            return 1
        return commitTemplate()
    elif params[1] == "visualize":
        if verify_template() == 1:
            print(errorTemplate)
            return 1
        return visualize_template()
    else:
        print(errorAction)
        return 1