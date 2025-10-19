from nicegui import ui, app
from components.header import *
from components.footer import *
from pages.home_page import show_home_page
from pages.admin_dashboard import *
from pages.trainee_dashboard import *
from pages.agent_forms import *
from pages.trainee_forms import *
from pages.trainee_signup import *
from pages.login import *
from pages.agent_signup import *




from pages.agent_dashboard import *



app.add_static_files('/assets', 'assets')

ui.run(storage_secret="asdfghjlzxcvbnm")  # remove on_air=True if you don’t need the live link