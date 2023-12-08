from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import csv
import pandas as pd


def browns_jersey():
    Browns_URL = "https://www.nflshop.com/cleveland-browns/mens-cleveland-browns-joe-flacco-nike-brown-game-player-jersey/t-14711349+p-354401779178181+z-9-38487849?_ref=p-SRP:m-GRID:i-r0c0:po-0"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }

    browns_page = requests.get(Browns_URL, headers=headers)

    browns1 = BeautifulSoup(browns_page.content, "html.parser")  # get content

    browns2 = BeautifulSoup(browns1.prettify(), "html.parser")  # clean up content
    product = browns2.find("h1").get_text().strip()

    price = browns2.find("span", class_="sr-only").get_text().strip()[1:]
    browns_name = "Cleveland Browns"
    today = datetime.date.today()

    
    browns_data = [browns_name, product, price, today]

    return browns_data


def ravens_jersey():
    Ravens_URL = "https://www.nflshop.com/baltimore-ravens/mens-baltimore-ravens-lamar-jackson-nike-purple-game-jersey/t-14372444+p-5831540296203+z-9-818208977?_ref=p-SRP:m-GRID:i-r0c1:po-1"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }

    ravens_page = requests.get(Ravens_URL, headers=headers)

    ravens1 = BeautifulSoup(ravens_page.content, "html.parser")  # get content

    ravens2 = BeautifulSoup(ravens1.prettify(), "html.parser")  # clean up content
    product = ravens2.find("h1").get_text().strip()

    price = ravens2.find("span", class_="sr-only").get_text().strip()[1:]
    ravens_name = "Baltimore Ravens"
    today = datetime.date.today()

    ravens_data = [ravens_name, product, price, today]
    return ravens_data


def steelers_jersey():
    Steelers_URL = "https://www.nflshop.com/pittsburgh-steelers/mens-pittsburgh-steelers-kenny-pickett-nike-black-player-game-jersey/t-36714861+p-1564842060846+z-9-2152273005?_ref=p-SRP:m-GRID:i-r0c0:po-0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }

    steelers_page = requests.get(Steelers_URL, headers=headers)

    steelers1 = BeautifulSoup(steelers_page.content, "html.parser")  # get content

    steelers2 = BeautifulSoup(steelers1.prettify(), "html.parser")  # clean up content
    product = steelers2.find("h1").get_text().strip()

    price = steelers2.find("span", class_="sr-only").get_text().strip()[1:]
    steelers_name = "Pittsburgh Steelers"
    today = datetime.date.today()

    steelers_data = [steelers_name, product, price, today]
    return steelers_data


def bengals_jersey():
    Bengals_URL = "https://www.nflshop.com/cincinnati-bengals/mens-cincinnati-bengals-joe-burrow-nike-black-player-game-jersey/t-14153548+p-3768878132291+z-9-1926936844?_ref=p-SRP:m-GRID:i-r0c0:po-0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }

    bengals_page = requests.get(Bengals_URL, headers=headers)

    bengals1 = BeautifulSoup(bengals_page.content, "html.parser")  # get content

    bengals2 = BeautifulSoup(bengals1.prettify(), "html.parser")  # clean up content
    product = bengals2.find("h1").get_text().strip()

    price = bengals2.find("span", class_="sr-only").get_text().strip()[1:]
    bengals_name = "Cincinnati Bengals "
    today = datetime.date.today()

    bengals_data = [bengals_name, product, price, today]
    return bengals_data


def afc_north_records():
    URL = "https://www.nfl.com/standings/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")  # get content

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")  # clean up content
    table = soup2.find_all("table")[1]
    table_headers = table.find_all("th")

    table_headers = [title.text.strip() for title in table_headers]
    df = pd.DataFrame(columns=table_headers)

    table_rows = table.find_all("tr")
    for row in table_rows[1:]:
        row_data = row.find_all("td")
        individual_data = [data.text.strip() for data in row_data]
        length = len(df)
        df.loc[length] = individual_data
    df = df.rename(columns={"AFC NORTH": "Team Name"})

    df["Team Name"] = df["Team Name"].str.split(n=2).str[:2].str.join(" ")
    df = df.drop(df.columns[[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], axis=1)
    return df


def check_price():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }

    header = ["Team Name", "Product", "Price", "Date"]
    ravens_data = ravens_jersey()
    steelers_data = steelers_jersey()
    browns_data = browns_jersey()
    bengals_data = bengals_jersey()

    with open("jersey-scraper.csv", "w", newline="", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(ravens_data)
        writer.writerow(steelers_data)
        writer.writerow(browns_data)
        writer.writerow(bengals_data)

    df = pd.read_csv("/home/djfox232/amazon-web-scraping/jersey-scraper.csv")
    df2 = afc_north_records()

    df3 = pd.merge(df, df2, left_on="Team Name", right_on="Team Name")
    print(df3)
    df3["Date"] = pd.to_datetime(df3["Date"])
    df3.to_csv(r"test.csv", index=False)
    with open("jersey-scraper.csv", "a+", newline="", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(ravens_data)
        writer.writerow(steelers_data)
        writer.writerow(browns_data)
        writer.writerow(bengals_data)
    df = pd.read_csv("/home/djfox232/amazon-web-scraping/jersey-scraper.csv")
    df3 = pd.merge(df, df2, left_on="Team Name", right_on="Team Name")
    df3.to_csv(r"merge_table.csv", index=False)


while True:
    check_price()
    time.sleep(604800)