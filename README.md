# PinkSale Trending Bot

A Python-based automation bot designed for PinkSale and other crypto launchpads. The project uses Selenium, authenticated proxies, and multiprocessing to automate browser interactions and generate concurrent activity across launchpad pages.

> **Disclaimer**
>
> This software is provided for educational and research purposes. Users are responsible for ensuring that their use of this software complies with the terms of service of any platform they interact with and all applicable laws and regulations.

---

## Features

* Browser automation with Selenium
* Authenticated HTTP proxy support
* Dynamic Chrome proxy extension generation
* Multi-process execution
* JSON-based configuration
* Easy deployment
* ChromeDriver integration
* Launchpad automation workflow

---

## Technologies

* Python 3
* Selenium
* ChromeDriver
* Multiprocessing
* Fake UserAgent
* JSON Configuration

---

## Project Structure

```text
pinksale-trending-bot/
│
├── Bot.bat
├── Setup.bat
├── sc.py
├── setup.py
├── Config.example.json
├── instructions.txt
├── chromedriver.exe
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/FelicioX/pinksale-trending-bot.git
```

Enter the project directory:

```bash
cd pinksale-trending-bot
```

Install dependencies:

```bash
python setup.py
```

or

```bash
pip install selenium fake-useragent
```

---

## Configuration

Rename:

```text
Config.example.json
```

to

```text
Config.json
```

Then edit the configuration:

```json
{
    "proxy": "your-proxy-host",
    "thread": 2,
    "url": "TOKEN_ADDRESS",
    "coin": "",
    "port": 12345,
    "user": "YOUR_USERNAME",
    "pasw": "YOUR_PASSWORD"
}
```

---

## Running

Windows:

```bash
Bot.bat
```

or

```bash
python sc.py
```

---

## How It Works

1. Loads the configuration file.
2. Creates authenticated proxy settings.
3. Generates a temporary Chrome proxy extension.
4. Launches one or more Chrome instances.
5. Opens the target launchpad.
6. Searches the configured token.
7. Performs automated browser interactions.
8. Repeats the workflow continuously.

---

## Requirements

* Python 3.8+
* Google Chrome
* ChromeDriver
* Selenium
* Authenticated HTTP Proxy

---

## License

This project is licensed under the MIT License.

See the **LICENSE** file for more information.

---

## Contributing

Contributions, suggestions, and improvements are welcome.

Please read **CONTRIBUTING.md** before submitting a Pull Request.

---

## Security

If you discover a security issue, please refer to **SECURITY.md**.

---

## Changelog

Project updates are documented in **CHANGELOG.md**.

---

## Author

**Felicio Xavier**

GitHub: https://github.com/FelicioX
