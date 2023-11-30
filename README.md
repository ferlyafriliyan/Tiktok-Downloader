<div align="center">

# TikDown <img src="https://github.com/ferlyafriliyan/Tiktok-Downloader/blob/main/assets/286881866-05bb5343-bd6d-494c-ad1d-5eb85bd3fed2.png" width="35px">

**Tik-Down** is a downloader designed for downloading TikTok videos. (https://snaptik.app)

<img src="https://github.com/ferlyafriliyan/Tiktok-Downloader/blob/main/assets/286882087-95819343-c111-4a6d-b742-5f28f23166e3.png" width="600" height="auto">

</div>

## Prerequisites

-   [Python](https://www.python.org/) (version 3.6 or higher)
-   [NodeJS](https://nodejs.org/en) (for decoder)

## Installation

To use _**Tik-Down**_, open your terminal and navigate to the folder that contains _**Tik-Down**_ content ::

```bash
pip install -r requirements.txt
```

## Example

```python
import os

from api import Colors, SnaptikDownloader

if __name__ == "__main__":
    """
    Support both type of tiktok URL;
     [>] https://vm.tiktok.com/ZSNxBbr3C/
     [>] https://vm.tiktok.com/ZSNxBwhY8/
    """

    os.system("cls" if os.name == "nt" else "clear")

    logging_enabled = False
    tiktok_url = input(f"{Colors.GREEN}Tiktok target URL{Colors.END}: ")
    SnaptikDownloader(tiktok_url, logging_enabled).start_download()

```

## **Legal Disclaimer**

> This was made for educational purposes only, nobody which directly involved in this project is responsible for any damages caused. **_You are responsible for your actions._**
