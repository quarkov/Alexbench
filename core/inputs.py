from os import name, popen


def input_hostname():
    hs = input("enter a hostname or press 'enter' to use default google.com: ")
    hostname = hs if hs else "google.com"
    if hostname.isdecimal():
        print("incorrect hostname, try again")
        return input_hostname()

    response = [line.split() for line in popen("ping -n 1 " + hostname)] if name == "nt" else\
        [line.split() for line in popen("ping -c 1 -q " + hostname)]
    ip = 0
    for chunk in response:
        for piece in chunk:
            if piece.count(".") == 3:
                ip = piece
                break
        if ip:
            break

    if ip:
        print("hostname is set as", hostname)
        print()
        return hostname
    else:
        print("incorrect hostname, try again")
        print()
        return input_hostname()


def digit_input(min_value, default):
    digit = input()
    if not digit:
        return default
    if not digit.isdecimal():
        print("an integer number is expected, try again")
        return digit_input(min_value, default)
    if int(digit) < min_value:
        print("an integer >=", min_value, "is expected, try again")
        return digit_input(min_value,default)
    return int(digit)

def input_params():
    print("enter test duration in minutes (int >= 1) or press 'enter' to use default 1 minute:")
    duration = digit_input(1, 1)
    print("enter measurement frequency in seconds (int >= 2) or press 'enter' to use default 2 seconds:")
    frequency = digit_input(2, 2)
    print("ok, parameters are set; duration =", duration, "min, frequency =", frequency, "secs.")
    return duration, frequency
