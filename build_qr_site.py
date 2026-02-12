# build_qr_site.py
import argparse
import json
import shutil
from pathlib import Path
import re
import qrcode  # pip install qrcode pillow

# --- Import your original script to source all messages (keeps content in sync) ---
# The builder calls your methods from alvida.py so the webpage text always matches your script. [1]
import alvida

# Mirror your colleagues list from alvida.py's __main__ block. [1]
COLLEAGUES = [
    ['Shiozaki san', 'Shrikanth san', 'Furuya san'],
    ['Rajeev san'], ['Jeeth'], ['Sumitra'],
    ['Pankaj', 'Gouse', 'Neel', 'Karthik', 'Chaithanya', 'Sudeep'],
    ['Deepali', 'Shreyanshi', 'Jyoti', 'Akshata',
        'Shiv', 'Ajay', 'Sandhya', 'Amar'],
    ['Varun', 'Prajwal', 'Vandita', 'Mahesh', 'Sameer', 'Harsha'],
]

# ---------------------------- Pull content from alvida.py ----------------------------


def build_messages():
    """Collect farewell, per-person goodbyes, closing, and default fallback
    from your alvida.py so the webpage text always matches your Python script. [1]
    """
    farewell = alvida.Alvida.say_farewell()
    closing = alvida.Alvida.say_closing_comments()
    # Per-person messages via your class to keep content identical. [1]
    per_person = {}
    for group in COLLEAGUES:
        for name in group:
            per_person[name] = alvida.Alvida(name).say_goodbye()
    # Default (else-branch) fallback from your code. [1]
    default_msg = alvida.Alvida("Colleague").say_goodbye()
    return farewell, per_person, closing, default_msg

# ---------------------------- Token index for client-side matcher ----------------------------


def _normalize(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r'[\-._]+', ' ', s)  # separators → spaces
    s = re.sub(r'[^a-z0-9\s]', '', s)  # keep only letters/numbers/spaces
    s = re.sub(r'\s+', ' ', s)  # collapse spaces
    return s


def _name_tokens(name: str):
    return [t for t in _normalize(name).split() if t]


def build_tokens_index(per_person: dict, min_len=4):
    """token -> canonical name mapping for client-side matcher."""
    idx = {}
    for name in per_person.keys():
        for t in _name_tokens(name):
            if len(t) >= min_len:
                idx[t] = name
    return idx

# ---------------------------- Optional content translations ----------------------------


def load_translations(path: str | None) -> dict:
    """
    Load optional translations JSON.
    Expected structure (example):
    {
      "ui": {
        "en": {"title": "Koushik's Farewell — Pythonic Theme",
               "placeholder": "Please enter your Name/Email to see your personalized Farewell Message",
               "direct_link": "Direct link"},
        "hi": {...},
        "ja": {...}
      },
      "content": {
        "hi": {
          "farewell": "...", "closing": "...", "default": "...",
          "messages": { "Shiv": "...", "Rajeev san": "...", "..." : "..." }
        },
        "ja": { ... }
      }
    }
    - All keys are optional; absent entries will fall back to English.
    """
    if not path:
        return {}
    p = Path(path)
    if not p.exists():
        print(
            f"[!] Translations file not found at {path}. Continuing without it.")
        return {}
    try:
        with p.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except Exception as e:
        print(f"[!] Failed to parse translations JSON: {e}")
        return {}

# ---------------------------- HTML renderer ----------------------------


