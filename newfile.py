from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# إعداد لون الخلفية (الأسود السيادي)
Window.clearcolor = (0.07, 0.07, 0.07, 1)

class SamsungCalc(App):
    def build(self):
        self.operators = ["/", "*", "+", "-", "÷", "×"]
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # شاشة العرض (Samsung Display)
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=65,
            background_color=(0.07, 0.07, 0.07, 1), foreground_color=(1, 1, 1, 1),
            border=(0,0,0,0)
        )
        main_layout.add_widget(self.solution)
        
        # شبكة الأزرار
        buttons_layout = GridLayout(cols=4, spacing=15)
        
        btns = [
            ('C', (0.17, 0.17, 0.17, 1), (0.1, 0.45, 0.9, 1)),
            ('÷', (0.17, 0.17, 0.17, 1), (0.1, 0.45, 0.9, 1)),
            ('×', (0.17, 0.17, 0.17, 1), (0.1, 0.45, 0.9, 1)),
            ('⌫', (0.17, 0.17, 0.17, 1), (0.1, 0.45, 0.9, 1)),
            ('7', (0.07, 0.07, 0.07, 1), (1, 1, 1, 1)),
            ('8', (0.07, 0.07, 0.07, 1), (1, 1, 1, 1)),
            ('9', (0.07, 0.07, 0.07, 1), (1, 1, 1, 1)),
            ('-', (0.17, 0.17, 0.17, 1), (0.1, 0.45, 0.9, 1)),
            ('4', (0.07, 0.07, 0.07, 1), (1, 1, 1, 1)),
            ('5', (0.07, 0.07, 0.07, 1), (1, 1, 1, 1)),
            ('6', (0.07, 0.07, 0.07, 1), (1, 1, 1, 1)),
            ('+', (0.17, 0.17, 0.17, 1), (0.1, 0.45, 0.9, 1)),
            ('1', (0.07, 0.07, 0.07, 1), (1, 1, 1, 1)),
            ('2', (0.07, 0.07, 0.07, 1), (1, 1, 1, 1)),
            ('3', (0.07, 0.07, 0.07, 1), (1, 1, 1, 1)),
            ('=', (0.1, 0.45, 0.9, 1), (1, 1, 1, 1)),
            ('%', (0.07, 0.07, 0.07, 1), (1, 1, 1, 1)),
            ('0', (0.07, 0.07, 0.07, 1), (1, 1, 1, 1)),
            ('.', (0.07, 0.07, 0.07, 1), (1, 1, 1, 1)),
        ]

        for text, bg, fg in btns:
            btn = Button(
                text=text, background_normal='', background_color=bg,
                color=fg, font_size=32, font_name='Roboto'
            )
            btn.bind(on_press=self.on_click)
            buttons_layout.add_widget(btn)
            
        main_layout.add_widget(buttons_layout)
        return main_layout

    def on_click(self, instance):
        current = self.solution.text
        text = instance.text
        
        if text == "C": self.solution.text = ""
        elif text == "⌫": self.solution.text = current[:-1]
        elif text == "=":
            try:
                # تحويل الرموز لـ لغة بايثون
                res = eval(current.replace('×', '*').replace('÷', '/'))
                self.solution.text = str(res)
            except: self.solution.text = "Error 🍚"
        else: self.solution.text += text

if __name__ == "__main__":
    SamsungCalc().run()
