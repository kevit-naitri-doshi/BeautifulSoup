import requests
from bs4 import BeautifulSoup
import datetime

def scrape_data(sign:int,day:str):
    try:
        page=requests.get(f'https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={sign}&laDate={day}').text

        source=BeautifulSoup(page,'lxml')
        
        title=source.find('section',class_='banner').div.div.a.h1.text
        ans=source.find('div',class_='grid grid-right-sidebar primis-rr').div.p
        summary=ans.text
        day=ans.strong.text

    except Exception as e:
        title=None
        summary=None
        # day=datetime.date(day)
        day=day

    return title,summary,day

def main():

    signs={'aries':1,
           'taurus':2,
           'gemini':3,
           'cancer':4,
           'leo':5,
           'virgo':6,
           'libra':7,
           'scorpio':8,
           'sagittarius':9,
           'capricorn':10,
           'aquarius':11,
           'pisces':12}
    
    sign=input("Enter your Sun sign: ")
    inputday=input("Enter the date of the horoscope you require (in YYYYMMDD format): ")
    check_sign=signs.get(sign.lower(),None)
    if check_sign is None:
        print("Invalid sign")
    else:
        horoscope_title,horoscope_summary,horoscope_date=scrape_data(check_sign,inputday)
        
        print("---------------------------------------------")
        print()
        print(horoscope_date)
        print()
        print(horoscope_title)
        print()
        print(horoscope_summary)
        print()
        print("---------------------------------------------")

if __name__=="__main__":
    main()

