from pathlib import Path
import requests
from PIL import Image
from io import BytesIO
import requests
from bs4 import BeautifulSoup
import re

# تابعی برای بدست آوردن تصاویر بر اساس یک کوئری جستجو
def fetch_images(query):
    # ساختن URL مورد نیاز برای جستجو در گوگل تصاویر
    query = '+'.join(query.split())
    url = f"https://www.google.com/search?hl=en&tbm=isch&q={query}"

    # ارسال درخواست به گوگل
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # جستجو برای تمام لینک‌های تصویری
    images = [img['src'] for img in soup.find_all('img')]

    # حذف احتمالی URL‌های تبلیغاتی
    images = [img for img in images if img.startswith('http')]

    return images

# استفاده از تابع و نشان دادن نتایج

# تابعی برای دریافت و نمایش تصویر از یک URL
def fetch_and_save_image(url, file_name):
    # ارسال درخواست برای گرفتن تصویر
    response = requests.get(url)

    # چک کردن اگر درخواست موفقیت آمیز بوده
    if response.status_code == 200:
        # تبدیل محتوای دریافتی به تصویر
        image = Image.open(BytesIO(response.content))

        # نمایش تصویر

        # ذخیره تصویر
        image.save(file_name)

        # p = Path('./pic/')
        # p.mkdir(exist_ok=True)
        # for i in range(10):
        #     with (p / f"{i}.jpg").open('w') as fp2:
        #         fp2.write()    
# استفاده از تابع و دانلود و ذخیره‌سازی تصویر
i=1
if __name__ == '__main__':
    query = 'cute kitten'
    image_links = fetch_images(query)
    for img_link in image_links:
        fetch_and_save_image(img_link,f"{i}.jpg")
        i+=1