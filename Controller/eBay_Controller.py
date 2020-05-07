import Engine as eng
text=""
def commands(text):

    if "login" in text:
        txt_username= '//*[@id="userid"]'
        txt_password= '//*[@id="pass"]'
        btn_signin='//*[@id="sgnBt"]'

        url='https://www.ebay.com/signin/'
        eng.page_load(url)

        eng.ebay_sign_in("email",txt_username,txt_password)
        eng.ebay_sign_in("password",txt_username,txt_password)
        eng.signin(btn_signin)

    elif "help" in text: 
        url='https://github.com/Hishan98/Python-Project/tree/master'
        eng.Help(url)

    elif "sign up" in text: 
        txt_firstname='//*[@id="firstname"]'
        txt_lastname='//*[@id="lastname"]'
        txt_email='//*[@id="email"]'
        txt_password='//*[@id="PASSWORD"]'
        btn_show_password='//*[@id="showPASSWORD"]/ul/li/span[2]'
        btn_signup='//*[@id="ppaFormSbtBtn"]'

        url='https://reg.ebay.com/reg/PartialReg'
        eng.page_load(url)

        eng.ebay_sign_up("firstname",txt_firstname,txt_lastname,txt_email,txt_password,btn_show_password)
        eng.ebay_sign_up("lastname",txt_firstname,txt_lastname,txt_email,txt_password,btn_show_password)
        eng.ebay_sign_up("email",txt_firstname,txt_lastname,txt_email,txt_password,btn_show_password)
        eng.ebay_sign_up("password",txt_firstname,txt_lastname,txt_email,txt_password,btn_show_password)
        eng.signup(btn_signup)

    elif text=="close": 
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
        txt_delete='//*[@id="gh-ac"]'
        eng.delete(txt_delete)
    elif "backspace" in text:
        txt_backspace='//*[@id="gh-ac"]'
        eng.backspace(txt_backspace)
    elif text=="ok":
        btn_search_ok='//*[@id="gh-btn"]'
        eng.okay(btn_search_ok)

    # select an item form the search results
   
    elif "first link" in text:
        getlist='//*[@id="srp-river-results"]/ul'
        getclass='s-item   '
        setnumber=1
        getitem='//*[@id="srp-river-results"]/ul/li['+str(setnumber)+']/div/div[2]/a' 
        eng.click_list(getlist,getclass,getitem,setnumber)

    elif "second link" in text: 
        getlist='//*[@id="srp-river-results"]/ul'
        getclass='s-item   '
        setnumber=2
        getitem='//*[@id="srp-river-results"]/ul/li['+str(setnumber)+']/div/div[2]/a' 
        eng.click_list(getlist,getclass,getitem,setnumber)

    elif "third link" in text:
        getlist='//*[@id="srp-river-results"]/ul'
        getclass='s-item   '
        setnumber=3
        getitem='//*[@id="srp-river-results"]/ul/li['+str(setnumber)+']/div/div[2]/a' 
        eng.click_list(getlist,getclass,getitem,setnumber) 

    elif "fourth link" in text:
        getlist='//*[@id="srp-river-results"]/ul'
        getclass='s-item   '
        setnumber=4
        getitem='//*[@id="srp-river-results"]/ul/li['+str(setnumber)+']/div/div[2]/a' 
        eng.click_list(getlist,getclass,getitem,setnumber) 

    elif "V link" in text:
        getlist='//*[@id="srp-river-results"]/ul'
        getclass='s-item   '
        setnumber=5
        getitem='//*[@id="srp-river-results"]/ul/li['+str(setnumber)+']/div/div[2]/a' 
        eng.click_list(getlist,getclass,getitem,setnumber)    

    # Item selections (Colors/Sizes & etc.)

    elif "select" in text:
        drop_list= '//*[@id="msku-sel-1"]'
        eng.drop_down_list(drop_list)

    elif "first item" in text:
        getlist='//*[@id="msku-sel-1"]'
        gettagname='option'
        Selection=0
        getitem='//*[@id="msku-opt-'+str(Selection)+'"]'
        eng.click_sub_list(getlist,gettagname,getitem,Selection)
    elif "second item" in text:
        getlist='//*[@id="msku-sel-1"]'
        gettagname='option'
        Selection=1
        getitem='//*[@id="msku-opt-'+str(Selection)+'"]'
        eng.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "third item" in text:
        getlist='//*[@id="msku-sel-1"]'
        gettagname='option'
        Selection=2
        getitem='//*[@id="msku-opt-'+str(Selection)+'"]'
        eng.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "fourth item" in text:
        getlist='//*[@id="msku-sel-1"]'
        gettagname='option'
        Selection=3
        getitem='//*[@id="msku-opt-'+str(Selection)+'"]'
        eng.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "V item" in text:
        getlist='//*[@id="msku-sel-1"]'
        gettagname='option'
        Selection=4
        getitem='//*[@id="msku-opt-'+str(Selection)+'"]'
        eng.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "set" in text:
        txt_quantity='//*[@id="qtyTextBox"]'
        eng.quantity("quentity",txt_quantity)

    # Buying Options

    elif "add to cart" in text:
        btn_add_to_cart='//*[@id="isCartBtn_btn"]'
        eng.add_to_cart(btn_add_to_cart)
    elif "watch list" in text:
        btn_watch_list='//*[@id="vi-atl-lnk"]/a/span[2]'
        eng.watch_list(btn_watch_list)
    elif "feedback" in text:
        btn_feedbacks='//*[@id="byrfdbk_atf_lnk_sm"]'
        eng.feedbacks(btn_feedbacks)
    elif "buy it now" in text:
        btn_buy_it_now='//*[@id="binBtn_btn"]'
        eng.buy_it_now(btn_buy_it_now)
    elif "pay" in text:
        btn_confirm_pay='//*[@id="page-form"]/div/button'
        eng.confirm_pay(btn_confirm_pay)

    #Selling Options
    # elif "sale" in text:
    #     import ebay_sell as eb
    #     eng.sell(wait,driver)

    elif "search" in text:
        url='https://www.ebay.com/'
        txt_searchbar='//*[@id="gh-ac"]'
        eng.search(url,txt_searchbar)