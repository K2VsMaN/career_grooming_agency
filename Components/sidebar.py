from nicegui import ui

def show_sidebar():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    with ui.column().classes('bg-gray-100 p-4 w-[20%] shadow-lg h-full justify-between items-center fixed'):
        with ui.row().classes('flex flex-col h-full'):  # Changed to ui.row
            with ui.column().classes('w-full items-center mb-6'):
                ui.icon('school').classes('text-primary text-3xl')
                ui.label('Trainee').classes('text-2xl font-bold text-text-light dark:text-text-dark')
            
            with ui.row().classes('mt-6 w-full flex-col'):  # Changed to ui.row
                ui.button('Dashboard', icon='dashboard') \
                    .classes('w-full flex items-center py-2.5 px-4 rounded transition duration-200 bg-primary text-white') \
                    .props('flat')
                ui.button('Resources', icon='source') \
                    .classes('w-full flex items-center py-2.5 px-4 rounded transition duration-200 hover:bg-gray-200 dark:hover:bg-gray-700') \
                    .props('flat')
                ui.button("Agent's Contact", icon='contact_phone') \
                    .classes('w-full flex items-center py-2.5 px-4 rounded transition duration-200 hover:bg-gray-200 dark:hover:bg-gray-700') \
                    .props('flat')
                ui.button('Upload Transcript', icon='upload_file') \
                    .classes('w-full flex items-center py-2.5 px-4 rounded transition duration-200 hover:bg-gray-200 dark:hover:bg-gray-700') \
                    .props('flat')
                ui.button('IT Course Selection', icon='model_training') \
                    .classes('w-full flex items-center py-2.5 px-4 rounded transition duration-200 hover:bg-gray-200 dark:hover:bg-gray-700') \
                    .props('flat')
        
            with ui.row().classes('w-full'):  # Changed to ui.row
                ui.button('Logout', icon='logout') \
                    .classes('w-full flex items-center py-2.5 px-4 rounded transition duration-200 hover:bg-gray-200 dark:hover:bg-gray-700 text-red-500') \
                    .props('flat')