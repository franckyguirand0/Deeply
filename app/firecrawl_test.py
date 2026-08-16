import os

from dotenv import load_dotenv
from firecrawl import Firecrawl

load_dotenv()

api_key = os.getenv("FIRECRAWL_API_KEY")

if not api_key:
    raise ValueError("FIRECRAWL_API_KEY no encontrada en .env")

app = Firecrawl(api_key=api_key)

url = "https://example.com"

result = app.scrape(
    url,
    formats=["markdown"]
)

print("🔥 Firecrawl conectado correctamente")
print()
print(result.markdown)