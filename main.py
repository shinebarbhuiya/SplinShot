
# ยฉ Shine Barbhuiya โข
# ยฉ @shinebarbhuiya
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

from pyrogram import Client, filters

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time
import pickle



chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--headless')




app = Client(
   "SplinShot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

start_msg = """

๐ค Welcome to SplinShot! ๐ค


๐น /insta {username} to get user bio
๐ /google {keyword} to get google search result 
๐ป /donate to donate me

Made with ๐พ by @shinebarbhuiya

"""

# google_msg = """

# ๐ Google Search ๐

# ๐Searching for 


# """


@app.on_message(filters.command(['insta']) & (filters.forwarded | filters.reply | filters.private))
async def insta(client, message):

    chrome_options.add_argument('window-size=791x441')

    insta_msg = f"""

๐ฅ Instagram Search ๐ฅ

๐Searching for {message.text.split()[-1]} ๐

Made With ๐ก By @shinebarbhuiya


"""

    txt =  await message.reply_text(insta_msg)

    
    
    # txt =  await message.reply_text("Getting screenshot for " + message.text.split()[-1])
    print(message.text.split()[-1])
    print(client)
    insta_msg = f"""

๐ฅ Instagram Search ๐ฅ

๐Getting the data . . . for {message.text.split()[-1]} ๐

Made With ๐ก By @shinebarbhuiya


"""
    await txt.edit(insta_msg)


    driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    username = message.text.replace('/insta ', '')
    print(username)

    print(username)
    print(type(username))
    
    
    # await txt.edit(text = "Just a little time more")
    
    driver.get("https://www.instagram.com/")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    # print("reached step 2")
    driver.get(f"https://www.instagram.com/{username}")
    print(f"https://www.instagram.com/{username}")

    

    insta_msg = """

๐ฅ Instagram Search ๐ฅ

๐ Success! Here is the image - } ๐

Made With ๐ก By @shinebarbhuiya


"""

    print("Reached Step 3")
    driver.save_screenshot("ss.png")
    await txt.edit(insta_msg)

    await app.send_photo(chat_id = message.chat.id, photo='ss.png')   
    os.remove('ss.png')          
    driver.quit()
    
    
@app.on_message(filters.command(['start']) & filters.private)
async def start(client, message):
    await message.reply_text(start_msg)

@app.on_message(filters.command(['help']) & filters.private)
async def help(client, message):
    await message.reply_text(start_msg)


@app.on_message(filters.command(['donate']) & filters.private)
async def donate(client, message):
    await message.reply_text("Thank you for it but I am too lazy to set up donation now! ๐คฅ")



@app.on_message(filters.command(['google']) & (filters.forwarded | filters.reply | filters.private))
async def google(client, message):
  
  search = message.text.replace('/google ','')
  google_msg = f"""

๐ Google Search ๐

๐Searching for {search} ๐

Made With ๐ก By @shinebarbhuiya


"""
  search = search.replace(' ','+') 
  print(search)
  
  txt = await message.reply_text(google_msg)

  driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
  
  driver.get(f'https://www.google.com/search?q={search}')
  # time.sleep(5)

  ele=driver.find_element("xpath", '//*[@id="rcnt"]')
  total_height = ele.size["height"]
  google_msg = f"""

๐ Google Search ๐

๐Making Request To The Google Server ๐

Made With ๐ก By @shinebarbhuiya


"""
  await txt.edit(text = google_msg) 

  driver.set_window_size(1313, total_height)      #the trick
  time.sleep(2)
  page1 = driver.title
  driver.save_screenshot(f"{page1}.png")
  google_msg = f"""

๐ Google Search ๐

๐Got The First Page. . . Sending You Now ๐

Made With ๐ก By @shinebarbhuiya


"""

  await txt.edit(text = google_msg) 
  await app.send_document(message.chat.id,f'{page1}.png', caption="@shinebarbhuiya" )
  # driver.save_screenshot("screenshot1.png")

  next_page_button = driver.find_element_by_xpath('//*[@id="xjs"]/table/tbody/tr/td[3]/a')

  next_page_button.click()
  # time.sleep(3)
  google_msg = f"""

๐ Google Search ๐

๐Getting Second Page. . . ๐

Made With ๐ก By @shinebarbhuiya


"""
  await txt.edit(text = google_msg) 

  el = driver.find_element_by_tag_name('body')
  page2 = driver.title
  el.screenshot(f"{page2}.png")
  google_msg = f"""

๐ Google Search ๐

๐Success!!! ๐

Made With ๐ก By @shinebarbhuiya


"""

  await txt.edit(text = google_msg)

  await app.send_document(message.chat.id, f'{page2}.png', caption = "@shinebarbhuiya")

  os.remove(f'{page1}.png')
  # os.remove(f"{page2}.png")
  driver.quit()


app.run()  # Automatically start() and idle()
