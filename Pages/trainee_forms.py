from nicegui import ui, run, app, events
import io
import requests
from utils.api import base_url

_create_event_btn: ui.button = None


def _run_create_event(data, files, token):
    """Send form data and files to backend."""
    return requests.post(
        f"{base_url}/forms/trainee",
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


@ui.page("/trainee/forms")
def show_trainee_forms():
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

    # -------------------------------
    # UI LAYOUT
    # -------------------------------
    with ui.card().classes("w-full max-w-2xl mx-auto my-8 p-8 rounded-xl shadow-2xl"):
        ui.label("Trainee Application Form").classes(
            "text-3xl font-bold text-center mb-6 text-gray-800"
        )

        with ui.stepper().props("vertical").classes("w-full") as stepper:

            # STEP 1: Trainee Information
            with ui.step("Trainee Information"):
                ui.label("Please fill in your personal details.").classes("text-gray-600")
                with ui.column().classes("w-full gap-1 mt-4"):
                    name = ui.input("Full Name").props("outlined dense").classes("w-full")
                    age = ui.input("Age").props('outlined dense type="number"').classes("w-full")
                    email = ui.input("Email").props('outlined dense type="email"').classes("w-full")
                    phone_number = ui.input("Phone Number").props('outlined dense type="tel"').classes("w-full")
                    gender = ui.select(["male", "female"], label="Select Gender").props("outlined dense").classes("w-full")

                with ui.stepper_navigation():
                    ui.button("Next", on_click=stepper.next).props("color=primary")

            # STEP 2: Document Uploads
            with ui.step("Document Uploads"):
                ui.label("Upload the required documents.").classes("text-gray-600")
                with ui.column().classes("w-full gap-4 mt-4"):
                    _create_upload("Ghana Card", "trainee_ghana_card")
                    _create_upload("Birth Certificate", "trainee_birth_cert")
                    _create_upload("WASSCE Certificate", "trainee_wassce_cert")

                with ui.stepper_navigation():
                    ui.button("Next", on_click=stepper.next).props("color=primary")
                    ui.button("Back", on_click=stepper.previous).props("flat color=primary")

            # STEP 3: Parent/Guardian Information
            with ui.step("Parent/Guardian Information"):
                ui.label("Provide your parent's or guardian's details.").classes("text-gray-600")
                with ui.column().classes("w-full gap-1 mt-4"):
                    parent_name = ui.input("Parent/Guardian's Full Name").props("outlined dense").classes("w-full")
                    parent_contact = ui.input("Parent/Guardian's Contact").props('outlined dense type="tel"').classes("w-full")
                    parent_occupation = ui.input("Parent/Guardian's Occupation").props("outlined dense").classes("w-full")
                    _create_upload("Parent/Guardian's Ghana Card", "parent_ghana_card")

                with ui.stepper_navigation():
                    _create_event_btn = ui.button(
                        "Submit Application",
                        on_click=lambda: _create_event(
                            {
                                "trainee_name": name.value,
                                "trainee_age": age.value,
                                "trainee_email": email.value,
                                "trainee_phone_number": phone_number.value,
                                "trainee_gender": gender.value,
                                "parent_name": parent_name.value,
                                "parent_contact": parent_contact.value,
                                "parent_occupation": parent_occupation.value,
                            },
                            uploaded_files,
                        ),
                    )
                    ui.button("Back", on_click=stepper.previous).props("flat color=primary")