from nicegui import ui

def show_header():
    print("Header is being rendered!")
    with ui.element('header').classes(
        'fixed top-0 inset-x-0 z-50 '
        'bg-white/50 backdrop-blur-md shadow-lg h-20 '
        'rounded-full mt-10 mx-16'
    ):
        with ui.row().classes('w-full h-full items-center justify-between px-10'):
            # Left: Logo
            ui.label('CGA').classes('text- font-bold text-lg')

            # Middle: Navigation
            with ui.row().classes('flex space-x-6 flex-grow justify-center'):
                ui.link('Home', '#').classes('text-black hover:text-gray-300 text-xl no-underline')
                ui.link('Mission', '#').classes('text-black hover:text-gray-300 text-xl no-underline')
                ui.link('Vision', '#').classes('text-black hover:text-gray-300 text-xl no-underline')
                ui.link('Mentors', '#').classes('text-black hover:text-gray-300 text-xl no-underline')

            # Right: Login pill button
            with ui.button(on_click=lambda: ui.open('/login')) \
    .props('rounded no-caps unelevated') \
    .classes('!bg-black !text-white h-12 px-5 shadow-lg hover:!bg-gray-800 transition-colors flex items-center'):
    
                ui.image('/assets/login-button.svg').classes('w-6 h-6 mr-2').style('filter: invert(1);')
                ui.label('Login').classes('text-white')
