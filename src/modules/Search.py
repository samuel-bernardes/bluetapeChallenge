import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver

from modules.Provider import keywords, urls
from modules.Format import Format
from modules.Config import options

driver = webdriver.Chrome(chrome_options=options)
class Search():

    def explore():

        data = {}

        for keyword in keywords:
            data[keyword] = []

        for url in urls:
            driver.get(url)
            source_code = BeautifulSoup(driver.page_source, "html.parser")
            for keyword in keywords:
                count = len(source_code(text=lambda t: keyword in t.text))
                data[keyword].append(count)

        driver.quit()

        df = pd.DataFrame(data, index=urls)
        df['URL'] = urls
        df = df.melt(id_vars='URL', value_name='Número de ocorrências')
        df = df.rename(columns={'variable': 'Palavra'})
        df = df.sort_values(by='Número de ocorrências', ascending=False)

        writer = pd.ExcelWriter('Results.xlsx', engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name='report', startrow=2)

        Format.style(writer, df)
