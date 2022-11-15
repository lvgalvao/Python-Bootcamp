from bs4 import BeautifulSoup


def main():
    with open("days/day-45/website.html") as file:
        contents = file.read()

        soup = BeautifulSoup(contents, "html.parser")

        # list of tags (try a and p)
        all_anchor_tags = soup.find_all(name="a")

        return print(all_anchor_tags)


if __name__ == "__main__":
    main()
