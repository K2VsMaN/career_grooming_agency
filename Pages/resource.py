from nicegui import ui
from components.sidebar import show_sidebar


@ui.page("/resources")
def resource_page():
    # Dummy data for existing resources
    resources = [
        {"title": "Introduction to Python", "type": "PDF", "icon": "picture_as_pdf"},
        {"title": "Web Development Basics", "type": "Video", "icon": "videocam"},
        {"title": "Advanced CSS Techniques", "type": "Article", "icon": "article"},
        {"title": "Getting Started with NiceGUI", "type": "Article", "icon": "article"},
    ]

    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    with ui.row().classes("w-full h-full flex-nowrap"):
        with ui.column().classes("w-[20%] h-full fixed"):
            show_sidebar()
        with ui.column().classes("w-full pl-[22%] p-8 overflow-y-auto bg-gray-50"):
            with ui.row().classes('w-full items-center justify-between'):
                ui.label("Learning Resources").classes("text-4xl font-bold text-gray-800")
                # This button would only be visible to admins/agents in a real app
                ui.button("Upload New", icon="upload", on_click=lambda: ui.navigate.to('/admin/upload_resource')).classes('bg-black text-white').props('no-caps')
            
            # Available resources list
            with ui.card().classes("w-full mt-6 p-6 rounded-xl shadow-md"):
                ui.label("Available Resources").classes("text-xl font-bold text-gray-800 mb-4")
                with ui.column().classes("w-full gap-4"):
                    for resource in resources:
                        with ui.row().classes("w-full items-center p-3 bg-gray-100 rounded-lg"):
                            ui.icon(resource["icon"], size="lg").classes("text-black")
                            with ui.column().classes("ml-4 flex-grow"):
                                ui.label(resource["title"]).classes("font-semibold text-gray-800")
                                ui.label(resource["type"]).classes("text-sm text-gray-500")
                            ui.button("View", icon="visibility").props("flat round color=black")