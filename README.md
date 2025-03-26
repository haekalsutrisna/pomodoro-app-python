# Haekal Pomodoro Timer

Haekal Pomodoro Timer adalah aplikasi sederhana berbasis Python dan Tkinter yang berfungsi sebagai timer teknik Pomodoro. Aplikasi ini memungkinkan pengguna untuk mengatur waktu kerja, waktu istirahat, serta jumlah sesi secara otomatis.

## 🚀 Fitur
- **Timer Work & Break Otomatis**: Memulai sesi kerja dan istirahat secara bergantian.
- **Penentuan Jumlah Sesi**: Pengguna dapat menentukan jumlah sesi Pomodoro yang diinginkan.
- **Paus & Reset Timer**: Dapat dijeda dan diatur ulang kapan saja.
- **Notifikasi Audio**: Alarm berbunyi saat sesi berakhir.
- **Antarmuka GUI**: Menggunakan Tkinter untuk tampilan yang user-friendly.

## 📸 Tampilan Aplikasi
<img src="https://github.com/user-attachments/assets/1b7de015-cb77-4a5f-b139-799b230a2810" width="300">

## 🔧 Instalasi
Pastikan Python telah terinstal di sistemmu.

```bash
# Clone repo
git clone https://github.com/haekalsutrisna/pomodoro-timer.git
cd pomodoro-timer

# Install dependencies
pip install -r requirements.txt
```

## 🎮 Cara Menggunakan
1. Jalankan aplikasi dengan perintah berikut:
    ```bash
    python pomodoro.py
    ```
2. Masukkan waktu kerja (Work Time) dan waktu istirahat (Break Time).
3. Masukkan jumlah sesi yang diinginkan.
4. Klik **Start** untuk memulai timer.
5. Timer akan otomatis bergantian antara sesi kerja dan istirahat.
6. Gunakan tombol **Pause** untuk menjeda dan **Reset** untuk mengatur ulang.

## 📂 Struktur Folder
```
📦 pomodoro-timer
 ┣ 📜 pomodoro.py  # Script utama aplikasi
 ┣ 📜 requirements.txt  # Dependensi yang dibutuhkan
 ┣ 📜 README.md  # Dokumentasi proyek
 ┗ 📜 alarm.mp3  # Suara alarm untuk notifikasi
```

## 📌 Dependensi
Aplikasi ini memerlukan beberapa pustaka Python:
```bash
pip install tkinter playsound
```

## 🛠 Kontribusi
Jika ingin berkontribusi, silakan lakukan **fork** repo ini dan buat **pull request**. Semua bantuan sangat dihargai! 🎉

## ⚡ Lisensi
Aplikasi ini dirilis di bawah lisensi MIT. Silakan gunakan dan modifikasi sesuai kebutuhan. 🚀
