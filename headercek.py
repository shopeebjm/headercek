import requests
import sys
import time
from colors import *

# daftar security header yang akan dicek
security_headers = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
    "X-XSS-Protection"
]


def cek_header(url):
    try:
        print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                     ┃
┃     ▌ ▌        ▌            ▌       ┃
┃     ▙▄▌▞▀▖▝▀▖▞▀▌▞▀▖▙▀▖▞▀▖▞▀▖▌▗▘     ┃
┃     ▌ ▌▛▀ ▞▀▌▌ ▌▛▀ ▌  ▌ ▖▛▀ ▛▚      ┃ 
┃     ▘ ▘▝▀▘▝▀▘▝▀▘▝▀▘▘  ▝▀ ▝▀▘▘ ▘     ┃
┃              Dev : shopeebjm         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")
        print(f"{g}[+]{rs} Memulai scanning pada target = [{r}{url}{rs}]\n")
        time.sleep(1)
        response = requests.get(url, timeout=10)
        headers = response.headers

        ditemukan = 0
        tidak_ada = 0

        for header in security_headers:
            if header in headers:
                ditemukan += 1
                print(f"{g}[✓]{rs} {header}")
            else:
                tidak_ada += 1
                print(f"{r}[✕]{rs} {header}")

        total = len(security_headers)

        print("\n===================================")
        print(f"{g}RINGKASAN HASIL SCAN{rs}")
        print(f"{g}[✓]{rs} Header ditemukan :", ditemukan)
        print(f"{r}[✕]{rs} Header tidak ada :", tidak_ada)
        print(f"{g}[+]{rs} Total header     :", total)
        print("===================================\n")

        # analisis keamanan
        if ditemukan >= 5:
            print(f"{g}[KESIMPULAN]{rs} Website {g}AMAN{rs} dari Clickjacking")
        elif ditemukan >= 3:
            print(f"{y}[KESIMPULAN]{rs} Website {y}CUKUP AMAN{rs} tapi masih bisa ditingkatkan")
        else:
            print(f"{r}[KESIMPULAN]{rs} Website {r}RENTAN{rs} Clickjacking")

    except requests.exceptions.RequestException as e:
        print(f"{r}[-] Gagal mengakses target:{rs}", e)


def main():
    if len(sys.argv) != 2:
        print("Penggunaan:")
        print("python headercek.py https://target.com")
        sys.exit()

    url = sys.argv[1]
    cek_header(url)


if __name__ == "__main__":
    main()
