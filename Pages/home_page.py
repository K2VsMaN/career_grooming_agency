from nicegui import ui
from components.header import show_header
from components.footer import show_footer



@ui.page("/")
def show_home_page():
    show_header()

    def show_role_selection_dialog():
        """Creates and opens a dialog for role selection."""
        with ui.dialog() as dialog, ui.card().classes('p-8 rounded-lg'):
            ui.label('How would you like to join us?').classes('text-2xl font-bold text-center w-full mb-6 text-gray-800')
            with ui.row().classes('w-full justify-center items-center gap-6'):
                ui.button('As a Trainee', on_click=lambda: ui.navigate.to('/trainee/forms')).props('color=primary size=lg').classes('px-8 py-4')
                ui.button('As an Agent', on_click=lambda: ui.navigate.to('/agent/forms')).props('color=secondary size=lg').classes('px-8 py-4')
        dialog.open()
    
    # Main content container
    ui.query(".nicegui-content").classes("m-0 p-0")
    
    with ui.column().classes('w-full overflow-x-hidden') as main_column:
        # Hero Section
        with ui.element('div') \
            .classes('relative w-full h-auto min-h-screen flex items-center justify-center py-16') \
            .style('background-image: url("/assets/H1.jpeg"); background-size: cover; background-position: center; background-repeat: no-repeat;') as hero_section:
            
            # Overlay for better text readability
            ui.element('div').classes('absolute inset-0 bg-gradient-to-r from-black/70 via-black/40 to-transparent')
            
            # Hero Section Content
            with ui.column().classes('relative w-full py-20 text-center text-white z-10 px-20 pr-6') as hero_content:
                ui.label('Career Grooming Agency').classes(
                    'bg-black text-white px-4 py-2 rounded-full text-sm font-medium mb-4'
                ).props("flat dense no-caps push ripple")
                
                # ui.label('Empowering Ghana\'s Future Tech Leaders').classes('text-4xl md:text-6xl font-bold text-white mb-6')
                ui.label("Empowering Ghana's\nFuture Tech Leaders").classes('text-4xl md:text-6xl font-bold text-white mb-1 whitespace-pre-line leading-tight')
                
                with ui.column().classes('text-xl text-gray-200 mb-8 gap-2') as hero_text:
                        ui.label('A digital platform that provides mentorship & career guidance,').classes('mb-0')
                        ui.label('to senior high school graduates passionate about technology.').classes('mt-0')
                
            with ui.row().classes(
    'relative z-10 w-full flex-col sm:flex-row gap-4 justify-start items-start '
    'pl-4 sm:pl-6 md:pl-16 -mt-20' # Added relative and z-10
) as hero_buttons:

                ui.button('Start Your Journey', on_click=show_role_selection_dialog).classes(
           'text-lg px-8 py-6 rounded-full border-2 border-white text-white '
           'transition-colors duration-200 ease-out '
           'hover:bg-yellow-400 hover:border-yellow-400 hover:text-black '
           'active:bg-yellow-400 active:border-yellow-400 active:text-black '
           'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-yellow-300 '
           '-mt-[30px]' 
       ).props('flat dense no-caps push ripple')

                ui.button('Learn More').classes(
           'text-lg px-8 py-6 rounded-full border-2 border-white text-white '
           'transition-colors duration-200 ease-out '
           'hover:bg-yellow-400 hover:border-yellow-400 hover:text-black '
           'active:bg-yellow-400 active:border-yellow-400 active:text-black '
           'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-yellow-300 '
           '-mt-[30px]').props('flat dense no-caps push ripple')
    
    # Mission & Vision

    with ui.element("section") \
        .classes("relative w-full h-auto m-0 p-0 overflow-hidden bg-gray-100 -mt-4"):

            with ui.column().classes('max-w-7xl mx-auto px-4 py-16'):
                with ui.row().classes('grid md:grid-cols-2 gap-8'):
                    with ui.card().classes('p-8 text-center bg-white shadow-md'):
                        ui.label('Our Mission').classes('text-2xl font-bold mb-4 w-full text-center')
                        ui.label(
                            'To bridge the gap between education and employment for talented SHS graduates in Ghana, '
                            'providing them with the skills, mentorship, and resources needed to succeed in the tech industry.'
                        ).classes('text-gray-700 leading-relaxed text-center')

                    with ui.card().classes('p-8 text-center bg-white shadow-md'):
                        ui.label('Our Vision').classes('text-2xl font-bold mb-4 w-full text-center')
                        ui.label(
                            'To create a generation of tech-ready professionals who will drive Ghana\'s digital transformation, '
                            'ensuring equal opportunities for all regardless of their financial background.'
                        ).classes('text-gray-700 leading-relaxed text-center')
                        
        # Our Collaborators
    # with ui.element("section").classes("relative w-full max-w-[1200px] mx-auto py-[60px] mt-[30px]"):
    #             ui.label("Our Collaborators").classes("block text-[36px] font-bold leading-[42px] text-center text-[#131315] mb-2")
    #             # Logo grid (flex, Figma sizes)
    #             brand_logos = [
    #                 ("assets/RCOA.png", "w-[380px] h-[150px]"),
    #                 ("assets/CTVET.webp", "w-[180px] h-[180px]"),
    #                 ("assets/MOC.png", "w-[180px] h-[180px]"),
    #                 ("assets/GES.jpg", "w-[220px] h-[150px]"),
    #                 ("assets/MOE.png", "w-[450px] h-[131px]"),
    #                 ("assets/Microsoft.png", "w-[182px] h-[39px]"),
    #                 ("assets/Medium.png", "w-[297px] h-[124px]"),
    #                 ("assets/Zoom.png", "w-[295px] h-[83px]"),
    #                 ("assets/Uber.png", "w-[134px] h-[44px]"),
    #                 ("assets/Grab.png", "w-[145px] h-[52px]")
    #             ]
    #             with ui.row().classes("flex flex-wrap justify-between items-center gap-y-8 gap-x-8 mb-8"):
    #                 for logo, size in brand_logos:
    #                     ui.image(logo).classes(f"object-contain bg-transparent rounded-md {size}")


   
    with ui.element("section").classes("relative w-full max-w-[1200px] mx-auto py-[60px]"):
        ui.label("Our Collaborators").classes("block text-[36px] font-bold leading-[42px] text-center text-[#131315] mb-2")

    # One-time CSS for the marquee
    ui.add_head_html("""
    <style>
      @keyframes logo-marquee {
        0%   { transform: translateX(0); }
        100% { transform: translateX(-50%); } /* shift by one full sequence */
      }
      .logo-track {
        animation: logo-marquee 40s linear infinite;
        will-change: transform;
      }
      .logo-item { flex-shrink: 0; } /* keep logo widths fixed */
      .logo-container:hover .logo-track { animation-play-state: paused; } /* pause on hover */
    </style>
    """)

    # Logos
    brand_logos = [
        ("assets/RCOA.png", "w-[380px] h-[150px]"),
        ("assets/CTVET.webp", "w-[180px] h-[180px]"),
        ("assets/MOC.png", "w-[180px] h-[180px]"),
        ("assets/GES.jpg", "w-[220px] h-[150px]"),
        ("assets/MOE.png", "w-[450px] h-[131px]"),
    ]

    # Infinite scrolling row
    with ui.element('div').classes('logo-container relative w-full overflow-hidden'):
        # track: two identical sequences so the loop is seamless
        with ui.element('div').classes('logo-track flex items-center gap-x-16 w-max'):
            for _ in range(2):  # duplicate the sequence
                for logo, size in brand_logos:
                    ui.image(logo).classes(f"logo-item object-contain bg-transparent rounded-md {size}")


