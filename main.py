import os, sys
from kivy.resources import resource_add_path

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.properties import ListProperty, NumericProperty
from kivy.metrics import dp
from kivy.metrics import Metrics
from kivy.core.window import Window
from kivy.uix.label import Label



kv = """
BoxLayout:
    padding: dp(15)
    spacing: dp(8)
    orientation: "vertical"
    ItemLog:
    #ItemLog:
<CLabel>:
    #font_size: sp(12)
    #size_hint_y: None
    #height: self.texture_size[1] + dp(3)
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
#<ZLabel>:
    #font_size: dp(9)
<TLabel@Label>:
    size_hint_y: None
    height: self.texture_size[1] + dp(3)

<ItemLog@RelativeLayout>:
    Image:
        id: bg_image 
        source: "Frame.png"
        fit_mode: "contain"
        size_hint_min: dp(340 + 30), dp(272 + 30)
    BoxLayout:
        orientation: "vertical"
        size_hint: None, None
        size: bg_image.norm_image_size
        pos_hint: {"center_x": 0.5, "center_y": 0.5 }
        Widget:
            size_hint_y: None
            height: dp(20)
        BoxLayout:
            orientation: "vertical"
            Widget:
            TLabel:
                text: "TITLE LABEL"
                font_size: sp(20)
            TLabel:
                text: "Subtitle"
                font_size: sp(14)
            TLabel:
                text: "Date time: 07/07/2025 14:30"
                font_size: sp(12)
            Widget:
        GridLayout:
            cols: 2
            padding: dp(15)
            spacing: dp(5)
            CLabel:
                text: "Name"
            CLabel:
                text: "14. Geographic Z A"
            CLabel:
                text: "Zone"
            CLabel:
                text: "New area Z"
            ZLabel:
                text: "User Name"
                image_scaled: bg_image.norm_image_size
            ZLabel:
                text: "Jonh Frutz"
                image_scaled: bg_image.norm_image_size


"""
class ZLabel(Label):
    image_scaled = ListProperty([])
    scale_factor = NumericProperty(1.0)
    base_font_size = NumericProperty(dp(20))  

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = self.base_font_size
        self.bind(image_scaled=self._update_scale)

    def _update_scale(self, *args):
        if self.image_scaled:
            ref_width = dp(340) 
            ref_height = dp(272)

            scale_w = self.image_scaled[0] / ref_width
            scale_h = self.image_scaled[1] / ref_height
            self.scale_factor = min(scale_w, scale_h)

            self.font_size = self.base_font_size * self.scale_factor

class CLabel(Label):
    min_font_size = NumericProperty(5)

    def on_size(self, *args):
        t_width, t_height= self.texture_size
        width, height = self.size
        if t_height < height and t_width < width:  # Grow
            while t_height < height and t_width < width:
                self.font_size += 1
                self.texture_update()
                t_width,t_height = self.texture_size
        elif t_height > height or t_width > width:  # shrink
            while t_height > height or t_width > width:
                self.font_size = max(self.min_font_size, self.font_size - 1)
                if self.font_size == self.min_font_size:
                    break
                self.texture_update()
                t_width, t_height = self.texture_size

class ExampleApp(App):
    def build(self):
        Window.minimum_width, Window.minimum_height = (dp(450), dp(665))
        return Builder.load_string(kv)

ExampleApp().run()