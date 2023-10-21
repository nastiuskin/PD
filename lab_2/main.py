import os
import requests
from urllib.parse import urlparse, urljoin, quote
from tqdm import tqdm
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Создаем базовую директорию для сохранения изображений
base_dir = "dataset"
os.makedirs(base_dir, exist_ok=True)

def download_images(query, num_images):
    # Кодируем поисковый запрос
    query_encoded = quote(query)
    search_url = f"https://yandex.ru/images/search?text={query_encoded}"

    # Инициализируем веб-драйвер
    driver = webdriver.Chrome()
    driver.get(search_url)

    # Создаем список для хранения URL изображений
    image_links = []

    while len(image_links) < num_images:
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        # Ищем все элементы <img> на странице
        for img in soup.find_all("img"):
            src = img.get("src")
            if src:
                image_links.append(src)

    # Завершаем работу веб-драйвера
    driver.quit()

    # Создаем директорию для сохранения изображений
    category_dir = os.path.join(base_dir, query)
    os.makedirs(category_dir, exist_ok=True)

    count = 0
    for img_link in image_links[:num_images]:
        try:
            # Проверяем схему URL и строим абсолютный URL, если необходимо
            if not urlparse(img_link).scheme:
                img_link = urljoin(search_url, img_link)

            # Получаем данные изображения
            img_data = requests.get(img_link, stream=True)
            img_size = int(img_data.headers.get("Content-length", 0))
            img_filename = f"{count + 1}.jpg"
            img_path = os.path.join(category_dir, img_filename)

            # Отображаем прогресс загрузки
            progress = tqdm(img_data.iter_content(1024),
                            f'Загрузка {img_filename}',
                            total=img_size,
                            unit="B",
                            unit_scale=True,
                            unit_divisor=1024,
                            disable=True)
            
            # Записываем данные изображения в файл
            with open(img_path, "wb") as img_file:
                for data in progress.iterable:
                    img_file.write(data)

            count += 1
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}")

# Загружаем изображения для запросов "tiger" и "leopard"
download_images("tiger", 10)
download_images("leopard", 10)
