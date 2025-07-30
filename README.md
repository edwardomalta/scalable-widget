# Scalable widget

I am trying to get this result:

![Example 1][example1]

---

So far I am not so away from that result:

![Example 2][example2]

---

But this are the results I am getting on my 2 devices a phone and a tablet:

O my phone:

![Phone example][device1]

On my tablet:

![Tablet example][device2]

---

For running this on my development computer I use this command:

`python main.py -m screen:droid2,portrait,scale=0.75`

[example1]: examples/example1.png
[example2]: examples/example2.png
[example3]: examples/example3.png
[device1]: examples/example-device1.jpeg
[device2]: examples/example-device2.jpeg


---

## Solution so far

Thank you to your help I find this solution:

```python
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
```

