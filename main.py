import asyncio
import aiohttp
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor

# Создание экземпляра Telegram-бота
bot = Bot(token='your token')
dp = Dispatcher(bot)

# Список уже отправленных объявлений
sent_ads = []


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def parse_ads(url):
    html = await fetch(url)
    soup = BeautifulSoup(html, 'html.parser')
    ads = soup.find_all('div', class_='items-items-kAJAg')

    for ad in ads:
        title = ad.find('h3').text.strip()
        city = ad.find('p', class_='styles-module-root-_KFFt styles-module-size_s-awPvv styles-module-size_s-_P6ZA styles-module-ellipsis-LKWy3 styles-module-ellipsis_oneLine-NY089 stylesMarningNormal-module-root-OSCNq stylesMarningNormal-module-paragraph-s-_c6vD styles-module-root_top-HYzCt styles-module-margin-top_0-_usAN')
        city_clear = [c.text for c in city]
        city_clear1 = ''.join(city_clear)
        price = ad.find('div', class_='price-price-JP7qe').text.strip()
        link = ad.find('a')['href']

        ad_id = link  # Используем ссылку объявления как идентификатор

        if ad_id not in sent_ads:
            # Отправка данных в чат бота
            await bot.send_message(chat_id='-961407817',
                                   text=f'Описание:  {title}'
                                        f'\n\nЦена:  {price}'
                                        f'\n\nГород:  {city_clear1}'
                                        f'\n\nСсылка:  https://www.avito.ru{link}')

            sent_ads.append(ad_id)  # Добавляем идентификатор объявления в список уже отправленных объявлений


async def main():
    base_url = 'https://www.avito.ru/respublika_krym/kvartiry/prodam-ASgBAgICAUSSA8YQ'
    page = 1

    while True:
        url = f'{base_url}?p={page}'

        # Запуск парсера для текущей страницы
        await parse_ads(url)

        # Переход к следующей странице
        page += 1

        # Ожидание 60 секунд перед следующим запросом
        await asyncio.sleep(60)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(main())
    executor.start_polling(dp)
