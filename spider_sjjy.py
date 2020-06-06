import requests
from bs4 import BeautifulSoup
import time
import re
import csv
import random


def ip():
    return [line.strip() for line in open('ip.txt', 'r').readlines()]


def random_choice(list_):
    random_index = random.randint(0, len(list_) - 1)
    return random_index, list_[random_index]


def original_soup(requirements, i):
    r = requirements.find_all('li')
    if len(r) != 0:
        r_list = [pattern.sub('', i.find('div').text.strip()) for i in r]
    else:
        r_list = ['--'] * len_requirements[i]
    return r_list

    
def home_page_scrapy(url_open):
    total = []
    soup = BeautifulSoup(url_open.text, 'lxml')
    # pet name
    pet_name = soup.find('h4').text
    pet_name = pet_name[:pet_name.index('ID:')]
    total.append(pet_name)
    # brif_info
    brif_intro = soup.find('h6', class_='member_name').text
    total.append(brif_intro)
    # educational background/height/car/wage/house/weight/star/region/animal_sign/blood
    # (then we can get 12 items, and we only need top ten)

    brif_info = soup.find_all('div', class_='fl pr')[:10]
    for item in brif_info:
        brif_info_split = item.text.strip()
        total.append(brif_info_split)
    # introduction(some \n and \u3000)
    try:
        introduction = soup.find('div', class_='js_text').text
        introduction = pattern.sub('', introduction)
        total.append(introduction)
    except:
        total.append('--')
    # hobbies(without personal tags)
    hobbies = soup.find('div', class_='list_a fn-clear').find('ul').find_all('li')

    if len(hobbies) != 0:
        hobby = [item.text.strip() for item in hobbies]
        hobby = ' '.join(hobby)
    else:
        hobby = '--'
    total.append(hobby)
    # requirement/lifestyle/economic/work/study/about_self/about_home
    requirements_data = []
    requirements = soup.find_all('ul', class_='js_list fn-clear')

    for i in range(len(requirements)):
        from_data = original_soup(requirements[i], i)
        requirements_data.extend(from_data)
    total.extend(requirements_data)
    # housework/pet
    housework_pet = soup.find_all('dd', class_='cur')
    
    if len(housework_pet) == 2:
        total.append(housework_pet[0].text)
        total.append(housework_pet[1].text)
    elif len(housework_pet) == 1:
        if housework_pet[0].text in homework_list:
            total.append(housework_pet[0].text)
            total.append('--')
        else:
            total.append('--')
            total.append(housework_pet[0].text)
    else:
        total.append('--')
        total.append('--')
    return total


if __name__ == '__main__':
    global headers, pattern, homework_list, len_requirements, driver
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        'Cookie': 'PHPSESSID=6403c18b4355b18391ef7005f321a473; SESSION_HASH=1e6f5ff221279bc8f3253bb2fb169e398c09e2a9; jy_refer=sp0.baidu.com; FROM_BD_WD=%25E4%25B8%2596%25E7%25BA%25AA%25E4%25BD%25B3%25E7%25BC%2598; FROM_ST_ID=1764229; FROM_ST=.jiayuan.com; accessID=20191212102207851989; ip_loc=51; user_access=1; _gscu_1380850711=76117330qdfp4220; _gscbrs_1380850711=1; COMMON_HASH=d51fc91766e72446ece5f9060b771166; stadate1=230492387; myloc=51%7C5101; myage=27; mysex=m; myuid=230492387; myincome=40; pop_sj=0; _gscs_1380850711=76117330hjzuba20|pv:3; main_search:231492387=%7C%7C%7C00; pop_1551429571=1576118734564; pop_avatar=1; PROFILE=231492387%3A%25E6%25B4%258B.%3Am%3Ahttps%3A%2F%2Fimages2.jyimg.com%2Fw4%2Fglobal%2Fi%3A0%3A%3A1%3Azwzp_m.jpg%3A1%3A1%3A50%3A10%3A-5; RAW_HASH=45SxTSIjE-h4gvJp0NDFeCDtxUldVaThROM%2Ara6HipUB3OtKguAPs4EdDI1Bmvou9jCRJLttE76CdMcNkGsYtyQnOezRCrotmdInCnRRECFZjSw.; pop_time=1576117564860'
    }
    homework_list = ['不会', '会一些', '精通']
    len_requirements = [8, 9, 6, 8, 3, 11, 7]
    pattern = re.compile('[\s*]+')
    # ip_pool = ip()
    # print('共有{}个代理ip'.format(len(ip_pool)))
    # driver = webdriver.Firefox()
    # driver.get('http://www.jiayuan.com/profile/index.php?uid=231252296')
    f = open('data_refresh_1_995.csv', 'a', newline='', encoding='utf-8')
    f_write = csv.writer(f)
    uid = [line.strip() for line in open('realid_without_deplication.txt', 'r').readlines()]
    for item in range(1, 995):
        print('第{}张主页: '.format(item + 1), end='')
        home_page_url = 'https://www.jiayuan.com/' + uid[item]
        print(home_page_url)
        # flag = True
        # while flag:
        #     if len(ip_pool) != 0:
        #         ip_index, ip_context = random_choice(ip_pool)
        #         proxy_ip = {'https': ip_context}
        #         try:
        #             url_open = requests.get(home_page_url, headers=headers, proxies=proxy_ip, timeout=3)
        #         except:
        #             ip_pool.pop(ip_index)
        #         else:
        #             flag = False
        #     else:
        #         url_open = requests.get(home_page_url, headers=headers)
        #         flag = False
        url_open = requests.get(home_page_url, headers=headers)
        try:
            info = home_page_scrapy(url_open)
            f_write.writerow(info)
            # time.sleep(random.randint(5, 15))
        except:
            print('Unknown wrong!')
            f_write.writerow([])
            # time.sleep(random.randint(5, 15))
            continue
        if (item + 1) % 7 == 0:
            time.sleep(15)
f.close()