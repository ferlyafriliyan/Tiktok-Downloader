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
