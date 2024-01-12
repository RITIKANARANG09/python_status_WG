from selenium import webdriver

driver=webdriver.Firefox()

driver.get("https://www.amazon.in/?tag=admpdesktopin-21&ref=pd_sl_11c94dca52f51b420fb512500e86443843773d02f04810ba6651f574&mfadid=adm")
print(driver.title)