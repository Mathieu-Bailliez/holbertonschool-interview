#!/usr/bin/python3
"""
Log parsing module.

Reads stdin line by line and computes metrics:
- total file size
- number of lines by status code
Statistics are printed every 10 lines and on keyboard interruption.
"""
import sys


def print_stats(total_size, status_counts):
    """
    Print the accumulated statistics.

    Args:
        total_size (int): sum of all file sizes read so far.
        status_counts (dict): number of lines per status code.
    """
    print("File size: {}".format(total_size))

    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """
    Read log lines from stdin and compute metrics.

    Prints statistics every 10 lines, at the end of input,
    and when a KeyboardInterrupt (CTRL + C) occurs.
    """
    total_size = 0

    status_counts = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }

    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            parts = line.split()
            try:
                total_size += int(parts[-1])
                status_code = parts[-2]
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except (ValueError, IndexError):
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    if line_count % 10 != 0:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
