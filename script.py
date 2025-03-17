from datetime import datetime
import time

def to_unix_time(date_string, format="%Y-%m-%d %H:%M:%S"):
    """Convert a given date string to Unix timestamp."""
    dt = datetime.strptime(date_string, format)
    return int(time.mktime(dt.timetuple()))

def from_unix_time(unix_timestamp, format="%Y-%m-%d %H:%M:%S"):
    """Convert a Unix timestamp to a human-readable date string."""
    dt = datetime.fromtimestamp(unix_timestamp)
    return dt.strftime(format)

def main():
    choice = input("Enter '1' to convert to Unix time, '2' to convert from Unix time: ")
    if choice == '1':
        date_string = input("Enter date (YYYY-MM-DD HH:MM:SS): ")
        print(f"Unix time: {to_unix_time(date_string)}")
    elif choice == '2':
        unix_timestamp = int(input("Enter Unix timestamp: "))
        print(f"Converted date: {from_unix_time(unix_timestamp)}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
