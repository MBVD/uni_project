import requests
from bs4 import BeautifulSoup

class TechnodomParser:
    def __init__(self, url = 'https://www.technodom.kz'):
        self.url = url
        self.product_data_list = []

    def is_duplicate(self, product_data):
            for existing_product in self.product_data_list:
                if (existing_product["name"] == product_data["name"] and
                    existing_product.get("price") == product_data.get("price") and
                    existing_product.get("image") == product_data.get("image")):
                    return True
            return False

    def parse_product_page(self, url):
        try:
            response = requests.get(url)
            
            if response.status_code != 200:
                print(f"Ошибка: не удалось загрузить страницу, код состояния {response.status_code}")
                return
            
            soup = BeautifulSoup(response.text, 'html.parser')

            product_data = {}
            try:
                product_data["name"] = soup.find('h1', class_='Typography Typography__XL Typography__XL_Bold').get_text(strip=True)
                price = soup.find('p', class_=['Typography Typography__Heading Typography__Heading_H1',
                                'Typography ProductPricesVariantB_accented__n2rtH Typography__Heading Typography__Heading_H1'])
                if price:
                    product_data["price"] = price.get_text(strip=True)
                    product_data["price"] = product_data["price"].replace('\xa0', ' ')

                product_data["image"] = soup.find('img', class_='Navigation_thumbImage__Rx52k Navigation_thumbImageActive__5lBVK')['src']

                specs = {}
                specs_section = soup.find('div', class_='TechnicalSpecifications_half__5Q7c7')
                if specs_section:
                    for spec_cat in specs_section.find_all('div', class_ = 'Description_container__XuEAV TechnicalSpecifications_attribute__KB2Vs Description_row__WY2q6'):
                        for spec_item in spec_cat.find_all('div', class_ = 'Description_item__mKeUf'):
                            key = spec_item.find('p', class_ = 'Typography Description_text__27B77 Description_leftText__v_3LD Typography__L').get_text(strip = True)
                            value = spec_item.find('p', class_ = ['Typography Description_text__27B77 Description_link__Ze5Ju Description_rightText__j_Zfk Typography__L', 'Typography Description_text__27B77 Description_rightText__j_Zfk Typography__L']).get_text(strip = True)
                            specs[key] = value
                
                product_data["specs"] = specs

                print(product_data)

                if not self.is_duplicate(product_data):
                    self.product_data_list.append(product_data)

            except AttributeError:
                print("Не удалось извлечь данные с страницы.")
                return
        
        except requests.RequestException as e:
            print(f"Ошибка при запросе: {e}")


    def parse_inner_catalog(self, url):
        try:
            response = requests.get(url)

            if response.status_code != 200:
                print(f"Ошибка: не удалось загрузить страницу, код состояния {response.status_code}")
                return
            
            soup = BeautifulSoup(response.text, 'html.parser')

            
            for link in soup.find_all('a', href=True):
                href = link['href']
                if '/p/' in href:
                    self.parse_product_page(self.url + href)
            

        except requests.RequestException as e:
            print(f"Ошибка при запросе: {e}")


    def parse_outer_catalog(self):

        try:
            response = requests.get(self.url+'/catalog')

            if response.status_code != 200:
                print(f"Ошибка: не удалось загрузить страницу, код состояния {response.status_code}")
                return
            
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a', href=True):
                href = link['href']
                if '/catalog/' in href:

                    parent_div = link.find_parent('div', class_ = 'Header_content__Qa_y3 Header_sticky__2DSLL MiddleContent_block__ztkbQ')
                    if not parent_div:
                        self.parse_inner_catalog(self.url + href)

        except requests.RequestException as e:
            print(f"Ошибка при запросе: {e}")