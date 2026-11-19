
import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(2)

action = ActionChains(driver)

driver.find_element(By.ID, "name").send_keys("Ashley Missy")
time.sleep(0.5)

driver.find_element(By.ID, "email").send_keys("ashlotmp@gmail.com")
time.sleep(0.5)

driver.find_element(By.ID, "phone").send_keys("0123456789")
time.sleep(0.5)

driver.find_element(By.ID, "textarea").send_keys("Minglanilla Cebu")
time.sleep(0.5)

driver.find_element(By.ID, "female").click()
time.sleep(0.5)

driver.find_element(By.ID, "saturday").click()
time.sleep(0.5)

driver.find_element(By.ID, "friday").click()
time.sleep(0.5)

country_fld = driver.find_element(By.ID, "country")
action.move_to_element(country_fld).perform()
Select(country_fld).select_by_value("germany")
time.sleep(0.5)

Select(driver.find_element(By.ID, "colors")).select_by_value("blue")
time.sleep(0.5)

Select(driver.find_element(By.ID, "animals")).select_by_value("deer")
time.sleep(0.5)

driver.find_element(By.ID, "datepicker").send_keys("11/19/2026")
time.sleep(0.5)

driver.find_element(By.ID, "txtDate").send_keys("17/11/2026")
time.sleep(0.5)

driver.find_element(By.ID, "start-date").send_keys("03/31/2026")
time.sleep(0.5)

driver.find_element(By.ID, "end-date").send_keys("04/09/2026")
time.sleep(0.5)

driver.find_element(By.CLASS_NAME, "submit-btn").click()
time.sleep(1)

home_txt = driver.find_element(By.LINK_TEXT, "Home")
action.move_to_element(home_txt).perform()
time.sleep(0.5)

posts_atom_txt = driver.find_element(By.LINK_TEXT, "Posts (Atom)")
action.key_down(Keys.CONTROL).click(posts_atom_txt).key_up(Keys.CONTROL).perform()
time.sleep(2)

driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

driver.find_element(By.ID, 'singleFileInput').send_keys(r"C:\Users\UCSOUTH\Downloads\jazz.jpg")
time.sleep(0.5)

btn_single_file_upload = driver.find_element(By.CSS_SELECTOR, '#singleFileForm button')
action.move_to_element(btn_single_file_upload).perform()
time.sleep(0.5)

btn_single_file_upload.click()
time.sleep(1)

multiple_file_upload = driver.find_element(By.ID, 'multipleFilesInput')
multiple_file_upload.send_keys(r"C:\Users\UCSOUTH\Downloads\buldak.jpg")
time.sleep(0.5)

multiple_file_upload.send_keys(r"C:\Users\UCSOUTH\Downloads\bokki.jpg")
time.sleep(0.5)

btn_multiple_file_upload = driver.find_element(By.CSS_SELECTOR, '#multipleFilesForm button')
action.move_to_element(btn_multiple_file_upload).perform()
time.sleep(0.5)

btn_multiple_file_upload.click()
time.sleep(1)

action.move_to_element(driver.find_element(By.XPATH, '//*[@id="productTable"]/tbody/tr[1]/td[4]/input')).perform()
time.sleep(1)

action.move_to_element(driver.find_element(By.XPATH, '//*[@id="productTable"]/tbody/tr[2]/td[4]/input')).perform()
time.sleep(1)

action.move_to_element(driver.find_element(By.XPATH, '//*[@id="productTable"]/tbody/tr[3]/td[4]/input')).perform()
time.sleep(1)

chk_smartwatch = driver.find_element(By.XPATH, '//*[@id="productTable"]/tbody/tr[4]/td[4]/input')
action.move_to_element(chk_smartwatch).perform()
time.sleep(1)

chk_smartwatch.click()
time.sleep(0.5)

driver.find_element(By.XPATH, '//*[@id="pagination"]/li[2]/a').click()
time.sleep(0.5)

driver.find_element(By.XPATH, '//*[@id="pagination"]/li[3]/a').click()
time.sleep(0.5)

driver.find_element(By.XPATH, '//*[@id="pagination"]/li[4]/a').click()
time.sleep(0.5)

