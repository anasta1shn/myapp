from bs4 import BeautifulSoup
import os

def test_index_html_exists():
    assert os.path.exists("index.html"), "Файл index.html не найден"

def test_button_and_background():
    with open("index.html", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    assert soup.find("button"), "Кнопка <button> не найдена"

    has_background = any("background-color" in style.text for style in soup.find_all("style"))
    assert has_background, "background-color не найден в <style>"
