import Engine as eng
text=""
def commands(text):

    if "login" in text:
        txt_username= '//*[@id="ap_email"]'
        btn_continue= '//*[@id="continue"]'

        txt_password= '//*[@id="ap_password"]'
        btn_signin='//*[@id="signInSubmit"]'

        btn_auth='//*[@id="continue"]'
        txt_OTP='//*[@id="cvf-page-content"]/div/div/div[1]/form/div[2]/input'
        btn_OTP='//*[@id="a-autoid-0"]/span/input'

        url='https://amazon.com/gp/sign-in.html'
        eng.page_load(url)

        eng.ebay_sign_in("email",txt_username,txt_password)
        eng.amazon_signin_continue(btn_continue)
        eng.ebay_sign_in("password",txt_username,txt_password)
        eng.signin(btn_signin)

        eng.amazon_signin_auth(btn_auth)

        eng.enter_otp("otp",txt_OTP)
        eng.btn_otp(btn_OTP)

    elif "help" in text: 
        url='https://github.com/Hishan98/Python-Project/tree/master'
        eng.Help(url)

    elif "sign up" in text: 
        txt_firstname='//*[@id="ap_customer_name"]'
        txt_email='//*[@id="ap_email"]'
        txt_password='//*[@id="ap_password"]'
        txt_re_password='//*[@id="ap_password_check"]'
        btn_signup='//*[@id="continue"]'

        txt_OTP='//*[@id="cvf-page-content"]/div/div/div[1]/form/div[2]/input'
        btn_OTP='//*[@id="a-autoid-0"]/span/input'

        url='https://www.amazon.com/ap/register?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_custrec_newcust'
        eng.page_load(url)

        eng.amazon_sign_up("firstname",txt_firstname,txt_email,txt_password,txt_re_password)
        eng.amazon_sign_up("email",txt_firstname,txt_email,txt_password,txt_re_password)
        eng.amazon_sign_up("password",txt_firstname,txt_email,txt_password,txt_re_password)
        eng.amazon_signup(btn_signup)

        eng.enter_otp("otp",txt_OTP)
        eng.btn_otp(btn_OTP)

    elif "resend otp" in text: 
        btn_resendOTP='//*[@id="cvf-page-content"]/div/div/div[1]/form/div[6]/a'
        eng.resend_otp(btn_resendOTP)

    elif text=="exit": 
        eng.driver.close()
    elif text=="back":
        eng.back()
    elif "scroll up" in text:
        eng.scroll_up()  
    elif "scroll down" in text:
        eng.scroll_down()
    elif "delete" in text:
        txt_delete='//*[@id="twotabsearchtextbox"]'
        eng.delete(txt_delete)
    elif "backspace" in text:
        txt_backspace='//*[@id="twotabsearchtextbox"]'
        eng.backspace(txt_backspace)
    elif text=="ok":
        btn_search_ok='//*[@id="nav-search"]/form/div[2]/div/input'
        eng.okay(btn_search_ok)

    # select an item form the search results
   
    elif "first link" in text:
        getlist='//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]'
        getclass='sg-col-inner'
        setnumber=1
        getitem='//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div['+str(setnumber)+']/div/span/div/div/div[2]/h2/a'
        eng.amazon_click_list(getlist,getclass,getitem,setnumber)

    elif "second link" in text: 
        getlist='//*[@id="anonCarousel1"]/ol'
        getclass='a-carousel-card'
        setnumber=1
        getitem='//*[@id="anonCarousel1"]/ol/li['+str(setnumber)+']/div/div/div[2]/h2/a' 
        eng.click_list(getlist,getclass,getitem,setnumber)

    elif "third link" in text:
        getlist='//*[@id="anonCarousel1"]/ol'
        getclass='a-carousel-card'
        setnumber=1
        getitem='//*[@id="anonCarousel1"]/ol/li['+str(setnumber)+']/div/div/div[2]/h2/a' 
        eng.click_list(getlist,getclass,getitem,setnumber)

    elif "fourth link" in text:
        getlist='//*[@id="anonCarousel1"]/ol'
        getclass='a-carousel-card'
        setnumber=1
        getitem='//*[@id="anonCarousel1"]/ol/li['+str(setnumber)+']/div/div/div[2]/h2/a' 
        eng.click_list(getlist,getclass,getitem,setnumber)

    elif "V link" in text:
        getlist='//*[@id="anonCarousel1"]/ol'
        getclass='a-carousel-card'
        setnumber=1
        getitem='//*[@id="anonCarousel1"]/ol/li['+str(setnumber)+']/div/div/div[2]/h2/a' 
        eng.click_list(getlist,getclass,getitem,setnumber)   

    # Item selections (Colors/Sizes & etc.)

    elif "first item" in text:
        getlist='//*[@id="variation_color_name"]/ul'
        gettagname='//*[@id="color_name_0"]'
        Selection=10
        getitem='//*[@id="a-autoid-'+str(Selection)+'-announce"]/div/div[1]/img'
        eng.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "second item" in text:
        getlist='//*[@id="variation_color_name"]/ul'
        gettagname='//*[@id="color_name_0"]'
        Selection=11
        getitem='//*[@id="a-autoid-'+str(Selection)+'-announce"]/div/div[1]/img'
        eng.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "third item" in text:
        getlist='//*[@id="variation_color_name"]/ul'
        gettagname='//*[@id="color_name_0"]'
        Selection=12
        getitem='//*[@id="a-autoid-'+str(Selection)+'-announce"]/div/div[1]/img'
        eng.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "fourth item" in text:
        getlist='//*[@id="variation_color_name"]/ul'
        gettagname='//*[@id="color_name_0"]'
        Selection=13
        getitem='//*[@id="a-autoid-'+str(Selection)+'-announce"]/div/div[1]/img'
        eng.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "V item" in text:
        getlist='//*[@id="variation_color_name"]/ul'
        gettagname='//*[@id="color_name_0"]'
        Selection=14
        getitem='//*[@id="a-autoid-'+str(Selection)+'-announce"]/div/div[1]/img'
        eng.click_sub_list(getlist,gettagname,getitem,Selection)

    elif "buying options" in text:
        btn_buyingopt='//*[@id="buybox-see-all-buying-choices-announce"]'
        eng.buyingopt_button_click(btn_buyingopt)

    elif "add to list" in text:
        btn_addTolist='//*[@id="wishListMainButton-announce"]'
        eng.common_button_click(btn_addTolist)

    # Buying Options
    elif "buy now" in text:
        btn_buy_it_now='//*[@id="buy-now-button"]'
        eng.buy_it_now(btn_buy_it_now)

    elif "add to cart" in text:
        btn_add_to_cart='//*[@id="add-to-cart-button"]'
        eng.add_to_cart(btn_add_to_cart)

    elif "view cart" in text:
        btn_view_cart='//*[@id="hlb-view-cart-announce"]'
        eng.common_button_click(btn_view_cart)

    elif "watch list" in text:
        btn_watch_list='//*[@id="vi-atl-lnk"]/a/span[2]'
        eng.watch_list(btn_watch_list)

    elif "checkout" in text:
        btn_watch_list='//*[@id="hlb-ptc-btn-native"]'
        eng.common_button_click(btn_watch_list)

    elif "enter password" in text:
        txt_only_password='//*[@id="ap_password"]'
        eng.enter_only_pw("password",txt_only_password)

    elif "deliver" in text:
        btn_deliver_address='//*[@id="address-book-entry-0"]/div[2]/span/a'
        eng.common_button_click(btn_deliver_address)

    # choose shipping option
    elif "continue" in text:
        btn_shipping_continue='//*[@id="shippingOptionFormId"]/div[1]/div[2]/div/span[1]/span/input'
        eng.common_button_click(btn_shipping_continue)

    # Add a card
    elif "Add a card" in text:
        card_name='//*[@id="pp-hO8xv2-60"]'
        card_number='//*[@id="pp-hO8xv2-61"]'
        card_month='//*[@id="pp-hO8xv2-66"]' #future developments
        card_year='//*[@id="pp-hO8xv2-67"]' #future developments
        
        eng.add_a_card("card name",card_name,card_number) 
        eng.add_a_card("card number",card_name,card_number) 
    

    elif "pay" in text:
        btn_confirm_pay='//*[@id="page-form"]/div/button'
        eng.confirm_pay(btn_confirm_pay)

    #Selling Options
    # elif "sale" in text:
    #     import ebay_sell as eb
    #     eng.sell(wait,driver)

    elif "search" in text:
        url='https://www.amazon.com/'
        txt_searchbar='//*[@id="twotabsearchtextbox"]'
        eng.search(url,txt_searchbar)