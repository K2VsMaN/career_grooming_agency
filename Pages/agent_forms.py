from nicegui import ui, run, app, events
import io
import requests
from utils.api import base_url

_create_event_btn: ui.button = None


def _run_create_event(data, files, token):
    """Send form data and files to backend."""
    return requests.post(
        f"{base_url}/forms/agent",
        data=data,
        files=files,
        headers={"Authorization": f"Bearer {token}"},
    )


async def _create_event(data, files):
    print("data", data)
    print("files", files)
    """Run the backend submission asynchronously."""
    _create_event_btn.props(add="disable loading")

    response = await run.cpu_bound(
        _run_create_event, data, files, app.storage.user.get("access_token")
    )

    print(response.status_code, response.content)
    _create_event_btn.props(remove="disable loading")

    if response.status_code == 200:
        ui.notify("Application submitted successfully!", type="positive")
        return ui.navigate.to("/")
    else:
        ui.notify(f"Submission failed: {response.status_code}", type="negative")


@ui.page("/agent/forms")
def show_agent_forms():
    global _create_event_btn
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

    def _create_upload(label: str, field_name: str):
        """Create a labeled upload input."""
        with ui.column().classes("w-full gap-1"):
            ui.label(label).classes("text-sm font-medium text-gray-700")
            ui.upload(
                on_upload=handle_document_upload(field_name),
                auto_upload=True,
                max_files=1,
            ).props("flat bordered").classes("w-full")

    with ui.card().classes("w-full max-w-2xl mx-auto my-8 p-8 rounded-xl shadow-2xl"):
        ui.label("Agent Application Form").classes(
            "text-3xl font-bold text-center mb-6 text-gray-800"
        )

        with ui.stepper().props("vertical").classes("w-full") as stepper:
            with ui.step("Personal Information"):
                ui.label(
                    "Please fill in your personal and professional details."
                ).classes("text-gray-600")
                with ui.column().classes("w-full gap-1 mt-4"):
                    name = (
                        ui.input("Full Name", placeholder="John Doe")
                        .props("outlined dense")
                        .classes("w-full")
                    )
                    email = (
                        ui.input("Email", placeholder="you@example.com")
                        .props("outlined dense type=email")
                        .classes("w-full")
                    )
                    phone_number = (
                        ui.input("Phone Number", placeholder="+233 (55) 555-5555")
                        .props("outlined dense type=tel")
                        .classes("w-full")
                    )
                    gender = (
                        ui.select(["male", "female"], label="Gender")
                        .props("outlined dense")
                        .classes("w-full")
                    )
                    profession = (
                        ui.input("Profession", placeholder="e.g., Software Engineer")
                        .props("outlined dense")
                        .classes("w-full")
                    )
                    years_of_experience = (
                        ui.input("Years of Experience", placeholder="5")
                        .props("outlined dense type=number")
                        .classes("w-full")
                    )
                with ui.stepper_navigation():
                    ui.button("Next", on_click=stepper.next).props("color=primary")

            with ui.step("Document Uploads"):
                ui.label(
                    "Upload your professional and identification documents."
                ).classes("text-gray-600")
                with ui.column().classes("w-full gap-4 mt-4"):
                    _create_upload("School or Professional Certificate", "certificate")
                    _create_upload("Ghana Card", "ghana_card")
                with ui.stepper_navigation():
                    _create_event_btn = ui.button(
                            "Submit Application",
                            on_click=lambda: _create_event(
                                {
                                    "full_name": name.value,
                                    "email": email.value,
                                    "phone_number": phone_number.value,
                                    "profession": profession.value,
                                    "years_of_experience": years_of_experience.value,
                                    "gender": gender.value,
                                },
                                uploaded_files,
                            ),
                        )
                    

                    ui.button("Back", on_click=stepper.previous).props(
                        "flat color=primary"
                    )
