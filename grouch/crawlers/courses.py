import requests
import re

from bs4 import BeautifulSoup

from grouch.core.configuration import config

s = requests.Session()
timeout = 10
BASE_URL = config.link


class Course:
    def __init__(self, crn: str, term: str):
        self.crn = crn
        self.term = term
        self.name = self._fetch_course_name()

    def _fetch_page(self, url: str) -> BeautifulSoup:
        """Fetches and parses the page content."""
        with s.get(url, timeout=timeout) as response:
            response.raise_for_status()
            return BeautifulSoup(response.content, "html.parser")

    def _fetch_course_name(self) -> str:
        """Fetches the course name."""
        url = f"{self.BASE_URL}{self.term}&crn_in={self.crn}"

        soup = self._fetch_page(url)
        header = soup.find("th", class_="ddlabel")
        return header.get_text() if header else "Unknown"

    def _get_prereqs_text(self) -> str:
        """Fetches the raw prerequisites text from the course page."""
        url = f"{self.BASE_URL}{self.term}&crn_in={self.crn}"

        soup = self._fetch_page(url)
        prereq_section = soup.find("td", class_="dddefault")
        if prereq_section and "Prerequisites:" in prereq_section.get_text():
            return prereq_section.get_text()
        return ""

    def _clean_prereqs(self, raw_prereqs: str) -> str:
        """Cleans and formats the prerequisites text."""
        fodder_words = config.fodder_words
        prereqs = raw_prereqs.split()
        prereqs = filter(lambda word: word.lower() not in fodder_words, prereqs)
        prereqs = " ".join(prereqs)
        return re.sub(r"\s+", " ", prereqs).strip()

    def get_prereqs(self) -> str:
        """Returns cleaned and formatted prerequisites."""
        try:
            raw_prereqs = self._get_prereqs_text()
            if raw_prereqs:
                prereqs = self._clean_prereqs(raw_prereqs)
                return prereqs if prereqs else "None"
            return "None"
        except Exception as e:
            return "None"

    def _fetch_registration_table(self, term: str) -> list[int]:
        """Fetches registration information as a list of integers."""
        url = f"{self.BASE_URL}{term}&crn_in={self.crn}"
        soup = self._fetch_page(url)
        table = soup.find("caption", string="Registration Availability")
        if table:
            data = [
                int(td.get_text())
                for td in table.find_parent("table").find_all("td", class_="dddefault")
            ]
            if len(data) >= 6:
                return data
        raise ValueError("Unable to fetch registration information.")

    def get_registration_info(self, term: str) -> dict:
        """Returns a dictionary with detailed registration info."""
        self.term = term
        data = self._fetch_registration_table(term)

        registration_info = {
            "seats": data[0],
            "taken": data[1],
            "vacant": data[2],
            "waitlist": {
                "seats": data[3],
                "taken": data[4],
                "vacant": data[5],
            },
        }
        return registration_info

    def is_open_by_term(self, term: str) -> bool:
        """Checks if the course is open for the specified term."""
        return self._fetch_registration_table(term)[2] > 0

    def is_open(self) -> bool:
        """Checks if the course is open for the current term."""
        return self.is_open_by_term(self.term)

    def waitlist_available_by_term(self, term: str) -> bool:
        """Checks if the waitlist is available for the specified term."""
        waitlist = self.get_registration_info(term)["waitlist"]
        return waitlist["vacant"] > 0

    def waitlist_available(self) -> bool:
        """Checks if the waitlist is available for the current term."""
        return self.waitlist_available_by_term(self.term)

    def __str__(self) -> str:
        """Returns a formatted string representation of the course."""
        data = self.get_registration_info(self.term)
        result = f"{self.name}\n"
        for key, value in data.items():
            if key == "waitlist":
                continue
            result += f"{key.capitalize()}:\t{value}\n"
        result += f"Waitlist open: {'yes' if self.waitlist_available() else 'no'}\n"
        result += f"Prerequisites: {self.get_prereqs()}"
        return result
