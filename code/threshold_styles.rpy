init python:
    threshold_gui_path = "threshold/images/gui/"

    threshold_link_font = threshold_gui_path + "fonts/gothic.ttf"
    threshold_header_font = threshold_gui_path + "fonts/corbel.ttf"
    threshold_main_font = "fonts/calibri.ttf"

    style.threshold_button_none = Style(style.button)
    style.threshold_button_none.background = None
    style.threshold_button_none.hover_background = None
    style.threshold_button_none.selected_background = None
    style.threshold_button_none.selected_hover_background = None
    style.threshold_button_none.selected_idle_background = None

    style.threshold_text_style = Style(style.default)
    style.threshold_text_style.color = "#e2c778"
    style.threshold_text_style.drop_shadow = (2, 2)
    style.threshold_text_style.drop_shadow_color = "#000"

    style.threshold_titles_style = Style(style.default)
    style.threshold_titles_style.font = threshold_link_font
    style.threshold_titles_style.color = "#fff"
    style.threshold_titles_style.drop_shadow = [(1, 1), (1, 1), (1, 1), (1, 1)]
    style.threshold_titles_style.drop_shadow_color = "#000"
    style.threshold_titles_style.italic = False
    style.threshold_titles_style.bold = False
    style.threshold_titles_style.text_align = 0.5
    style.threshold_titles_style.xmaximum = 0.8

    style.threshold_save_load_button_main_menu = Style(style.button)
    style.threshold_save_load_button_main_menu.background = threshold_gui_path + "save_load/main_menu/thumbnail_idle.png"
    style.threshold_save_load_button_main_menu.hover_background = threshold_gui_path + "save_load/main_menu/thumbnail_hover.png"
    style.threshold_save_load_button_main_menu.selected_background = threshold_gui_path + "save_load/main_menu/thumbnail_selected.png"
    style.threshold_save_load_button_main_menu.selected_hover_background = threshold_gui_path + "save_load/main_menu/thumbnail_selected.png"
    style.threshold_save_load_button_main_menu.selected_idle_background = threshold_gui_path + "save_load/main_menu/thumbnail_selected.png"

    style.threshold_save_load_button_day = Style(style.button)
    style.threshold_save_load_button_day.background = threshold_gui_path + "save_load/day/thumbnail_idle.png"
    style.threshold_save_load_button_day.hover_background = threshold_gui_path + "save_load/day/thumbnail_hover.png"
    style.threshold_save_load_button_day.selected_background = threshold_gui_path + "save_load/day/thumbnail_selected.png"
    style.threshold_save_load_button_day.selected_hover_background = threshold_gui_path + "save_load/day/thumbnail_selected.png"
    style.threshold_save_load_button_day.selected_idle_background = threshold_gui_path + "save_load/day/thumbnail_selected.png"

    style.threshold_save_load_button_night = Style(style.button)
    style.threshold_save_load_button_night.background = threshold_gui_path + "save_load/night/thumbnail_idle.png"
    style.threshold_save_load_button_night.hover_background = threshold_gui_path + "save_load/night/thumbnail_hover.png"
    style.threshold_save_load_button_night.selected_background = threshold_gui_path + "save_load/night/thumbnail_selected.png"
    style.threshold_save_load_button_night.selected_hover_background = threshold_gui_path + "save_load/night/thumbnail_selected.png"
    style.threshold_save_load_button_night.selected_idle_background = threshold_gui_path + "save_load/night/thumbnail_selected.png"

    style.threshold_save_load_button_prologue = Style(style.button)
    style.threshold_save_load_button_prologue.background = threshold_gui_path + "save_load/prologue/thumbnail_idle.png"
    style.threshold_save_load_button_prologue.hover_background = threshold_gui_path + "save_load/prologue/thumbnail_hover.png"
    style.threshold_save_load_button_prologue.selected_background = threshold_gui_path + "save_load/prologue/thumbnail_selected.png"
    style.threshold_save_load_button_prologue.selected_hover_background = threshold_gui_path + "save_load/prologue/thumbnail_selected.png"
    style.threshold_save_load_button_prologue.selected_idle_background = threshold_gui_path + "save_load/prologue/thumbnail_selected.png"

    style.threshold_save_load_button_sunset = Style(style.button)
    style.threshold_save_load_button_sunset.background = threshold_gui_path + "save_load/sunset/thumbnail_idle.png"
    style.threshold_save_load_button_sunset.hover_background = threshold_gui_path + "save_load/sunset/thumbnail_hover.png"
    style.threshold_save_load_button_sunset.selected_background = threshold_gui_path + "save_load/sunset/thumbnail_selected.png"
    style.threshold_save_load_button_sunset.selected_hover_background = threshold_gui_path + "save_load/sunset/thumbnail_selected.png"
    style.threshold_save_load_button_sunset.selected_idle_background = threshold_gui_path + "save_load/sunset/thumbnail_selected.png"

    style.threshold_base_font = Style(style.default)
    style.threshold_base_font.font = threshold_main_font
    style.threshold_base_font.size = 28
    style.threshold_base_font.line_spacing = 2

    style.threshold_qte_text = Style(style.threshold_base_font)
    style.threshold_qte_text.font = threshold_header_font
    style.threshold_qte_text.size = 60
    style.threshold_qte_text.kerning = 3
    style.threshold_qte_text.color = "#cfd1d1"
    style.threshold_qte_text.hover_color = "#ffffff"
    style.threshold_qte_text.selected_color = "#ffffff"
    style.threshold_qte_text.selected_idle_color = "#ffffff"
    style.threshold_qte_text.selected_hover_color = "#ffffff"
    style.threshold_qte_text.insensitive_color = "#ffffff"

    style.threshold_settings_link = Style(style.threshold_base_font)
    style.threshold_settings_link.font = threshold_link_font
    style.threshold_settings_link.size = 60
    style.threshold_settings_link.kerning = 3
    style.threshold_settings_link.color = "#909ca3"
    style.threshold_settings_link.hover_color = "#ffffff"
    style.threshold_settings_link.selected_color = "#909ca3"
    style.threshold_settings_link.selected_idle_color = "#909ca3"
    style.threshold_settings_link.selected_hover_color = "#ffffff"
    style.threshold_settings_link.insensitive_color = "#909ca3"

    style.threshold_settings_link_main_menu = Style(style.threshold_base_font)
    style.threshold_settings_link_main_menu.font = threshold_link_font
    style.threshold_settings_link_main_menu.size = 60
    style.threshold_settings_link_main_menu.kerning = 3
    style.threshold_settings_link_main_menu.color = "#ffffff"
    style.threshold_settings_link_main_menu.hover_color = "#ffffff"
    style.threshold_settings_link_main_menu.selected_color = "#ffffff"
    style.threshold_settings_link_main_menu.selected_idle_color = "#ffffff"
    style.threshold_settings_link_main_menu.selected_hover_color = "#ffffff"
    style.threshold_settings_link_main_menu.insensitive_color = "#ffffff"

    style.threshold_settings_link_main_menu_preferences = Style(style.threshold_base_font)
    style.threshold_settings_link_main_menu_preferences.font = threshold_link_font
    style.threshold_settings_link_main_menu_preferences.size = 60
    style.threshold_settings_link_main_menu_preferences.kerning = 3
    style.threshold_settings_link_main_menu_preferences.color = "#d1d1d1"
    style.threshold_settings_link_main_menu_preferences.hover_color = "#ffffff"
    style.threshold_settings_link_main_menu_preferences.selected_color = "#d1d1d1"
    style.threshold_settings_link_main_menu_preferences.selected_idle_color = "#d1d1d1"
    style.threshold_settings_link_main_menu_preferences.selected_hover_color = "#ffffff"
    style.threshold_settings_link_main_menu_preferences.insensitive_color = "#d1d1d1"

    style.threshold_settings_header_main_menu_preferences = Style(style.threshold_base_font)
    style.threshold_settings_header_main_menu_preferences.font = threshold_header_font
    style.threshold_settings_header_main_menu_preferences.size = 60
    style.threshold_settings_header_main_menu_preferences.color = "#d1d1d1"
    style.threshold_settings_header_main_menu_preferences.hover_color = "#ffffff"
    style.threshold_settings_header_main_menu_preferences.selected_color = "#ffffff"

    style.threshold_settings_header_main_menu_preferences_locked = Style(style.threshold_base_font)
    style.threshold_settings_header_main_menu_preferences_locked.font = threshold_header_font
    style.threshold_settings_header_main_menu_preferences_locked.size = 60
    style.threshold_settings_header_main_menu_preferences_locked.color = "#C0C0C0"
    style.threshold_settings_header_main_menu_preferences_locked.hover_color = "#C0C0C0"
    style.threshold_settings_header_main_menu_preferences_locked.selected_color = "#C0C0C0"

    style.threshold_settings_header_main_menu_quit = Style(style.threshold_base_font)
    style.threshold_settings_header_main_menu_quit.font = threshold_header_font
    style.threshold_settings_header_main_menu_quit.size = 60
    style.threshold_settings_header_main_menu_quit.color = "#d1d1d1"
    style.threshold_settings_header_main_menu_quit.hover_color = "#ffffff"

    style.threshold_settings_header_main_menu_preferences_inverse = Style(style.threshold_base_font)
    style.threshold_settings_header_main_menu_preferences_inverse.font = threshold_header_font
    style.threshold_settings_header_main_menu_preferences_inverse.size = 60
    style.threshold_settings_header_main_menu_preferences_inverse.color = "#ffffff"
    style.threshold_settings_header_main_menu_preferences_inverse.hover_color = "#ffffff"
    style.threshold_settings_header_main_menu_preferences_inverse.selected_color = "#ffffff"

    style.threshold_main_menu = Style(style.threshold_base_font)
    style.threshold_main_menu.font = "threshold/images/gui/fonts/gotham_pro_light.ttf"
    style.threshold_main_menu.size = 95
    style.threshold_main_menu.kerning = 3
    style.threshold_main_menu.color = "#ffffff"
    style.threshold_main_menu.hover_color = "#ffffff"
    style.threshold_main_menu.selected_color = "#ffffff"
    style.threshold_main_menu.selected_idle_color = "#ffffff"
    style.threshold_main_menu.selected_hover_color = "#ffffff"
    style.threshold_main_menu.insensitive_color = "#ffffff"

    style.threshold_main_menu_locked = Style(style.threshold_base_font)
    style.threshold_main_menu_locked.font = threshold_header_font
    style.threshold_main_menu_locked.size = 60
    style.threshold_main_menu_locked.kerning = 3
    style.threshold_main_menu_locked.color = "#C0C0C0"
    style.threshold_main_menu_locked.hover_color = "#C0C0C0"
    style.threshold_main_menu_locked.selected_color = "#C0C0C0"
    style.threshold_main_menu_locked.selected_idle_color = "#C0C0C0"
    style.threshold_main_menu_locked.selected_hover_color = "#C0C0C0"
    style.threshold_main_menu_locked.insensitive_color = "#C0C0C0"

    style.threshold_settings_header_day = Style(style.threshold_base_font)
    style.threshold_settings_header_day.font = threshold_header_font
    style.threshold_settings_header_day.size = 50
    style.threshold_settings_header_day.color = "#4d2e19"
    style.threshold_settings_header_day.hover_color = "#a27146"
    
    style.threshold_settings_header_night = Style(style.threshold_base_font)
    style.threshold_settings_header_night.font = threshold_header_font
    style.threshold_settings_header_night.size = 50
    style.threshold_settings_header_night.color = "#161d3d"
    style.threshold_settings_header_night.hover_color = "#008193"

    style.threshold_settings_header_prologue = Style(style.threshold_base_font)
    style.threshold_settings_header_prologue.font = threshold_header_font
    style.threshold_settings_header_prologue.size = 50
    style.threshold_settings_header_prologue.color = "#161d3d"
    style.threshold_settings_header_prologue.hover_color = "#008193"

    style.threshold_settings_header_sunset = Style(style.threshold_base_font)
    style.threshold_settings_header_sunset.font = threshold_header_font
    style.threshold_settings_header_sunset.size = 50
    style.threshold_settings_header_sunset.color = "#5a3525"
    style.threshold_settings_header_sunset.hover_color = "#636840"

    style.threshold_settings_text_day = Style(style.threshold_settings_header_day)
    style.threshold_settings_text_day.size = 36
    style.threshold_settings_text_day.selected_color = "#4d2e19"
    style.threshold_settings_text_day.hover_color = "#a27146"

    style.threshold_settings_text_night = Style(style.threshold_settings_header_night)
    style.threshold_settings_text_night.size = 36
    style.threshold_settings_text_night.selected_color = "#161d3d"
    style.threshold_settings_text_night.hover_color = "#008193"

    style.threshold_settings_text_prologue = Style(style.threshold_settings_header_prologue)
    style.threshold_settings_text_prologue.size = 36
    style.threshold_settings_text_prologue.selected_color = "#161d3d"
    style.threshold_settings_text_prologue.hover_color = "#008193"

    style.threshold_settings_text_sunset = Style(style.threshold_settings_header_sunset)
    style.threshold_settings_text_sunset.size = 36
    style.threshold_settings_text_sunset.selected_color = "#5a3525"
    style.threshold_settings_text_sunset.hover_color = "#636840"

    style.threshold_text_history = Style(style.threshold_base_font)
    style.threshold_text_history.color = "#ffffff"
    style.threshold_text_history.drop_shadow = (2, 2)
    style.threshold_text_history.drop_shadow_color = "#000"