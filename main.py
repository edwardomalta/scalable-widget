from kivy.app import App
from kivy.lang import Builder


kv = """
BoxLayout:
    padding: dp(15)
    spacing: dp(8)
    orientation: "vertical"
    ItemLog:
    ItemLog:

<BLabel@Label>:
    font_size: sp(12)
    size_hint_y: None
    height: self.texture_size[1] + dp(3)
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.5
        RoundedRectangle:
            pos: self.x - dp(2), self.y - dp(2)
            size: self.size
            radius: [dp(5),]
        Color:
            rgba: 0, 0, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size

<ItemLog@RelativeLayout>:
    Image:
        id: bg_image 
        source: "Frame.png"
        allow_stretch: True
        keep_ratio: True
    BoxLayout:
        orientation: "vertical"
        size_hint_x: None
        width: dp(bg_image.width)
        pos_hint: {"center_x": 0.5 }
        Widget:
            size_hint_y: None
            height: dp(20)
        BoxLayout:
            orientation: "vertical"
            Widget:
            Label:
                text: "TITLE LABEL"
                font_size: sp(20)
            Label:
                text: "Subtitle"
                font_size: sp(14)
            Label:
                text: "Date time: 07/07/2025 14:30"
                font_size: sp(12)
            Widget:
        GridLayout:
            cols: 2
            padding: dp(15)
            spacing: dp(5)
            BLabel:
                text: "Name"
            BLabel:
                text: "14. Geographic Z A"
            BLabel:
                text: "Zone"
            BLabel:
                text: "New area Z"
            BLabel:
                text: "User Name"
            BLabel:
                text: "Jonh Fritz"


"""

class ExampleApp(App):
    def build(self):
        return Builder.load_string(kv)

ExampleApp().run()