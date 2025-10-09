from nicegui import ui

def show_footer():
    with ui.footer().classes('bg-gray-800 text-white p-4 text-center w-full'):
        ui.label('© 2025 Career Grooming Agency. All rights reserved.').classes('text-sm')