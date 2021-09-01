
# © Shine Barbhuiya ™
# © @shinebarbhuiya
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

from pyrogram import Client, filters

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time
import pickle



chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('headless')




app = Client(
   "SplinShot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

start_msg = """

🤖 Welcome to SplinShot! 🤖


👹 /insta {username} to get user bio
🔍 /google {keyword} to get google search result 
👻 /donate to donate me

Made with 👾 by @shinebarbhuiya

"""

# google_msg = """

# 📟 Google Search 📟

# 🔍Searching for 


# """


@app.on_message(filters.command(['insta']) & (filters.forwarded | filters.reply | filters.private))
async def insta(client, message):

    chrome_options.add_argument('window-size=791x441')

    insta_msg = f"""

🔥 Instagram Search 🔥

🔍Searching for {message.text.split()[-1]} 🔍

Made With 💡 By @shinebarbhuiya


"""

    txt =  await message.reply_text(insta_msg)

    
    
    # txt =  await message.reply_text("Getting screenshot for " + message.text.split()[-1])
    print(message.text.split()[-1])
    print(client)
    insta_msg = f"""

🔥 Instagram Search 🔥

🔍Getting the data . . . for {message.text.split()[-1]} 🔍

Made With 💡 By @shinebarbhuiya


"""
    await txt.edit(insta_msg)


    driver = webdriver.Chrome(options=chrome_options)

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

🔥 Instagram Search 🔥

🔍 Success! Here is the image - } 🔍

Made With 💡 By @shinebarbhuiya


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
    await message.reply_text("Thank you for it but I am too lazy to set up donation now! 🤥")



@app.on_message(filters.command(['google']) & (filters.forwarded | filters.reply | filters.private))
async def google(client, message):
  
  search = message.text.replace('/google ','')
  google_msg = f"""

📟 Google Search 📟

🔍Searching for {search} 🔍

Made With 💡 By @shinebarbhuiya


"""
  search = search.replace(' ','+') 
  print(search)
  
  txt = await message.reply_text(google_msg)

  driver = webdriver.Chrome(options=chrome_options)
  
  driver.get(f'https://www.google.com/search?q={search}')
  # time.sleep(5)

  ele=driver.find_element("xpath", '//*[@id="rcnt"]')
  total_height = ele.size["height"]
  google_msg = f"""

📟 Google Search 📟

🔍Making Request To The Google Server 🔍

Made With 💡 By @shinebarbhuiya


"""
  await txt.edit(text = google_msg) 

  driver.set_window_size(1313, total_height)      #the trick
  time.sleep(2)
  page1 = driver.title
  driver.save_screenshot(f"{page1}.png")
  google_msg = f"""

📟 Google Search 📟

🔍Got The First Page. . . Sending You Now 🔍

Made With 💡 By @shinebarbhuiya


"""

  await txt.edit(text = google_msg) 
  await app.send_document(message.chat.id,f'{page1}.png', caption="@shinebarbhuiya" )
  # driver.save_screenshot("screenshot1.png")

  next_page_button = driver.find_element_by_xpath('//*[@id="xjs"]/table/tbody/tr/td[3]/a')

  next_page_button.click()
  # time.sleep(3)
  google_msg = f"""

📟 Google Search 📟

🔍Getting Second Page. . . 🔍

Made With 💡 By @shinebarbhuiya


"""
  await txt.edit(text = google_msg) 

  el = driver.find_element_by_tag_name('body')
  page2 = driver.title
  el.screenshot(f"{page2}.png")
  google_msg = f"""

📟 Google Search 📟

🔍Success!!! 🔍

Made With 💡 By @shinebarbhuiya


"""

  await txt.edit(text = google_msg)

  await app.send_document(message.chat.id, f'{page2}.png', caption = "@shinebarbhuiya")

  os.remove(f'{page1}.png')
  # os.remove(f"{page2}.png")
  driver.quit()


app.run()  # Automatically start() and idle()