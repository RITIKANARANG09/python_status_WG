from bs4 import BeautifulSoup
SIMPLE_HTML='''<html>
<head></head>
<body>
<h1> TITLE </h1>
<p class ="subtitle"> p with class </p>
<p>P without class</p>
<ul>
   <li>A</li>
   <li>B</li>
   <li>C</li>
   <li>D</li>
</ul>
</body>
</html>   
'''
simple_soup=BeautifulSoup(SIMPLE_HTML,'html.parser')
def find_title():
    print(simple_soup.find('h1').string)

def find_list_items():
    list_items=simple_soup.find_all('li')
    lists=[l.string for l in list_items]
    print(lists)
def find_subtitle():
    paragraph=simple_soup.find('p',{'class':'subtitle'})
    print(paragraph.string)
def find_other_paragraph():
    paragraphs=simple_soup.find_all('p')
    other_paragraph=[p for p in paragraphs if 'subtitle' not in p.attrs.get('class',[])]
    #other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs['class']]
    print(other_paragraph[0].string)





find_title()
find_list_items()
find_subtitle()
find_other_paragraph()
