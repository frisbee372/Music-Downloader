# run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Anda dapat mengubah debug menjadi False untuk production
    app.run(debug=True)
