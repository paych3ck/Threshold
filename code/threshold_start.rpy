init python:
    mods["thld_start"]=u"{font=thld/images/gui/fonts/gotham_pro_light.ttf}{size=40}Преддверие{/font}{/size}"

    try:
        modsImages["thld_start"] = ("thld/images/gui/misc/thld_tabular_list_preview.png", False)

    except:
        pass  

label thld_start:
    $ persistent.timeofday = "night"
    $ thld_screens_save_act()
    $ thld_set_mode_adv()