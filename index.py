# index.py
from app import app
from layout import create_layout
import callbacks

app.layout = create_layout()

if __name__ == '__main__':
    app.run_server(debug=True)
