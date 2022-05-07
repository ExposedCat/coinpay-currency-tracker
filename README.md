<div align="center">
    <h1>Coin Pay Telegram Bot - Currency Tracker</h1>

[![Developer](https://img.shields.io/badge/Developer-Telegram-blue?style=for-the-badge)](https://t.me/ExposedCat)
![Updated Badge](https://badges.pufler.dev/updated/exposedcat/coinpay-currency-tracker?style=for-the-badge)

<img src="https://i.imgur.com/aYajiCM.png" alt="Bot preview">

</div>

<div align="center">
    <h2>Features</h2>
</div>
<ul>
    <li>Multilanguage support: English and Russian</li>
    <li>User-friendly experience: no notification while interacting with bot, intuitive interface, text markup, minimalistic & pretty design</li>
    <li>Optimized API requests: No excess api polling</li>
    <li>Scalable file architecture</li>
    <li>Strict code formatting rules following PEP8 standard</li>
    <li>As async, as possible</li>
    <li>Well-readable git repository with beautiful README</li>
</ul>

<div align="center">
    <h2>Stack</h2>
</div>
<ul>
    <li>Language: Python 3.10</li>
    <li>Telegram API library: AioGram 2.20</li>
    <li>Database: MongoDB</li>
    <li>Database engine: Motor</li>
</ul>

<div align="center">
    <h2>Running</h2>
</div>

0. Install [Docker](https://docs.docker.com/get-docker/)  
1. Clone repo:  
```bash
git clone https://github.com/ExposedCat/coinpay-currency-tracker.git
```
2. Go to project root:
```bash
cd coinpay-tracker
```
3. Replace `docker-compose-example.yml` with `docker-compose.yml` and fill your Telegram bot http API token
4. Build app image:
```bash
sudo docker build -t coinpay-tracker
```
5. Run image:
```bash
sudo docker-compose up -d --build
```
**Done**.  
You can stop the app via
```bash
sudo docker-compose down
```