chk_e_reader = driver.find_element(By.XPATH, '//*[@id="productTable"]/tbody/tr[1]/td[4]/input')
action.move_to_element(chk_e_reader).perform()
time.sleep(0.5)

chk_e_reader.click()
time.sleep(0.5)

wiki_input = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
action.move_to_element(wiki_input).perform()
time.sleep(0.5)

wiki_input.send_keys("Jazz", Keys.ENTER)
time.sleep(0.5)

action.move_to_element(driver.find_element(By.LINK_TEXT, 'Jazz')).perform()
time.sleep(0.5)

action.move_to_element(driver.find_element(By.LINK_TEXT, 'Jazz Saxophone')).perform()
time.sleep(0.5)

action.move_to_element(driver.find_element(By.LINK_TEXT, 'Jazz Singers')).perform()
time.sleep(0.5)

shrek_2 = driver.find_element(By.LINK_TEXT, 'Best Jazz')
action.move_to_element(shrek_2).perform()
time.sleep(0.5)

shrek_2.click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(0.5)

dynamic_button = driver.find_element(By.XPATH, '//*[@id="HTML5"]/div[1]/button')
action.move_to_element(dynamic_button).perform()
time.sleep(1)
dynamic_button.click()
time.sleep(0.5)
dynamic_button.click()
time.sleep(0.5)
dynamic_button.click()
time.sleep(0.5)
action.move_to_element(dynamic_button).perform()
time.sleep(1)

driver.find_element(By.ID, 'alertBtn').click()
time.sleep(0.5)
driver.switch_to.alert.accept()
time.sleep(0.5)

driver.find_element(By.ID, 'confirmBtn').click()
time.sleep(0.5)
driver.switch_to.alert.dismiss()
time.sleep(0.5)

driver.find_element(By.ID, 'promptBtn').click()
time.sleep(0.5)
driver.switch_to.alert.send_keys("Shrek")
time.sleep(0.5)
driver.switch_to.alert.accept()
time.sleep(0.5)

new_tab_btn = driver.find_element(By.XPATH, '//*[@id="HTML4"]/div[1]/button')
action.move_to_element(new_tab_btn).perform()
time.sleep(1)
new_tab_btn.click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(0.5)

popup_btn = driver.find_element(By.ID, 'PopUp')
action.move_to_element(popup_btn).perform()
time.sleep(1)
popup_btn.click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(0.5)

action.move_to_element(driver.find_element(By.CLASS_NAME, 'dropbtn')).perform()
time.sleep(1)
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Mobiles')).perform()
time.sleep(0.5)
laptops_link = driver.find_element(By.LINK_TEXT, 'Laptops')
action.move_to_element(laptops_link).perform()
time.sleep(0.5)
laptops_link.click()
time.sleep(0.5)

field1_txt = driver.find_element(By.ID, 'field1')
action.move_to_element(field1_txt).perform()
time.sleep(0.5)
copy_btn = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
action.move_to_element(copy_btn).perform()
time.sleep(0.5)
action.double_click(copy_btn).perform()
time.sleep(1)

draggable = driver.find_element(By.ID, 'draggable')
action.move_to_element(draggable).perform()
time.sleep(1)
action.drag_and_drop(draggable, driver.find_element(By.ID, 'droppable')).perform()
time.sleep(1)

slider_handles = driver.find_elements(By.CLASS_NAME, 'ui-slider-handle')
action.move_to_element(slider_handles[0]).perform()
time.sleep(1)
action.drag_and_drop_by_offset(slider_handles[0], 50, 0).perform()
time.sleep(1)
action.drag_and_drop_by_offset(slider_handles[1], -30, 0).perform()
time.sleep(1)

action.move_to_element(driver.find_element(By.XPATH, '//*[name()="circle"]')).perform()
time.sleep(0.5)
action.move_to_element(driver.find_element(By.XPATH, '//*[name()="rect"]')).perform()
time.sleep(0.5)
action.move_to_element(driver.find_element(By.XPATH, '//*[name()="polygon"]')).perform()
time.sleep(0.5)

