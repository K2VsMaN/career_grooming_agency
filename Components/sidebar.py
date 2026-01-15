from nicegui import ui, app

def _sign_out():
    """Clear user session and navigate to the home page."""
    app.storage.user.clear()
    ui.navigate.to("/")

def show_sidebar():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    current_path = ui.context.client.page.path

    # The main sidebar container.
    with ui.column().classes('bg-gray-100 p-4 w-[20%] shadow-lg h-full justify-between items-center fixed'):
        # Top section: Header and branding
        with ui.column().classes('w-full items-center mb-4'):
            # Header
            ui.icon('school').classes('text-black text-3xl')
            ui.label('Trainee').classes('text-2xl font-bold text-gray-800')

        ui.separator().classes('w-full h-px bg-gray-300 mb-4')

        # Navigation links section
        with ui.column().classes('w-full space-y-2 flex-grow'):            
            # Dashboard
            is_dashboard_active = current_path == '/trainee/dashboard'
            with ui.row().classes(
                f'w-full items-center cursor-pointer p-2 rounded-lg '
                f'{"bg-black" if is_dashboard_active else "hover:bg-gray-200"}'
            ):
                ui.icon('dashboard').classes(f'{"text-white" if is_dashboard_active else "text-gray-600"}')
                ui.link('Dashboard', '/trainee/dashboard').classes(
                    f'{"text-white" if is_dashboard_active else "text-gray-700"} font-semibold no-underline text-base'
                )

            # Resources
            is_resources_active = current_path == '/resources'
            with ui.row().classes(
                f'w-full items-center cursor-pointer p-2 rounded-lg '
                f'{"bg-black" if is_resources_active else "hover:bg-gray-200"}'
            ):
                ui.icon('source').classes(f'{"text-white" if is_resources_active else "text-gray-600"}')
                ui.link('Resources', '/resources').classes(
                    f'{"text-white" if is_resources_active else "text-gray-700"} font-semibold no-underline text-base'
                )

            # Agent's Contact
            is_agent_contact_active = current_path == '/agent/contact' # Assuming a future path
            with ui.row().classes(
                f'w-full items-center cursor-pointer p-2 rounded-lg '
                f'{"bg-black" if is_agent_contact_active else "hover:bg-gray-200"}'
            ):
                ui.icon('contact_phone').classes(f'{"text-white" if is_agent_contact_active else "text-gray-600"}')
                ui.link("Agent's Contact", '#').classes( # Keep '#' for now, update when page exists
                    f'{"text-white" if is_agent_contact_active else "text-gray-700"} font-semibold no-underline text-base'
                )

            # Upload Transcript
            is_upload_transcript_active = current_path == '/trainee/upload_transcript' # Assuming a future path
            with ui.row().classes(
                f'w-full items-center cursor-pointer p-2 rounded-lg '
                f'{"bg-black" if is_upload_transcript_active else "hover:bg-gray-200"}'
            ):
                ui.icon('upload_file').classes(f'{"text-white" if is_upload_transcript_active else "text-gray-600"}')
                ui.link('Upload Transcript', '#').classes( # Keep '#' for now, update when page exists
                    f'{"text-white" if is_upload_transcript_active else "text-gray-700"} font-semibold no-underline text-base'
                )

            # IT Course Selection
            is_course_selection_active = current_path == '/trainee/course_selection' # Assuming a future path
            with ui.row().classes(
                f'w-full items-center cursor-pointer p-2 rounded-lg '
                f'{"bg-black" if is_course_selection_active else "hover:bg-gray-200"}'
            ):
                ui.icon('model_training').classes(f'{"text-white" if is_course_selection_active else "text-gray-600"}')
                ui.link('IT Course Selection', '#').classes( # Keep '#' for now, update when page exists
                    f'{"text-white" if is_course_selection_active else "text-gray-700"} font-semibold no-underline text-base'
                )

        # Logout button at the bottom
        with ui.column().classes('w-full items-center mt-auto'):
            ui.separator().classes('w-full h-px bg-gray-300 mb-4')
            with ui.row().classes('w-full items-center cursor-pointer p-2 rounded-lg hover:bg-red-100 transition-colors'):
                ui.icon('logout').classes('text-red-600')
                ui.button(text='Logout', on_click=_sign_out).props('flat no-caps').classes('bg-transparent text-red-600 font-semibold shadow-none text-base')