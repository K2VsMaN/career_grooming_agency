from nicegui import ui, run, app, events
import io
import requests
from utils.api import base_url


_create_event_btn: ui.button = None


def _run_create_event(data, files, token):
    return requests.post(
        f"{base_url}/forms/agent",
        data=data,
        files=files,
        headers={"Authorization": f"Bearer {token}"},
    )


async def _create_event(data, files):
    _create_event_btn.props(add="disable loading")
    print(files)
    response = await run.cpu_bound(
        _run_create_event, data, files, app.storage.user.get("access_token")
    )
    print(response.status_code, response.content)
    _create_event_btn.props(remove="disable loading")
    if response.status_code == 200:
        return ui.navigate.to("/")
    # elif response.status_code == 401:
    #     return ui.navigate.to("/")


@ui.page("/trainee/forms")
def show_trainee_forms():
    global _create_event_btn
    document_content = None

    
        

    def handle_document_upload(e: events.UploadEventArguments):
        nonlocal document_content

        # Get the file path
        temp_path = e.file._path
        with open(temp_path, "rb") as f:
            file_bytes = f.read()

        document_content = (e.file.name, io.BytesIO(file_bytes), e.file.content_type)
        print(f"Uploaded: {e.file.name}, type: {e.file.content_type}, size: {len(file_bytes)} bytes")
        
        

    def _create_upload(label: str):
        with ui.column().classes("w-full gap-1"):
            ui.label(label).classes("text-sm font-medium text-gray-700")
            ui.upload(
                on_upload=handle_document_upload, auto_upload=True, max_files=1
            ).props("flat bordered").classes("w-full")

    with ui.card().classes("w-full max-w-2xl mx-auto my-8 p-8 rounded-xl shadow-2xl"):
        ui.label("Trainee Application Form").classes(
            "text-3xl font-bold text-center mb-6 text-gray-800"
        )

        with ui.stepper().props("vertical").classes("w-full") as stepper:
            with ui.step("Trainee Information"):
                ui.label("Please fill in your personal details.").classes(
                    "text-gray-600"
                )
                with ui.column().classes("w-full gap-1 mt-4"):
                    name = (
                        ui.input("Full Name", placeholder="Enter full name")
                        .props("outlined dense")
                        .classes("w-full")
                    )
                    age = (
                        ui.input("Age", placeholder="Enter age")
                        .props('outlined dense type="number"')
                        .classes("w-full")
                    )
                    email = (
                        ui.input("Email", placeholder="Enter email address")
                        .props('outlined dense type="email"')
                        .classes("w-full")
                    )
                    phone_number = (
                        ui.input("Phone Number", placeholder="Enter phone number")
                        .props('outlined dense type="tel"')
                        .classes("w-full")
                    )
                    gender = (
                        ui.select(["male", "female"], label="Select Gender")
                        .props("outlined dense")
                        .classes("w-full")
                    )
                    # ui.select(['Web Development', 'Data Science', 'UI/UX Design'], label='Select Course').props('outlined dense').classes('w-full')
                with ui.stepper_navigation():
                    ui.button("Next", on_click=stepper.next).props("color=primary")

            with ui.step("Document Uploads"):
                ui.label("Upload the required documents.").classes("text-gray-600")
                with ui.column().classes("w-full gap-4 mt-4"):
                    ghana_card = _create_upload("Ghana Card")
                    birth_cert = _create_upload("Birth Certificate")
                    wassce_cert = _create_upload("WASSCE Certificate")
                    print(ghana_card)
                with ui.stepper_navigation():
                    ui.button("Next", on_click=stepper.next).props("color=primary")
                    ui.button("Back", on_click=stepper.previous).props(
                        "flat color=primary"
                    )

            with ui.step("Parent/Guardian Information"):
                ui.label("Provide your parent's or guardian's details.").classes(
                    "text-gray-600"
                )
                with ui.column().classes("w-full gap-1 mt-4"):
                    parent_name = (
                        ui.input(
                            "Parent/Guardian's Full Name", placeholder="Enter full name"
                        )
                        .props("outlined dense")
                        .classes("w-full")
                    )
                    parent_contact = (
                        ui.input(
                            "Parent/Guardian's Contact",
                            placeholder="Enter contact number",
                        )
                        .props('outlined dense type="tel"')
                        .classes("w-full")
                    )
                    parent_occupation = (
                        ui.input(
                            "Parent/Guardian's Occupation",
                            placeholder="Enter occupation",
                        )
                        .props("outlined dense")
                        .classes("w-full")
                    )
                    parent_ghana_card = _create_upload("Parent/Guardian's Ghana Card")
                with ui.stepper_navigation():
                    _create_event_btn = (
                        ui.button(
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
                                files={
                                    "trainee_ghana_card": document_content[ghana_card],
                                    "trainee_birth_cert": document_content[birth_cert],
                                    "trainee_wassce_cert": document_content[
                                        wassce_cert
                                    ],
                                    # "parent_ghana_card": document_content[
                                    #     parent_ghana_card
                                    # ],
                                },
                            ),
                        ),
                    )
                    # ui.notify('Application Submitted!', type='positive')
                    ui.button("Back", on_click=stepper.previous).props(
                        "flat color=primary"
                    )