# Featured Mentors
    with ui.element("section").classes("relative w-full max-w-[1200px] mx-auto py-[24px] mt-[30px]"):
        ui.label("Featured Mentors").classes(
            "block text-[36px] font-bold leading-[42px] text-center text-[#131315] mb-10"
        )

        mentors = [
    {"name": "Ama Boateng", "role": "Data Scientist", "sub": "ML, analytics, Python","image": "assets/mentors/M1.jpg"}, 
    {"name": "Kwesi Mensah", "role": "Product Designer", "sub": "Design systems, UX strategy","image": "assets/mentors/M2.jpg"},
    {"name": "Kwame Asare", "role": "Cloud Engineer", "sub": "Azure, DevOps, IaC", "image": "assets/mentors/M3.jpg"},
]
        with ui.element('div').classes('grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8'):
            for m in mentors:
                with ui.element('div').classes(
                    'bg-white rounded-3xl border border-gray-200 shadow-lg '
                    'p-6 flex flex-col items-center text-center transition-shadow hover:shadow-xl'
                ):
                    # Image placeholder / real image
                    with ui.element('div').classes(
                        'w-full h-[500px] rounded-2xl bg-gray-50 border border-gray-200 '
                        'flex items-center justify-center mb-5 overflow-hidden'
                    ):
                        if m.get('image'):
                            ui.image(m['image']).classes('w-full h-full object-contain')
                        else:
                            ui.icon('person').classes('text-gray-400 text-7xl')

                    # Rows: Name, Role, Subtext
                    ui.label(m['name']).classes('text-xl font-semibold text-[#131315]')
                    ui.label(m['role']).classes('text-sm text-gray-600 mt-1')
                    ui.label(m['sub']).classes('text-sm text-gray-500 mt-2')

    show_footer()

# Dummy Text
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit.Maecenas porttitor congue massa.Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero, sit amet commodo magna eros quis urna. 