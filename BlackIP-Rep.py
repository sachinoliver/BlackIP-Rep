import re, csv, glob, sys
import asyncio, os
import pycountry_convert as pc
from collections import defaultdict
from rich import print
from rich.table import Column, Table
from selenium import webdriver
from pyppeteer import launch
from selenium.webdriver.firefox.options import Options
from time import sleep
from bs4 import BeautifulSoup


def Banner():
    print("""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗██╗██████╗       ██████╗ ███████╗██████╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██║██╔══██╗      ██╔══██╗██╔════╝██╔══██╗
██████╔╝██║     ███████║██║     █████╔╝ ██║██████╔╝█████╗██████╔╝█████╗  ██████╔╝
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██║██╔═══╝ ╚════╝██╔══██╗██╔══╝  ██╔═══╝
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗██║██║           ██║  ██║███████╗██║
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝           ╚═╝  ╚═╝╚══════╝╚═╝
                                                                                 """)


def arguments():
    parser = argparse.ArgumentParser(usage="python3 "+sys.argv[0]+" file_contains_ip_list.txt")
    parser.add_argument("file",help="A file containing ip address should be provided")
    parser.add_argument("-vt", '--virustotal' ,help="Screenshot from Virus Total")
    # parser.add_argument("-v", "--verbosity", type=int,
    #                     help="increase output verbosity",default=0)
    args = parser.parse_args()
    t = "test"
    return args.file, t

def directorys():
    try:
        os.makedirs('BlackIP-Rep/screenshots')
    except FileExistsError:
        pass

async def spam():
    print("[+] Starting...")
    file, t = arguments()
    with open(file, 'r') as f:
        lines = f.readlines()
    browser = await launch(options={'args': ['--no-sandbox']}, headless=True)
    page = await browser.newPage()
    await page.goto("https://www.bulkblacklist.com/")
    await page.waitForSelector("[name=ips]")
    await page.click("[name=ips]")
    for line in lines:
        await page.keyboard.type(line.strip())
        await page.keyboard.press("Enter")
    sleep(4)
    await page.click('input[type="submit"]')
    await page.waitForSelector("table.table-hover",visible=True)
    sleep(6)
    await page.pdf({'path':'./BlackIP-Rep/BulkBlacklist.pdf'})
    content=await page.content()
    soup =BeautifulSoup(content, "html.parser")
    s = soup.select("td > a")
    list1 = [n for n in s]
    for i in range(len(list1)):
        l = str(list1[i])
        if "r.png" in l:
            ip = re.findall(r'[0-9]+(?:.[0-9]+){3}', l )
            ip = ip[0]
            with open('unsorted.txt', 'a') as f:
                f.write('%s\n' %ip)
            f.close()

    print("[+] PDF written successfully...")


    with open('unsorted.txt', 'r') as f:
        lines = set(f.readlines())
        lines = list(lines)
        with open( "ip.txt", 'w') as f:
            for i in lines:
                i = i.strip()
                f.write('%s\n' %i)
        f.close()
    f.close()

    print("[+] Taking Screenshots...")

    file = open('ip.txt')
    for line in file:
        print("IP: {}".format(line.strip()))
        ips = line.strip()
        option = Options()
        option.headless = True
        driver = webdriver.Firefox(options=option)
        driver.set_window_size(1920,1080)
        driver.get('https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a' + ips + '&run=toolpage')
        #driver.get('https://www.virustotal.com/gui/ip-address/' + ip )
        sleep(4)

        driver.get_screenshot_as_file("BlackIP-Rep/screenshots/"+ips+".png")
        driver.quit()
    file.close
    print("[+] Screenshots has been saved...")
    os.renames("ip.txt",'./BlackIP-Rep/spamedips.txt')
    os.remove("unsorted.txt")

async def whois():
    file, t = arguments()
    with open(file, 'r') as f:
        lines = f.readlines()
    browser = await launch(options={'args': ['--no-sandbox']}, headless=False)
    page = await browser.newPage()
    await page.goto("https://www.infobyip.com/ipbulklookup.php/")
    await page.waitForSelector("[name=ips]")
    await page.click("[name=ips]")
    for line in lines:
        await page.keyboard.type(line.strip())
        await page.keyboard.press("Enter")
    await page.click('input[type="submit"]')
    xp = '//a[contains(text(), "Download CSV")]'
    await page.waitForXPath(xp)
    accept, = await page.xpath(xp)
    await accept.click()
    await page._client.send("Page.setDownloadBehavior", {
  "behavior": "allow",
  "downloadPath": "./"})
    sleep(4)
    csv = glob.glob('*.csv')
    csv = csv[0]
    os.renames(csv,'./BlackIP-Rep/whoislookup.csv')




def conti():
    columns = defaultdict(list)
    file = './BlackIP-Rep/whoislookup.csv'
    with open(file) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            for (i,v) in enumerate(row):
                columns[i].append(v)
        ip = columns[0]
        country = columns[2]
        regions = columns[3]
        city = columns[4]

    test = 0
    for i in tqdm(range(len(regions))):
        if regions[test] == "":
            regions[test] = "None"
        if city[test] == "":
            city[test] = "None"
        test += 1
        sleep(0.02)
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("NO:", style="dim")
    table.add_column("IP", style="dim")
    table.add_column("Continent")
    table.add_column("Country", justify="left")
    table.add_column("Region", justify="left")
    table.add_column("City", justify="left")


    qq = 0
    for cont in country:
        if cont != "Private network":
            country_code = pc.country_name_to_country_alpha2(cont , cn_name_format="default")
            continent_name = pc.country_alpha2_to_continent_code(country_code)
            #print(f"IP: {ip[qq]} Continent: {continent_name}, Country: {cont} ({country_code}), {regions[qq]}, {city[qq]}")
            table.add_row(
    str(qq + 1),"[cyan]"+ip[qq]+"[/cyan]","[yellow]" + continent_name + "[/yellow]", cont + " ("+ country_code +")" , regions[qq], city[qq]
    )
            qq += 1
        else:
           #print(f"IP: {ip[qq]}  Continent: None , Country: Private network, region: None, City: None")
            table.add_row(
    str(qq + 1),"[red]"+ip[qq]+"[/red]", "[green]"+continent_name+"[/green]", cont, regions[qq], city[qq]
    )
    print(table)
    print("[+] Files has been stored at: {}/BlackIP-Rep".format(os.getcwd()))

Banner()
arguments()
directorys()
asyncio.get_event_loop().run_until_complete(spam())
asyncio.get_event_loop().run_until_complete(whois())
conti()
print("[+] Done")
print("[+] Happy Hacking")
