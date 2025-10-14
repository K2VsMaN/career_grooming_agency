from nicegui import ui

# Set the page title
ui.page_title('Simple Forms')

# Embed Roboto font for a cleaner look
ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet"/>')
ui.add_head_html('<style>body { font-family: \'Roboto\', sans-serif; }</style>')

@ui.page('/agent/forms')
def show_agent_forms():
# --- Main Form Layout ---
    with ui.element('div').classes('min-h-screen flex items-center justify-center p-4 bg-gray-50'):
        # Card Container
        with ui.card().classes('w-full max-w-md mx-auto shadow-lg p-6 space-y-6'):
            ui.label('FORMS').classes('text-2xl font-bold text-center w-full')

            # Text/Number Inputs
            ui.input(label='Full Name', placeholder='John Doe').classes('w-full')
            ui.input(label='Email', placeholder='you@example.com', type='email').classes('w-full')
            ui.input(label='Phone Number', placeholder='+1 (555) 555-5555').classes('w-full')
            ui.input(label='Profession', placeholder='Software Engineer').classes('w-full')
            ui.number(label='Years of Experience', placeholder='5', step=1, min=0).classes('w-full')

            # Dropdown
            gender_options = ['Male', 'Female', 'Other', 'Prefer not to say']
            ui.select(gender_options, label='Gender', value='Male').classes('w-full')

            # --- File Upload Visual: School Certificate ---
            ui.label('School or Professional Certificate').classes('text-sm font-medium text-gray-700')
            with ui.upload().classes('w-full q-pa-md border-2 border-dashed rounded-md bg-gray-50 text-center') as upload_area:
                upload_area.default_slot.clear()
                with upload_area.default_slot:
                    ui.icon('cloud_upload', size='lg').classes('text-gray-400')
                    with ui.row().classes('justify-center items-center'):
                        ui.label('Upload a file').classes('text-blue-600 font-medium')
                        ui.label('or drag and drop').classes('text-gray-600')
                    ui.label('PNG, JPG, PDF up to 10MB').classes('text-xs text-gray-500 mt-[-0.5rem]')

            # --- File Upload Visual: Ghana Card ---
            ui.label('Ghana Card').classes('text-sm font-medium text-gray-700')
            with ui.upload().classes('w-full q-pa-md border-2 border-dashed rounded-md bg-gray-50 text-center') as upload_area:
                upload_area.default_slot.clear()
                with upload_area.default_slot:
                    ui.icon('cloud_upload', size='lg').classes('text-gray-400')
                    with ui.row().classes('justify-center items-center'):
                        ui.label('Upload a file').classes('text-blue-600 font-medium')
                        ui.label('or drag and drop').classes('text-gray-600')
                    ui.label('PNG, JPG, PDF up to 10MB').classes('text-xs text-gray-500 mt-[-0.5rem]')

            # Submit Button
            ui.button('Submit').classes('w-full bg-blue-600 hover:bg-blue-700 text-white shadow-md')

