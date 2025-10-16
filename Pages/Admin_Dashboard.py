from nicegui import ui

@ui.page("/admin_dashboard")
def show_admin_dashboard():
    # Main content (pushed right to clear the fixed sidebar)
    with ui.element('div').classes(
        # adjust these paddings to match your sidebar width and outer margins
        'min-h-screen bg-gray-50 pl-[284px] p-4 md:p-6 lg:p-8'
    ):
        with ui.column().classes("w-full pl-[25%] p-10 overflow-y-auto bg-gray-50"):
            with ui.element('main').classes('flex-1 w-full max-w-[1400px] mx-auto'):
            # Grid of stat cards
                stats = [
                {'title': 'Total Users',    'value': '156',     'sub': '89 active users',        'icon': 'groups'},
                {'title': 'Total Agents',   'value': '12',      'sub': '8 active agents',        'icon': 'group_add'},
                {'title': 'Total Sponsors', 'value': '6',       'sub': '4 active sponsors',      'icon': 'calculate'},
                {'title': 'Total Funds',    'value': '$45,000', 'sub': '$32,000 distributed',    'icon': 'attach_money'},
            ]
            with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6'):
                for s in stats:
                    with ui.element('div').classes(
                        'bg-white rounded-2xl border border-gray-200 '
                        'shadow-sm hover:shadow-md transition-shadow p-5'
                    ):
                        # Header: title + icon (top-right)
                        with ui.element('div').classes('flex items-start justify-between'):
                            ui.label(s['title']).classes('text-slate-900 font-semibold')
                            ui.icon(s['icon']).classes('text-gray-400')

                        # Main metric
                        ui.label(s['value']).classes('text-3xl font-extrabold text-slate-900 mt-5')

                        # Sub text
                        ui.label(s['sub']).classes('text-sm text-gray-500 mt-1')
