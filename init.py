# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "requests",
# ]
# ///
#
# Advent of code working directories creator
# IMPORTANT Remember to edit the USER_SESSION_ID & author values with yours
# Author = Alexe Simon
# Date = 06/12/2018

import os
import sys

try:
    import requests
except ImportError:
    sys.exit(
        "You need requests module. This script should auto-install it with uv."
    )

# USER SPECIFIC PARAMETERS
# Folders will be created here
base_pos = "./"
# Get your session cookie from adventofcode.com
USER_SESSION_ID = "53616c7465645f5fe5e373b8d59d6bf234c1338ff34991234b90da925762340c9ce6700db511427a8af6d6ba20a245f9e4115d41ce155e16af213d4e74fd2292"  # noqa: E501
# Set to false to not download statements (only part 1 available)
DOWNLOAD_STATEMENTS = True
# Set to false to not download inputs
DOWNLOAD_INPUTS = True
# Set to false to not make code templates
MAKE_CODE_TEMPLATE = True
# Set to false to not create URL shortcuts
MAKE_URL = True
# Name automatically put in the code templates
author = "Mouly Taha"
# Set to true to re-download everything (be gentle with AoC servers!)
OVERWRITE = False

# DATE SPECIFIC PARAMETERS
# Date automatically put in the code templates
date = "December 2025"
# You can go as early as 2015
starting_advent_of_code_year = 2025
# Download all data up until this year
last_advent_of_code_year = 2025
# For unfinished years, download days up until this day
last_advent_of_code_day = 12

# Code
MAX_RECONNECT_ATTEMPT = 2
years = range(starting_advent_of_code_year, last_advent_of_code_year + 1)
days = range(1, 26)
link = "https://adventofcode.com/"  # ex use : https://adventofcode.com/2017/day/19/input
USER_AGENT = "adventofcode_working_directories_creator"

print(
    "Setup will download data and create working directories "
    "and files for adventofcode."
)
if not os.path.exists(base_pos):
    os.mkdir(base_pos)
for y in years:
    print("Year " + str(y))
    if not os.path.exists(base_pos + str(y)):
        os.mkdir(base_pos + str(y))
    year_pos = base_pos + str(y)
    for d in (
        d
        for d in days
        if (y < last_advent_of_code_year or d <= last_advent_of_code_day)
    ):
        print("    Day " + str(d))
        if not os.path.exists(year_pos + "/" + str(d)):
            os.mkdir(year_pos + "/" + str(d))
        day_pos = year_pos + "/" + str(d)
        if MAKE_CODE_TEMPLATE and not os.path.exists(
            day_pos + "/advent_code.py"
        ):
            with open(
                day_pos + "/advent_code.py", "w+", encoding="utf-8"
            ) as code:
                code_content = (
                    f"# Advent of code Year {y} Day {d} solution\n"
                    f"# Author = {author}\n"
                    f"# Date = {date}\n\n"
                    "from pathlib import Path\n\n"
                    'input_file_path = Path(__file__).parent / "input.txt"\n'
                    'with open(input_file_path, encoding="utf-8") '
                    "as input_file:\n"
                    "    input_data = input_file.read()\n\n\n"
                    'print("Part One :", str(None))\n\n'
                    'print("Part Two :", str(None))\n'
                )
                code.write(code_content)
        if (
            DOWNLOAD_INPUTS
            and (not os.path.exists(day_pos + "/input.txt") or OVERWRITE)
            and USER_SESSION_ID != ""
        ):
            done = False
            error_count = 0
            while not done:
                try:
                    with requests.get(
                        url=link + str(y) + "/day/" + str(d) + "/input",
                        cookies={"session": USER_SESSION_ID},
                        headers={"User-Agent": USER_AGENT},
                    ) as response:
                        if response.ok:
                            data = response.text
                            with open(
                                day_pos + "/input.txt", "w+", encoding="utf-8"
                            ) as input_file:
                                input_file.write(data.rstrip("\n"))
                        else:
                            print(
                                "        Server response for input "
                                "is not valid."
                            )
                    done = True
                except requests.exceptions.RequestException:
                    error_count += 1
                    if error_count > MAX_RECONNECT_ATTEMPT:
                        print("        Giving up.")
                        done = True
                    elif error_count == 0:
                        print(
                            "        Error while requesting input from server. "
                            "Request probably timed out. Trying again."
                        )
                    else:
                        print("        Trying again.")
                except Exception as e:
                    print(
                        "        Non handled error while requesting input "
                        f"from server. {e}"
                    )
                    done = True
        if DOWNLOAD_STATEMENTS and (
            not os.path.exists(day_pos + "/statement.html") or OVERWRITE
        ):
            done = False
            error_count = 0
            while not done:
                try:
                    with requests.get(
                        url=link + str(y) + "/day/" + str(d),
                        cookies={"session": USER_SESSION_ID},
                        headers={"User-Agent": USER_AGENT},
                    ) as response:
                        if response.ok:
                            html = response.text
                            start = html.find("<article")
                            end = html.rfind("</article>") + len("</article>")
                            end_success = html.rfind("</code>") + len("</code>")
                            with open(
                                day_pos + "/statement.html",
                                "w+",
                                encoding="utf-8",
                            ) as statement:
                                statement.write(
                                    html[start : max(end, end_success)]
                                )
                        done = True
                except requests.exceptions.RequestException:
                    error_count += 1
                    if error_count > MAX_RECONNECT_ATTEMPT:
                        print(
                            "        Error while requesting statement "
                            "from server. "
                            "Request probably timed out. Giving up."
                        )
                        done = True
                    else:
                        print(
                            "        Error while requesting statement "
                            "from server. "
                            "Request probably timed out. Trying again."
                        )
                except Exception as e:
                    print(
                        "        Non handled error while requesting statement "
                        f"from server. {e}"
                    )
                    done = True
        if MAKE_URL and (
            not os.path.exists(day_pos + "/link.url") or OVERWRITE
        ):
            with open(day_pos + "/link.url", "w+", encoding="utf-8") as url:
                url.write(f"[InternetShortcut]\nURL={link}{y}/day/{d}\n")
print(
    "Setup complete : adventofcode working directories and files "
    "initialized with success."
)
