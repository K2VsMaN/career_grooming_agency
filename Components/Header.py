from nicegui import ui

def show_header():
    with ui.element('header').classes(
        'fixed top-0 inset-x-0 z-50 '
        'bg-white/50 backdrop-blur-md shadow-md h-20 '
        'rounded-full mt-10 mx-16'
    ):
        with ui.row().classes('w-full h-full items-center justify-between px-10'):
            # Left: Logo
            ui.label('CGA').classes('text-black font-bold text-lg')

            # Middle: Navigation
            with ui.row().classes('flex space-x-6 flex-grow justify-center'):
                ui.link('Home', '#').classes('text-black hover:text-gray-300 text-sm no-underline')
                ui.link('Mission', '#').classes('text-black hover:text-gray-300 text-sm no-underline')
                ui.link('Vision', '#').classes('text-black hover:text-gray-300 text-sm no-underline')
                ui.link('Stories', '#').classes('text-black hover:text-gray-300 text-sm no-underline')

            # Right: Login pill button (SVG image + label inside)
            with ui.button(on_click=lambda: ui.open('/login')) \
                .props('rounded no-caps unelevated color=yellow-300 text-color=white') \
                .classes('h-12 px-5 shadow-lg hover:bg-yellow-300 transition-colors flex items-center'):
                ui.image('/assets/login-button.png').classes('w-6 h-6 mr-2 fill-white text-white')
                ui.label('Login').classes('text-white')

