#!/usr/bin/python3
import sys

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
valid_codes = set(status_codes.keys())
line_count = 0

def print_stats():
    """ Function to print the accumulated statistics """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

try:
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            if len(parts) < 7:
                continue

            # Extracting file size and status code
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update total file size
            total_size += file_size

            # Update the count of the status code if it's valid
            if status_code in valid_codes:
                status_codes[status_code] += 1

        except (ValueError, IndexError):
            continue

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print final stats when interrupted by CTRL + C
    print_stats()
    raise

