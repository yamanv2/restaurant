# In this file i don't know why it shows an error "AttributeError: 'NoneType' object has no attribute 'find_all'"
# So i'm just sending you the final file so that you can read that and if you read then must tell me where i'm doing it wrong. 



import requests
import pandas as pd
from bs4 import BeautifulSoup


HEADER = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36', 'Accept-Language':'en-US, en;q=0.5'})

data = []

for i in range(1,21):
    URL = f"https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{i}"
    webpage = requests.get(URL, headers = HEADER)
    # print(webpage.content)

    soup = BeautifulSoup(webpage.content, "html.parser")
    # print(soup.prettify())

    links = soup.find_all('a', attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    # print(links)
    
    for j in range(21):
        link = links[j].get('href')
        product_url = "https://www.amazon.in/" + link
        # print(product_url)

        product = requests.get(product_url, headers = HEADER)
        # print(new_webpage)


        new_product = BeautifulSoup(product.content, "html.parser")
        # print(new_product)

        product_name = new_product.find("span", attrs={'id':'productTitle'}).text.strip()
        # print(product_name)

        product_price = new_product.find("span", attrs={'class':'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'}).find("span", attrs={'class':"a-offscreen"}).text
        # print(product_price)


        rating = new_product.find("span", attrs={"class":"a-icon-alt"}).text
        # print(rating)

        product_review_count = new_product.find("span", attrs={"id":"acrCustomerReviewText"}).text
        # print(product_review_count)

        description = new_product.find("ul", attrs={"class":"a-unordered-list a-vertical a-spacing-mini"}).text.strip()
        # print(description)

        product_ASIN = new_product.find("div", attrs={"id":"detailBullets_feature_div"})
        ASIN1 = product_ASIN.find_all('span')
        ASIN = ASIN1[11].text
        # PRINT(ASIN)



        new_product_manufacturer = new_product.find("div", attrs={"id":"detailBullets_feature_div"})
        manufacturer1 = new_product_manufacturer.find_all('span')
        manufacturer = manufacturer1[8].text
        # print(manufacturer)


        data.append([product_url, product_name, product_price, rating, product_review_count, description, ASIN, manufacturer])

df = pd.DataFrame(data, columns=['URL', 'Name', 'Price', 'Rating', 'No of Review', 'Description', 'ASIN', 'Manufacturer'])

df.to_csv('data.csv')





# Items to scrape
# • Product URL
# • Product Name
# • Product Price
# • Rating
# • Number of reviews
# Part 2
# With the Product URL received in the above case, hit each URL, and add below items:
# • Description
# • ASIN
# • Product Description
# • Manufacturer