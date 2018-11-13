import socket


def input_hostname():
    default = "gdansk.pl"
    for attempt in range(3):
        hs = input("enter a hostname or press 'enter' to use default " + default + ": ")
        hostname = hs if hs else default
        try:
            socket.gethostbyname(hostname)
            print("hostname is set as", hostname)
            print()
            return hostname
        except (socket.error, UnicodeError):
            print("incorrect hostname, try again")
    print("hostname is set by default:", default)
    return default


def digit_input(min_value, max_value, default):
    for attempt in range(3):
        d = input()
        digit = d if d else default
        try:
            if max_value >= int(digit) >= min_value:
                return int(digit)
            else:
                print(max_value, ">= an integer >=", min_value, "is expected, try again")
        except ValueError:
            print("it's not an integer, try again")
    print("value is set by default:", default)
    return default


def input_params():
    print("enter test duration in minutes (1440 >= int >= 1) or press 'enter' to use default 1 minute:")
    duration = digit_input(1, 1440, 1)
    print("enter measurement interval in seconds (",duration*60, ">= int >= 2) or press 'enter' to use default 5 seconds:")
    interval = digit_input(2, duration*60, 5)
    print("ok, parameters are set; duration =", duration, "min, interval =", interval, "sec.")
    return duration, interval
