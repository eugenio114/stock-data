import time
import os
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

startTime = datetime.now()

chromedriver = '' #add chomedriver path here

chrome_options = Options()
chrome_options.add_argument("headless")

#runs the browser in the background
driver = webdriver.Chrome(chromedriver, options=chrome_options, keep_alive=True)



#_______TRENDING STOCKS ON STOCKTWITS__https://stocktwits.com/______#
driver.get("https://stocktwits.com/rankings/trending")

t_def = []
t_symbol_list = []
t_name_list = []
t_score_list = []
t_price_list = []
t_price_pc_change_list = []

for i in range (1, 10):

    t_def.append('Trending')

    t_symbol_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[2]/span'''
    t_symbol = driver.find_element_by_xpath(t_symbol_list_path)
    t_symbol_list.append(t_symbol.text)

    t_name_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[3]/span'''
    t_name = driver.find_element_by_xpath(t_name_list_path)
    t_name_list.append(t_name.text)

    t_score_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[4]'''
    t_score = driver.find_element_by_xpath(t_score_list_path)
    t_score_list.append(t_score.text)

    t_price_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[5]'''
    t_price = driver.find_element_by_xpath(t_price_list_path)
    t_price_list.append(t_price.text)

    t_price_pc_change_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[6]/span'''
    t_price_pc_change = driver.find_element_by_xpath(t_price_pc_change_list_path)
    t_price_pc_change_list.append(t_price_pc_change.text)

trending = list(zip(t_symbol_list, t_name_list, t_score_list, t_price_list, t_price_pc_change_list))


df = pd.DataFrame(trending, columns= ['symbol', 'name', 'score', 'price', 'price_pc_change'])
df.to_csv('stocktwits_trending.csv', index=False)
print(f'''Execution Time: {datetime.now()-startTime}''')
print(trending)


# _______MESSAGES STOCKS ON STOCKTWITS__https://stocktwits.com/______#
driver.get("https://stocktwits.com/rankings/messages")

m_def = []
m_symbol_list = []
m_name_list = []
m_count_list = []
m_price_list = []
m_price_pc_change_list = []

for i in range(1, 10):
    t_def.append('Messages')

    m_symbol_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[2]/span'''
    m_symbol = driver.find_element_by_xpath(m_symbol_list_path)
    m_symbol_list.append(m_symbol.text)

    m_name_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[3]/span'''
    m_name = driver.find_element_by_xpath(m_name_list_path)
    m_name_list.append(m_name.text)

    m_count_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[4]'''
    m_count = driver.find_element_by_xpath(m_count_list_path)
    m_count_list.append(m_count.text)

    m_price_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[5]'''
    m_price = driver.find_element_by_xpath(m_price_list_path)
    m_price_list.append(m_price.text)

    m_price_pc_change_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[6]/span'''
    m_price_pc_change = driver.find_element_by_xpath(m_price_pc_change_list_path)
    m_price_pc_change_list.append(m_price_pc_change.text)

messages = list(zip(m_symbol_list, m_name_list, m_count_list, m_price_list, m_price_pc_change_list))

df = pd.DataFrame(messages, columns=['symbol', 'name', 'count', 'price', 'price_pc_change'])
df.to_csv('stocktwits_messages.csv', index=False)
print(f'''Execution Time: {datetime.now() - startTime}''')
print(messages)


#_______MESSAGES STOCKS ON STOCKTWITS__https://stocktwits.com/______#
driver.get("https://stocktwits.com/rankings/watchers")

w_def = []
w_symbol_list = []
w_name_list = []
w_count_list = []
w_price_list = []
w_price_pc_change_list = []

for i in range(1, 10):
    w_def.append('Watchers')

    w_symbol_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[2]/span'''
    w_symbol = driver.find_element_by_xpath(w_symbol_list_path)
    w_symbol_list.append(w_symbol.text)

    w_name_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[3]/span'''
    w_name = driver.find_element_by_xpath(w_name_list_path)
    w_name_list.append(w_name.text)

    w_count_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[4]'''
    w_count = driver.find_element_by_xpath(w_count_list_path)
    w_count_list.append(w_count.text)

    w_price_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[5]'''
    w_price = driver.find_element_by_xpath(w_price_list_path)
    w_price_list.append(w_price.text)

    w_price_pc_change_list_path = f'''//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[6]/span'''
    w_price_pc_change = driver.find_element_by_xpath(w_price_pc_change_list_path)
    w_price_pc_change_list.append(w_price_pc_change.text)

watchers = list(zip(w_symbol_list, w_name_list, w_count_list, w_price_list, w_price_pc_change_list))

df = pd.DataFrame(watchers, columns=['symbol', 'name', 'count', 'price', 'price_pc_change'])
df.to_csv('stocktwits_watchers.csv', index=False)
print(f'''Execution Time: {datetime.now() - startTime}''')
print(watchers)