from ._anvil_designer import Login_copyTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from anvil import open_form

anvil.users.login_with_form()


class Login_copy(Login_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    mail = self.mail_entered.text
    pwd = self.pwd_entered.text
    # Call your 'send_feedback' server function
    # pass in name, email and feedback as arguments
    anvil.server.call("send_feedback", mail, pwd)

  def button_1_click(self, **event_args):
    """Navigate to Form2 when button is clicked"""
    open_form("Blog")

  def home_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Login")
