# app/downloader.py
import os
import yt_dlp
import logging

def download_audio(search_query):
    """
    Mencari dan mendownload audio dari YouTube berdasarkan query pencarian.
    Output file akan dikonversi ke format AAC dengan bitrate 320 kbps.
    Mengembalikan nama file jika berhasil, atau None jika gagal.
    """
    downloads_folder = 'downloads'
    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        # Template nama file; file akan disimpan di folder downloads
        'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'aac',
            'preferredquality': '320',
        }],
        'postprocessor_args': ['-b:a', '320k'],
        'logger': MyLogger(),
        'noplaylist': True,
    }
    
    # Menggunakan fitur pencarian ytsearch dari yt-dlp
    search_url = f"ytsearch1:{search_query}"
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(search_url, download=True)
            if 'entries' in info and len(info['entries']) > 0:
                # Setelah download, file sudah dikonversi.
                downloaded_file = ydl.prepare_filename(info['entries'][0])
                # Ubah ekstensi file menjadi .aac
                base, _ = os.path.splitext(downloaded_file)
                final_file = base + '.aac'
                return final_file.split(os.sep)[-1]  # Mengembalikan nama file saja
            else:
                return None
    except Exception as e:
        logging.error("Error di download_audio: %s", str(e))
        return None

class MyLogger:
    def debug(self, msg):
        pass  # Opsional: Tambahkan logging debug jika diinginkan

    def warning(self, msg):
        logging.warning(msg)

    def error(self, msg):
        logging.error(msg)
