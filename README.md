# Avito Bot for Telegram

## Overview

Avito Bot is a Telegram bot developed using Python that scrapes data from Avito and presents it in an easy-to-read format. It provides the following details for each listing:
- **Description**
- **Price**
- **City**
- **Link to the original listing**

## Features

- **Automated Data Scraping**: The bot automatically scrapes new listings from Avito and formats them for easy reading.
- **Customizable Intervals**: By default, the bot sends new listings every 1 minute. The interval can be adjusted to suit your needs.
- **User-friendly**: Provides concise and clear information directly in your Telegram chat.
- **Flexible Messaging**: Can send messages to chats and work as a standalone bot.
- **Initial Region**: The default setup uses listings from the Republic of Crimea, but this can be customized.

## Technologies Used

- **Python**
- **aiogram**
- **asyncio**
- **aiohttp**
- **BeautifulSoup**
