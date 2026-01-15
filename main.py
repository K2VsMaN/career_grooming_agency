from nicegui import ui, app
from Components.Header import *
from Components.Footer import *
from Pages.home_page import *
from Pages.Admin_Dashboard import *
from Pages.trainee_dashboard import *
from Pages.agent_forms import *
from Pages.trainee_forms import *
from Pages.trainee_signup import *
from Pages.login import *
from Pages.agent_signup import *
from Pages.admin_signup import *
from Pages.resource import *
from Pages.upload_resource import *



from Pages.agent_dashboard import *



app.add_static_files('/assets', 'assets')

ui.run(storage_secret="asdfghjlzxcvbnm")  # remove on_air=True if you don’t need the live link