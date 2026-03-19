import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import csv
import json
import time

BASE_URL = "https://suayed.facmed.unam.mx/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; SitemapResearchBot/1.0; +https://example.com)"
}

session = requests.Session()
session.headers.update(HEADERS)


def get_soup(url: str) -> BeautifulSoup | None:
    try:
        r = session.get(url, timeout=20)
        r.raise_for_status()
        return BeautifulSoup(r.text, "html.parser")
    except Exception as e:
        print(f"Error en {url}: {e}")
        return None


def clean_text(text: str) -> str:
    return " ".join(text.split()).strip()


def same_domain(url: str, base: str) -> bool:
    return urlparse(url).netloc == urlparse(base).netloc


def extract_main_nav(home_url: str):
    soup = get_soup(home_url)
    if not soup:
        return []

    items = []
    seen = set()

    # Busca enlaces de navegación con un criterio flexible
    for a in soup.select("a[href]"):
        href = a.get("href", "").strip()
        label = clean_text(a.get_text(" ", strip=True))

        if not href or not label:
            continue

        full_url = urljoin(home_url, href)

        if not same_domain(full_url, home_url):
            continue

        # Filtrar cosas irrelevantes
        if label.lower() in {"image", "facebook", "twitter", "instagram", "visit us"}:
            continue

        # Mantener solo rutas útiles del sitio
        parsed = urlparse(full_url)
        if parsed.path in {"/", "/index.php/", ""}:
            key = ("Inicio", BASE_URL)
            if key not in seen:
                items.append({"title": "Inicio", "url": BASE_URL})
                seen.add(key)
            continue

        if "/index.php/" in full_url:
            key = (label, full_url)
            if key not in seen:
                items.append({"title": label, "url": full_url})
                seen.add(key)

    return items


def extract_intro_content(url: str):
    soup = get_soup(url)
    if not soup:
        return {"page_title": "", "summary": ""}

    # Título HTML
    page_title = ""
    if soup.title and soup.title.string:
        page_title = clean_text(soup.title.string)

    # Buscar encabezado principal visible
    h1 = soup.find(["h1", "h2", "h3"])
    visible_title = clean_text(h1.get_text(" ", strip=True)) if h1 else ""

    # Tomar algunos párrafos o bloques introductorios
    texts = []
    for el in soup.find_all(["p", "h2", "h3", "h4", "li"], limit=60):
        txt = clean_text(el.get_text(" ", strip=True))
        if len(txt) >= 40:
            texts.append(txt)

    summary = " ".join(texts[:4])[:900]

    return {
        "page_title": page_title,
        "visible_title": visible_title,
        "summary": summary,
    }


def build_sitemap_dataset():
    nav_items = extract_main_nav(BASE_URL)

    # Deduplicación básica y priorización manual opcional
    wanted = []
    seen_urls = set()
    for item in nav_items:
        if item["url"] not in seen_urls:
            wanted.append(item)
            seen_urls.add(item["url"])

    rows = []
    for item in wanted:
        print(f"Procesando: {item['title']} -> {item['url']}")
        content = extract_intro_content(item["url"])
        rows.append({
            "nav_title": item["title"],
            "url": item["url"],
            "page_title": content.get("page_title", ""),
            "visible_title": content.get("visible_title", ""),
            "summary": content.get("summary", ""),
        })
        time.sleep(0.6)

    return rows


def save_csv(rows, filename="suayed_sitemap_base.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["nav_title", "url", "page_title", "visible_title", "summary"]
        )
        writer.writeheader()
        writer.writerows(rows)


def save_json(rows, filename="suayed_sitemap_base.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    data = build_sitemap_dataset()
    save_csv(data)
    save_json(data)
    print(f"\nListo. Se guardaron {len(data)} registros.")
