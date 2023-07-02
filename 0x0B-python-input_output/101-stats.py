#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""

import sys

def compute_metrics():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for i, line in enumerate(sys.stdin, 1):
            ip, _, _, _, _, status_code, file_size = line.split()[0], line.split()[8], line.split()[11], line.split()[12], line.split()[13], line.split()[14], line.split()[15]
            total_size += int(file_size)
            if int(status_code) in status_codes:
                status_codes[int(status_code)] += 1

            if i % 10 == 0:
                print(f"Total file size: {total_size}")
                for status, count in sorted(status_codes.items()):
                    if count > 0:
                        print(f"{status}: {count}")

    except KeyboardInterrupt:
        print(f"Total file size: {total_size}")
        for status, count in sorted(status_codes.items()):
            if count > 0:
                print(f"{status}: {count}")

if __name__ == "__main__":
    compute_metrics()