def render_html(final_url: str,
                farewell: str,
                per_person: dict,
                closing: str,
                tokens_index: dict,
                default_msg: str,
                translations: dict,
                out_path: Path,
                logo_img_tag: str):
    """
    Write a Yokogawa-themed, Python-console-styled single HTML file, with:
    - language selector (UI i18n + optional content translations)
    - dark/light mode toggle
    - responsive wrapping in consoles
    - NOTE: Farewell/Closing remain hidden until user provides Name/Email
    """
    # Prepare embedded JSON
    farewell_json = json.dumps(farewell, ensure_ascii=False)
    closing_json = json.dumps(closing, ensure_ascii=False)
    per_person_json = json.dumps(per_person, ensure_ascii=False)
    tokens_json = json.dumps(tokens_index, ensure_ascii=False)
    default_json = json.dumps(default_msg, ensure_ascii=False)
    translations_json = json.dumps(translations, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Farewell — Parachi Sai Koushik</title>
<style>
 :root {{
  /* --- Dark (default) Yokogawa palette --- */
  --brand-yellow: #FFDD00; /* Signature diamond */
  --brand-blue:  #004B8D;  /* Deep Yokogawa blue */
  --bg:    #062247; /* Dark blue background */
  --panel: #0C2F5A; /* Console panel */
  --border:#17457B; /* Subtle border */
  --fg:    #EAF2FF; /* Foreground text */
  --muted: #AFC2E3; /* Dimmed text */
  --accent: var(--brand-yellow);
  --prompt: var(--brand-yellow);
 }}
 body[data-theme="light"] {{
  --bg:    #F5F9FF;
  --panel: #FFFFFF;
  --border:#C9D8EE;
  --fg:    #0B1A2F;
  --muted: #5A6C86;
  --prompt:#C9A600; /* softened yellow in light mode */
 }}
 * {{ box-sizing: border-box; }}
 html, body {{ height: 100%; }}
 body {{
  background: var(--bg);
  color: var(--fg);
  font-family: Consolas, Menlo, "Courier New", monospace;
  margin: 0; padding: 24px 18px;
  transition: background-color .2s ease, color .2s ease;
 }}
 .wrap {{ max-width: 980px; margin: 0 auto; }}
 .header {{
  display: grid;
  grid-template-columns: auto 1fr auto auto;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
 }}
 .logo {{ height: 44px; width: auto; display: block; }}
 .title {{ font-size: 22px; margin: 0; letter-spacing: .3px; font-weight: 700; }}
 .controls {{ display: flex; gap: 10px; align-items: center; }}
 .select, .toggle {{
  border: 1px solid var(--border);
  background: var(--panel);
  color: var(--fg);
  padding: 8px 10px;
  border-radius: 8px;
  font-family: inherit;
  font-size: 14px;
  cursor: pointer;
 }}
 .toggle:hover, .select:hover {{ filter: brightness(1.05); }}
 .underline {{
  height: 3px; width: 210px; background:
  linear-gradient(90deg, var(--brand-yellow), var(--brand-blue));
  border-radius: 999px; margin: 10px 0 18px;
 }}
 .inputWrap {{ margin: 10px 0 14px; }}
 input[type="text"] {{
  width: 100%;
  padding: 12px 14px;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: #3A3F47; /* grey input background */
  color: #F3F4F6;      /* light grey text */
  font-family: inherit;
  font-size: 15px;
  outline: none;
  box-shadow: inset 0 0 0 1px transparent;
  transition: background-color .2s ease, color .2s ease;
 }}
 body[data-theme="light"] input[type="text"] {{
  background: #E6E8EB; color: #0B1A2F; /* lighter grey in light mode */
 }}
 input[type="text"]::placeholder {{ color: #D1D5DB; opacity: 0.95; }}
 body[data-theme="light"] input[type="text"]::placeholder {{ color: #6B7280; }}
 input[type="text"]:focus {{ box-shadow: inset 0 0 0 1px var(--accent); }}

 .terminal {{
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 18px;
  font-size: 15px;
  position: relative;
  overflow: hidden;
  transition: background-color .2s ease, color .2s ease, border-color .2s ease;
 }}
 .terminal pre {{
  margin: 0;
  white-space: pre-wrap; /* wrap long lines */
  overflow-wrap: anywhere; /* break long words/URLs */
  word-break: break-word; /* fallback for older engines */
  hyphens: auto; /* optional hyphenation */
  line-height: 1.55;
  max-width: 100%;
 }}
 .prompt {{ color: var(--prompt); font-weight: 700; }}
 .prompt::after {{
  content: "▌"; margin-left: 3px; color: var(--accent);
  animation: blink 1.05s step-end infinite;
 }}
 @keyframes blink {{ 50% {{ opacity: 0; }} }}
 @media (prefers-reduced-motion: reduce) {{
  .prompt::after, .typing::after {{ animation: none; }}
 }}
 .typing::after {{
  content: '▌'; color: var(--accent);
  margin-left: 2px; animation: blink 1.05s step-end infinite;
 }}
 .footer {{ margin-top: 20px; color: var(--muted); font-size: 14px; }}
 a {{ color: var(--accent); text-decoration: none; }}
 a:hover {{ text-decoration: underline; }}

 @media (max-width: 540px) {{
  .header {{
   grid-template-columns: auto 1fr auto;
   grid-auto-rows: auto;
   row-gap: 8px;
  }}
  .controls {{ grid-column: 1 / -1; justify-content: flex-end; }}
  .logo {{ height: 38px; }}
  .title {{ font-size: 20px; }}
 }}
</style>
</head>
<body>
 <div class="wrap">
  <!-- Header with logo + title + controls -->
  <div class="header">
   {logo_img_tag}
   <h1 id="title" class="title">Koushik's Farewell — Pythonic Theme</h1>
   <div class="controls">
    <!-- Language selector -->
    <select id="lang" class="select" aria-label="Language">
     <option value="en">English</option>
     <option value="hi">हिन्दी</option>
     <option value="ja">日本語</option>
    </select>
    <!-- Dark/Light toggle -->
    <button id="themeToggle" class="toggle" type="button" aria-label="Toggle theme">🌙</button>
   </div>
  </div>
  <div class="underline"></div>

  <!-- INPUT (before the first console) -->
  <div class="inputWrap">
   <input id="who" type="text"
          placeholder="Please enter your Name/Email to see Farewell Message" />
  </div>

  <!-- FIRST CONSOLE (hidden until first valid input) -->
  <div class="terminal" id="farewellBox" style="margin-top:8px; display:none;">
   <span class="prompt">>></span> from alvida import Alvida<br>\n
   <span class="prompt">>></span> Alvida.say_farewell()
   <pre id="farewell" class="typing"></pre>
  </div>

  <!-- RESULT CONSOLE -->
  <div class="terminal" id="resultBox" style="margin-top:16px; display:none;">
   <pre id="result" class="typing"></pre>
  </div>

  <!-- CLOSING CONSOLE (hidden until first valid input) -->
  <div class="terminal" id="closingBox" style="margin-top:16px; display:none;">
   <span class="prompt">>></span> Alvida.say_closing_comments()<br>\n
   <pre id="closing" class="typing"></pre>
  </div>

  <div class="footer">
   <br/><span id="directLinkLabel">Direct link</span>: <a href="{final_url}">{final_url}</a>
  </div>
 </div>

<script>
 // ---------------------------- Data injected from Python (sourced from alvida.py) ----------------------------
 const farewellTextEN = {farewell_json};
 const closingTextEN  = {closing_json};
 const messagesEN     = {per_person_json};
 const tokenIndex     = {tokens_json};      // token->canonical name
 const defaultMsgEN   = {default_json};     // from Alvida("Colleague").say_goodbye()
 const TRANSLATIONS   = {translations_json};
 const MIN = 4;

 // ---------------------------- UI strings by language (fallbacks) ----------------------------
 const UI_FALLBACK = {{
  en: {{
    title: "Koushik's Farewell — Pythonic Theme",
    placeholder: "Please enter your Name/Email to see Farewell Message",
    direct_link: "Direct link"
  }},
  hi: {{
    title: "फेयरवेल — पायथन कंसोल",
    placeholder: "फेयरवेल संदेश देखने के लिए अपना नाम/ईमेल दर्ज करें",
    direct_link: "सीधा लिंक"
  }},
  ja: {{
    title: "送別 — Python コンソール",
    placeholder: "送別メッセージを見るには氏名/メールを入力してください",
    direct_link: "直接リンク"
  }}
 }};
 function uiStrings(lang) {{
  const source = (TRANSLATIONS.ui && TRANSLATIONS.ui[lang]) || UI_FALLBACK[lang] || UI_FALLBACK.en;
  return {{
    title:       source.title       || UI_FALLBACK.en.title,
    placeholder: source.placeholder || UI_FALLBACK.en.placeholder,
    direct_link: source.direct_link || UI_FALLBACK.en.direct_link
  }};
 }}

 // ---------------------------- Content accessors per language ----------------------------
 function contentFor(lang) {{
  const pack = (TRANSLATIONS.content && TRANSLATIONS.content[lang]) || null;
  return {{
    farewell:  pack?.farewell  ?? farewellTextEN,
    closing:   pack?.closing   ?? closingTextEN,
    defaultMsg:pack?.default   ?? defaultMsgEN,
    messages:  pack?.messages  ?? {{}},
  }};
 }}

 // ---------------------------- Normalization (mirrors Python) ----------------------------
 function normalize(s) {{
  s = s.toLowerCase().trim();
  s = s.replace(/[\\-._]+/g, ' ');
  s = s.replace(/[^a-z0-9\\s]/g, '');
  s = s.replace(/\\s+/g, ' ');
  return s;
 }}
 function tokensFrom(input) {{
  const local = input.split('@')[0]; // if email, use local part
  const norm  = normalize(local);
  return norm ? norm.split(' ').filter(Boolean) : [];
 }}
 function findName(userInput) {{
  const toks = tokensFrom(userInput);
  if (!toks.length) return null;
  // 1) exact token hit
  for (const t of toks) {{
    if (tokenIndex[t]) return tokenIndex[t];
  }}
  // 2) substring either direction, min length 4
  for (const t of toks) {{
    if (t.length < MIN) continue;
    for (const key in tokenIndex) {{
      if (key.length < MIN) continue;
      if (key.includes(t) || t.includes(key)) return tokenIndex[key];
    }}
  }}
  return null;
 }}

 // ---------------------------- Typing animation helpers ----------------------------
 function typeInto(el, text, speed=12, cb=null) {{
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced) {{ el.textContent = text; el.classList.remove('typing'); if (cb) cb(); return; }}
  el.textContent = '';
  let i = 0;
  (function tick() {{
    if (i < text.length) {{
      el.textContent += text[i++];
      setTimeout(tick, speed);
    }} else {{
      el.classList.remove('typing');
      if (cb) cb();
    }}
  }})();
 }}

 // ---------------------------- Theme toggle (dark/light) ----------------------------
 const themeToggleBtn = document.getElementById('themeToggle');
 function applyTheme(theme) {{
  if (theme === 'light') {{
    document.body.setAttribute('data-theme', 'light');
    themeToggleBtn.textContent = '☀️';
  }} else if (theme === 'dark') {{
    document.body.removeAttribute('data-theme');
    themeToggleBtn.textContent = '🌙';
  }} else {{
    if (window.matchMedia('(prefers-color-scheme: light)').matches) {{
      document.body.setAttribute('data-theme', 'light');
      themeToggleBtn.textContent = '☀️';
    }} else {{
      document.body.removeAttribute('data-theme');
      themeToggleBtn.textContent = '🌙';
    }}
  }}
 }}
 function initTheme() {{
  const saved = localStorage.getItem('theme') || 'auto';
  applyTheme(saved);
  themeToggleBtn.addEventListener('click', () => {{
    const current = localStorage.getItem('theme') || 'auto';
    const next = current === 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', next);
    applyTheme(next);
  }});
  window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', () => {{
    if ((localStorage.getItem('theme') || 'auto') === 'auto') applyTheme('auto');
  }});
 }}

 // ---------------------------- Language selector ----------------------------
 const langSelect = document.getElementById('lang');
 const titleEl = document.getElementById('title');
 const inputEl = document.getElementById('who');
 const directLinkLabel = document.getElementById('directLinkLabel');
 const farewellBox = document.getElementById('farewellBox');
 const closingBox  = document.getElementById('closingBox');
 let hasActivated = false; // becomes true after first valid input

 function applyLanguage(lang) {{
  const ui = uiStrings(lang);
  titleEl.textContent = ui.title;
  inputEl.setAttribute('placeholder', ui.placeholder);
  directLinkLabel.textContent = ui.direct_link;

  // Only render farewell/closing AFTER the first valid user input.
  if (hasActivated) {{
    const pack = contentFor(lang);
    const farewellEl = document.getElementById('farewell');
    const closingEl  = document.getElementById('closing');
    farewellEl.classList.add('typing');
    closingEl.classList.add('typing');
    typeInto(farewellEl, pack.farewell, 10, () => {{
      typeInto(closingEl, pack.closing, 10);
    }});
  }}
 }}

 function initLanguage() {{
  const saved = localStorage.getItem('lang');
  let lang = saved || (navigator.language || 'en').slice(0,2).toLowerCase();
  if (!['en','hi','ja'].includes(lang)) lang = 'en';
  langSelect.value = lang;
  applyLanguage(lang);
  langSelect.addEventListener('change', () => {{
    const chosen = langSelect.value;
    localStorage.setItem('lang', chosen);
    applyLanguage(chosen);
  }});
 }}

 // ---------------------------- Result console behavior ----------------------------
 const resultBox = document.getElementById('resultBox');
 const resultEl  = document.getElementById('result');

 function showResult(text) {{
  resultBox.style.display = 'block';
  resultEl.classList.add('typing');
  typeInto(resultEl, text, 12);
 }}

 function showMessageForInput(rawInput) {{
  // Do not show ANY message when input is empty/whitespace.
  if (!rawInput || !rawInput.trim()) {{
    resultBox.style.display = 'none';
    return;
  }}

  const lang = langSelect.value || 'en';
  const pack = contentFor(lang);
  const name = findName(rawInput);

  // First time with valid input → reveal farewell & closing consoles.
  if (!hasActivated) {{
    hasActivated = true;
    farewellBox.style.display = 'block';
    closingBox.style.display  = 'block';
    const farewellEl = document.getElementById('farewell');
    const closingEl  = document.getElementById('closing');
    farewellEl.classList.add('typing');
    closingEl.classList.add('typing');
    typeInto(farewellEl, pack.farewell, 10, () => {{
      typeInto(closingEl, pack.closing, 10);
    }});
  }}

  if (name) {{
    const translated = pack.messages[name];
    const base = translated ?? messagesEN[name] ?? pack.defaultMsg ?? defaultMsgEN;
    const header = `>>> Alvida('{{name}}').say_goodbye()\\n\\n`.replace('{{name}}', name);
    showResult(header + base);
  }} else {{
    // No match despite non-empty input → show default.
    showResult(pack.defaultMsg ?? defaultMsgEN);
  }}
 }}

 // Handle Enter on input
 inputEl.addEventListener('keydown', (e) => {{
  if (e.key === 'Enter') {{
    showMessageForInput(inputEl.value);
  }}
 }});

 // Deep-link: ?q=...
 const urlParams = new URLSearchParams(window.location.search);
 const q = urlParams.get('q');

 function boot() {{
  initTheme();
  initLanguage();
  if (q && q.trim()) {{
    inputEl.value = q;
    showMessageForInput(q);
  }}
 }}
 boot();
</script>
</body>
</html>
"""
    out_path.write_text(html, encoding="utf-8")

# ---------------------------- QR builder ----------------------------


def make_qr(final_url: str, png_path: Path):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(final_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(png_path)

# ---------------------------- Main (CLI) ----------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Build Yokogawa-themed Farewell site + QR (uses alvida.py)")
    parser.add_argument("--url", required=True,
                        help="Public URL where index.html will be hosted (e.g., GitHub Pages link).")
    parser.add_argument("--out", default="site",
                        help="Output folder (default: site)")
    parser.add_argument("--logo", default="Yokogawa_logo.png",
                        help="Path to the logo image to place at top-left.")
    parser.add_argument("--translations", default=None,
                        help="Optional JSON with UI/content translations.")
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Gather English baseline content from your alvida.py (keeps page in sync with your script). [1]
    farewell, per_person, closing, default_msg = build_messages()
    tokens_index = build_tokens_index(per_person)

    # Load optional translations
    translations = load_translations(args.translations)

    # Copy logo into site and reference it
    logo_src = Path(args.logo)
    logo_dest = out_dir / "logo.png"
    if logo_src.exists():
        shutil.copyfile(logo_src, logo_dest)
        logo_img_tag = '<img src="logo.png" class="logo" alt="Yokogawa logo" />'
    else:
        print(f"[!] Logo not found at {logo_src}. Proceeding without it.")
        logo_img_tag = ""

    # Write HTML
    html_path = out_dir / "index.html"
    render_html(
        final_url=args.url,
        farewell=farewell,
        per_person=per_person,
        closing=closing,
        tokens_index=tokens_index,
        default_msg=default_msg,
        translations=translations,
        out_path=html_path,
        logo_img_tag=logo_img_tag
    )

    # Build QR
    qr_path = out_dir / "farewell_qr.png"
    make_qr(args.url, qr_path)

    print(f"[+] Wrote {html_path}")
    print(f"[+] Wrote {qr_path}")
    if logo_dest.exists():
        print(f"[+] Copied logo to {logo_dest}")
    print("[i] Upload the folder to a static host and paste the QR into your Outlook email.")


if __name__ == "__main__":
    main()
