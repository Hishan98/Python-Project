import ebay as eb
text=""
def commands(text):

    if "login" in text:
        txt_username= '//*[@id="userid"]'
        txt_password= '//*[@id="pass"]'
        btn_signin='//*[@id="sgnBt"]'

        url='https://www.ebay.com/signin/'
        eb.page_load(url)

        eb.ebay_sign_in("email",txt_username,txt_password)
        eb.ebay_sign_in("password",txt_username,txt_password)
        eb.signin(btn_signin)

    elif "sign up" in text: 
        txt_firstname='//*[@id="firstname"]'
        txt_lastname='//*[@id="lastname"]'
        txt_email='//*[@id="email"]'
        txt_password='//*[@id="PASSWORD"]'
        btn_show_password='//*[@id="showPASSWORD"]/ul/li/span[2]'
        btn_signup='//*[@id="ppaFormSbtBtn"]'

        url='https://reg.ebay.com/reg/PartialReg'
        eb.page_load(url)

        eb.ebay_sign_up("firstname",txt_firstname,txt_lastname,txt_email,txt_password,btn_show_password)
        eb.ebay_sign_up("lastname",txt_firstname,txt_lastname,txt_email,txt_password,btn_show_password)
        eb.ebay_sign_up("email",txt_firstname,txt_lastname,txt_email,txt_password,btn_show_password)
        eb.ebay_sign_up("password",txt_firstname,txt_lastname,txt_email,txt_password,btn_show_password)
        eb.signup(btn_signup)

    elif text=="exit": 
        eb.driver.close()
    elif text=="back":
        eb.back()
    elif "scroll up" in text:
        eb.scroll_up()  
    elif "scroll down" in text:
        eb.scroll_down()
    elif "delete" in text:
        txt_delete='//*[@id="gh-ac"]'
        eb.delete(txt_delete)
    elif "backspace" in text:
        txt_backspace='//*[@id="gh-ac"]'
        eb.backspace(txt_backspace)
    elif text=="ok":
        btn_search_ok='//*[@id="gh-btn"]'
        eb.okay(btn_search_ok)

    # select an item form the search results
   
    elif "first link" in text:
        getlist='//*[@id="srp-river-results"]/ul'
        getclass='s-item   '
        setnumber=1
        getitem='//*[@id="srp-river-results-listing'+str(setnumber)+'"]/div/div[2]/a' 
        eb.click_list(getlist,getclass,getitem,setnumber)

    elif "second link" in text: 
        getlist='//*[@id="srp-river-results"]/ul'
        getclass='s-item   '
        setnumber=2
        getitem='//*[@id="srp-river-results-listing'+str(setnumber)+'"]/div/div[2]/a' 
        eb.click_list(getlist,getclass,getitem,setnumber)

    elif "third link" in text:
        getlist='//*[@id="srp-river-results"]/ul'
        getclass='s-item   '
        setnumber=3
        getitem='//*[@id="srp-river-results-listing'+str(setnumber)+'"]/div/div[2]/a' 
        eb.click_list(getlist,getclass,getitem,setnumber) 

    elif "fourth link" in text:
        getlist='//*[@id="srp-river-results"]/ul'
        getclass='s-item   '
        setnumber=4
        getitem='//*[@id="srp-river-results-listing'+str(setnumber)+'"]/div/div[2]/a' 
        eb.click_list(getlist,getclass,getitem,setnumber) 

    elif "V link" in text:
        getlist='//*[@id="srp-river-results"]/ul'
        getclass='s-item   '
        setnumber=5
        getitem='//*[@id="srp-river-results-listing'+str(setnumber)+'"]/div/div[2]/a' 
        eb.click_list(getlist,getclass,getitem,setnumber)    

    # Item selections (Colors/Sizes & etc.)

    elif "select" in text:
        drop_list= '//*[@id="msku-sel-1"]'
        eb.drop_down_list(drop_list)

    elif "first item" in text:
        getlist='//*[@id="msku-sel-1"]'
        gettagname='option'
        Selection=0
        getitem='//*[@id="msku-opt-'+str(Selection)+'"]'
        eb.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "second item" in text:
        getlist='//*[@id="msku-sel-1"]'
        gettagname='option'
        Selection=1
        getitem='//*[@id="msku-opt-'+str(Selection)+'"]'
        eb.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "third item" in text:
        getlist='//*[@id="msku-sel-1"]'
        gettagname='option'
        Selection=2
        getitem='//*[@id="msku-opt-'+str(Selection)+'"]'
        eb.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "fourth item" in text:
        getlist='//*[@id="msku-sel-1"]'
        gettagname='option'
        Selection=3
        getitem='//*[@id="msku-opt-'+str(Selection)+'"]'
        eb.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "V item" in text:
        getlist='//*[@id="msku-sel-1"]'
        gettagname='option'
        Selection=4
        getitem='//*[@id="msku-opt-'+str(Selection)+'"]'
        eb.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "set" in text:
        txt_quantity='//*[@id="qtyTextBox"]'
        eb.quantity("quentity",txt_quantity)

    # Buying Options

    elif "add to cart" in text:
        btn_add_to_cart='//*[@id="isCartBtn_btn"]'
        eb.add_to_cart(btn_add_to_cart)
    elif "watch list" in text:
        btn_watch_list='//*[@id="vi-atl-lnk"]/a/span[2]'
        eb.watch_list(btn_watch_list)
    elif "feedback" in text:
        btn_feedbacks='//*[@id="byrfdbk_atf_lnk_sm"]'
        eb.feedbacks(btn_feedbacks)
    elif "buy it now" in text:
        btn_buy_it_now='//*[@id="binBtn_btn"]'
        eb.buy_it_now(btn_buy_it_now)
    elif "pay" in text:
        btn_confirm_pay='//*[@id="page-form"]/div/button'
        eb.confirm_pay(btn_confirm_pay)

    #Selling Options
    # elif "sale" in text:
    #     import ebay_sell as eb
    #     eb.sell(wait,driver)

    elif "search" in text:
        url='https://www.ebay.com/'
        txt_searchbar='//*[@id="gh-ac"]'
        eb.search(url,txt_searchbar)