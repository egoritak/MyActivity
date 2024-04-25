import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime, timedelta
import os

class NoteApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Display the current time and duration
        self.current_time = Label(text=f"Current Time [HH:MM]: {datetime.now().strftime('%H:%M')}")
        self.duration = Label(text="Duration [HH:MM]: 00:05")
        self.note_input = TextInput(hint_text='Note [TEXT]', size_hint=(1, 0.2))
        
        # Buttons to add notes and show history
        self.add_note_btn = Button(text='Add Note', size_hint=(1, 0.1))
        self.add_note_btn.bind(on_press=self.add_note)
        self.show_history_btn = Button(text='Show History', size_hint=(1, 0.1))
        self.show_history_btn.bind(on_press=self.show_history)
        
        # Add widgets to the layout
        self.layout.add_widget(self.current_time)
        self.layout.add_widget(self.duration)
        self.layout.add_widget(self.note_input)
        self.layout.add_widget(self.add_note_btn)
        self.layout.add_widget(self.show_history_btn)
        
        return self.layout

    def add_note(self, instance):
        # Write the note to a file
        with open('notes.txt', 'a') as f:
            time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M')
            f.write(f"{time_stamp} - {self.note_input.text}\n")
        self.note_input.text = ''  # Clear the input field after adding

    def show_history(self, instance):
        # Read notes from the file and display them
        if os.path.exists('notes.txt'):
            with open('notes.txt', 'r') as f:
                history = f.read()
            print("Note History:")
            print(history)
        else:
            print("No history available.")

if __name__ == '__main__':
    NoteApp().run()
