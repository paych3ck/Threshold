init python: 
    from os import path

    for file_name in renpy.list_files():
        if "threshold" in file_name:
            file_path = path.splitext(path.basename(file_name))[0]

            if file_name.startswith("threshold/images/bg/"):
                renpy.image("bg " + file_path, file_name)

            elif file_name.startswith("threshold/images/gui/"):
                renpy.image(file_path, file_name)

            elif file_name.startswith("threshold/images/sprites/"):
                renpy.image(file_path, ConditionSwitch("persistent.sprite_time == 'sunset'", im.MatrixColor(file_name, im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time == 'night'", im.MatrixColor(file_name, im.matrix.tint(0.63, 0.78, 0.82)), True, file_name))

            elif file_name.startswith("threshold/sounds/"):
                globals()[file_path] = file_name

    threshold_std_set_for_preview = {}
    threshold_std_set = {}
    store.threshold_colors = {}
    store.threshold_names = {}
    store.threshold_names_list = []
    threshold_speaker_color = "speaker_color"

    store.threshold_names_list.append("threshold_narrator")

    store.threshold_names_list.append("threshold_th")

    threshold_colors["threshold_myself"] = {"speaker_color": (6, 91, 13, 255)}
    threshold_names["threshold_myself"] = "Я"
    store.threshold_names_list.append("threshold_myself")

    threshold_colors["threshold_pi_i_p"] = {"speaker_color": (75, 2, 135, 255)}
    threshold_names["threshold_pi_i_p"] = "Пионер"
    store.threshold_names_list.append("threshold_pi_i_p")

    threshold_colors["threshold_pi_evi"] = {"speaker_color": (255, 242, 38, 255)}
    threshold_names["threshold_pi_evi"] = "Пионер"
    store.threshold_names_list.append("threshold_pi_evi")

    threshold_colors["threshold_pi_teapot"] = {"speaker_color": (85, 19, 19, 255)}
    threshold_names["threshold_pi_teapot"] = "Пионер"
    store.threshold_names_list.append("threshold_pi_teapot")

    threshold_colors["threshold_teapot"] = {"speaker_color": (85, 19, 19, 255)}
    threshold_names["threshold_teapot"] = "Чайник"
    store.threshold_names_list.append("threshold_teapot")

    threshold_colors["threshold_pi_ann"] = {"speaker_color": (175, 145, 81, 255)}
    threshold_names["threshold_pi_ann"] = "Распорядитель"
    store.threshold_names_list.append("threshold_pi_ann")

    threshold_colors["threshold_pi_mad"] = {"speaker_color": (159, 147, 147, 255)}
    threshold_names["threshold_pi_mad"] = "Помешанный"
    store.threshold_names_list.append("threshold_pi_mad")

    threshold_colors["threshold_guest"] = {"speaker_color": (159, 147, 147, 255)}
    threshold_names["threshold_guest"] = "Гость"
    store.threshold_names_list.append("threshold_guest")

    threshold_colors["threshold_nit"] = {"speaker_color": (159, 147, 147, 255)}
    threshold_names["threshold_nit"] = "Ниточник"
    store.threshold_names_list.append("threshold_nit")

    def threshold_char_define(character_name, is_nvl = False):
        global DynamicCharacter
        global nvl
        global threshold_store
        global threshold_speaker_color
        threshold_gl = globals()
        
        if character_name == "threshold_narrator":
            if is_nvl:
                threshold_gl["threshold_narrator"] = Character(None, kind = nvl, what_style = "threshold_text_style")
            
            else:
                threshold_gl["threshold_narrator"] = Character(None, what_style = "threshold_text_style")
            
            return

        if character_name == "threshold_th":
            if  is_nvl:
                threshold_gl["threshold_th"] = Character(None, kind = nvl, what_style = "threshold_text_style", what_prefix = "~ ", what_suffix = " ~")
            
            else:
                threshold_gl["threshold_th"] = Character(None, what_style = "threshold_text_style", what_prefix = "~ ", what_suffix = " ~")
            
            return
        
        if is_nvl:
            threshold_gl[character_name] = DynamicCharacter("%s_name" % character_name, color = store.threshold_colors[character_name][threshold_speaker_color], kind = nvl, what_style = "threshold_text_style", who_suffix = ":")
            threshold_gl["%s_name" % character_name] = store.threshold_names[character_name]
        
        else:
            threshold_gl[character_name] = DynamicCharacter("%s_name" % character_name, color = store.threshold_colors[character_name][threshold_speaker_color], what_style = "threshold_text_style")
            threshold_gl["%s_name" % character_name] = store.threshold_names[character_name]

    def threshold_set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global threshold_store
        
        for character_name in store.threshold_names_list:
            threshold_char_define(character_name)

    def threshold_set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global threshold_narrator
        global threshold_th
        threshold_narrator_nvl = threshold_narrator
        th_nvl = threshold_th
        
        global threshold_store
        
        for character_name in store.threshold_names_list:
            threshold_char_define(character_name, True)

    def threshold_reload_names():
        global threshold_store
        
        for character_name in store.threshold_names_list:
            threshold_char_define(character_name)

    threshold_reload_names()

    class threshold_main_menu_parallax(renpy.Displayable):
        def __init__(self, image_name, xstep, ystep):
            super(threshold_main_menu_parallax, self).__init__()
            self.image_name = renpy.displayable(image_name)
            self.xstep = xstep
            self.ystep = ystep
            self.x = None
            self.y = None
        
        def render(self, width, height, st, at):
            first_render = renpy.render(self.image_name, width, height, st, at)
            render = renpy.Render(width, height)            
            render.blit(first_render, (0, 0))
        
            if self.x is not None:
                image_render = renpy.render(self.image_name, width, height, st, at)
                render_width, render_height = (config.screen_width, config.screen_height)
                xpos = (self.x - render_width / 2) * self.xstep / render_width
                ypos = (self.y - render_height / 2) * self.ystep / render_height
                render.blit(image_render, (xpos, ypos))
        
            return render
        
        def event(self, ev, x, y, st):
            if x  < 0 or y < 0:
                return
        
            if (x != self.x) or (y != self.y):
                self.x = x
                self.y = y
                renpy.redraw(self, 0)

init:
    image threshold_main_menu_bg:
        contains:
            #"threshold_main_menu_background"
            "nikitalol"
            xpos -50
            ypos -50
            zoom 1.1

    transform threshold_buttons_atl():
        on idle:
            easein 0.5 zoom 1.0

        on hover:
            easein 0.5 zoom 1.05

    transform threshold_bus_moving():
        subpixel True
        truecenter
        zoom 1.03

        parallel:
            linear 0.2 xoffset -2
            linear 0.3 xoffset 3
            linear 0.2 xoffset -1
            linear 0.3 xoffset 2
            repeat

        parallel:
            linear 0.2 yoffset -1
            linear 0.25 yoffset 2
            linear 0.2 yoffset -1
            repeat