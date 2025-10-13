from nicegui import ui, app
from components.header import show_header
from components.footer import show_footer
from pages.home_page import show_home_page
from pages.trainee.trainee_dashboard import show_trainee_dashboard


app.add_static_files("/assets", "assets")


@ui.page("/")
def home_page():
    show_header()
    show_home_page()
    show_footer()

@ui.page('/trainee/trainee_dashboard')
def trainee_dashboard():
    show_trainee_dashboard()     

    
ui.run()
