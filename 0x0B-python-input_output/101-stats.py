#!/usr/bin/python3
import sys

def print_metrics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(status_code, count))

def parse_line(line):
    try:
        elements = line.split()
        status_code = int(elements[-2])
        file_size = int(elements[-1])
        return status_code, file_size
    except (IndexError, ValueError):
        return None, 0

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = parse_line(line)
            if status_code is not None:
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        pass

    print_metrics(total_size, status_codes)

if __name__ == "__main__":
    main()
