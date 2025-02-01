from ._anvil_designer import BlogTemplate
from anvil import *
import anvil.server


class Blog(BlogTemplate):
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
