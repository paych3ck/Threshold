init python: 
    from os import path

    for file_name in renpy.list_files():
        if "thld" in file_name:
            file_path = path.splitext(path.basename(file_name))[0]

            if file_name.startswith("thld/images/bg/"):
                renpy.image("bg " + file_path, file_name)

            elif file_name.startswith("thld/images/gui/"):
                renpy.image(file_path, file_name)

            elif file_name.startswith("thld/images/sprites/"):
                renpy.image(file_path, ConditionSwitch("persistent.sprite_time == 'sunset'", im.MatrixColor(file_name, im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time == 'night'", im.MatrixColor(file_name, im.matrix.tint(0.63, 0.78, 0.82)), True, file_name))

            elif file_name.startswith("thld/sounds/"):
                globals()[file_path] = file_name

    thld_std_set_for_preview = {}
    thld_std_set = {}
    store.thld_colors = {}
    store.thld_names = {}
    store.thld_names_list = []
    thld_speaker_color = "speaker_color"

    store.thld_names_list.append("thld_narrator")

    store.thld_names_list.append("thld_th")

    thld_colors["thld_myself"] = {"speaker_color": (6, 91, 13, 255)}
    thld_names["thld_myself"] = "Я"
    store.thld_names_list.append("thld_myself")

    thld_colors["thld_pi_i_p"] = {"speaker_color": (75, 2, 135, 255)}
    thld_names["thld_pi_i_p"] = "Пионер"
    store.thld_names_list.append("thld_pi_i_p")

    thld_colors["thld_pi_evi"] = {"speaker_color": (255, 242, 38, 255)}
    thld_names["thld_pi_evi"] = "Пионер"
    store.thld_names_list.append("thld_pi_evi")

    thld_colors["thld_pi_teapot"] = {"speaker_color": (85, 19, 19, 255)}
    thld_names["thld_pi_teapot"] = "Пионер"
    store.thld_names_list.append("thld_pi_teapot")

    thld_colors["thld_teapot"] = {"speaker_color": (85, 19, 19, 255)}
    thld_names["thld_teapot"] = "Чайник"
    store.thld_names_list.append("thld_teapot")

    thld_colors["thld_pi_ann"] = {"speaker_color": (175, 145, 81, 255)}
    thld_names["thld_pi_ann"] = "Распорядитель"
    store.thld_names_list.append("thld_pi_ann")

    thld_colors["thld_pi_mad"] = {"speaker_color": (159, 147, 147, 255)}
    thld_names["thld_pi_mad"] = "Помешанный"
    store.thld_names_list.append("thld_pi_mad")

    thld_colors["thld_guest"] = {"speaker_color": (159, 147, 147, 255)}
    thld_names["thld_guest"] = "Гость"
    store.thld_names_list.append("thld_guest")

    thld_colors["thld_nit"] = {"speaker_color": (159, 147, 147, 255)}
    thld_names["thld_nit"] = "Ниточник"
    store.thld_names_list.append("thld_nit")

    def thld_char_define(character_name, is_nvl = False):
        global DynamicCharacter
        global nvl
        global thld_store
        global thld_speaker_color
        thld_gl = globals()
        
        if character_name == "thld_narrator":
            if is_nvl:
                thld_gl["thld_narrator"] = Character(None, kind = nvl, what_style = "thld_text_style")
            
            else:
                thld_gl["thld_narrator"] = Character(None, what_style = "thld_text_style")
            
            return

        if character_name == "thld_th":
            if  is_nvl:
                thld_gl["thld_th"] = Character(None, kind = nvl, what_style = "thld_text_style", what_prefix = "~ ", what_suffix = " ~")
            
            else:
                thld_gl["thld_th"] = Character(None, what_style = "thld_text_style", what_prefix = "~ ", what_suffix = " ~")
            
            return
        
        if is_nvl:
            thld_gl[character_name] = DynamicCharacter("%s_name" % character_name, color = store.thld_colors[character_name][thld_speaker_color], kind = nvl, what_style = "thld_text_style", who_suffix = ":")
            thld_gl["%s_name" % character_name] = store.thld_names[character_name]
        
        else:
            thld_gl[character_name] = DynamicCharacter("%s_name" % character_name, color = store.thld_colors[character_name][thld_speaker_color], what_style = "thld_text_style")
            thld_gl["%s_name" % character_name] = store.thld_names[character_name]

    def thld_set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global thld_store
        
        for character_name in store.thld_names_list:
            thld_char_define(character_name)

    def thld_set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global thld_narrator
        global thld_th
        thld_narrator_nvl = thld_narrator
        th_nvl = thld_th
        
        global thld_store
        
        for character_name in store.thld_names_list:
            thld_char_define(character_name, True)

    def thld_reload_names():
        global thld_store
        
        for character_name in store.thld_names_list:
            thld_char_define(character_name)

    thld_reload_names()

    class ThldBlackRectangle(renpy.Displayable):
        def __init__(self, width, height, alpha, **kwargs):
            super(ThldBlackRectangle, self).__init__(**kwargs)
            self.width = width
            self.height = height
            self.alpha = alpha
            self.frame = Solid("#000000", xsize=self.width, ysize=self.height)

        def render(self, width, height, st, at):
            t = Transform(child=self.frame, alpha=self.alpha)
            obj = renpy.render(t, width, height, st, at)
            render = renpy.Render(self.width, self.height)
            render.blit(obj, (0, 0))
            return render

    class ThldMainMenuParallax(renpy.Displayable):
        def __init__(self, image_name, xstep, ystep):
            super(ThldMainMenuParallax, self).__init__()
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
    image thld_main_menu_bg:
        contains:
            "thld_main_menu_background"
            xpos -50
            ypos -50
            zoom 1.1

    image thld_logo_frame = DinBlackRectangle(width=720, height=1080, alpha=0.6)
    image thld_start_button_frame = DinBlackRectangle(width=720, height=1080, alpha=0.6)

    transform thld_buttons_atl():
        on idle:
            easein 0.5 zoom 1.0

        on hover:
            easein 0.5 zoom 1.05

    transform thld_bus_moving():
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