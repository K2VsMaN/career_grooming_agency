from nicegui import ui

def _create_input(placeholder: str, icon: str) -> ui.input:
    """Helper function to create a styled input field with a prepended icon."""
    inp = ui.input(placeholder=placeholder) \
        .props('outlined dense bg-color=white') \
        .classes('w-full focus-within:border-indigo-500') \
        .style('transition: border-color 0.3s;')
    with inp.add_slot('prepend'):
        ui.icon(icon).classes('text-gray-500')
    return inp

@ui.page('/agent/signup')
def show_agent_signup():
    """Creates an agent registration form with improved styling."""
    with ui.card().classes('w-full max-w-md mx-auto my-8 rounded-xl shadow-2xl'):
        with ui.column().classes('w-full p-8 gap-4'):
            ui.label('Create An Account').classes('text-3xl font-bold text-center mb-4 text-gray-800')

            # ui.label('Sign up as:').classes('text-sm font-medium text-center mb-2')
            with ui.row().classes('w-full grid grid-cols-2 gap-4 mb-4'):
                with ui.column().classes('items-center justify-center p-4 border-2 rounded-lg cursor-pointer bg-indigo-500 text-white border-indigo-500 transition-all'):
                    ui.icon('support_agent').classes('text-4xl mb-2')
                    ui.label('Agent').classes('text-sm font-medium')
                with ui.column().on('click', lambda: ui.navigate.to('/trainee/signup')).classes('group items-center justify-center p-4 border-2 rounded-lg cursor-pointer border-gray-300 hover:border-indigo-500 text-gray-500 hover:text-gray-700 transition-all'):
                    ui.icon('school').classes('text-4xl mb-2 text-gray-400 group-hover:text-indigo-500')
                    ui.label('Trainee').classes('text-sm font-medium')

            _create_input('Username', 'person_outline')
            _create_input('Email', 'mail_outline')
            _create_input('Password', 'lock_outline').props('type=password')
            _create_input('Verification Code', 'verified_user')

            ui.button('Sign Up', on_click=lambda: ui.notify('Creating Agent Account...')).classes('w-full bg-indigo-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-indigo-600 transition-colors')

            with ui.row().classes('w-full justify-center mt-4'):
                ui.label('Already have an account?').classes('text-sm text-gray-600')
                ui.link('Login', '/login').classes('text-sm font-medium text-indigo-500 hover:underline ml-1')
