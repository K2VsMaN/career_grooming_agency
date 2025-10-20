from nicegui import ui, run, app, events
import requests
from utils.api import base_url

_create_event_btn: ui.button = None


def _run_create_event(data, files, token):
    return requests.post(
        f"{base_url}/forms/trainee",
        data=data,
        files=files,
        headers={"Authorization": f"Bearer {token}"},
    )


async def _create_event(data, files):
    _create_event_btn.props(add="disable loading")
    response = await run.cpu_bound(
        _run_create_event, data, files, app.storage.user.get("access_token")
    )
    print(response.status_code, response.content)
    _create_event_btn.props(remove="disable loading")
    if response.status_code == 200:
        return ui.navigate.to("/")
    # elif response.status_code == 401:
    #     return ui.navigate.to("/")


def _create_upload(label: str):
    """Helper function to create a styled file upload component."""
    with ui.column().classes("w-full gap-1"):
        ui.label(label).classes("text-sm font-medium text-gray-700")
        ui.upload(auto_upload=True, max_files=1).props("flat bordered").classes(
            "w-full"
        )


@ui.page("/agent/forms")
def show_agent_forms():
    global _create_event_btn
    document_content = None

    def handle_document_upload(e: events.UploadEventArguments):
        nonlocal document_content
        document_content = e.content.read()

    def _create_upload(label: str):
        with ui.column().classes("w-full gap-1"):
            ui.label(label).classes("text-sm font-medium text-gray-700")
            ui.upload(
                on_upload=handle_document_upload, auto_upload=True, max_files=1
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
                        ui.select(["Male", "Female", "Other"], label="Gender")
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
                    cert = _create_upload("School or Professional Certificate")
                    ghana_card = _create_upload("Ghana Card")
                with ui.stepper_navigation():
                    _create_event_btn = (
                        ui.button(
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
                                files={
                                    "certificate": document_content[cert],
                                    "ghana_card": document_content[ghana_card],
                                },
                            ),
                        ),
                    )

                    ui.button("Back", on_click=stepper.previous).props(
                        "flat color=primary"
                    )
