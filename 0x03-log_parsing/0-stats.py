#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys
import re


def print_stats(total_size, status_counts):
    """Print the current statistics"""
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))


def parse_log_line(line):
    """
    Parse a log line and extract status code and file size
    Returns (status_code, file_size) or (None, None) if invalid format
    """
    # Expected format: <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status> <size>
    pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    match = re.match(pattern, line.strip())
    
    if match:
        try:
            status_code = int(match.group(3))
            file_size = int(match.group(4))
            return status_code, file_size
        except ValueError:
            return None, None
    return None, None


def main():
    """Main function to process log lines"""
    total_size = 0
    status_counts = {}
    valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
    line_count = 0
    
    try:
        for line in sys.stdin:
            status_code, file_size = parse_log_line(line)
            
            if status_code is not None and file_size is not None:
                # Add to total file size
                total_size += file_size
                
                # Count status codes (only valid ones)
                if status_code in valid_status_codes:
                    status_counts[status_code] = status_counts.get(status_code, 0) + 1
            
            line_count += 1
            
            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
                
    except KeyboardInterrupt:
        # Print final stats on keyboard interruption
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
