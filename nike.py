from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver
import time

#remove webdriver flag
option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("--kiosk");
driver = webdriver.Chrome(executable_path='/Users/dhjoo/Desktop/Workspace/shopbot/chromedriver',options=option)
#driver.fullscreen_window()
#driver.maximize_window()
#########큰 모니터에 풀스크린.
#driver = webdriver.Safari()
driver.get('https://www.nike.com/kr/launch/t/men/fw/basketball/CK5424-500/vvki54/zoom-freak-2')
driver.get('https://www.nike.com/kr/launch/t/women/fw/nike-sportswear/CU1450-500/dlva36/w-nike-fontanka-edge')
driver.get('https://www.nike.com/kr/launch/t/men/fw/nike-sportswear/DD3054-001/vbce45/air-vapormax-evo-nrg')

def getLoginInfo():
    f = open("login.txt","r")
    info = f.readline().split('/')
    return info[0], info[1]

ID, PW = getLoginInfo()

def login():
    driver.find_element_by_xpath('//*[@id="jq_m_right_click"]/ul/li[1]/span/a[2]').click()
    time.sleep(0.5)
    driver.find_element_by_id('j_username').send_keys(ID)
    time.sleep(0.5)
    driver.find_element_by_id('j_password').send_keys(PW)
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="common-modal"]/div/div/div/div[2]/div/div[2]/div/button').click()

login()
##########꼭 로그인 미리 하시고!!
timeout = 0.01
#shoeURL = 'https://www.nike.com/kr/ko_kr/t/men/fw/nike-sportswear/DD9223-100/tsry65/air-more-uptempo' #솔닷
shoeURL = 'https://www.nike.com/kr/launch/t/men/fw/nike-sportswear/DD3054-001/vbce45/air-vapormax-evo-nrg' #아직 출시 안됨
#shoeURL = 'https://www.nike.com/kr/launch/t/men/fw/basketball/CK5424-500/vvki54/zoom-freak-2' #사이즈 선택 가능
#페이지 로드 직후 버튼만 이 함수 쓰면 된다.
def donghyeon_click(element, pause = timeout):
    while True:
        try:
            driver.find_element_by_xpath(element).click()
            break
        except NoSuchElementException:
            time.sleep(timeout)
            #print('못찾겠다')
            donghyeon_click(element)
            break
        except ElementClickInterceptedException :
            time.sleep(timeout)
            #print('못찾겠다')
            donghyeon_click(element)
            break


def load_shoe_page_2():
    driver.get(shoeURL)
    while True:
        try:
            element = driver.find_element_by_xpath('/html/body/section/section/section/article/div/div[2]/div/div[3]/div[2]/span')
            print("Not Yet!")
            load_shoe_page_2()
            break
        except NoSuchElementException:
            print('available')
            break

load_shoe_page_2()

def GimmeDatShoe_ver_recursive():
    start_time = time.time()
    load_shoe_page_2()
    #time.sleep(timeout)
    donghyeon_click('/html/body/section/section/section/article/div/div[2]/div/div[3]/div[2]/div/div/form/div/div[1]/a')
    #time.sleep(timeout)
    # 사이즈 찾기
    #for kobe starts with 225
    donghyeon_click('/html/body/section/section/section/article/div/div[2]/div/div[3]/div[2]/div/div/form/div/div[1]/ul/li[11]/a/span')
    #for jordan starts with 250
    #donghyeon_click('/html/body/section/section/section/article/div/div[2]/div/div[3]/div[2]/div/div/form/div/div[1]/ul/li[7]/a/span')
    print('사이즈 선택 완료')
    #donghyeon_click('/html/body/section/section/section/article/div/div[2]/div/div[3]/div[2]/div/div/form/div/div[1]/ul[text()='270']')
    #time.sleep(timeout)
    # 바로 구매 버튼 클릭
    donghyeon_click('/html/body/section/section/section/article/div/div[2]/div/div[3]/div[2]/div/div/form/div/div[2]/div')
    time.sleep(timeout)
    donghyeon_click('//*[@id="shipping_info"]/div[1]/ul/li[4]/div[1]/a')
    donghyeon_click('//*[@id="shipping_info"]/div[1]/ul/li[4]/div[1]/ul/li[2]/a/span')
    print('다음버튼 누르는중')
    donghyeon_click('//*[@id="shipping_info"]/div[1]/ul/li[5]/div[1]/div/div[1]/label/i')
    donghyeon_click('// *[ @ id = "btn-next"]')
    time.sleep(timeout)
    print('kakao 찾는중')
    donghyeon_click('//*[@id="payment-review"]/div[1]/ul/li[1]/div/div[1]/h6')
    #time.sleep(timeout)
    print('박스 찾는 중')
    donghyeon_click('//*[@id="payment-review"]/div[1]/ul/li[2]/form/div/span/label/i')
    #time.sleep(timeout)
    donghyeon_click('//*[@id="complete_checkout"]/button', pause = timeout)
    print('얼른 결제하자!!!')
    print("---- %s seconds ----" % (time.time() - start_time))


