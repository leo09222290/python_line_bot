#2023/06/09
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def recommend(a):
    restaurant_dic = {}
    # a=input("請輸入地點")
    # 設定 ChromeDriver 的路徑
    options = Options()
    options.chrome_executable_path = "C:\\Users\\USER\\Desktop\\0531\\chromedriver.exe"
    
    # 啟動 ChromeDriver
    driver = webdriver.Chrome(options=options)
    
    # 前往 Google Maps 網站
    driver.get("https://www.google.com/maps/")
    
    # 定位搜尋欄位，輸入餐廳關鍵字
    search_input = driver.find_element(By.ID, "searchboxinput")
    
    search_input.send_keys(a+"餐廳")
    search_button = driver.find_element(By.ID, "searchbox-searchbutton")
    search_button.click()
    rating_filter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/button/span/span'))
    )
    
    rating_filter.click()
    four_stars_plus = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="action-menu"]/div[7]'))
    )
    four_stars_plus.click()
    
    time.sleep(2)
    # 等待頁面載入餐廳列表
    restaurant_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]'))
    )
    
    
    # 解析餐廳列表
    restaurants = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]'))
    )
    for i, restaurant in enumerate(restaurants[:5], 1):
        name = restaurant.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]').text
        address = restaurant.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[1]/span[2]/span[2]').text
        
        # 檢查是否有營業時間資訊
        try:
            hours = restaurant.find_element(By.XPATH, ".//span[contains(@class, 'section-result-info')]").text
        except:
            hours = "營業時間未提供"
            restaurant_dic[0]=[name,address,hours]
            print("餐廳名稱:", name)
            print("地址:", address)
            print("營業時間:", hours)
            print()
            print("------------------------")
    for i, restaurant in enumerate(restaurants[:5], 1):
        name = restaurant.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[5]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2]').text
        address = restaurant.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[5]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[1]/span[2]/span[2]').text
        
        # 檢查是否有營業時間資訊
        try:
            hours = restaurant.find_element(By.XPATH, ".//span[contains(@class, 'section-result-info')]").text
        except:
            hours = "營業時間未提供"
            restaurant_dic[1]=[name,address,hours]
            print("餐廳名稱:", name)
            print("地址:", address)
            print("營業時間:", hours)
            print()
            print("------------------------")
    for i, restaurant in enumerate(restaurants[:5], 1):
         name = restaurant.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[7]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2]').text
         address = restaurant.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[7]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[1]/span[2]/span[2]').text
        
         # 檢查是否有營業時間資訊
         try:
             hours = restaurant.find_element(By.XPATH, ".//span[contains(@class, 'section-result-info')]").text
         except:
             hours = "營業時間未提供"
             restaurant_dic[2]=[name,address,hours]
             print("餐廳名稱:", name)
             print("地址:", address)
             print("營業時間:", hours)
             print()
             print("------------------------")
    for i, restaurant in enumerate(restaurants[:5], 1):
        name = restaurant.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[9]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2]').text
        address = restaurant.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[9]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[1]/span[2]/span[2]').text
        
        # 檢查是否有營業時間資訊
        try:
            hours = restaurant.find_element(By.XPATH, ".//span[contains(@class, 'section-result-info')]").text
        except:
            hours = "營業時間未提供"
            restaurant_dic[3]=[name,address,hours]
            print("餐廳名稱:", name)
            print("地址:", address)
            print("營業時間:", hours)
            print()
            print("------------------------")
    for i, restaurant in enumerate(restaurants[:5], 1):
        name = restaurant.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[11]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2]').text
        address = restaurant.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[11]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[1]/span[2]/span[2]').text
        
        # 檢查是否有營業時間資訊
        try:
            hours = restaurant.find_element(By.XPATH, ".//span[contains(@class, 'section-result-info')]").text
        except:
            hours = "營業時間未提供"
            restaurant_dic[4]=[name,address,hours]
            print("餐廳名稱:", name)
            print("地址:", address)
            print("營業時間:", hours)
            print()
            print("------------------------")
    return restaurant_dic
    # print(restaurant_dic)
    # print(restaurant_dic[4][1])
# recommend('大安')