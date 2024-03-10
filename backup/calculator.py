from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from calculation import Calculator
from kivy.core.clipboard import Clipboard
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def clear_default_text(instance, value):
    if value and instance.text == 'Enter data.':
        instance.text = ''


class BulkCalculator(App):

    def __init__(self, **kwargs):
        super().__init__()
        self.copied_label = None
        self.background = None
        self.result_field = None
        self.text_input = None
        self.copy_label_timeout = 0.5

    def build(self):
        main_layout = RelativeLayout()

        self.background = Image(source='background.jpg', allow_stretch=True, keep_ratio=False)
        main_layout.add_widget(self.background)

        instructions_label = Label(
            text='Enter mathematical expression below then hit Calculate to see the result.',
            font_name='Orbitron',
            font_size=20,
            size=(200, 100),
            pos_hint={'center_x': 0.5, 'top': 1.4},
            color='black',
            text_size=(400, None),
        )
        main_layout.add_widget(instructions_label)

        self.text_input = TextInput(size=(400, 150),
                                    text='Enter data.',
                                    size_hint=(None, None),
                                    pos_hint={'center_x': 0.5, 'top': 0.6},
                                    multiline=False,
                                    font_name='Orbitron')
        self.text_input.bind(focus=clear_default_text)
        main_layout.add_widget(self.text_input)

        calculate_btn = Button(size=(400, 50),
                               size_hint=(None, None),
                               pos_hint={'center_x': 0.5, 'top': 0.38},
                               text='Calculate',
                               font_name='Orbitron')
        calculate_btn.bind(on_press=self.calculate)
        main_layout.add_widget(calculate_btn)

        clear_btn = Button(size=(400, 50),
                           size_hint=(None, None),
                           pos_hint={'center_x': 0.5, 'top': 0.28},
                           text='Clear',
                           font_name='Orbitron')
        clear_btn.bind(on_press=self.clear)
        main_layout.add_widget(clear_btn)

        self.result_field = TextInput(
            size=(400, 55),
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'top': 0.20},
            multiline=False,
            font_size=30,
            font_name='Orbitron',
            readonly=True,
            cursor_color=[0, 0, 0, 0],
        )
        self.result_field.bind(focus=self.copy_result)
        main_layout.add_widget(self.result_field)

        self.copied_label = Label(
            text="Copied",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5, 'top': 0.15},
            opacity=0,
            font_name='Orbitron'
        )
        main_layout.add_widget(self.copied_label)

        return main_layout

    def calculate(self, instance):
        expression = self.text_input.text

        if expression:
            calculator = Calculator(expression)

            result = calculator.calculating()
            self.result_field.text = result

    def clear(self, instance):
        self.text_input.text = ''
        self.result_field.text = ''

    def copy_result(self, instance, value):

        if self.result_field.text:
            Clipboard.copy(self.result_field.text)
            self.show_copied_label()

    def show_copied_label(self):
        self.copied_label.opacity = 1
        Clock.schedule_once(self.hide_copied_label, self.copy_label_timeout)

    def hide_copied_label(self, dt):
        self.copied_label.opacity = 0


if __name__ == '__main__':
    BulkCalculator().run()
