# save_as_html.py
import webbrowser
from pathlib import Path
import html
import datetime

INPUT = "scraped_data.txt"      # produced by your web scraper
OUTPUT = "scraped_results.html"

def parse_line(line):
    # Expected format: Title --> href
    if "-->" in line:
        title, href = line.split("-->", 1)
        return title.strip(), href.strip()
    return line.strip(), ""

def build_html(rows):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    header = f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Web Scraping Project – ShadowFox Internship</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {{ background-color: #f8f9fa; }}
    h1 {{ font-size: 1.8rem; color: #0d6efd; }}
    #searchInput {{ margin-bottom: 15px; }}
  </style>
  <script>
    function filterTable() {{
      let input = document.getElementById("searchInput").value.toLowerCase();
      let rows = document.querySelectorAll("tbody tr");
      rows.forEach(row => {{
        row.style.display = row.textContent.toLowerCase().includes(input) ? "" : "none";
      }});
    }}
  </script>
</head>
<body>
<div class="container my-5">
  <div class="text-center mb-4">
    <h1>Web Scraping Project – ShadowFox Internship</h1>
    <p class="text-muted">Developed by <strong>Aishwarya Varshini</strong></p>
    <p>Data generated on: <code>{timestamp}</code></p>
  </div>

  <div class="card shadow-sm">
    <div class="card-body">
      <input type="text" id="searchInput" onkeyup="filterTable()" 
             class="form-control" placeholder="🔍 Search titles...">

      <table class="table table-striped table-hover mt-3">
        <thead class="table-primary">
          <tr><th>#</th><th>Title</th><th>Link</th></tr>
        </thead>
        <tbody>
"""
    footer = """
        </tbody>
      </table>
    </div>
  </div>
  <p class="text-muted mt-3 text-center">Generated automatically using Python (BeautifulSoup + HTML writer)</p>
</div>
</body>
</html>
"""
    body = []
    for i, (title, href) in enumerate(rows, start=1):
        t = html.escape(title) if title else "&nbsp;"
        if href:
            h = html.escape(href)
            link_html = f'<a href="{h}" target="_blank">{h}</a>'
        else:
            link_html = "&nbsp;"
        body.append(f"<tr><td>{i}</td><td>{t}</td><td>{link_html}</td></tr>")
    return header + "\n".join(body) + footer

def main():
    p = Path(INPUT)
    if not p.exists():
        print(f"⚠️ Input file '{INPUT}' not found. Run your scraper first.")
        return

    rows = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rows.append(parse_line(line))

    html_content = build_html(rows)
    out_path = Path(OUTPUT)
    out_path.write_text(html_content, encoding="utf-8")
    print(f"✅ HTML page generated: {out_path.resolve()}")

    # Automatically open in browser
    webbrowser.open(out_path.resolve().as_uri())

if __name__ == "__main__":
    main()
