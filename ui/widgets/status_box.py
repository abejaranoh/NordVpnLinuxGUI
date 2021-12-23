from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

from kivymd.uix.card import MDSeparator

from ui.widgets.proctection_status import ProtectionStatus
from ui.widgets.location_status import LocationStatus
from ui.widgets.help_status import HelpStatus


Builder.load_string("""
<StatusBox>
    canvas:                
        Color:
            rgba: 0.6, 0.6, 0.6, 0.6
        Line:
            width: 1
            rounded_rectangle: self.x, self.y, self.width, self.height, 15
    orientation: "horizontal"
    padding: 0, dp(8)
    ProtectionStatus:
    MDSeparator:
        size_hint_x: 0.01
        orientation: "vertical"
    LocationStatus:
    MDSeparator:
        size_hint_x: 0.01
        orientation: "vertical"
    HelpStatus:
""")


class StatusBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)