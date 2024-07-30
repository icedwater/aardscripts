#! /usr/bin/env python

"""
Estimate next million-mob double from the mobdeaths file.

File format:
dd/mm/yy hh:mm:ss +08 Mob Deaths : since_reboot, since_launch

First attempt: difference of last two lines
"""
mobdfile = "mobdeaths.txt"

def load_tail(mobdfile: str, tail: int=2) -> list[str]:
    """
    Return the last few lines of a file.
    :param mobdfile:    string containing path to the file
    :param tail:        number of lines to display
    :return lines:      list of lines from the file
    """
    data = []

    with open(mobdfile, 'r') as mdf:
        data = mdf.readlines()

    lines = [line.strip() for line in data[-tail:]]

    return lines

def parse_mobs(line: str) -> dict:
    """
    Construct an object from a given line in mobdeaths file.
    :param line:        the line in question
    :return mobdeaths:  the data as a dictionary.
    """
    date, time, zone, _, _, _, _, start = line.split(' ')
    day, month, year = [int(d) for d in date.split('/')]
    hour, minute, second = [int(t) for t in time.split(':')]
    # since_reboot = int(reboot)
    since_start = int(start.replace(',',''))

    mobdeaths = {}
    mobdeaths["min"] = (365.25 * 24 * 60) * year + (30 * 24 * 60) * month + (24 * 60) * day + 60 * hour + minute
    mobdeaths["mobs"] = since_start

    return mobdeaths


def guess_minutes(lines: list) -> int:
    """
    From a provided list of mobdeaths lines, guess time to hourdub in minutes.
    :param lines:       the list of lines
    :return kill_rate:  the estimated mob kills per minute
    :return minutes:    the estimated number of minutes
    """
    start_line = parse_mobs(lines[0])
    end_line = parse_mobs(lines[-1])

    mob_diff = end_line.get("mobs") - start_line.get("mobs")
    time_diff = end_line.get("min") - start_line.get("min")
    kill_rate = round(mob_diff / time_diff)

    mob_gap = (1_000_000 - (end_line.get("mobs") % 1_000_000))
    minutes = round(mob_gap / kill_rate)

    return (kill_rate, minutes)



def main():
    mobd = load_tail(mobdfile=mobdfile, tail=4)
    (rate, dubmin) = guess_minutes(mobd)
    print(f"### At {rate} mobs per minute, hour of double in approximately {round(dubmin/60)} hours and {dubmin%60} minutes. ###")

if __name__ == "__main__":
    main()


