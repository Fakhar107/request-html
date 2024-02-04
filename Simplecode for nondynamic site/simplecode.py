from requests_html import HTMLSession

s = HTMLSession()
r = s.get('https://metro.co.uk/news/tech/')

# Corrected class names in the find method
posts = r.html.find('li.trending-module-item.trending-module-item-category.category-colour-background-hover')

for post in posts:
    # Extract text content inside the <h2> element
    title = post.find('h2.trending-module-item-title', first=True).text
    
    # Extract attributes of the first <a> element
    link_attrs = post.find('a.trending-module-item-inner', first=True).attrs['href']
    
    print(title, link_attrs)


