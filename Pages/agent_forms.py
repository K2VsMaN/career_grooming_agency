from nicegui import ui

def _create_upload(label: str):
    """Helper function to create a styled file upload component."""
    with ui.column().classes('w-full gap-1'):
        ui.label(label).classes('text-sm font-medium text-gray-700')
        ui.upload(auto_upload=True, max_files=1).props('flat bordered').classes('w-full')

@ui.page('/agent/forms')
def show_agent_forms():
    """Displays the agent application forms with a modern stepper layout."""
    with ui.card().classes('w-full max-w-2xl mx-auto my-8 p-8 rounded-xl shadow-2xl'):
        ui.label('Agent Application Form').classes('text-3xl font-bold text-center mb-6 text-gray-800')

        with ui.stepper().props('vertical').classes('w-full') as stepper:
            with ui.step('Personal Information'):
                ui.label('Please fill in your personal and professional details.').classes('text-gray-600')
                with ui.column().classes('w-full gap-1 mt-4'):
                    ui.input('Full Name', placeholder='John Doe').props('outlined dense').classes('w-full')
                    ui.input('Email', placeholder='you@example.com').props('outlined dense type=email').classes('w-full')
                    ui.input('Phone Number', placeholder='+233 (55) 555-5555').props('outlined dense type=tel').classes('w-full')
                    ui.select(['Male', 'Female', 'Other'], label='Gender').props('outlined dense').classes('w-full')
                    ui.input('Profession', placeholder='e.g., Software Engineer').props('outlined dense').classes('w-full')
                    ui.input('Years of Experience', placeholder='5').props('outlined dense type=number').classes('w-full')
                with ui.stepper_navigation():
                    ui.button('Next', on_click=stepper.next).props('color=primary')

            with ui.step('Document Uploads'):
                ui.label('Upload your professional and identification documents.').classes('text-gray-600')
                with ui.column().classes('w-full gap-4 mt-4'):
                    _create_upload('School or Professional Certificate')
                    _create_upload('Ghana Card')
                with ui.stepper_navigation():
                    ui.button('Submit Application', on_click=lambda: ui.notify('Application Submitted!', type='positive')).props('color=primary')
                    ui.button('Back', on_click=stepper.previous).props('flat color=primary')
