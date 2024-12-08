from shiny import App
from ui import app_ui
from server import server


# Create and run the app
app = App(app_ui, server)
