from nicegui import ui

# --- 1. Custom Styling Setup ---
PRIMARY_COLOR = '#4F46E5' # Matching the primary color from the provided HTML source
ui.colors(primary=PRIMARY_COLOR)

# Embed Inter font and basic styles
ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"/>')
ui.add_head_html('<style>body { font-family: \'Inter\', sans-serif; }</style>')

# Custom CSS to replicate the file button's specific styling and section header border
ui.add_head_html(f'''
<style>
.file-button-visual .q-btn {{
    background: {PRIMARY_COLOR}1A !important; /* primary/10 */
    color: {PRIMARY_COLOR} !important; 
    font-weight: 600 !important;
    text-transform: none !important;
    border-radius: 0.25rem !important;
    padding: 0.5rem 1rem !important;
    line-height: 1 !important;
    height: auto !important;
}}
.section-header {{
    color: {PRIMARY_COLOR};
    border-bottom: 1px solid #E5E7EB; /* border-light from HTML */
}}
</style>
''')

ui.page_title('Trainee Application Form')

@ui.page('/trainee/forms')
def show_trainee_forms():
# --- 2. Main Form Layout ---
    with ui.element('div').classes('min-h-screen flex flex-col items-center justify-center p-4 bg-gray-50'):
        with ui.element('div').classes('w-full max-w-md mx-auto'):
            # Header
            ui.label('FORMS').classes('text-2xl font-bold text-center mb-6')

            # Form Content Column
            with ui.column().classes('space-y-6 w-full'):
                
                # --------------------------------------------------------------------------
                # --- Trainee Information Section ---
                with ui.card().classes('w-full p-6 space-y-4 shadow-md'):
                    ui.label('Trainee Information').classes('text-lg font-semibold pb-2 w-full section-header')
                    
                    # Inputs
                    ui.input(label='Full Name', placeholder='Enter full name').classes('w-full')
                    ui.number(label='Age', placeholder='Enter age').classes('w-full')
                    ui.input(label='Email', placeholder='Enter email address', type='email').classes('w-full')
                    ui.input(label='Phone Number', placeholder='Enter phone number', type='tel').classes('w-full')
                    
                    # Selects
                    gender_options = ['Select Gender', 'Male', 'Female', 'Other']
                    ui.select(gender_options, label='Gender', value=gender_options[0]).classes('w-full')
                    course_options = ['Select Course', 'Web Development', 'Data Science', 'UI/UX Design']
                    ui.select(course_options, label='Course of Choice', value=course_options[0]).classes('w-full')

                # --------------------------------------------------------------------------
                # --- Document Uploads Section ---
                with ui.card().classes('w-full p-6 space-y-4 shadow-md'):
                    ui.label('Document Uploads').classes('text-lg font-semibold pb-2 w-full section-header')
                    
                    # File Upload: Ghana Card
                    ui.label('Ghana Card').classes('block text-sm font-medium text-gray-700')
                    with ui.row().classes('w-full items-center mt-1'):
                        ui.button('Choose File').classes('file-button-visual').props('flat')
                        ui.label('No file chosen').classes('text-gray-500 text-sm')

                    # File Upload: Birth Certificate
                    ui.label('Birth Certificate').classes('block text-sm font-medium text-gray-700')
                    with ui.row().classes('w-full items-center mt-1'):
                        ui.button('Choose File').classes('file-button-visual').props('flat')
                        ui.label('No file chosen').classes('text-gray-500 text-sm')

                    # File Upload: WASSCE Certificate
                    ui.label('WASSCE Certificate').classes('block text-sm font-medium text-gray-700')
                    with ui.row().classes('w-full items-center mt-1'):
                        ui.button('Choose File').classes('file-button-visual').props('flat')
                        ui.label('No file chosen').classes('text-gray-500 text-sm')
                
                # --------------------------------------------------------------------------
                # --- Parent/Guardian Information Section ---
                with ui.card().classes('w-full p-6 space-y-4 shadow-md'):
                    ui.label('Parent/Guardian Information').classes('text-lg font-semibold pb-2 w-full section-header')
                    
                    # Inputs
                    ui.input(label='Parent/Guardian Full Name', placeholder="Enter parent's full name").classes('w-full')
                    ui.input(label='Parent/Guardian Contact', placeholder="Enter parent's contact", type='tel').classes('w-full')
                    ui.input(label='Parent/Guardian Occupation', placeholder="Enter parent's occupation").classes('w-full')
                    
                    # File Upload: Parent/Guardian Ghana Card
                    ui.label('Parent/Guardian Ghana Card').classes('block text-sm font-medium text-gray-700')
                    with ui.row().classes('w-full items-center mt-1'):
                        ui.button('Choose File').classes('file-button-visual').props('flat')
                        ui.label('No file chosen').classes('text-gray-500 text-sm')

                # --------------------------------------------------------------------------
                # --- Submit Button ---
                ui.button('Submit Application', color='primary') \
                .classes('w-full py-3 text-white font-medium shadow-md')

