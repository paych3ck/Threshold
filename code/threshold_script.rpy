init python:
    class threshold_FunctionCallback(Action):
        def __init__(self,function, *arguments):
            self.function = function
            self.arguments = arguments

        def __call__(self):
            return self.function(self.arguments)
    
    def threshold_on_load_callback(slot):
        try:
            if persistent.threshold_on_save_timeofday[slot]:
                persistent.timeofday = persistent.threshold_on_save_timeofday[slot][0]
                persistent.sprite_time = persistent.threshold_on_save_timeofday[slot][1]
                persistent.font_size = persistent.threshold_on_save_timeofday[slot][2]
                _preferences.volumes["music"] = persistent.threshold_on_save_timeofday[slot][3]
                _preferences.volumes["sfx"] = persistent.threshold_on_save_timeofday[slot][4]
                _preferences.volumes["voice"] = persistent.threshold_on_save_timeofday[slot][5]
        
        except:
            pass
    
    def threshold_on_save_callback(slot):
        if not persistent.threshold_on_save_timeofday:
            persistent.threshold_on_save_timeofday = {}

        persistent.threshold_on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, _preferences.volumes["music"], _preferences.volumes["sfx"], _preferences.volumes["voice"])
        
    def threshold_screen_save():
        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[("threshold_old_" + screen_name, None)] = renpy.display.screen.screens[(screen_name, None)]
        
    def threshold_screen_act():
        config.window_title = u"Преддверие"
        config.name = "Threshold"
        config.version = "1.0"

        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("threshold_" + screen_name, None)]

        layout.LOADING = "Потерять несохраненные данные?"
            
        config.mouse_displayable = MouseDisplayable("threshold/images/gui/misc/cursor.png", 0, 0)
        config.main_menu_music = "threshold/sounds/music/threshold_reef_inevitability.mp3"
        config.linear_saves_page_size = None
        persistent._file_page = "threshold_FilePage_1"  

    def threshold_screens_diact():
        config.window_title = u"Бесконечное лето"
        config.name = "Everlasting_Summer"
        config.version = "1.2"

        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("threshold_old_" + screen_name, None)]
         
        layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"
            
        config.mouse_displayable = MouseDisplayable("images/misc/mouse/1.png", 0, 0)
        config.main_menu_music = "sound/music/blow_with_the_fires.ogg"

        persistent._file_page = 1

        for channel in ["ambience", "music", "sound", "sound_loop"]:
            renpy.music.stop(channel)

        renpy.play(music_list["blow_with_the_fires"], channel = "music")

    def threshold_screens_save_act():
        threshold_screen_save()
        threshold_screen_act()