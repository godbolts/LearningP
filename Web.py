import requests
from bs4 import BeautifulSoup

def loe_saladus(link, algus, lõpp):
    response = requests.get(link)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        page_content = soup.get_text()  # Get all the text content from the page
        start_index = page_content.find(algus)
        end_index = page_content.find(lõpp, start_index)

        if start_index != -1 and end_index != -1:
            # Extract the line of text between the starting and ending tags
            extracted_text = page_content[start_index + len(algus):end_index].strip()
            return extracted_text
        else:
            print("Tags not found on the page.")

    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")

sõne = loe_saladus('https://courses.cs.ut.ee/2022/programmeerimine/Main/Kodu5', 'ylisalajane:', ':ylisalajane')
number_list = [int(num) for num in sõne.split(',')]
tähestik = (' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'Š', 'Z', 'Ž', 'T', 'U', 'V', 'W', 'Õ', 'Ä', 'Ö', 'Ü', 'X', 'Y')

for täht in number_list:
    if 0 <= täht <= len(tähestik):
        lause = tähestik[täht]
        print(lause, end = '')