GimmeDatShoe_ver_recursive()

##### deprecated from here

def GimmeDatShoe():
    time.sleep(0.5)
    driver.find_element_by_xpath('/html/body/section/section/section/article/div/div[2]/div/div[3]/div[2]/div/div/form/div/div[1]/a').click()
    time.sleep(0.5)
    # 사이즈 찾기
    driver.find_element_by_xpath('/html/body/section/section/section/article/div/div[2]/div/div[3]/div[2]/div/div/form/div/div[1]/ul/li[11]/a/span').click()
    time.sleep(0.5)
    # 바로 구매 버튼 클릭
    driver.find_element_by_xpath('/html/body/section/section/section/article/div/div[2]/div/div[3]/div[2]/div/div/form/div/div[2]/div').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('// *[ @ id = "btn-next"]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="payment-review"]/div[1]/ul/li[1]/div/div[1]/h6').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="payment-review"]/div[1]/ul/li[2]/form/div/span/label/i').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="complete_checkout"]/button').click()

def load_shoe_page():
    driver.get(shoeURL)
    while True:
        try:
            driver.find_element_by_xpath('/html/body/section/section/section/article/div/div[2]/div/div[3]/div[2]/div/div/form/div/div[1]/a').click()
            driver.find_element_by_xpath('/html/body/section/section/section/article/div/div[2]/div/div[3]/div[2]/div/div/form/div/div[1]/ul/li[11]/a/span').click()
            break
        except NoSuchElementException:
            time.sleep(timeout)
            #print('못찾겠다')
            load_shoe_page()
            break
        except ElementClickInterceptedException :
            time.sleep(timeout)
            #print('못찾겠다')
            load_shoe_page()
            break

class Nike:

    def __init__(self):
        self.login() #로그인은 미리 해두기.
        self.findSizeInput()
        self.order()
        # self.payment()

    def login(self):

        # 쿠키 담기
        #cookies = {'domain':'.nike.com', 'name':'ActiveID', 'value':''}
        '''
        driver.maximize_window()
        driver.implicitly_wait(3)
        '''
        driver.get(
            #'https://www.nike.com/kr/ko_kr/t/adult-unisex/fw/football-soccer/AQ4174-001/fiuv99/superfly-7-elite-fg'
            'https://www.nike.com/kr/launch/t/men/fw/basketball/CK5424-500/vvki54/zoom-freak-2')

        #driver.add_cookie(cookies)
        #driver.refresh()

        '''
        for cookie in cookies:
            driver.add_cookie(cookie)
            '''


    def findSizeInput(self):
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/section/section/section/article/div/div[2]/div/div[3]/div[2]/div/div/form/div/div[1]/a').click()
        time.sleep(0.5)
        # 사이즈 찾기
        driver.find_element_by_xpath('/html/body/section/section/section/article/div/div[2]/div/div[3]/div[2]/div/div/form/div/div[1]/ul/li[11]/a/span').click()
        time.sleep(0.5)
        # 바로 구매 버튼 클릭
        driver.find_element_by_xpath('/html/body/section/section/section/article/div/div[2]/div/div[3]/div[2]/div/div/form/div/div[2]/div').click()

    def order(self):
        #time.sleep(0.5)
        #driver.find_element_by_xpath('//*[@id="shipping_info"]/div[1]/ul/li[3]/div/span/label/i').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('// *[ @ id = "btn-next"]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="payment-review"]/div[1]/ul/li[1]/div/div[1]/h6').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="payment-review"]/div[1]/ul/li[2]/form/div/span/label/i').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="complete_checkout"]/button').click()

        '''
        # 결제
        iframe = driver.find_element_by_xpath("/html/body/div[13]/iframe[2]")
        driver.switch_to.frame(iframe)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/li[2]/a').click()
        driver.find_element_by_id('userPhone').send_keys('01056741111')
        '''

if __name__ == "__main__":
    nike = Nike()
