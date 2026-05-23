"""
AegisBridge Server — serves AegisBridge.html at http://localhost:5000
OpenRouter API calls go directly from browser to openrouter.ai (no proxy needed).
Uses only Python built-in libraries — nothing to install.
"""
import http.server, os, sys, threading, webbrowser

PORT = 5000
DIR  = os.path.dirname(os.path.abspath(__file__))

MIME = {
    '.html': 'text/html; charset=utf-8',
    '.js':   'application/javascript',
    '.css':  'text/css',
    '.png':  'image/png',
    '.jpg':  'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.webp': 'image/webp',
    '.ico':  'image/x-icon',
}

class H(http.server.BaseHTTPRequestHandler):
    def log_message(self, fmt, *a):
        print('  [GET]', self.path[:80])

    def do_GET(self):
        path = self.path.split('?')[0]
        if path == '/':
            path = '/AegisBridge.html'
        fp = os.path.join(DIR, path.lstrip('/'))
        if not os.path.isfile(fp):
            self.send_response(404); self.end_headers()
            self.wfile.write(b'Not found'); return
        ext  = os.path.splitext(fp)[1].lower()
        data = open(fp, 'rb').read()
        self.send_response(200)
        self.send_header('Content-Type',   MIME.get(ext, 'text/plain'))
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

def main():
    print()
    print('  ╔══════════════════════════════════════╗')
    print('  ║     AegisBridge  —  Local Server     ║')
    print('  ╚══════════════════════════════════════╝')
    print()
    print('  ✅  Open this in your browser:')
    print('      http://localhost:%d' % PORT)
    print()
    print('  !! KEEP THIS WINDOW OPEN !!')
    print('     Close it = app stops working')
    print()
    print('  Press Ctrl+C here to stop the server.')
    print('  ──────────────────── LOG ────────────────')

    threading.Thread(
        target=lambda: (lambda: (
            __import__('time').sleep(1.5),
            webbrowser.open('http://localhost:%d' % PORT)
        ))(),
        daemon=True
    ).start()

    try:
        http.server.HTTPServer(('127.0.0.1', PORT), H).serve_forever()
    except KeyboardInterrupt:
        print('\n  Stopped.')
    except OSError as e:
        if '10048' in str(e) or 'already in use' in str(e):
            print('  [ERROR] Port %d is busy. Close whatever is using it.' % PORT)
        else:
            print('  [ERROR]', e)
        input('  Press Enter to close...')
        sys.exit(1)

if __name__ == '__main__':
    main()
