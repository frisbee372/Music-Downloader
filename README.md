# Spotify Music Downloader 🎵🚀

Selamat datang di **Downloader Lagu** – aplikasi web berbasis Python yang memungkinkan kamu untuk mendownload lagu dari YouTube dengan kualitas tinggi (AAC 320 kbps) dan mencari lagu berdasarkan link Spotify!  
Dibangun dengan [Flask](https://flask.palletsprojects.com/) dan didukung oleh [yt-dlp](https://github.com/yt-dlp/yt-dlp) serta [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/).

---

## Fitur Utama 😎

- **Download & Konversi Audio**  
  🎶 Mendownload audio dari YouTube menggunakan `yt-dlp` dan mengkonversinya ke format AAC 320 kbps dengan FFmpeg.

- **Pencarian Berdasarkan Spotify**  
  🔍 Mengambil informasi lagu (judul & artis) dari link Spotify menggunakan API Spotify via `Spotipy`.

- **Antarmuka Web Modern**  
  🖥️ Dibangun dengan Flask, dilengkapi dengan tampilan bergaya Material Design & efek frosted glass.

- **Notifikasi, Progress Bar & Alert**  
  📢 Menampilkan alert (flash messages) dan progress bar (simulasi) untuk memberi feedback saat proses download & converting.

---

## Teknologi yang Digunakan 🔧

- ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
- ![Flask](https://img.shields.io/badge/Flask-2.x-blue?logo=flask&logoColor=white)
- ![yt-dlp](https://img.shields.io/badge/yt--dlp-red?logo=youtube&logoColor=white)
- ![Spotipy](https://img.shields.io/badge/Spotify-API-green?logo=spotify&logoColor=white)
- ![FFmpeg](https://img.shields.io/badge/FFmpeg-4.x-orange?logo=ffmpeg&logoColor=white)

---

## Instalasi 👅

```bash
# Clone Repository
$ git clone https://github.com/username/repository.git

# Buat Virtual Environment
$ python3 -m venv venv

# Aktifkan Virtual Environment
$ source venv/bin/activate  # Untuk macOS/Linux
$ venv\Scripts\activate     # Untuk Windows

# Install Dependencies
$ pip install -r requirements.txt

# Set Environment Variables
$ export SPOTIPY_CLIENT_ID='your_spotify_client_id'
$ export SPOTIPY_CLIENT_SECRET='your_spotify_client_secret'

# Install FFmpeg (macOS: Homebrew)
$ brew install ffmpeg  # Untuk macOS/Linux
$ sudo apt install ffmpeg  # Untuk Ubuntu/Debian
$ choco install ffmpeg  # Untuk Windows

# Jalankan Aplikasi
$ python run.py
```

---

## Penggunaan Aplikasi 💪

1. Jalankan Aplikasi:
   ```bash
   $ python run.py
   ```
2. Buka Browser:
   - Kunjungi: [http://127.0.0.1:5000](http://127.0.0.1:5000)
3. Masukkan Link Spotify:
   - Tempelkan URL lagu dari Spotify di form yang tersedia
4. Download & Konversi:
   - Klik tombol **"Download"** dan perhatikan progress bar
   - Notifikasi akan muncul untuk status download & konversi

---

## Lisensi 📝

Proyek ini dilisensikan di bawah MIT License.