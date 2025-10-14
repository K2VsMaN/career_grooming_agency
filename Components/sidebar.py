from nicegui import ui

def show_sidebar():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
active_item = 'Dashboard'  # set this dynamically per page

def show_sidebar():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    with ui.element('aside').classes(
        'sticky top-4 h-[92vh] w-[260px] '
        'bg-white/70 backdrop-blur-xl '
        'border-2 border-blue-300/60 rounded-3xl '
        'shadow-[0_10px_30px_rgba(37,99,235,0.15)] '
        'p-4 flex flex-col'
    ):
        # User header
        with ui.row().classes('items-center gap-3 px-2 py-3'):
            ui.avatar('assets/mentors/M1.jpg').classes('w-12 h-12')  # or ui.avatar('AU') for initials
            with ui.column().classes('leading-tight'):
                ui.label('Admin User').classes('font-semibold text-slate-900')
                ui.label('Administrator').classes('text-xs text-slate-500')

        ui.element('div').classes('h-px bg-slate-200 my-3')

        # Navigation
        nav_items = [
            {'label': 'Dashboard', 'icon': 'grid_view', 'to': '/dashboard'},
            {'label': 'Agents', 'icon': 'groups_2', 'to': '/agents'},
            {'label': 'Trainees', 'icon': 'school', 'to': '/trainees'},
            {'label': 'Sponsors', 'icon': 'business_center', 'to': '/sponsors'},
            {'label': 'Settings', 'icon': 'settings', 'to': '/settings'},
        ]

        base_item = (
            'flex items-center gap-3 px-3 py-2 rounded-xl '
            'text-slate-700 hover:bg-blue-50 hover:text-blue-700 '
            'transition-colors cursor-pointer'
        )
        active_classes = ' bg-blue-100 text-blue-700 font-semibold'

        for item in nav_items:
            is_active = item['label'].lower() == active_item.lower()
            classes = base_item + (active_classes if is_active else '')
            with ui.row().classes(classes) as row:
                ui.icon(item['icon']).classes('text-current')  # inherits current text color
                ui.label(item['label']).classes('text-sm')
            row.on('click', lambda e, to=item['to']: ui.open(to))

        # Push logout to the bottom
        ui.element('div').classes('mt-auto')

        with ui.row().classes(
            'flex items-center gap-3 px-3 py-2 rounded-xl '
            'text-slate-600 hover:text-red-600 hover:bg-red-50 cursor-pointer'
        ) as logout_row:
            ui.icon('logout')
            ui.label('Logout').classes('text-sm')
        logout_row.on('click', lambda e: ui.open('/logout'))