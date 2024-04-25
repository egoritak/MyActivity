import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from datetime import datetime, timedelta
import os
import json

class NoteApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Current time components
        now = datetime.now()
        time_layout = BoxLayout(size_hint=(1, 0.2))  # Allocate space
        time_layout.add_widget(Label(text='TIME:', size_hint=(0.1, 1)))
        self.hour_spinner = Spinner(
            text=f'{now.hour:02d}',
            values=[f"{i:02d}" for i in range(24)],
            size_hint=(0.45, 1),  # Adjusted for half the remaining space
        )
        self.minute_spinner = Spinner(
            text=f'{now.minute:02d}',
            values=[f"{i:02d}" for i in range(60)],
            size_hint=(0.45, 1),  # Adjusted for half the remaining space
        )
        time_layout.add_widget(self.hour_spinner)
        time_layout.add_widget(self.minute_spinner)
        self.hour_spinner.bind(text=self.update_time)
        self.minute_spinner.bind(text=self.update_time)

        # Duration components
        duration_layout = BoxLayout(size_hint=(1, 0.2))
        duration_layout.add_widget(Label(text='DUR:', size_hint=(0.1, 1)))
        self.duration_hour_spinner = Spinner(
            text='00',
            values=[f"{i:02d}" for i in range(24)],
            size_hint=(0.45, 1),  # Same as hour_spinner for alignment
        )
        self.duration_minute_spinner = Spinner(
            text='05',
            values=[f"{i:02d}" for i in range(60)],
            size_hint=(0.45, 1),  # Same as minute_spinner for alignment
        )
        duration_layout.add_widget(self.duration_hour_spinner)
        duration_layout.add_widget(self.duration_minute_spinner)
        self.duration_hour_spinner.bind(text=self.set_duration)
        self.duration_minute_spinner.bind(text=self.set_duration)

        # Note input field
        self.note_input = TextInput(hint_text='Enter your note here', size_hint=(1, 0.2))

        # Buttons for adding and showing history
        button_layout = BoxLayout(size_hint=(1, 0.2))
        self.add_note_btn = Button(text='ADD NOTE', size_hint=(0.5, 1))
        self.show_history_btn = Button(text='SHOW HISTORY', size_hint=(0.5, 1))
        self.add_note_btn.bind(on_press=self.add_note)
        self.show_history_btn.bind(on_press=self.show_history)
        button_layout.add_widget(self.add_note_btn)
        button_layout.add_widget(self.show_history_btn)

        # Add all components to the main layout
        self.layout.add_widget(time_layout)
        self.layout.add_widget(duration_layout)
        self.layout.add_widget(self.note_input)
        self.layout.add_widget(button_layout)

        return self.layout

    def update_time(self, spinner, text):
        # This method is intentionally left empty
        pass

    def set_duration(self, spinner, text):
        # This method is intentionally left empty
        pass

    def add_note(self, instance):
        note_data = {
            "time": f"{self.hour_spinner.text}:{self.minute_spinner.text}",
            "duration": f"{self.duration_hour_spinner.text}:{self.duration_minute_spinner.text}",
            "text": self.note_input.text
        }
        with open('notes.json', 'a') as f:
            json.dump(note_data, f)
            f.write('\n')
        self.note_input.text = ''  # Clear the input field after adding

    def show_history(self, instance):
        if os.path.exists('notes.json'):
            with open('notes.json', 'r') as f:
                for line in f:
                    note = json.loads(line)
                    print(note)  # Consider enhancing this to show in the app UI
        else:
            print("No history available.")

if __name__ == '__main__':
    NoteApp().run()
