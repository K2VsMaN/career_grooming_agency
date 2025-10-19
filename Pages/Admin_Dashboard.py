from nicegui import ui
from typing import List, Dict, Any

# --- Data Abstraction ---



STATS_DATA = [
    {'title': 'Number of Applications', 'value': '152', 'icon': 'description'},
    {'title': 'Total Agents',           'value': '12',  'icon': 'groups'},
    {'title': 'Total Trainees',         'value': '85',  'icon': 'school'},
    {'title': 'Sponsors',               'value': '24',  'icon': 'work'},
]

USERS_DATA = [
    {'id': 1, 'name': 'John Doe',   'role': 'Agent',   'status': ('Active', 'bg-emerald-100 text-emerald-700'), 'details': '8 Trainees',  'avatar': '/assets/mentors/M1.jpg'},
    {'id': 2, 'name': 'Alex Ray',   'role': 'Trainee', 'status': ('Pending Assignment', 'bg-yellow-100 text-yellow-700'), 'details': 'Unassigned', 'avatar': '/assets/mentors/M2.jpg'},
    {'id': 3, 'name': 'Jane Smith', 'role': 'Agent',   'status': ('Active', 'bg-emerald-100 text-emerald-700'), 'details': '5 Trainees',  'avatar': '/assets/mentors/M3.jpg'},
    {'id': 4, 'name': 'Peter Jones','role': 'Agent',   'status': ('Inactive', 'bg-red-100 text-red-700'), 'details': '10 Trainees', 'avatar': '/assets/mentors/M4.jpg'},
]

SPONSORS_DATA = [
    {'name': 'TechCorp Inc.', 'meta': '15 Scholarships', 'logo': '/assets/sponsors/techcorp.png'},
    {'name': 'Innovate LLC',  'meta': '10 Scholarships', 'logo': '/assets/sponsors/innovate.png'},
    {'name': 'CodeFoundry',   'meta': '8 Scholarships',  'logo': '/assets/sponsors/codefoundry.png'},
]

# --- Reusable UI Components / Helper Functions ---

def _create_stat_cards(stats: List[Dict[str, str]]):
    """Creates the grid of statistic cards."""
    with ui.element('div').classes('grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 mt-6'):
        for s in stats:
            with ui.element('div').classes('bg-white rounded-2xl border border-gray-200 shadow-sm p-5'):
                with ui.element('div').classes('flex items-start justify-between'):
                    with ui.column().classes('gap-1'):
                        ui.label(s['title']).classes('text-sm text-gray-600')
                        ui.label(s['value']).classes('text-2xl font-bold text-slate-900')
                    with ui.element('div').classes('w-10 h-10 rounded-full bg-blue-50 text-blue-600 flex items-center justify-center'):
                        ui.icon(s['icon']).classes('text-xl')

def _create_application_management():
    """Creates the application management card with action buttons."""
    with ui.element('div').classes('bg-white rounded-2xl border border-gray-200 shadow-sm mt-6 p-5'):
        ui.label('Application Management').classes('text-slate-900 font-semibold mb-3')
        with ui.row().classes('gap-3'):
            ui.button('Get Forms', icon='download', on_click=lambda: ui.notify('Downloading forms...')).classes(
                'bg-black text-white hover:bg-neutral-900 rounded-lg'
            ).props('no-caps unelevated')
            ui.button('Delete Forms', icon='delete', on_click=lambda: ui.notify('Deleting selected forms...', type='negative')).classes(
                'bg-black text-white hover:bg-neutral-900 rounded-lg'
            ).props('no-caps unelevated')

