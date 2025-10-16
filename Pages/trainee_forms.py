from nicegui import ui

def _create_upload(label: str):
    """Helper function to create a styled file upload component."""
    with ui.column().classes('w-full gap-1'):
        ui.label(label).classes('text-sm font-medium text-gray-700')
        ui.upload(auto_upload=True, max_files=1).props('flat bordered').classes('w-full')

@ui.page('/trainee/forms')
def show_trainee_forms():
    """Displays the trainee application forms with an improved, modern layout."""
    with ui.card().classes('w-full max-w-2xl mx-auto my-8 p-8 rounded-xl shadow-2xl'):
        ui.label('Trainee Application Form').classes('text-3xl font-bold text-center mb-6 text-gray-800')

        with ui.stepper().props('vertical').classes('w-full') as stepper:
            with ui.step('Trainee Information'):
                ui.label('Please fill in your personal details.').classes('text-gray-600')
                with ui.column().classes('w-full gap-1 mt-4'):
                    ui.input('Full Name', placeholder='Enter full name').props('outlined dense').classes('w-full')
                    ui.input('Age', placeholder='Enter age').props('outlined dense type="number"').classes('w-full')
                    ui.input('Email', placeholder='Enter email address').props('outlined dense type="email"').classes('w-full')
                    ui.input('Phone Number', placeholder='Enter phone number').props('outlined dense type="tel"').classes('w-full')
                    ui.select(['Male', 'Female', 'Other'], label='Select Gender').props('outlined dense').classes('w-full')
                    ui.select(['Web Development', 'Data Science', 'UI/UX Design'], label='Select Course').props('outlined dense').classes('w-full')
                with ui.stepper_navigation():
                    ui.button('Next', on_click=stepper.next).props('color=primary')

            with ui.step('Document Uploads'):
                ui.label('Upload the required documents.').classes('text-gray-600')
                with ui.column().classes('w-full gap-4 mt-4'):
                    _create_upload('Ghana Card')
                    _create_upload('Birth Certificate')
                    _create_upload('WASSCE Certificate')
                with ui.stepper_navigation():
                    ui.button('Next', on_click=stepper.next).props('color=primary')
                    ui.button('Back', on_click=stepper.previous).props('flat color=primary')

            with ui.step('Parent/Guardian Information'):
                ui.label("Provide your parent's or guardian's details.").classes('text-gray-600')
                with ui.column().classes('w-full gap-1 mt-4'):
                    ui.input("Parent/Guardian's Full Name", placeholder="Enter full name").props('outlined dense').classes('w-full')
                    ui.input("Parent/Guardian's Contact", placeholder="Enter contact number").props('outlined dense type="tel"').classes('w-full')
                    ui.input("Parent/Guardian's Occupation", placeholder="Enter occupation").props('outlined dense').classes('w-full')
                    _create_upload("Parent/Guardian's Ghana Card")
                with ui.stepper_navigation():
                    ui.button('Submit Application', on_click=lambda: ui.notify('Application Submitted!', type='positive')).props('color=primary')
                    ui.button('Back', on_click=stepper.previous).props('flat color=primary')
