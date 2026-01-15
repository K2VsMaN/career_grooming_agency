from nicegui import ui, events


@ui.page("/admin/upload_resource")
def upload_resource_page():
    """A dedicated page for uploading new learning resources."""

    def handle_upload(e: events.UploadEventArguments):
        """Simulate file upload handling."""
        ui.notify(f"File '{e.name}' was selected for upload.", type="info")

    with ui.column().classes("w-full h-full items-center bg-gray-50 p-8"):
        with ui.card().classes("w-full max-w-2xl p-8 rounded-xl shadow-2xl"):
            with ui.row().classes('w-full items-center justify-between mb-6'):
                ui.label("Upload New Resource").classes("text-3xl font-bold text-gray-800")
                ui.button("Back to Resources", icon="arrow_back", on_click=lambda: ui.navigate.to('/resources')).props('flat round color=black')

            # Form for uploading a new resource
            title = ui.input("Resource Title").props("outlined dense").classes("w-full")
            description = ui.textarea("Description").props("outlined dense").classes("w-full")
            resource_type = ui.select(["PDF", "Video", "Article", "Other"], label="Resource Type").props("outlined dense").classes("w-full")
            
            ui.upload(on_upload=handle_upload, auto_upload=True, max_files=1).props("flat bordered").classes("w-full mt-2")
            
            ui.button(
                "Upload Resource",
                on_click=lambda: ui.notify("This is a frontend-only demonstration.", type="info"),
            ).classes("w-full mt-4 bg-black text-white font-semibold py-2 rounded-lg hover:bg-gray-800")