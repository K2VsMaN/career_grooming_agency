<<<<<<< HEAD
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
=======
from nicegui import ui, app

# --- Configuration (Necessary for the correct look and feel) ---
# Define custom colors (Reverting to Trainee Dashboard Blue)
BLUE_PRIMARY = '#6366F1'
ui.colors(primary=BLUE_PRIMARY, secondary='#E0E7FF') 

ui.add_head_html("""
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        body { font-family: 'Roboto', sans-serif; }
    </style>
""")

# Placeholder sign-out function for the button's click handler
def _sign_out():
    ui.notify('Trainee logging out...', type='warning')
    # In a real app, this would navigate to the login page and clear the session.

def show_sidebar(current_page: str = "/trainee/dashboard"):
    """
    Creates the Trainee Dashboard sidebar using a static ui.column structure.
    
    Args:
        current_page (str): The current URL path to highlight the active link.
    """
    # Remove default NiceGUI padding/margin so the fixed sidebar is flush against the edge
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0") 
    
    # Main sidebar container: Fixed position, full height, 20% width
    with ui.column().classes('bg-white p-4 w-[20%] shadow-lg h-screen justify-between items-center fixed top-0 left-0'):
        
        # --- Top section with branding ---
        with ui.column().classes('w-full items-center mb-6'):
            # Branding: Trainee
            with ui.row().classes('items-center space-x-2'):
                ui.icon('school').classes('text-primary text-4xl') # School Icon
                ui.label('Trainee').classes('text-4xl font-extrabold').style(f"color:{BLUE_PRIMARY}")
            
            ui.label("Trainee Dashboard").classes('text-lg font-bold text-gray-800 mt-2')
            
            # Separator
            ui.separator().classes('w-full h-0.5 mb-6').style(f"background:{BLUE_PRIMARY}")

        # --- Navigation links section ---
        with ui.column().classes('w-full space-y-2 flex-grow'):
            
            # Helper function for dynamic styling of navigation rows
            def nav_link_row(name, icon, target):
                is_active = target == current_page
                
                # Active/Hover classes for the row
                base_class = 'w-full items-center cursor-pointer transition-colors p-2 rounded-lg'
                if is_active:
                    # Blue background for active link
                    row_class = f'bg-primary text-white {base_class}'
                    icon_class = 'text-white'
                    link_class = 'text-white font-extrabold no-underline text-lg'
                else:
                    # Light hover background
                    row_class = f'hover:bg-blue-100 {base_class}'
                    icon_class = 'text-primary'
                    link_class = 'text-gray-700 font-semibold no-underline text-lg'

                with ui.row().classes(row_class):
                    ui.icon(icon).classes(icon_class)
                    ui.link(name, target).classes(link_class)
            
            # Define Navigation Items (Trainee Links)
            nav_link_row('Dashboard', 'dashboard', '/trainee/dashboard')
            nav_link_row('Resources', 'source', '/trainee/resources')
            nav_link_row("Agent's Contact", 'contact_phone', '/trainee/agent_contact')
            nav_link_row('Upload Transcript', 'upload_file', '/trainee/upload_transcript')
            nav_link_row('IT Course Selection', 'model_training', '/trainee/course_selection')

        # --- Logout button at the bottom ---
        with ui.column().classes('w-full items-center mt-auto'):
            # Separator
            ui.separator().classes('w-full h-0.5 mb-6').style("background: #ccc") # Neutral color separator
            
            # Logout Row (Red theme)
            with ui.row().classes('w-full items-center cursor-pointer p-2 rounded-lg hover:bg-red-100 transition-colors'):
                ui.icon('logout').classes('text-red-600')
                # Logout Button
                ui.button(text='Logout', on_click=_sign_out, color='red') \
                    .classes('bg-transparent text-red-600 font-semibold shadow-none text-lg') \
                    .props('flat no-caps')
>>>>>>> d882f559fafc17694cf5194f1f9cdfbc4308cfe5
