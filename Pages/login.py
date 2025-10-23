from nicegui import ui, app, run
import requests
from utils.api import base_url

_login_btn: ui.button = None


def _run_login(data):
    return requests.post(f"{base_url}/users/login", data=data)


async def _login(data):
    _login_btn.props(add="disable loading")
    response = await run.cpu_bound(_run_login, data)
    print(response.status_code, response.content)
    _login_btn.props(remove="disable loading")
    if response.status_code == 200:
        json_data = response.json()
        app.storage.user["access_token"] = json_data["access_token"]
        app.storage.user["username"] = json_data.get("username", "User")  # Store username
        if json_data["role"] == "trainee":
            return ui.navigate.to("/trainee/dashboard")
        elif json_data["role"] == "agent":
            return ui.navigate.to("/pages/agent_dashboard")
        elif json_data["role"] == "admin":
            return ui.navigate.to("/pages/admin_dashboard")

    if response.status_code == 404:
        return ui.navigate.to("/agent/signup")
    # elif response.status_code == 401:
    #     return ui.notify(message="Invalid credentials!", type="warning")
   


# The page container and styling
@ui.page("/login")
def login_page():
    global _login_btn
    """Creates a stylish login page."""
    with ui.column().classes(
        "w-full h-screen flex items-center justify-center bg-gray-100"
    ):
        with ui.card().classes("w-full max-w-md p-8 rounded-xl shadow-2xl"):
            # Header
            with ui.column().classes("w-full items-center gap-1 mb-6"):
                ui.label("Welcome Back!").classes("text-3xl font-bold text-gray-800")
                ui.label("Sign in to access your account").classes("text-gray-500")

            # Form
            with ui.column().classes("w-full gap-4"):
                # Email Input
                email = (
                    ui.input(placeholder="you@example.com")
                    .props("outlined dense bg-color=white type=email")
                    .classes("w-full")
                )
                with email.add_slot("prepend"):
                    ui.icon("mail_outline", color="gray-5")

                # Password Input
                password = (
                    ui.input(
                        placeholder="Password",
                        password=True,
                        password_toggle_button=True,
                    )
                    .props("outlined dense bg-color=white")
                    .classes("w-full")
                )
                with password.add_slot("prepend"):
                    ui.icon("lock_outline", color="gray-5")

                # Sign In Button
                _login_btn = ui.button(
                    text="Sign In",
                    on_click=lambda: _login(
                        {"email": email.value, "password": password.value}
                    ),
                ).classes(
                    "w-full bg-indigo-500 text-white font-bold py-3 rounded-lg hover:bg-indigo-600 transition-colors"
                )

            # Footer Link
            with ui.row().classes("w-full justify-center mt-6"):
                ui.label("Don't have an account?").classes("text-gray-600")
                ui.link("Sign up", "/trainee/signup").classes(
                    "ml-1 font-medium text-indigo-500 hover:underline"
                )
