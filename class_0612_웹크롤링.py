﻿# # 셀레늄 모듈 임포트
# from selenium import webdriver
# import time

# # 크롬 물리드라이버 가동 명령
# driver = webdriver.Chrome("C:\chrome/chromedriver.exe")

# # 물리 드라이버로 사이트 이동 명령
# driver.get("https://www.naver.com")

# time.sleep(1)
# # xpath를 이용하여 자동으로 클릭 제어하기
# login_btn = driver.find_element_by_xpath('//*[@id="account"]/a')
# # //*[@id="account"]/div/a/i # 원래 패스가 이거였는데
# # //*[@id="account"]/a # 최근에 이걸로 바뀜
# login_btn.click()

# # xpath를 이용하여 자동으로 텍스트 작성하기
# time.sleep(2)
# id_input = driver.find_element_by_xpath('//*[@id="id"]')
# id_input.send_keys('naverID')

# time.sleep(2)
# pw_input = driver.find_element_by_xpath('//*[@id="pw"]')
# pw_input.send_keys('naverPassword')

# time.sleep(1)
# login_btn = driver.find_element_by_xpath('//*[@id="log.login"]')
# login_btn.click()

