import tkinter as tk
import time
import threading
from playsound import playsound

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Haekal Pomodoro Timer")
        self.root.geometry("350x400")

        self.running = False
        self.time_left = 0
        self.current_session = 0  # Full sessions (work + break)

        # Label & Input for Timer Settings
        tk.Label(root, text="Work Time (minutes):").pack()
        self.work_input = tk.Entry(root)
        self.work_input.pack()
        self.work_input.insert(0, "25")

        tk.Label(root, text="Break Time (minutes):").pack()
        self.break_input = tk.Entry(root)
        self.break_input.pack()
        self.break_input.insert(0, "5")

        tk.Label(root, text="Number of Sessions:").pack()
        self.session_input = tk.Entry(root)
        self.session_input.pack()
        self.session_input.insert(0, "4")

        # Session Label
        self.session_label = tk.Label(root, text="Session: 0", font=("Arial", 14))
        self.session_label.pack(pady=5)

        # Session Type Label (Work / Break)
        self.session_type_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.session_type_label.pack(pady=5)

        # Timer Label
        self.timer_label = tk.Label(root, text="00:00", font=("Arial", 50))
        self.timer_label.pack(pady=10)

        # Frame for Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Buttons
        self.start_button = tk.Button(button_frame, text="Start", command=self.start_pomodoro)
        self.start_button.grid(row=0, column=0, padx=5, pady=5)

        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause_timer)
        self.pause_button.grid(row=0, column=1, padx=5, pady=5)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=5, pady=5)

    def start_pomodoro(self):
        """Starts the Pomodoro cycle where 1 session = Work + Break."""
        if not self.running:
            try:
                self.total_sessions = int(self.session_input.get())  # Total full Pomodoro cycles
                self.current_session = 0  # Reset session count
                self.running = True
                threading.Thread(target=self.run_sessions, daemon=True).start()
            except ValueError:
                self.timer_label.config(text="Invalid Input")

    def run_sessions(self):
        """Runs work and break sessions in a loop based on the session count."""
        while self.current_session < self.total_sessions and self.running:
            self.current_session += 1
            self.session_label.config(text=f"Session: {self.current_session}")

            # Work Phase
            self.run_timer(int(self.work_input.get()) * 60, "Work Time")

            if not self.running:
                break  # Stop if paused

            # Break Phase
            self.run_timer(int(self.break_input.get()) * 60, "Break Time")

        if self.running:
            self.timer_label.config(text="🎉 Congratulations! 🎉", font=("Arial", 20))
            self.session_type_label.config(text="All sessions completed!", fg="green")

    def run_timer(self, duration, session_type):
        """Runs a countdown timer for the given duration and updates session type label."""
        self.session_type_label.config(text=session_type, fg="blue" if session_type == "Work Time" else "red")
        self.time_left = duration

        while self.time_left > 0 and self.running:
            mins, secs = divmod(self.time_left, 60)
            self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
            time.sleep(1)
            self.time_left -= 1

        if self.time_left == 0 and self.running:
            self.timer_label.config(text=f"{session_type} Over!")
            threading.Thread(target=self.play_alarm, daemon=True).start()

    def play_alarm(self):
        """Plays the alarm sound once."""
        try:
            playsound("alarm.mp3")
        except:
            print("Alarm sound error: file not found")

    def pause_timer(self):
        """Pauses the timer."""
        self.running = False

    def reset_timer(self):
        """Resets the timer and stops all sessions."""
        self.running = False
        self.time_left = 0
        self.current_session = 0
        self.timer_label.config(text="00:00")
        self.session_label.config(text="Session: 0")
        self.session_type_label.config(text="")

# Run the application
root = tk.Tk()
app = PomodoroApp(root)
root.mainloop()
