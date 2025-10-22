from nicegui import ui

def show_sidebar():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    # The main sidebar container. `justify-between` pushes content to the top and bottom. `items-start` aligns content to the left.
    with ui.column().classes('bg-gray-100 p-4 w-[20%] shadow-lg h-full justify-between items-start fixed'):
        # Top section: Header and navigation links
        with ui.column().classes('w-full items-start gap-2'):
            # Header
            with ui.column().classes('items-center mb-4'):
                ui.icon('school').classes('text-primary text-3xl')
                ui.label('Trainee').classes('text-2xl font-bold text-gray-800')

            # Navigation buttons
            ui.button('Dashboard', icon='dashboard') \
                .classes('w-full justify-start py-2.5 px-4 rounded transition duration-200 bg-primary text-white') \
                .props('flat no-caps')
            ui.button('Resources', icon='source') \
                .classes('w-full justify-start py-2.5 px-4 rounded transition duration-200 hover:bg-gray-200') \
                .props('flat no-caps')
            ui.button("Agent's Contact", icon='contact_phone') \
                .classes('w-full justify-start py-2.5 px-4 rounded transition duration-200 hover:bg-gray-200') \
                .props('flat no-caps')
            ui.button('Upload Transcript', icon='upload_file') \
                .classes('w-full justify-start py-2.5 px-4 rounded transition duration-200 hover:bg-gray-200') \
                .props('flat no-caps')
            ui.button('IT Course Selection', icon='model_training') \
                .classes('w-full justify-start py-2.5 px-4 rounded transition duration-200 hover:bg-gray-200') \
                .props('flat no-caps')

        # Bottom section: Logout button
        with ui.column().classes('w-full'):
            ui.button('Logout', icon='logout') \
                .classes('w-full justify-start py-2.5 px-4 rounded transition duration-200 hover:bg-gray-200 text-red-500') \
                .props('flat no-caps')