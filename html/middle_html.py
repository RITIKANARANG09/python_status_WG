from bs4 import BeautifulSoup

ITEM_HTML='''<html><head></head><body>
<li class="col-xs-6">
    <article class="product_pod">
        <div class="image_cotainer">
            <a href="catalogue/a-ligt-in-the-attic_1000/index.html>
        </div>
          <p class="star-rating three">
            <i class="icon-star"></li>
            <i class="icon-star"></li>
            <i class="icon-star"></li>
            <i class="icon-star"></li>
            <i class="icon-star"></li>
        </p>
    <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="a light">
    <div class="product_price">
  <p class="price_color">$51</p>
<p class="instock availability">
    <i class ="icon_ok"></i>
        in stock
</p>

</html>
'''
soup=BeautifulSoup(ITEM_HTML,'html.parser')

def find_item_name():
    locator='article.prduct_pod h3 a'
    item_link=soup.select_one(locator)
    item_name=item_link.attrs['title']
    print(item_name)

find_item_name()