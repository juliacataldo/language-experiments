#!/usr/bin/env python3
"""
serve.py — a tiny local web server for running jsPsych experiments and saving data.

WHY YOU NEED THIS
-----------------
Double-clicking an .html file lets you *run* an experiment, but JavaScript in a
browser cannot write files to your computer, so no data is saved. This little
server acts as a "mini-server" on your own machine: it serves your experiment
files AND accepts the data your experiment sends back, writing it to ./data/.

It uses only Python's standard library, so there is nothing to install.

HOW TO USE
----------
1. Open a terminal/command prompt INSIDE your experiment folder (the folder
   that contains ldt.html and the jspsych/ folder).
2. Run:   python3 serve.py        (on Windows, try:  python serve.py)
3. In your browser, go to:   http://localhost:8000/ldt.html
4. Finish the experiment. A .csv file will appear in the ./data/ folder.
5. Press Ctrl+C in the terminal to stop the server when you're done.
"""

import http.server
import socketserver
import json
import os
import datetime

PORT = 8000
DATA_DIR = "data"


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Only handle requests aimed at the "save" endpoint; ignore anything else.
        if self.path.rstrip("/").endswith("save"):
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                payload = json.loads(body)
                filename = str(payload.get("filename", "data"))
                data = payload.get("data", "")
            except Exception:
                self.send_response(400)
                self.end_headers()
                return

            os.makedirs(DATA_DIR, exist_ok=True)

            # Build a safe, unique filename like  ldt_20260211_153000.csv
            safe = "".join(c for c in filename if c.isalnum() or c in ("-", "_")) or "data"
            stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            path = os.path.join(DATA_DIR, f"{safe}_{stamp}.csv")

            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(data)
            print("Saved:", path)

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"ok")
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving this folder at http://localhost:{PORT}/   (press Ctrl+C to stop)")
        print(f"Open, for example:  http://localhost:{PORT}/ldt.html")
        print(f"Saved data will go in the ./{DATA_DIR}/ folder.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
