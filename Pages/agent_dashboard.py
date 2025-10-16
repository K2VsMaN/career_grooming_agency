from nicegui import ui

@ui.page("/pages/agent_dashboard")
def show_agent_dashbaord():
    
    # ---------- sample data ----------
    trainees = [
        {'id': 'T1', 'name': 'John Doe',     'track': 'Software Development • CGA2025ABC', 'course': 'Web Development Basics', 'last_active': '2024-03-15', 'next_session': '2024-03-20', 'avatar': '/assets/mentors/M1.jpg'},
        {'id': 'T2', 'name': 'Ama Mensah',   'track': 'Data Science • CGA2025DEF',         'course': 'Database Fundamentals',   'last_active': '2024-03-14', 'next_session': '2024-03-22',      'avatar': '/assets/mentors/M2.jpg'},
        {'id': 'T3', 'name': 'Kwame Asante', 'track': 'Cybersecurity • CGA2025GHI',        'course': 'Network Security',        'last_active': '2024-03-16', 'next_session': '2024-03-23', 'avatar': '/assets/mentors/M3.jpg'},
    ]

    # ---------- state ----------
    state = {'q': '', 'selected': set()}

    # ---------- helpers ----------
    def remove_selected():
        ids = state['selected']
        if not ids:
            ui.notify('No trainees selected', color='grey')
            return
        trainees[:] = [t for t in trainees if t['id'] not in ids]
        state['selected'].clear()
        render_list.refresh()
        ui.notify('Selected trainees removed')

    def add_trainee():
        if not (new_name.value and new_track.value):
            ui.notify('Please fill in the required fields')
            return
        new_id = f'T{len(trainees) + 1}'
        trainees.append({
            'id': new_id,
            'name': new_name.value,
            'track': new_track.value,
            'course': new_course.value or '—',
            'last_active': new_last.value or '—',
            # 'next_session': new_next.value or '—',
            'badges': ['pending'],
            'avatar': new_avatar.value,
        })
        dlg_assign.close()
        render_list.refresh()
        ui.notify(f'{new_name.value} added')

    # ---------- dialogs ----------
    with ui.dialog() as dlg_assign, ui.card().classes('w-[560px] max-w-full'):
        ui.label('Assign task').classes('text-lg font-semibold')
        with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 gap-3 mt-2 w-full'):
            new_name  = ui.input('Full Name *').props('outlined dense')
            new_track = ui.input('Track / Cohort *').props('outlined dense')
            new_course = ui.input('Current Course').props('outlined dense')
            new_avatar = ui.input('Avatar URL (/assets/mentors/M3.jpg)').props('outlined dense')
            new_last = ui.input('Last Active (YYYY-MM-DD)').props('outlined dense')
            # new_next = ui.input('Next Session (YYYY-MM-DD)').props('outlined dense')
        with ui.row().classes('justify-end gap-2 w-full mt-2'):
            ui.button('Cancel').classes('rounded-lg').on('click', dlg_assign.close)
            ui.button('Add Trainee').classes('bg-black text-white hover:bg-neutral-900 rounded-lg').props('no-caps').on('click', add_trainee)

    # ---------- trainee list (refreshable) ----------
    @ui.refreshable
    def render_list():
        q = state['q'].lower().strip()
        filtered = [t for t in trainees if q in t['name'].lower() or q in t['track'].lower() or q in t['course'].lower()]

        # Header row
        with ui.element('div').classes(
            'bg-gray-50 text-xs font-semibold text-gray-500 uppercase tracking-wide '
            'grid grid-cols-12 items-center px-4 py-3 rounded-t-xl border border-gray-200 border-b-0'
        ):
            ui.label('').classes('col-span-1')                     # checkbox col
            ui.label('Member').classes('col-span-5')
            ui.label('Current Course').classes('col-span-3')
            ui.label('Last Active').classes('col-span-2')
            ui.label('Actions').classes('col-span-1 text-right')

        # Rows
        with ui.element('div').classes('border border-gray-200 rounded-b-xl divide-y divide-gray-200 bg-white'):
            for t in filtered:
                with ui.element('div').classes('grid grid-cols-12 items-center px-4 py-3 hover:bg-gray-50'):
                    # Checkbox (selection)
                    def toggle_selected(e, tid=t['id']):
                        if e.value:
                            state['selected'].add(tid)
                        else:
                            state['selected'].discard(tid)
                    ui.checkbox(on_change=toggle_selected).props('dense size=sm').classes('col-span-1')

                    # Member cell with avatar + name + badges
                    with ui.row().classes('col-span-5 items-center gap-3'):
                        ui.avatar().props(f'size=36px src={t["avatar"]}')
                        with ui.column().classes('leading-tight'):
                            ui.label(t['name']).classes('text-slate-900 font-medium')
                            with ui.row().classes('gap-2'):
                                ui.label(t['track']).classes('text-xs text-gray-500')
                        
                        

                    # Course
                    ui.label(t['course']).classes('col-span-3 text-slate-800')

                    # Last active
                    ui.label(t['last_active']).classes('col-span-2 text-slate-800')

                    # Actions
                    ui.button('View Details').classes(
                        'col-span-1 justify-self-end bg-black text-white hover:bg-neutral-900 rounded-lg'
                    ).props('no-caps flat').on('click', lambda e, who=t['name']: ui.notify(f'Viewing {who}'))

    # ---------- layout ----------
    with ui.element('div').classes('min-h-screen bg-gray-50 px-4 md:px-6 lg:px-8 py-6'):
        # Header
        with ui.column().classes('gap-1'):
            ui.label('Agent Dashboard').classes('text-3xl font-extrabold text-slate-900')
            ui.label('Welcome back! Manage your trainees and their progress.').classes('text-sm md:text-base text-gray-500')

        # Stats (optional summary)
        stats = [
            {'title': 'Total Trainees', 'value': '12', 'icon': 'groups'},
            {'title': 'Avg Progress',   'value': '—',  'icon': 'trending_up'}, 
            {'title': 'Sessions This Week', 'value': '8', 'icon': 'event'},
            {'title': 'Materials Shared',   'value': '24', 'icon': 'content_copy'},
        ]
        with ui.element('div').classes('grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 mt-6'):
            for s in stats:
                with ui.element('div').classes('bg-white rounded-2xl border border-gray-200 shadow-sm p-5'):
                    with ui.element('div').classes('flex items-start justify-between'):
                        with ui.column().classes('gap-1'):
                            ui.label(s['title']).classes('text-sm text-gray-600')
                            ui.label(s['value']).classes('text-2xl font-bold text-slate-900')
                        with ui.element('div').classes('w-10 h-10 rounded-full bg-blue-50 text-blue-600 flex items-center justify-center'):
                            ui.icon(s['icon']).classes('text-xl')

        # Main trainees section (primary view)
        with ui.element('div').classes('bg-white rounded-2xl border border-gray-200 shadow-sm mt-6 p-5'):
            with ui.row().classes('items-center justify-between gap-3 flex-wrap'):
                with ui.column():
                    ui.label('Assigned Trainees').classes('text-slate-900 font-semibold')
                    ui.label("Manage and monitor your trainees' progress").classes('text-sm text-gray-500')
                with ui.row().classes('gap-2'):
                    search = ui.input(placeholder='Search trainees...').props('outlined dense').classes('w-[240px]')
                    search.on('input', lambda e: (state.__setitem__('q', e.value or ''), render_list.refresh()))
                    ui.button('Assign New Task', icon='add').classes(
                        'bg-black text-white hover:bg-neutral-900 rounded-lg'
                    ).props('no-caps').on('click', dlg_assign.open)
                    ui.button('Remove task', icon='person_remove').classes(
                        'bg-black text-white hover:bg-neutral-900 rounded-lg'
                    ).props('no-caps').on('click', lambda: remove_selected())

            render_list()