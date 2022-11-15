from bs4 import BeautifulSoup


class BS(BeautifulSoup):
    def extract_data_from_report3(filename):
        html_report_part1 = open(filename, "r")
        soup = BeautifulSoup(html_report_part1, "html.parser")
        return soup
