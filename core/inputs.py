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
        except socket.error:
            print("incorrect hostname, try again")
    print("hostname is set by default:", default)
    return default


def digit_input(min_value, default):
    for attempt in range(3):
        d = input()
        digit = d if d else default
        try:
            if int(digit) >= min_value:
                return int(digit)
            else:
                print("an integer >=", min_value, "is expected, try again")
        except ValueError:
            print("it's not an integer, try again")
    print("value is set by default:", default)
    return default


def input_params():
    print("enter test duration in minutes (int >= 1) or press 'enter' to use default 1 minute:")
    duration = digit_input(1, 1)
    print("enter measurement frequency in seconds (int >= 2) or press 'enter' to use default 2 seconds:")
    frequency = digit_input(2, 2)
    print("ok, parameters are set; duration =", duration, "min, frequency =", frequency, "sec.")
    return duration, frequency
