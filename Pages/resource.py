from nicegui import ui
from nicegui import ui, events


@ui.page("/resources")
def resource_page():
    def handle_upload(e: events.UploadEventArguments):
        """Simulate file upload handling."""
        ui.notify(f"File '{e.name}' was selected.", type="info")

    # Dummy data for existing resources
    resources = [
        {"title": "Introduction to Python", "type": "PDF", "icon": "picture_as_pdf"},
        {"title": "Web Development Basics", "type": "Video", "icon": "videocam"},
        {"title": "Advanced CSS Techniques", "type": "Article", "icon": "article"},
    ]

    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    with ui.column().classes("w-full h-full items-center"):
        with ui.column().classes("w-full max-w-4xl p-8 overflow-y-auto bg-gray-50"):
            ui.label("Learning Resources").classes("text-4xl font-bold text-gray-800")

            # Upload new resource card
            with ui.card().classes("w-full mt-6 p-6 rounded-xl shadow-md"):
                ui.label("Upload New Resource").classes("text-xl font-bold text-gray-800 mb-4")
                title = ui.input("Resource Title").props("outlined dense").classes("w-full")
                description = ui.textarea("Description").props("outlined dense").classes("w-full")
                resource_type = ui.select(["PDF", "Video", "Article", "Other"], label="Resource Type").props("outlined dense").classes("w-full")
                
                ui.upload(on_upload=handle_upload, auto_upload=True, max_files=1).props("flat bordered").classes("w-full mt-2")
                
                ui.button(
                    "Upload Resource",
                    on_click=lambda: ui.notify("This is a frontend-only demonstration.", type="info"),
                ).classes("w-full mt-4 bg-indigo-500 text-white font-semibold py-2 rounded-lg hover:bg-indigo-600")

            # Existing resources list
            with ui.card().classes("w-full mt-8 p-6 rounded-xl shadow-md"):
                ui.label("Available Resources").classes("text-xl font-bold text-gray-800 mb-4")
                with ui.column().classes("w-full gap-4"):
                    for resource in resources:
                        with ui.row().classes("w-full items-center p-3 bg-gray-100 rounded-lg"):
                            ui.icon(resource["icon"], size="lg").classes("text-indigo-500")
                            with ui.column().classes("ml-4 flex-grow"):
                                ui.label(resource["title"]).classes("font-semibold text-gray-800")
                                ui.label(resource["type"]).classes("text-sm text-gray-500")
                            ui.button("View", icon="visibility").props("flat round color=primary")