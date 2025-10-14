from nicegui import ui, app
from components.header import show_header
from components.footer import show_footer
from pages.home_page import show_home_page
<<<<<<< HEAD
from pages.admin_dashboard import show_admin_dashboard

app.add_static_files('/assets', 'assets')
=======
from pages.trainee.trainee_dashboard import show_trainee_dashboard
>>>>>>> d882f559fafc17694cf5194f1f9cdfbc4308cfe5


@ui.page('/')
def home_page():
    show_header()
    show_home_page()
    show_footer()
<<<<<<< HEAD
=======
    
ui.run(on_air=True)
>>>>>>> d882f559fafc17694cf5194f1f9cdfbc4308cfe5


@ui.page('/pages/admin_dashboard')
def admin_dashboard():
    show_admin_dashboard()


ui.run(on_air=True)  # remove on_air=True if you don’t need the live link