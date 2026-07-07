from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class HelloApp(App):
    """PyAPK Builder test app - real build"""

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        title = Label(
            text='Hello from Python!',
            font_size='36sp',
            bold=True,
        )
        count = [0]

        def on_press(_):
            count[0] += 1
            btn.text = f'Clicks: {count[0]}'

        btn = Button(
            text='Press Me',
            font_size='28sp',
            size_hint=(1, 0.5),
        )
        btn.bind(on_press=on_press)
        layout.add_widget(title)
        layout.add_widget(btn)
        return layout


if __name__ == '__main__':
    HelloApp().run()
