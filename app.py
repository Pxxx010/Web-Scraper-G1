from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configuração do navegador
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Headless mais recente
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--disable-webgl")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicializa o driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Acessa o site
driver.get("https://g1.globo.com/")

# Aguarda os elementos carregarem
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".feed-post")))

# Busca as notícias
noticias = driver.find_elements(By.CSS_SELECTOR, ".feed-post")

# Prepara o arquivo para salvar
with open("noticias.txt", "w", encoding="utf-8") as arquivo:
    for i, noticia in enumerate(noticias[:10], start=1):
        try:
            titulo = noticia.find_element(By.CSS_SELECTOR, "a.feed-post-link").text
            link = noticia.find_element(By.CSS_SELECTOR, "a.feed-post-link").get_attribute("href")
            categoria = noticia.find_element(By.CSS_SELECTOR, ".feed-post-header-chapeu").text

            # Escreve no arquivo
            arquivo.write(f"Notícia {i}\n")
            arquivo.write(f"Título   : {titulo}\n")
            arquivo.write(f"Link     : {link}\n")
            arquivo.write(f"Categoria: {categoria}\n")
            arquivo.write("-" * 50 + "\n")

        except Exception as e:
            print(f"Erro na notícia {i}: {e}")

# Fecha o navegador
driver.quit()

print("Notícias salvas em 'noticias.txt' com sucesso!")
