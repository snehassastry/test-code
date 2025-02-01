from ._anvil_designer import BlogTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from anvil import open_form
anvil.users.login_with_form()

class Blog(BlogTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  def home_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Login')
  def blog_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Blog')

