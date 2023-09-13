init python:
    mods["threshold_start"]=u"{font=threshold/images/gui/fonts/gotham_pro_light.ttf}{size=40}Преддверие{/font}{/size}"

    try:
        modsImages["threshold_start"] = ("threshold/images/gui/misc/threshold_tabular_list_preview.png", False)

    except:
        pass  

label threshold_start:
    $ persistent.timeofday = "night"
    $ threshold_screens_save_act()
    $ threshold_set_mode_adv()