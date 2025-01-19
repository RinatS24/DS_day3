import sys
import os

def install_libs():
    os.system("pip install -r array_libs.txt")

def main(short_name,name_row):
    install_libs()
    import requests
    from bs4 import BeautifulSoup

    url = f"https://finance.yahoo.com/quote/{short_name}/financials/"
    headrs = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    req = requests.get(url,headers=headrs)

    soup = BeautifulSoup(req.text, "lxml")

    detect_error = soup.find("div",class_="noData yf-wnifss")

    if detect_error is None:
        find_my_row = soup.find_all("div",class_="row lv-0 yf-t22klz")

        temp = ''
        for item in find_my_row:
            if item.find("div",class_="rowTitle yf-t22klz",title=name_row) is not None:
                temp = item.text.strip().split()
                break
        row_data = [name_row]    
        for item in temp:
            if item[0].isdigit() or (item[0]=='-' and item[1].isdigit()):
                if item[-1]=="0" and item[-2]=="0":
                    row_data.append(item[:-3])
                else:
                    row_data.append(item)
            elif item == "--":
                row_data.append(item)

        if len(row_data)>1:   
            print(tuple(row_data))
if __name__ == "__main__":
    if len(sys.argv) == 3 and os.getenv("VIRTUAL_ENV") != None:
        main(sys.argv[1],sys.argv[2])



# python3 -m cProfile -s cumulative financial.py 'MSFT' 'Total Revenue' > profiling-sleep.txt
# python3 -m cProfile -s cumulative financial.py 'MSFT' 'Total Revenue' > profiling-tottime.txt