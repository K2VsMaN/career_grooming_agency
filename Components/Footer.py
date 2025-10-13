from nicegui import ui

def show_footer():
    with ui.element('footer').classes(
    'w-full bg-gray-800 text-white py-4 px-4 mt-10'
):
        with ui.row().classes('max-w-[1200px] mx-auto w-full justify-center'):
            ui.label('© 2025 Career Grooming Agency. All rights reserved.').classes('text-sm text-center')