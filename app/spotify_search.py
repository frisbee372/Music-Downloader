import os
import logging

try:
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
except ImportError:
    logging.error("Modul spotipy belum terinstal. Install dengan 'pip install spotipy'")
    spotipy = None

def get_track_info(spotify_url):
    """
    Mengambil informasi lagu (judul dan artis) dari link Spotify.
    Pastikan environment variables SPOTIPY_CLIENT_ID dan SPOTIPY_CLIENT_SECRET telah diset.
    Mengembalikan dictionary dengan key 'name' dan 'artists', atau None jika gagal.
    """
    if spotipy is None:
        return None

    try:
        # Menggunakan environment variables dengan nama yang tepat
        client_id = os.environ.get('SPOTIPY_CLIENT_ID')
        client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
        
        # Jika belum diset, log error
        if not client_id or not client_secret:
            logging.error("Spotify API credentials belum diset di environment variables.")
            return None
        
        auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(auth_manager=auth_manager)
        track = sp.track(spotify_url)
        if track:
            track_name = track['name']
            artists = ', '.join([artist['name'] for artist in track['artists']])
            return {'name': track_name, 'artists': artists}
        else:
            return None
    except Exception as e:
        logging.error("Error di get_track_info: %s", str(e))
        return None
