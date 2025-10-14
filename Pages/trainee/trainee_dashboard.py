from nicegui import ui, app

# Configure app to use Roboto font and Material Icons
ui.add_head_html("""
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
        }
    </style>
""")

# Define custom colors to match the image closely
ui.colors(primary='#6366F1', secondary='#E0E7FF', light='#F9FAFB', dark='#1F2937', positive='#10B981', negative='#EF4444')


def show_trainee_dashboard():
    with ui.column().classes('p-6 gap-6 w-full max-w-screen-xl mx-auto'):
        # Header for desktop view
        with ui.row().classes('w-full items-center justify-between mb-6'):
            ui.label('Dashboard').classes('text-3xl font-bold text-gray-800')
            ui.image('https://picsum.photos/id/1005/40/40').classes('w-10 h-10 rounded-full border-2 border-gray-300') # Placeholder profile pic

        # Welcome Card
        with ui.card().classes('w-full bg-primary text-white p-6 rounded-lg shadow-lg flex items-center justify-between'):
            with ui.column().classes('gap-1'):
                ui.label('Welcome back, Alex!').classes('text-2xl font-bold')
                ui.label('Let\'s continue your learning journey.').classes('text-base')

        # Overall Progress Card
        with ui.card().classes('w-full p-6 rounded-lg shadow-md bg-white'):
            ui.label('Overall Progress').classes('text-xl font-semibold mb-4 text-gray-800')
            with ui.column().classes('w-full'):
                with ui.row().classes('w-full items-center justify-between mb-2'):
                    ui.badge('TASK IN PROGRESS', color='secondary').classes('text-primary font-semibold text-xs')
                    ui.label('60%').classes('text-primary font-semibold text-sm')
                ui.linear_progress(0.6, color='primary').classes('h-4 rounded-full')

        with ui.row().classes('w-full flex-wrap gap-6'):
            # Your Agent Card
            with ui.card().classes('p-6 rounded-lg shadow-md bg-white flex-1 min-w-[300px]'):
                ui.label('Your Agent').classes('text-xl font-semibold mb-4 text-gray-800')
                with ui.row().classes('items-center gap-4'):
                    ui.image('https://picsum.photos/id/237/80/80').classes('rounded-full w-16 h-16') # Placeholder agent pic
                    with ui.column():
                        ui.label('Sarah Johnson').classes('font-bold text-lg text-gray-800')
                        ui.label('Senior IT Advisor').classes('text-gray-600')
                        ui.button('Contact', icon='email', on_click=lambda: ui.notify('Contacting Sarah...')) \
                            .props('flat dense').classes('mt-2 text-primary bg-primary/20 rounded-full px-3 py-1 text-sm')

            # AI Course Assistant Card
            with ui.card().classes('p-6 rounded-lg shadow-md bg-white flex-1 min-w-[300px]'):
                ui.label('AI Course Assistant').classes('text-xl font-semibold mb-4 text-gray-800')
                with ui.row().classes('w-full items-start justify-between mb-4'):
                    ui.label('Get personalized course recommendations.').classes('text-gray-600')
                    ui.icon('auto_awesome').classes('text-primary text-3xl animate-pulse')
                ui.button('Find a Course', on_click=lambda: ui.notify('Finding a course...')) \
                    .classes('w-full bg-primary text-white py-2.5 rounded-lg font-semibold hover:opacity-90')

        # Upload Transcript Card
        with ui.card().classes('w-full p-6 rounded-lg shadow-md bg-white'):
            ui.label('Upload Your Transcript').classes('text-xl font-semibold mb-4 text-gray-800')
            with ui.column().classes('border-2 border-dashed border-gray-300 rounded-lg p-6 text-center cursor-pointer hover:border-primary transition duration-200 w-full'):
                ui.icon('cloud_upload').classes('text-5xl text-gray-400')
                ui.label('Click to browse or drag and drop your file here').classes('mt-2 text-gray-600')
                ui.label('PDF, DOCX, PNG, JPG up to 10MB').classes('text-xs text-gray-500 mt-1')

