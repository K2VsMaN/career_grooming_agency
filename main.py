from nicegui import ui, app
from components.header import *
from components.footer import *
from pages.home_page import show_home_page
from pages.admin_dashboard import *
from pages.agent_dashboard import *



app.add_static_files('/assets', 'assets')

ui.run()  # remove on_air=True if you don’t need the live link