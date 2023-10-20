page = "<a href=\"https://algo.com\">Algo</a>"

def extract_links(page):
    link_ref = page.find("<a href=")
    first_quote = link_ref + 9
    sol = page[first_quote:]
    url = sol[:sol.find('"')]
    return url

print(extract_links(page))