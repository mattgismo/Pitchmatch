from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn

app = FastAPI(title="Pitch Match!")

LANDING_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>Pitch Match!</title>
  <style>
    body {font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; margin:0; background: linear-gradient(135deg,#0f172a 0%, #111827 50%, #0b1220 100%); color:#fff; display:flex; align-items:center; justify-content:center; height:100vh;}
    .card {background: rgba(255,255,255,0.04); padding:32px; border-radius:12px; box-shadow: 0 6px 30px rgba(2,6,23,0.6); max-width:720px; text-align:center;}
    h1 {font-size:36px; margin:0 0 8px 0;}
    p {margin:8px 0 16px 0; color:#cbd5e1;}
    .cta {display:inline-block; padding:10px 18px; border-radius:8px; background:linear-gradient(90deg,#ef4444,#f97316); color:#fff; text-decoration:none; font-weight:600;}
    footer {margin-top:18px; font-size:13px; color:#94a3b8;}
  </style>
</head>
<body>
  <div class="card">
    <h1>🎶 Pitch Match!</h1>
    <p>Try a simple singing analysis API. Upload your recording and compare pitch & timing.</p>
    <a class="cta" href="/api">Try API (JSON)</a>
    <footer>Created by Matt Gismondi — developed with ChatGPT guidance.</footer>
  </div>
</body>
</html>
"""

@app.get('/', response_class=HTMLResponse)
async def homepage():
    return HTMLResponse(LANDING_HTML)

@app.get('/api')
async def api_home():
    return JSONResponse({'message': '🎶 Welcome to Pitch Match! Ready to sing?'})

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
