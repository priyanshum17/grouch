from datetime import datetime


def get_term(season: str) -> str:
    """
    Returns the term code based on the specified season and the current date.

    Term codes follow the format: YYYYMM, where:
    - YYYY is the year.
    - MM is the month code corresponding to the term:
      - "02" for Spring
      - "05" for Summer
      - "08" for Fall

    The logic is as follows:
    - If the current month is after April, Spring corresponds to the next year.
    - Otherwise, Spring corresponds to the current year.
    - Summer and Fall always correspond to the current year.

    Args:
        season (str): The season for which to generate the term code. Valid values are "spring", "summer", and "fall".

    Returns:
        str: The term code as a string in the format YYYYMM.

    Raises:
        ValueError: If the provided season is not "spring", "summer", or "fall".
    """
    now = datetime.now()
    season = season.lower()

    if season == "spring":
        term_year = now.year + 1 if now.month > 4 else now.year
        term_code = f"{term_year}02"
    elif season == "summer":
        term_code = f"{now.year}05"
    elif season == "fall":
        term_code = f"{now.year}08"
    else:
        raise ValueError(
            "Invalid season. Valid options are 'spring', 'summer', and 'fall'."
        )

    return term_code
