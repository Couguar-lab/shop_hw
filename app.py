import http.server
import socketserver
import os

PORT = 8000
TEMPLATES_DIR = "templates"
CONTACTS_FILE = os.path.join(TEMPLATES_DIR, "contacts.html")

# Читаем contacts.html один раз при старте
with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
    contacts_content = f.read()

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(contacts_content.encode("utf-8"))

    # Дополнительное задание со звёздочкой
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw_data = self.rfile.read(length).decode("utf-8")
        print("\n" + "="*60)
        print("ПОЛУЧЕН POST-ЗАПРОС")
        print("Путь:", self.path)
        print("Данные формы:")
        print(raw_data)
        print("="*60 + "\n")

        # Отвечаем той же страницей
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(contacts_content.encode("utf-8"))

print(f"Сервер запущен → http://localhost:{PORT}")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()