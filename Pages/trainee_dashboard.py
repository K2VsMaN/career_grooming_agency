from nicegui import ui, run, events, app
import io
from components.sidebar import show_sidebar
import requests
from utils.api import base_url

_upload_btn: ui.upload = None

def _run_upload_transcript(files):
    return requests.post(f"{base_url}/dashboard/trainee/transcript", files=files)

async def _upload(files):
    _upload_btn.props(add="disable loading")
    response = await run.cpu_bound(_run_upload_transcript, files)
    print(response.status_code, response.content)
    _upload_btn.props(remove="disable loading")
    if response.status_code == 200:
        return ui.navigate.to("/trainee/dashboard")
    # elif response.status_code == 409:
    #     return ui.notify(message="Not Successful!", type="warning")

# def _run_create_event(data, files, token):
#     """Send form data and files to backend."""
#     return requests.post(
#         f"{base_url}/dashboard/trainee/progress",
#         data=data,
#         headers={"Authorization": f"Bearer {token}"},
#     )




@ui.page('/trainee/dashboard')
def dashboard_layout(field_name: str = "transcript"):
    global _upload_btn

    uploaded_files = {}  # Dictionary to store all uploaded files

    def handle_document_upload(field_name: str):
        """Create upload handler for each field."""
        def inner(e: events.UploadEventArguments):
            # Handle both in-memory and temp-file uploads
            if hasattr(e.file, "_path") and e.file._path:
                with open(e.file._path, "rb") as f:
                    file_bytes = f.read()
            elif hasattr(e.file, "_data"):
                file_bytes = e.file._data
            else:
                ui.notify(f"Could not read file {e.file.name}", type="warning")
                return

            # Store file in memory for backend upload
            uploaded_files[field_name] = (
                e.file.name,
                io.BytesIO(file_bytes),
                e.file.content_type,
            )

            size_kb = len(file_bytes) / 1024
            print(
                f"{field_name} uploaded: {e.file.name} "
                f"({size_kb:.2f} KB, {e.file.content_type})"
            )
            ui.notify(f"{e.file.name} uploaded successfully!", type="positive")

        return inner 
@ui.page('pages/trainee/dashboard')
def dashboard_layout():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    with ui.row().classes("w-full h-full  flex-nowrap"):
        with ui.column().classes("w-[20%] h-full fixed"):
            show_sidebar()
    with ui.column().classes("w-full pl-[22%] p-5 overflow-y-auto bg-gray-50"):
        # Header
        with ui.row().classes('w-full items-center'):
            # Get username from storage, default to 'Trainee'
            username = app.storage.user.get('username', 'Trainee').capitalize()

            ui.label('Trainee Dashboard').classes('text-4xl font-bold text-gray-800')
        
        # Welcome Banner
        with ui.card().classes('w-full p-6 rounded-xl bg-indigo-500 text-white flex items-center justify-between shadow-lg cursor-pointer hover:shadow-xl transition-shadow'):
            with ui.column():
                ui.label(f'Welcome back, {username}!').classes('text-2xl font-bold')
                ui.label("Let's continue your learning journey.").classes('mt-1 opacity-90')
            ui.icon('school', size='3rem').classes('opacity-50')
        
        # Main Grid
        with ui.row().classes('w-full grid grid-cols-1 lg:grid-cols-3 gap-8'):
            # Left Column (Progress and Agent)
            with ui.column().classes('lg:col-span-2 gap-8'):
                with ui.card().on('click', lambda: ui.notify('Navigating to detailed progress...')).classes('w-full p-6 rounded-xl shadow-md cursor-pointer hover:shadow-xl transition-shadow'):
                    progress = ui.label('Overall Progress').classes('text-xl font-bold text-gray-800 mb-4')
                    with ui.row().classes('w-full items-center justify-between mb-1'):
                        ui.label('Tasks Completed').classes('text-gray-500')
                        ui.label('60%').classes('font-semibold text-indigo-600')
                    ui.linear_progress(0.6, show_value=False).props('color=indigo rounded')

                with ui.card().on('click', lambda: ui.notify('Contacting agent...')).classes('w-full p-6 rounded-xl shadow-md cursor-pointer hover:shadow-xl transition-shadow'):
                    ui.label('Your Agent').classes('text-xl font-bold text-gray-800 mb-4')
                    with ui.row().classes('items-center gap-4'):
                        ui.image('https://randomuser.me/api/portraits/women/32.jpg').classes('w-16 h-16 rounded-full')
                        with ui.column().classes('gap-0'):
                            ui.label('Sarah Johnson').classes('font-bold text-lg text-gray-800')
                            ui.label('Senior IT Advisor').classes('text-gray-500')
                        ui.button('Contact', icon='mail_outline', on_click=lambda: ui.notify('Contacting agent...')) \
                            .props('flat round color=primary').classes('ml-auto pointer-events-none') # Make button non-interactive as card is clickable

            # Right Column (AI Assistant and Upload)
            with ui.column().classes('lg:col-span-1 gap-8'):
                with ui.card().on('click', lambda: ui.notify('Finding a course...')).classes('w-full p-6 rounded-xl shadow-md items-center text-center cursor-pointer hover:shadow-xl transition-shadow'):
                    ui.icon('auto_awesome', size='2.5rem').classes('text-indigo-500 animate-pulse')
                    ui.label('AI Course Assistant').classes('text-xl font-bold text-gray-800 mt-2')
                    ui.label('Get personalized course recommendations.').classes('text-gray-500 text-sm mb-4')
                    ui.button('Find a Course', on_click=lambda: ui.notify('Finding a course...')).classes('w-full bg-indigo-500 text-white font-semibold py-2 rounded-lg hover:bg-indigo-600 pointer-events-none')

                with ui.card().classes('w-full p-6 rounded-xl shadow-md'):
                    ui.label('Upload Transcript').classes('text-xl font-bold text-gray-800 mb-4')
                    _upload_btn = ui.upload(on_upload=handle_document_upload(field_name), auto_upload=True).props('flat bordered accept=image/*').classes('w-full')
                    ui.label('Please upload an image file (e.g., PNG, JPG).').classes('text-xs text-gray-500 mt-1 text-center w-full')
