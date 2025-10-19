from nicegui import ui

# The page container and styling
@ui.page('/login')
def login_page():
    """Creates a stylish login page."""
    with ui.column().classes('w-full h-screen flex items-center justify-center bg-gray-100'):
        with ui.card().classes('w-full max-w-md p-8 rounded-xl shadow-2xl'):
            # Header
            with ui.column().classes('w-full items-center gap-1 mb-6'):
                ui.label('Welcome Back!').classes('text-3xl font-bold text-gray-800')
                ui.label('Sign in to access your account').classes('text-gray-500')

            # Form
            with ui.column().classes('w-full gap-4'):
                # Email Input
                email_input = ui.input(placeholder='you@example.com') \
                    .props('outlined dense bg-color=white type=email') \
                    .classes('w-full')
                with email_input.add_slot('prepend'):
                    ui.icon('mail_outline', color='gray-5')

                # Password Input
                password_input = ui.input(placeholder='Password', password=True, password_toggle_button=True) \
                    .props('outlined dense bg-color=white') \
                    .classes('w-full')
                with password_input.add_slot('prepend'):
                    ui.icon('lock_outline', color='gray-5')

                # Sign In Button
                ui.button('Sign In', on_click=lambda: ui.notify('Signing in...')) \
                    .classes('w-full bg-indigo-500 text-white font-bold py-3 rounded-lg hover:bg-indigo-600 transition-colors')

            # Footer Link
            with ui.row().classes('w-full justify-center mt-6'):
                ui.label("Don't have an account?").classes('text-gray-600')
                ui.link('Sign up', '/trainee/signup').classes('ml-1 font-medium text-indigo-500 hover:underline')