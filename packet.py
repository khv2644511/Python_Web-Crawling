from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# from seleniumwire import decode


# Create a new instance of the Chrome web driver

def get_chrome_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')  # 안전하지 않은 작업을 방지
    chrome_options.add_argument('--window-size=1280,920')  # 창 크기 설정
    chrome_options.add_argument('--disable-dev-shm-usage')  # 공유 메모리 사용 제한
    return chrome_options
chrome_options = get_chrome_options()
chrome_driver_path = ChromeDriverManager().install()
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options) 

# Perform a GET request to a webpage
driver.get('https://www.google.com')
request = driver.wait_for_request('./images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')

content_type = request.response.headers.get('Content-Type', '')

if 'text' in content_type or 'json' in content_type:
    # If the content is text, decode it as utf-8
    print(f'{request.response.body.decode("utf-8")}, 응답코드 {request.response.status_code}, 컨텐츠 유형: {content_type}')
elif 'image' in content_type:
    # If the content is an image, handle it as binary data
    image_data = request.response.body
    print(f'Image retrieved, 응답코드 {request.response.status_code}, 컨텐츠 유형: {content_type}')
    # Optionally, save the image to a file
    with open('downloaded_image.png', 'wb') as f:
        f.write(image_data)
else:
    # If the content type is something else
    print(f'Unhandled content type {content_type}, 응답코드 {request.response.status_code}')
# print(f'{request.response.body.decode("utf-8")}, 응답코드 {request.response.status_code}, 컨텐츠 유형: {request.response.headers["Content-Type"]}')
# response = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))".decode('utf-8')
# print(response)

# Access the requests made by the browser
# for request in driver.requests:
#     if request.response:
#         print(request.response.body, request.response.status_code)


# Close the web driver
driver.quit()