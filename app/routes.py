# app/routes.py
import os
import logging
from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory
from app import downloader, spotify_search

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/download', methods=['POST'])
def download():
    spotify_url = request.form.get('spotify_url')
    if not spotify_url:
        flash("Harap masukkan link Spotify.", "error")
        return redirect(url_for('main.index'))
    
    try:
        # Ambil informasi lagu dari Spotify
        track_info = spotify_search.get_track_info(spotify_url)
        if not track_info:
            flash("Lagu tidak ditemukan dari Spotify.", "error")
            return redirect(url_for('main.index'))
        
        # Buat query pencarian berdasarkan judul dan artis
        search_query = f"{track_info['name']} {track_info['artists']}"
        
        # Download audio dari YouTube menggunakan query tersebut
        result_filename = downloader.download_audio(search_query)
        if result_filename:
            flash("Download berhasil!", "success")
            # Kirim file yang sudah didownload agar bisa diunduh oleh user
            return send_from_directory('downloads', result_filename, as_attachment=True)
        else:
            flash("Download gagal. Silakan coba lagi.", "error")
            return redirect(url_for('main.index'))
        
    except Exception as e:
        logging.error("Error di /download: %s", str(e))
        flash("Terjadi error saat download.", "error")
        return redirect(url_for('main.index'))
