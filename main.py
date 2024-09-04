import time, sys

from datetime import datetime

from notifiers import load_notifiers, notify

print("Starting...")

notifiers = load_notifiers()

print("Loaded all notifiers\n")

while True:
    try:
        for n in notifiers:
            prev_spots = n.spots
            prev_wl_spots = n.wl_spots
            n.fetch_info()

            if n.spots > 0 and not prev_spots > 0:
                contents = [
                    "The following course is now open to register:",
                    f"Name: {n.course.name}",
                    f"CRN: {n.course.crn}",
                    f"Spots open: {n.spots}",
                ]
                notify(n, contents)
            elif not n.spots > 0 and prev_spots > 0:
                contents = [
                    "The following course is now closed to register:",
                    f"Name: {n.course.name}",
                    f"CRN: {n.course.crn}",
                ]
                notify(n, contents)
            elif n.wl_spots > 0 and not prev_wl_spots > 0:
                contents = [
                    "The following course is now open to waitlist:",
                    f"Name: {n.course.name}",
                    f"CRN: {n.course.crn}",
                    f"Waitlist spots open: {n.wl_spots}",
                ]
                notify(n, contents)
            elif not n.wl_spots > 0 and prev_wl_spots > 0:
                contents = [
                    "The following course is now closed to waitlist:",
                    f"Name: {n.course.name}",
                    f"CRN: {n.course.crn}",
                ]
                notify(n, contents)

        now = datetime.now()
        sys.stdout.write(f'Last time checked: {now.strftime("%I:%M:%S%p")}\r')
    except Exception as ex:
        now = datetime.now()
        print(f'[{now.strftime("%I:%M:%S%p")}] {ex}')

    time.sleep(0.5)
