from nicegui import ui
from components.sidebar import show_sidebar

@ui.page('pages/trainee/dashboard')
def dashboard_layout():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    with ui.row().classes("w-full h-full  flex-nowrap"):
        with ui.column().classes("w-[20%] h-full fixed"):
            show_sidebar()
    with ui.column().classes("w-full pl-[22%] p-5 overflow-y-auto bg-gray-50"):
        # Header
        with ui.row().classes('w-full items-center justify-between'):
            ui.label('Trainee Dashboard').classes('text-4xl font-bold text-gray-800')
            ui.image('https://randomuser.me/api/portraits/men/32.jpg').classes('w-12 h-12 rounded-full ring-2 ring-indigo-500')
        
        # Welcome Banner
        with ui.card().classes('w-full p-6 rounded-xl bg-indigo-500 text-white flex items-center justify-between shadow-lg'):
            with ui.column():
                ui.label('Welcome back, Alex!').classes('text-2xl font-bold')
                ui.label("Let's continue your learning journey.").classes('mt-1 opacity-80')
            ui.icon('school', size='3rem').classes('opacity-50')
        
        # Main Grid
        with ui.row().classes('w-full grid grid-cols-1 lg:grid-cols-3 gap-8'):
            # Left Column (Progress and Agent)
            with ui.column().classes('lg:col-span-2 gap-8'):
                with ui.card().classes('w-full p-6 rounded-xl shadow-md'):
                    ui.label('Overall Progress').classes('text-xl font-bold text-gray-800 mb-4')
                    with ui.row().classes('w-full items-center justify-between mb-1'):
                        ui.label('Tasks Completed').classes('text-gray-500')
                        ui.label('60%').classes('font-semibold text-indigo-600')
                    ui.linear_progress(0.6, show_value=False).props('color=indigo rounded')

                with ui.card().classes('w-full p-6 rounded-xl shadow-md'):
                    ui.label('Your Agent').classes('text-xl font-bold text-gray-800 mb-4')
                    with ui.row().classes('items-center gap-4'):
                        ui.image('https://randomuser.me/api/portraits/women/32.jpg').classes('w-16 h-16 rounded-full')
                        with ui.column().classes('gap-0'):
                            ui.label('Sarah Johnson').classes('font-bold text-lg text-gray-800')
                            ui.label('Senior IT Advisor').classes('text-gray-500')
                        ui.button('Contact', icon='mail_outline', on_click=lambda: ui.notify('Contacting agent...')) \
                            .props('flat round color=primary').classes('ml-auto')

            # Right Column (AI Assistant and Upload)
            with ui.column().classes('lg:col-span-1 gap-8'):
                with ui.card().classes('w-full p-6 rounded-xl shadow-md items-center text-center'):
                    ui.icon('auto_awesome', size='2.5rem').classes('text-indigo-500 animate-pulse')
                    ui.label('AI Course Assistant').classes('text-xl font-bold text-gray-800 mt-2')
                    ui.label('Get personalized course recommendations.').classes('text-gray-500 text-sm mb-4')
                    ui.button('Find a Course').classes('w-full bg-indigo-500 text-white font-semibold py-2 rounded-lg hover:bg-indigo-600')

                with ui.card().classes('w-full p-6 rounded-xl shadow-md'):
                    ui.label('Upload Transcript').classes('text-xl font-bold text-gray-800 mb-4')
                    ui.upload(auto_upload=True).props('flat bordered').classes('w-full')
                    ui.label('PDF, DOCX, PNG, JPG up to 10MB').classes('text-xs text-gray-400 mt-1 text-center w-full')
