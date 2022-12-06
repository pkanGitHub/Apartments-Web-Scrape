from colorama import init, Fore, Style
from apartmentspider import ApartmentSpider
from scrapy.crawler import CrawlerProcess
import os

def read_json_file():
    check_file = os.stat("apartment.json").st_size
    if check_file == 0:
        return True
    return False

def check_input_is_empty(input):
    if len(input.strip()) == 0:
        return True
    return False

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
    input_check = check_input_is_empty(city)
    if input_check:
        print(f"{Fore.RED}You must enter a city, try again!")
        return get_city()
    elif word > 1: 
        print(f"\n{Fore.RED}ONLY ONE WORD city name is allowed at this time, please try again")
        return get_city()
    return city

def get_state():
    with open("states.txt") as file:
        lines = file.readlines()
        states = []
    for line in lines:
        states.append(line.replace("\n", ""))

    state = input("\nEnter the state in (2)LETTER format, (e.g MO): ").upper()
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
    # reset colorama for new lines
    init(autoreset=True)
    location = get_location()
    # run spider(s) and save the data into a file
    run_spider(ApartmentSpider, location)

    # check if json file is empty
    check_empty_file = read_json_file()
    if check_empty_file:
        loc = location.replace("-", " ")
        print(f"\n\n\n{Fore.RED}Uh-oh!! There is NO data from {loc}.")
    else:
        print("\nYour results are saved in 'apartment.json' file")

main()