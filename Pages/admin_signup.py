from nicegui import ui, run
import requests
from utils.api import base_url

_signup_btn: ui.button = None


def _run_signup(data):
    return requests.post(f"{base_url}/users/signup", data=data)


async def _signup(data):
    _signup_btn.props(add="disable loading")
    response = await run.cpu_bound(_run_signup, data)
    print(response.status_code, response.content)
    _signup_btn.props(remove="disable loading")
    if response.status_code == 200:
        return ui.navigate.to("/login")
    elif response.status_code == 409:
        return ui.notify(message="User already exists!", type="warning")


def _create_input(
    placeholder: str, icon: str, is_password: bool = False
) -> ui.input:
    """Helper function to create a styled input field with a prepended icon."""
    inp = (
        ui.input(
            placeholder=placeholder,
            password=is_password,
            password_toggle_button=is_password,
        )
        .props("outlined dense bg-color=white")
        .classes("w-full focus-within:border-indigo-500")
        .style("transition: border-color 0.3s;")
    )
    with inp.add_slot("prepend"):
        ui.icon(icon).classes("text-gray-500")
    return inp


@ui.page("/admin/signup")
def show_admin_signup():
    global _signup_btn
    """Creates an admin registration form with improved styling."""
    with ui.card().classes("w-full max-w-md mx-auto my-8 rounded-xl shadow-2xl"):
        with ui.column().classes("w-full p-8 gap-4"):
            ui.label("Create An Account").classes(
                "text-3xl font-bold text-center mb-4 text-gray-800"
            )

            # Role selection: Agent, Trainee, Admin
            with ui.row().classes("w-full grid grid-cols-3 gap-2 mb-4"):
                # Agent (inactive)
                with ui.column().on(
                    "click", lambda: ui.navigate.to("/agent/signup")
                ).classes(
                    "group items-center justify-center p-3 border-2 rounded-lg cursor-pointer border-gray-300 hover:border-indigo-500 text-gray-500 hover:text-gray-700 transition-all"
                ):
                    ui.icon("support_agent").classes("text-3xl mb-1 text-gray-400 group-hover:text-indigo-500")
                    ui.label("Agent").classes("text-sm font-medium")

                # Trainee (inactive)
                with ui.column().on(
                    "click", lambda: ui.navigate.to("/trainee/signup")
                ).classes(
                    "group items-center justify-center p-3 border-2 rounded-lg cursor-pointer border-gray-300 hover:border-indigo-500 text-gray-500 hover:text-gray-700 transition-all"
                ):
                    ui.icon("school").classes("text-3xl mb-1 text-gray-400 group-hover:text-indigo-500")
                    ui.label("Trainee").classes("text-sm font-medium")

                # Admin (active)
                with ui.column().classes(
                    "items-center justify-center p-3 border-2 rounded-lg cursor-pointer bg-indigo-500 text-white border-indigo-500 transition-all"
                ):
                    ui.icon("admin_panel_settings").classes("text-3xl mb-1")
                    ui.label("Admin").classes("text-sm font-medium")

            username = _create_input("Username", "person_outline")
            email = _create_input("Email", "mail_outline")
            password = _create_input("Password", "lock_outline", is_password=True)
            confirm_password = _create_input("Confirm Password", "lock_outline", is_password=True)

            _signup_btn = ui.button(
                text="Sign Up",
                on_click=lambda: _signup(
                    {
                        "username": username.value,
                        "email": email.value,
                        "password": password.value,
                        "confirm_password": confirm_password.value,
                        "role": "admin",
                    }
                ),
            ).classes(
                "w-full bg-indigo-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-indigo-600 transition-colors"
            )

            with ui.row().classes("w-full justify-center mt-4"):
                ui.label("Already have an account?").classes("text-sm text-gray-600")
                ui.link("Login", "/login").classes(
                    "text-sm font-medium text-indigo-500 hover:underline ml-1"
                )