def _create_user_management_table(users: List[Dict[str, Any]]):
    """Creates the main user management table and its controls."""
    selected_ids = set()

    def update_table():
        """Refreshes the user table display."""
        user_list.refresh()

    def remove_selected():
        """Removes selected users from the data list and updates the table."""
        if not selected_ids:
            ui.notify('No users selected to remove.', type='warning')
            return

        # In a real app, you would make an API call here to delete users.
        # For this demo, we filter the list in-place.
        initial_count = len(users)
        users[:] = [user for user in users if user['id'] not in selected_ids]
        removed_count = initial_count - len(users)
        selected_ids.clear()
        ui.notify(f'Removed {removed_count} user(s).', type='positive')
        update_table()

    def assign_with_ai():
        """Placeholder for AI assignment logic."""
        ui.notify('Using AI to assign roles...', type='info')
        # Here you would implement the AI assignment logic

    with ui.element('div').classes('lg:col-span-2'):
        with ui.element('div').classes('bg-white rounded-2xl border border-gray-200 shadow-sm p-5'):
            ui.label('Agent & Trainee Management').classes('text-slate-900 font-semibold')

            with ui.row().classes('mt-3 gap-2'):
                ui.button('Assign with AI', icon='smart_toy', on_click=assign_with_ai).classes(
                    'bg-black text-white hover:bg-neutral-900 rounded-lg'
                ).props('no-caps unelevated')
                ui.button('Remove', icon='person_remove', on_click=remove_selected).classes(
                    'bg-black text-white hover:bg-neutral-900 rounded-lg'
                ).props('no-caps unelevated')

            # Table-like list, decorated to be refreshable
            @ui.refreshable
            def user_list():
                with ui.element('div').classes('mt-4 rounded-xl border border-gray-200 overflow-hidden bg-white'):
                    # Header row
                    with ui.element('div').classes(
                        'bg-gray-50 text-xs font-semibold text-gray-500 uppercase tracking-wide '
                        'grid grid-cols-12 items-center px-4 py-3'
                    ):
                        ui.label('').classes('col-span-1')
                        ui.label('Member').classes('col-span-5')
                        ui.label('Role').classes('col-span-2')
                        ui.label('Status').classes('col-span-2')
                        ui.label('Details').classes('col-span-2 text-right')

                    # Data rows
                    with ui.element('div').classes('divide-y divide-gray-200'):
                        if not users:
                            with ui.element('div').classes('text-center py-10 text-gray-500'):
                                ui.icon('group_off', size='lg').classes('opacity-50')
                                ui.label('No users to display.')
                            return

                        for user in users:
                            with ui.element('div').classes('grid grid-cols-12 items-center px-4 py-3 hover:bg-gray-50'):
                                # Checkbox to add/remove user ID from the selected set
                                ui.checkbox(on_change=lambda e, user_id=user['id']: selected_ids.add(user_id) if e.value else selected_ids.remove(user_id)).props('dense size=sm').classes('col-span-1')

                                with ui.row().classes('col-span-5 items-center gap-3'):
                                    ui.avatar().props(f'size=32px src={user["avatar"]}')
                                    ui.label(user['name']).classes('text-slate-800')

                                ui.label(user['role']).classes('col-span-2 text-slate-700')

                                with ui.element('div').classes('col-span-2'):
                                    ui.label(user['status'][0]).classes(
                                        f'inline-block px-2 py-1 rounded-full text-xs {user["status"][1]}'
                                    )

                                with ui.row().classes('col-span-2 justify-end items-center gap-1'):
                                    ui.label(user['details']).classes('text-slate-700 text-sm')
                                    ui.icon('chevron_right').classes('text-gray-400')
            user_list()

def _create_sponsors_panel(sponsors: List[Dict[str, str]]):
    """Creates the side panel for sponsor information."""
    with ui.element('div').classes('lg:col-span-1'):
        with ui.element('div').classes('bg-white rounded-2xl border border-gray-200 shadow-sm p-5'):
            ui.label('Sponsor Information').classes('text-slate-900 font-semibold')

            for s in sponsors:
                with ui.element('div').classes(
                    'mt-3 border border-gray-200 rounded-xl px-4 py-3 '
                    'flex items-center justify-between hover:bg-gray-50'
                ):
                    with ui.row().classes('items-center gap-3'):
                        with ui.element('div').classes(
                            'w-8 h-8 rounded-full bg-white ring-1 ring-gray-200 '
                            'flex items-center justify-center overflow-hidden'
                        ):
                            ui.image(s['logo']).classes('w-6 h-6 object-contain')
                        with ui.column().classes('leading-tight'):
                            ui.label(s['name']).classes('text-sm font-medium text-slate-900')
                            ui.label(s['meta']).classes('text-xs text-gray-500')
                    ui.icon('chevron_right').classes('text-gray-400')

            ui.link('View All Sponsors', '#').classes('block text-blue-600 mt-4')

@ui.page("/pages/admin_dashboard")
def show_admin_dashboard():
    """Main function to build and display the admin dashboard."""
    with ui.element('div').classes('min-h-screen bg-gray-50 px-4 md:px-6 lg:px-8 py-6'):

        # Header
        with ui.column().classes('gap-1'):
            ui.label('Admin Dashboard').classes('text-3xl font-extrabold text-slate-900')
            ui.label('Oversee and manage the entire platform.').classes('text-sm md:text-base text-gray-500')

        _create_stat_cards(STATS_DATA)
        _create_application_management()

        with ui.element('div').classes('grid grid-cols-1 lg:grid-cols-3 gap-6 mt-6'):
            # Note: The user data is passed as a mutable list, so changes inside
            # the function will persist.
            _create_user_management_table(USERS_DATA)
            _create_sponsors_panel(SPONSORS_DATA)