from nicegui import ui, app
from components.header import show_header
from components.footer import show_footer
from pages.home_page import show_home_page
from pages.admin_dashboard import show_admin_dashboard

app.add_static_files('/assets', 'assets')


@ui.page('/')
def home_page():
    show_header()
    show_home_page()
    show_footer()


@ui.page('/pages/admin_dashboard')
def admin_dashboard():
    show_admin_dashboard()


ui.run(on_air=True)  # remove on_air=True if you don’t need the live link