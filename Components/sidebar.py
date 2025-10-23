from nicegui import ui, app

def _sign_out():
    """Clear user session and navigate to the home page."""
    app.storage.user.clear()
    ui.navigate.to("/")

def show_sidebar():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    # The main sidebar container.
    with ui.column().classes('bg-gray-100 p-4 w-[20%] shadow-lg h-full justify-between items-center fixed'):
        # Top section: Header and branding
        with ui.column().classes('w-full items-center mb-4'):
            # Header
            ui.icon('school').classes('text-primary text-3xl')
            ui.label('Trainee').classes('text-2xl font-bold text-gray-800')

        ui.separator().classes('w-full h-px bg-gray-300 mb-4')

        # Navigation links section
        with ui.column().classes('w-full space-y-2 flex-grow'):
            # Dashboard (Active)
            with ui.row().classes('w-full items-center cursor-pointer bg-primary p-2 rounded-lg'):
                ui.icon('dashboard').classes('text-white')
                ui.link('Dashboard', '/trainee/dashboard').classes('text-white font-semibold no-underline text-base')

            # Resources
            with ui.row().classes('w-full items-center cursor-pointer hover:bg-gray-200 p-2 rounded-lg'):
                ui.icon('source').classes('text-gray-600')
                ui.link('Resources', '#').classes('text-gray-700 font-semibold no-underline text-base')

            # Agent's Contact
            with ui.row().classes('w-full items-center cursor-pointer hover:bg-gray-200 p-2 rounded-lg'):
                ui.icon('contact_phone').classes('text-gray-600')
                ui.link("Agent's Contact", '#').classes('text-gray-700 font-semibold no-underline text-base')

            # Upload Transcript
            with ui.row().classes('w-full items-center cursor-pointer hover:bg-gray-200 p-2 rounded-lg'):
                ui.icon('upload_file').classes('text-gray-600')
                ui.link('Upload Transcript', '#').classes('text-gray-700 font-semibold no-underline text-base')

            # IT Course Selection
            with ui.row().classes('w-full items-center cursor-pointer hover:bg-gray-200 p-2 rounded-lg'):
                ui.icon('model_training').classes('text-gray-600')
                ui.link('IT Course Selection', '#').classes('text-gray-700 font-semibold no-underline text-base')

        # Logout button at the bottom
        with ui.column().classes('w-full items-center mt-auto'):
            ui.separator().classes('w-full h-px bg-gray-300 mb-4')
            with ui.row().classes('w-full items-center cursor-pointer p-2 rounded-lg hover:bg-red-100 transition-colors'):
                ui.icon('logout').classes('text-red-600')
                ui.button(text='Logout', on_click=_sign_out).props('flat no-caps').classes('bg-transparent text-red-600 font-semibold shadow-none text-base')