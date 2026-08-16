import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

load_dotenv()

def main():
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        print("Error: FIRECRAWL_API_KEY no encontrada en .env")
        return

    app = FirecrawlApp(api_key=api_key)
    
    # Prueba rápida scrapeando una URL
    response = app.scrape_url("https://example.com")
    print("¡Firecrawl conectado con éxito! 🚀")
    
    # Extraer el contenido en formato markdown
    if hasattr(response, "markdown"):
        print(response.markdown[:100])
    elif isinstance(response, dict):
        print(response.get("markdown", "")[:100])

if __name__ == "__main__":
                        main()