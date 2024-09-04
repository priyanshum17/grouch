# Partially copied from https://github.com/JIceberg/grouch/blob/main/src/tracker.py


from datetime import datetime


def get_term(season: str):
    now = datetime.now()
    if season.lower() == "spring":
        return f"{now.year + 1}" + "02" if now.month > 4 else f"{now.year}" + "02"
    else:
        return (
            f"{now.year}" + "05" if season.lower() == "summer" else f"{now.year}" + "08"
        )
