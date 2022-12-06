from colorama import init, Fore, Style
from apartmentspider import ApartmentSpider
from scrapy.crawler import CrawlerProcess

def run_spider(spider, location):
    process = CrawlerProcess(settings=
    {
        "FEEDS" : {
            'apartment.json': {'format': 'json', 'overwrite': True}
        },
    })
    process.crawl(spider, start_urls=[f"https://www.apartments.com/{location}"])
    process.start()

def get_city():
    city = input("\nWhich city would you like to look up? (e.g Columbia): ").upper()
    word = len(city.split())
    if word > 1: 
        print(f"\n{Fore.RED}ONLY ONE WORD city name is allowed at this time, please try again")
        return get_city()
    return city

def get_state():
    with open("states.txt") as file:
        lines = file.readlines()
        states = []
    for line in lines:
        states.append(line.replace("\n", ""))

    state = input("\nEnter the state in (2)LETTER format, (e.g MO):").upper()
    if state not in states:
        print(f"{Fore.RED}The state does not exist, try again")
        return get_state()
    return state

def get_location():
    print(f"\n{Fore.BLUE}*** Welcome to the Apartments Lookup App! ***")
    display_note()
    print("\nPlease only enter 'ONE' word for the following user prompts: ")
    city = get_city()
    state = get_state()
    return f"{city}-{state}"

def display_note():
    print(f"{Fore.BLUE}*\n* After COMPLETE the user prompts\n*")
    print(f"{Fore.BLUE}* The results will be saved onto 'apartment.json' file\n*")
    print(f"{Fore.BLUE}* {Fore.RED}NOT ALL APARTMENTS HAVE RESULTS FOR PRICING AND BEDS")
    print(f"{Fore.BLUE}* {Fore.RED}due to the 'selectors' used in the site is inconsistent")
    print(f"{Fore.BLUE}*\n* One of best results: Columbia MO, Buffalo NY... etc\n*")
    print(f"{Fore.BLUE}* ********************************************")


def main():
    init(autoreset=True)
    #run the web scrape and save the data into a file
    location = get_location()
    run_spider(ApartmentSpider, location)
    print("\nYour results are saved in 'apartment.json' file")

main()