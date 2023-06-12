import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com/wfootball/schedule/index?year=2023&month=05&category=epl"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 일정 정보가 있는 태그와 클래스를 확인하고 추출
schedule_table = soup.find("div", {"class": "schedule_month"})
dates = schedule_table.find_all("strong", {"class": "td_date"})
matches = schedule_table.find_all("ul", {"class": "list_play"})

# 날짜와 해당 날짜의 경기 일정을 출력
for date, match in zip(dates, matches):
    print(date.text.strip())
    for item in match.find_all("div", {"class": "vs"}):
        time = item.find("span", {"class": "time"}).text.strip()
        team1 = item.find("span", {"class": "team_lft"}).text.strip()
        team2 = item.find("span", {"class": "team_rgt"}).text.strip()
        print(f"{time} | {team1} vs {team2}")
    print()


