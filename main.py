import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from datetime import datetime, timedelta
import os

class NoteApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Current Time Adjustments
        now = datetime.now()
        self.current_time_label = Label(text=f'Current Time: {now.strftime("%H:%M")}')
        self.hour_spinner = Spinner(
            text=f'{now.hour:02d}',
            values=[f"{i:02d}" for i in range(24)],
            size_hint=(None, None),
            size=(100, 44),
            pos_hint={'center_x': 0.5}
        )
        self.minute_spinner = Spinner(
            text=f'{now.minute:02d}',
            values=[f"{i:02d}" for i in range(60)],
            size_hint=(None, None),
            size=(100, 44),
            pos_hint={'center_x': 0.5}
        )
        
        # Automatically update time when spinners change
        self.hour_spinner.bind(text=self.update_time)
        self.minute_spinner.bind(text=self.update_time)

        # Duration Adjustments
        self.duration_label = Label(text='Duration: 00:05')
        self.duration_hour_spinner = Spinner(
            text='00',
            values=[f"{i:02d}" for i in range(24)],
            size_hint=(None, None),
            size=(100, 44),
            pos_hint={'center_x': 0.5}
        )
        self.duration_minute_spinner = Spinner(
            text='05',
            values=[f"{i:02d}" for i in range(60)],
            size_hint=(None, None),
            size=(100, 44),
            pos_hint={'center_x': 0.5}
        )

        # Automatically update duration when spinners change
        self.duration_hour_spinner.bind(text=self.set_duration)
        self.duration_minute_spinner.bind(text=self.set_duration)

        # Note Input and Buttons
        self.note_input = TextInput(hint_text='Note [TEXT]', size_hint=(1, 0.2))
        self.add_note_btn = Button(text='Add Note', size_hint=(1, 0.1))
        self.add_note_btn.bind(on_press=self.add_note)
        self.show_history_btn = Button(text='Show History', size_hint=(1, 0.1))
        self.show_history_btn.bind(on_press=self.show_history)

        # Adding widgets to layout
        self.layout.add_widget(self.current_time_label)
        self.layout.add_widget(self.hour_spinner)
        self.layout.add_widget(self.minute_spinner)
        self.layout.add_widget(self.duration_label)
        self.layout.add_widget(self.duration_hour_spinner)
        self.layout.add_widget(self.duration_minute_spinner)
        self.layout.add_widget(self.note_input)
        self.layout.add_widget(self.add_note_btn)
        self.layout.add_widget(self.show_history_btn)

        return self.layout

    def update_time(self, spinner, text):
        current_time = datetime.now().replace(hour=int(self.hour_spinner.text), minute=int(self.minute_spinner.text))
        self.current_time_label.text = f'Current Time: {current_time.strftime("%H:%M")}'

    def set_duration(self, spinner, text):
        duration = timedelta(hours=int(self.duration_hour_spinner.text), minutes=int(self.duration_minute_spinner.text))
        self.duration_label.text = f'Duration: {str(duration)[:-3]}'

    def add_note(self, instance):
        with open('notes.txt', 'a') as f:
            time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M')
            f.write(f"{time_stamp} - {self.note_input.text}\n")
        self.note_input.text = ''  # Clear the input field

    def show_history(self, instance):
        if os.path.exists('notes.txt'):
            with open('notes.txt', 'r') as f:
                history = f.read()
            print("Note History:")
            print(history)
        else:
            print("No history available.")

if __name__ == '__main__':
    NoteApp().run()
