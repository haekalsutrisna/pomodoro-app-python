import tkinter as tk
import time
import threading
from playsound import playsound
import pygame  # Untuk kontrol lebih lanjut pada suara
from plyer import notification  # Notifikasi Windows

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Haekal Pomodoro Timer")
        self.root.geometry("350x450")
        self.root.iconbitmap("pomodoro.ico")

        self.running = False
        self.time_left = 0
        self.current_session = 0  # Full sessions (work + break)

        # Inisialisasi pygame mixer
        pygame.mixer.init()

        # Label & Input untuk pengaturan timer
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
        self.session_input.insert(0, "2")

        # Label sesi
        self.session_label = tk.Label(root, text="Session: 0", font=("Arial", 14))
        self.session_label.pack(pady=5)

        # Label jenis sesi (Work / Break)
        self.session_type_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.session_type_label.pack(pady=5)

        # Timer Label
        self.timer_label = tk.Label(root, text="00:00", font=("Arial", 50))
        self.timer_label.pack(pady=10)

        # Frame untuk tombol
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Tombol-tombol utama
        self.start_button = tk.Button(button_frame, text="Start", command=self.start_pomodoro)
        self.start_button.grid(row=0, column=0, padx=5, pady=5)

        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause_timer)
        self.pause_button.grid(row=0, column=1, padx=5, pady=5)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=5, pady=5)

        # Tombol Stop Alarm
        self.stop_alarm_button = tk.Button(root, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED)
        self.stop_alarm_button.pack(pady=5)

    def start_pomodoro(self):
        """Mulai siklus Pomodoro (Work + Break)."""
        if not self.running:
            try:
                self.total_sessions = int(self.session_input.get())  # Total sesi
                self.current_session = 0  # Reset jumlah sesi
                self.running = True
                threading.Thread(target=self.run_sessions, daemon=True).start()
            except ValueError:
                self.timer_label.config(text="Invalid Input")

    def run_sessions(self):
        """Menjalankan sesi kerja dan istirahat sesuai jumlah sesi yang dimasukkan."""
        while self.current_session < self.total_sessions and self.running:
            self.current_session += 1
            self.session_label.config(text=f"Session: {self.current_session}")

            # Fase Kerja
            self.show_notification(f"Session {self.current_session} Work Time", "Work Time starts! Stay focused Sindhy 💪")
            self.run_timer(int(self.work_input.get()) * 60, "Work Time")

            if not self.running:
                break  # Hentikan jika dihentikan

            # Fase Istirahat
            self.show_notification(f"Session {self.current_session} Break time", "Break Time starts! Relax for a moment Sindhy ☕")
            self.run_timer(int(self.break_input.get()) * 60, "Break Time")

        if self.running:
            self.timer_label.config(text="🎉 Congratulations! 🎉", font=("Arial", 20))
            self.session_type_label.config(text="All sessions completed!", fg="green")

    def run_timer(self, duration, session_type):
        """Menjalankan hitungan mundur timer."""
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
        """Memutar suara alarm dan menampilkan notifikasi dengan tombol stop."""
        try:
            pygame.mixer.music.load("alarm.mp3")
            pygame.mixer.music.play()
            self.stop_alarm_button.config(state=tk.NORMAL)  # Aktifkan tombol stop alarm

            # Tampilkan notifikasi Windows
            notification.notify(
                title="Pomodoro Timer",
                message=f"{self.session_type_label.cget('text')} Over! Click Button in Application to stop the alarm.",
                app_name="Haekal Pomodoro Timer",
                timeout=10  # Notifikasi akan hilang setelah 10 detik
            )
        except:
            print("Alarm sound error: file not found")

    def stop_alarm(self):
        """Menghentikan suara alarm."""
        pygame.mixer.music.stop()
        self.stop_alarm_button.config(state=tk.DISABLED)  # Matikan tombol stop alarm

    def pause_timer(self):
        """Menghentikan sementara timer."""
        self.running = False

    def reset_timer(self):
        """Mengatur ulang timer dan menghentikan semua sesi."""
        self.running = False
        self.time_left = 0
        self.current_session = 0
        self.timer_label.config(text="00:00")
        self.session_label.config(text="Session: 0")
        self.session_type_label.config(text="")
        self.stop_alarm()  # Hentikan alarm jika masih berjalan

    def show_notification(self, title, message):
        """Menampilkan notifikasi untuk setiap sesi."""
        notification.notify(
            title=title,
            message=message,
            app_name="Haekal Pomodoro Timer",
            timeout=5
        )

# Jalankan aplikasi
root = tk.Tk()
app = PomodoroApp(root)
root.mainloop()
