import Engine as eng
text=""
def commands(text):
    
    if "login" in text:
        txt_username= '//*[@id="fm-login-id"]'
        txt_password= '//*[@id="fm-login-password"]'
        btn_signin='//*[@id="login-form"]/div[5]/button'

        url='https://login.aliexpress.com/'
        eng.page_load(url)

        eng.ebay_sign_in("email",txt_username,txt_password)
        eng.ebay_sign_in("password",txt_username,txt_password)
        eng.signin(btn_signin)

    elif "help" in text: 
        url='https://github.com/Hishan98/Python-Project/tree/master'
        eng.Help(url)

    elif "sign up" in text: 
        txt_email='//*[@id="expressbuyerlogin"]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[1]/input'
        txt_password='//*[@id="expressbuyerlogin"]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[2]/input'
        btn_show_password='//*[@id="expressbuyerlogin"]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[2]/span'
        btn_signup='//*[@id="expressbuyerlogin"]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[5]/a'

        url='https://reg.ebay.com/reg/PartialReg'
        eng.page_load(url)

        signup_page='//*[@id="expressbuyerlogin"]/div/div[2]/div[1]/div/ul/li[1]/div'
        eng.ali_signup_page(signup_page)

        eng.ali_sign_up("email",txt_email,txt_password,btn_show_password)
        eng.ali_sign_up("password",txt_email,txt_password,btn_show_password)
        eng.ali_signup(btn_signup)

    elif text=="close": 
        import speech as sp
        sp.speak("Thank You For using Aliexpress") 
        url='chrome-search://local-ntp/local-ntp.html'
        eng.newtab(url)
        import webreopening as Main
        Main.site_selection2()

    elif text=="back":
        eng.back()
    elif "scroll up" in text:
        eng.scroll_up()  
    elif "scroll down" in text:
        eng.scroll_down()
    elif "delete" in text:
        txt_delete='//*[@id="search-key"]'
        eng.delete(txt_delete)
    elif "backspace" in text:
        txt_backspace='//*[@id="search-key"]'
        eng.backspace(txt_backspace)
    elif text=="ok":
        btn_search_ok='//*[@id="form-searchbar"]/div[1]/input'
        eng.okay(btn_search_ok)

    # select an item form the search results
   
    elif "first link" in text:
        getlist='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul' 
        getclass='list-item'
        setnumber=1
        getitem='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/li['+str(setnumber)+']/div/div[2]/div[1]/div[1]/a' 
        try_getitem='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/div[1]/li['+str(setnumber)+']/div/div[2]/div/div[1]/a'
        eng.ali_click_list(getlist,getclass,getitem,setnumber,try_getitem)

    elif "second link" in text: 
        getlist='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul' 
        getclass='list-item'
        setnumber=2
        getitem='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/li['+str(setnumber)+']/div/div[2]/div[1]/div[1]/a' 
        try_getitem='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/div[1]/li['+str(setnumber)+']/div/div[2]/div/div[1]/a'
        eng.ali_click_list(getlist,getclass,getitem,setnumber,try_getitem)

    elif "third link" in text:
        getlist='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul' 
        getclass='list-item'
        setnumber=3
        getitem='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/li['+str(setnumber)+']/div/div[2]/div[1]/div[1]/a' 
        try_getitem='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/div[1]/li['+str(setnumber)+']/div/div[2]/div/div[1]/a'
        eng.ali_click_list(getlist,getclass,getitem,setnumber,try_getitem)

    elif "fourth link" in text:
        getlist='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul' 
        getclass='list-item'
        setnumber=4
        getitem='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/li['+str(setnumber)+']/div/div[2]/div[1]/div[1]/a' 
        try_getitem='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/div[1]/li['+str(setnumber)+']/div/div[2]/div/div[1]/a'
        eng.ali_click_list(getlist,getclass,getitem,setnumber,try_getitem)

    elif "V link" in text:
        getlist='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul' 
        getclass='list-item'
        setnumber=5
        getitem='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/li['+str(setnumber)+']/div/div[2]/div[1]/div[1]/a' 
        try_getitem='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/div[1]/li['+str(setnumber)+']/div/div[2]/div/div[1]/a'
        eng.ali_click_list(getlist,getclass,getitem,setnumber,try_getitem)

    # Item selections (Colors/Sizes & etc.)

    elif "first item" in text:

        maindiv='//*[@id="root"]/div/div[2]/div/div[2]/div[7]/div'
        subdivs='sku-property'

        getlist='//*[@id="root"]/div/div[2]/div/div[2]/div[7]/div/div[1]/ul'
        gettagname='sku-property-item'
        Selection=1
        getitem='//*[@id="root"]/div/div[2]/div/div[2]/div[7]/div/div/ul/li[1]/div'

        eng.ali_click_sub_list(getlist,gettagname,getitem,Selection,maindiv,subdivs)
        
    elif "second item" in text:
        getlist='//*[@id="root"]/div/div[2]/div/div[2]/div[7]/div/div/ul'
        gettagname='sku-property-item'
        Selection=2
        getitem='//*[@id="root"]/div/div[2]/div/div[2]/div[7]/div/div/ul/li['+str(Selection)+']/div/img'
        eng.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "third item" in text:
        getlist='//*[@id="root"]/div/div[2]/div/div[2]/div[7]/div/div/ul'
        gettagname='sku-property-item'
        Selection=3
        getitem='//*[@id="root"]/div/div[2]/div/div[2]/div[7]/div/div/ul/li['+str(Selection)+']/div/img'
        eng.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "fourth item" in text:
        getlist='//*[@id="root"]/div/div[2]/div/div[2]/div[7]/div/div/ul'
        gettagname='sku-property-item'
        Selection=4
        getitem='//*[@id="root"]/div/div[2]/div/div[2]/div[7]/div/div/ul/li['+str(Selection)+']/div/img'
        eng.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "V item" in text:
        getlist='//*[@id="root"]/div/div[2]/div/div[2]/div[7]/div/div/ul'
        gettagname='sku-property-item'
        Selection=5
        getitem='//*[@id="root"]/div/div[2]/div/div[2]/div[7]/div/div/ul/li['+str(Selection)+']/div/img'
        eng.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "set" in text:
        txt_quantity='//*[@id="root"]/div/div[2]/div/div[2]/div[8]/span/span/span[2]/input'
        eng.ali_quantity("quentity",txt_quantity)

    # Buying Options

    elif "add to cart" in text:
        btn_add_to_cart='//*[@id="root"]/div/div[2]/div/div[2]/div[11]/span[2]/button'
        eng.add_to_cart(btn_add_to_cart)

    elif "feedback" in text:
        btn_feedbacks='//*[@id="product-detail"]/div[1]/div/div[1]/ul/li[2]/div/span'
        eng.feedbacks(btn_feedbacks)

    elif "buy it now" in text:
        btn_buy_it_now='//*[@id="root"]/div/div[2]/div/div[2]/div[11]/span[1]/button'
        eng.buy_it_now(btn_buy_it_now)

    elif "pay" in text:
        btn_confirm_pay='//*[@id="product-detail"]/div[1]/div/div[1]/ul/li[2]/div/span'
        eng.confirm_pay(btn_confirm_pay)

    elif "close ads" in text:
        eng.close_ads()

    elif "search" in text:
        url='https://www.aliexpress.com/'
        txt_searchbar='//*[@id="search-key"]'
        eng.search(url,txt_searchbar)
    else:
        eng.unknown_command()