driver.find_element(By.ID, 'comboBox').click()
time.sleep(0.5)
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", driver.find_element(By.ID, 'dropdown'))
time.sleep(1)
action.move_to_element(driver.find_element(By.XPATH, '//*[@id="dropdown"]/div[1]')).perform()
time.sleep(0.5)
action.move_to_element(driver.find_element(By.XPATH, '//*[@id="dropdown"]/div[2]')).perform()
time.sleep(0.5)
action.move_to_element(driver.find_element(By.XPATH, '//*[@id="dropdown"]/div[3]')).perform()
time.sleep(0.5)
item_90= driver.find_element(By.XPATH, '//*[@id="dropdown"]/div[90]')
action.move_to_element(item_90).perform()
time.sleep(0.5)
item_90.click()
time.sleep(0.5)

action.move_to_element(driver.find_element(By.ID, 'section1')).perform()
time.sleep(0.5)
driver.find_element(By.ID, 'input1').send_keys("Section 1")
time.sleep(0.5)
driver.find_element(By.ID, 'btn1').click()
time.sleep(0.5)

action.move_to_element(driver.find_element(By.ID, 'section2')).perform()
time.sleep(0.5)
driver.find_element(By.ID, 'input2').send_keys("Section 2")
time.sleep(0.5)
driver.find_element(By.ID, 'btn2').click()
time.sleep(0.5)

action.move_to_element(driver.find_element(By.ID, 'section3')).perform()
time.sleep(0.5)
driver.find_element(By.ID, 'input3').send_keys("Section 3")
time.sleep(0.5)
driver.find_element(By.ID, 'btn3').click()
time.sleep(0.5)

shadow_host = driver.find_element(By.ID, 'shadow_host')
action.move_to_element(shadow_host).perform()
time.sleep(1)
shadow_root = shadow_host.shadow_root
shadow_root.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys("Shadow DOM")
time.sleep(0.5)
shadow_root.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
time.sleep(0.5)
shadow_root.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(r"C:\Users\UCSOUTH\Downloads\jazz.jpg")
time.sleep(0.5)
action.move_to_element(shadow_root.find_element(By.CSS_SELECTOR, 'a')).perform()
time.sleep(0.5)
print(shadow_root.find_element(By.CSS_SELECTOR, '#nested_shadow_host').shadow_root.find_element(By.CSS_SELECTOR, '#nested_shadow_content').text)
time.sleep(1)

action.move_to_element(driver.find_element(By.ID, 'samsung')).perform()
time.sleep(0.5)
action.move_to_element(driver.find_element(By.ID, 'realme')).perform()
time.sleep(0.5)
action.move_to_element(driver.find_element(By.ID, 'moto')).perform()
time.sleep(0.5)

for laptop_id in ['apple', 'lenovo', 'dell']:
    laptop_link = driver.find_element(By.ID, laptop_id)
    action.move_to_element(laptop_link).perform()
    time.sleep(0.5)
    laptop_link.click()
    time.sleep(2)
    driver.back()
    time.sleep(1)

for code in ['400', '401', '403', '404', '408', '500', '502', '503']:
    broken_link = driver.find_element(By.LINK_TEXT, f'Errorcode {code}')
    action.move_to_element(broken_link).perform()
    time.sleep(0.5)
    broken_link.click()
    time.sleep(2)
    driver.back()
    time.sleep(1)

for link_text in ['Udemy Courses', 'Online Trainings', 'Blog', 'PlaywrightPractice', 'Hidden Elements & AJAX', 'Download Files']:
    nav_link = driver.find_element(By.LINK_TEXT, link_text)
    action.move_to_element(nav_link).perform()
    time.sleep(0.5)
    nav_link.click()
    time.sleep(2)
    driver.back()
    time.sleep(1)

# time.sleep(5)

action.move_to_element(
    driver.find_element(By.CLASS_NAME, "dropbtn")
).perform()
time.sleep(1)

action.move_to_element(
    driver.find_element(By.LINK_TEXT, "Mobiles")
).perform()
time.sleep(0.5)

laptops_link = driver.find_element(By.LINK_TEXT, "Laptops")
action.move_to_element(laptops_link).perform()
time.sleep(0.5)
laptops_link.click()
time.sleep(0.5)

field1_txt = driver.find_element(By.ID, "field1")
action.move_to_element(field1_txt).perform()
time.sleep(0.5)

copy_btn = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
action.move_to_element(copy_btn).perform()
action.double_click(copy_btn).perform()
time.sleep(1)

