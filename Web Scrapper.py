import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


try:
    # Path to chromedriver.exe
    driver = webdriver.Chrome(executable_path='webdriver/chromedriver.exe')
    driver.get("https://projects.ce.pdn.ac.lk/co328/")

    results = []
    content = driver.page_source
    soup = BeautifulSoup(content,features="html.parser")


    for element in soup.findAll(attrs='col-lg-3 col-md-6 col-sm-6 d-flex m-0 img-hover-zoom-card'): #class attribute
        name = element.find('p') #tag name
        if name not in results:
            cleaned = name.text.strip('\n')
            results.append(cleaned.strip())

    #store the results in a text file
    with open('README.md', 'w') as f:
        f.write("## Number of Projects: " + str(len(results)) + "\n")

        count = 1
        for item in results:
            f.write("#### " + str(count) + "." + item + "\n")
            count += 1

    print(results)
    driver.quit()

except Exception as e:
    print(e)
    driver.quit()
