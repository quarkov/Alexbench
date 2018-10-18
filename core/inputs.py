def input_hostname():
    hs = input("enter a hostname or press 'enter' to use default google.com: ")
    hostname = hs if hs else "google.com"
    print("hostname is set as", hostname)
    print()
    return hostname


def input_params():
    dr = input("enter test duration in minutes (int) or press 'enter' to use default 1: ")
    fr = input("enter frequency in seconds (int) or press 'enter' to use default 10: ")
    duration, freq = (int(dr), int(fr)) if all((dr, fr)) else (1, 10)
    print("test duration is set as", duration, "minutes,", "frequency is set as", freq, "seconds")
    print()
    return duration, freq