draggable = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

action.move_to_element(draggable).perform()
action.drag_and_drop(draggable, target).perform()
time.sleep(1)

slider_handles = driver.find_elements(By.CLASS_NAME, "ui-slider-handle")

action.move_to_element(slider_handles[0]).perform()
action.drag_and_drop_by_offset(slider_handles[0], 50, 0).perform()
time.sleep(1)

action.drag_and_drop_by_offset(slider_handles[1], -30, 0).perform()
time.sleep(1)

for element in ['//*[name()="circle"]',
                '//*[name()="rect"]',
                '//*[name()="polygon"]']:
    svg_element = driver.find_element(By.XPATH, element)
    action.move_to_element(svg_element).perform()
    time.sleep(0.5)

driver.find_element(By.ID, "comboBox").click()
time.sleep(0.5)

dropdown = driver.find_element(By.ID, "dropdown")
driver.execute_script(
    "arguments[0].scrollTop = arguments[0].scrollHeight", dropdown
)
time.sleep(1)

for i in range(1, 4):
    item = driver.find_element(
        By.XPATH, f'//*[@id="dropdown"]/div[{i}]'
    )
    action.move_to_element(item).perform()
    time.sleep(0.5)

item_90 = driver.find_element(By.XPATH, '//*[@id="dropdown"]/div[90]')
action.move_to_element(item_90).perform()
time.sleep(0.5)
item_90.click()
time.sleep(0.5)

for section, input_id, button_id in [
    ("section1", "input1", "btn1"),
    ("section2", "input2", "btn2"),
    ("section3", "input3", "btn3")
]:
    action.move_to_element(driver.find_element(By.ID, section)).perform()
    driver.find_element(By.ID, input_id).send_keys(section)
    time.sleep(0.5)
    driver.find_element(By.ID, button_id).click()
    time.sleep(0.5)

shadow_host = driver.find_element(By.ID, "shadow_host")
action.move_to_element(shadow_host).perform()
time.sleep(1)

shadow_root = shadow_host.shadow_root

shadow_root.find_element(
    By.CSS_SELECTOR, 'input[type="text"]'
).send_keys("Shadow DOM")
time.sleep(0.5)

shadow_root.find_element(
    By.CSS_SELECTOR, 'input[type="checkbox"]'
).click()
time.sleep(0.5)

shadow_file = r"C:\Users\YOUR_USERNAME\Pictures\sample.jpg"

if os.path.isfile(shadow_file):
    shadow_root.find_element(
        By.CSS_SELECTOR, 'input[type="file"]'
    ).send_keys(shadow_file)

time.sleep(0.5)

nested_host = shadow_root.find_element(
    By.CSS_SELECTOR, "#nested_shadow_host"
)

nested_root = nested_host.shadow_root

print(
    nested_root.find_element(
        By.CSS_SELECTOR, "#nested_shadow_content"
    ).text
)

time.sleep(1)

for phone_id in ["samsung", "realme", "moto"]:
    phone = driver.find_element(By.ID, phone_id)
    action.move_to_element(phone).perform()
    time.sleep(0.5)

for laptop_id in ["apple", "lenovo", "dell"]:
    laptop_link = driver.find_element(By.ID, laptop_id)
    action.move_to_element(laptop_link).perform()
    time.sleep(0.5)
    laptop_link.click()
    time.sleep(2)
    driver.back()
    time.sleep(1)

for code in ["400", "401", "403", "404", "408", "500", "502", "503"]:
    broken_link = driver.find_element(
        By.LINK_TEXT, f"Errorcode {code}"
    )
    action.move_to_element(broken_link).perform()
    time.sleep(0.5)
    broken_link.click()
    time.sleep(2)
    driver.back()
    time.sleep(1)

for link_text in [
    "Udemy Courses",
    "Online Trainings",
    "Blog",
    "PlaywrightPractice",
    "Hidden Elements & AJAX",
    "Download Files"
]:
    nav_link = driver.find_element(By.LINK_TEXT, link_text)
    action.move_to_element(nav_link).perform()
    time.sleep(0.5)
    nav_link.click()
    time.sleep(2)
    driver.back()
    time.sleep(1)

time.sleep(5)
driver.quit()
