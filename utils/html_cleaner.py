from bs4 import BeautifulSoup


def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")

    # Remove inline styling
    for tag in soup.find_all(True):
        tag.attrs.pop("style", None)

    # Remove empty list items
    for li in soup.find_all("li"):
        if not li.get_text(strip=True):
            li.decompose()

    return str(soup)
