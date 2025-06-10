from jinja2 import Environment, FileSystemLoader
import random, string, os, json

def generate_random_filename(n=12):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n)) + ".html"

env = Environment(loader=FileSystemLoader("src/templates"))

TEMPLATES = {
    "article": "base_article.html.j2",
    "faq": "base_faq.html.j2",
    "list": "base_list.html.j2",
    "flat": "base_flat.html.j2"
}

# 固定コンテンツ（意味を統一）
base_content = {
    "title": "LLMOとは何か",
    "description": "LLMOの定義とその重要性に関する解説",
    "heading": "LLMOとは",
    "section1_title": "定義",
    "section1_body": "LLMOは大規模言語モデルの最適化技術を指します。",
    
}

metadata = {}

for variant, template_file in TEMPLATES.items():
    for i in range(100):  # 各構造100ページ生成
        filename = generate_random_filename()
        template = env.get_template(template_file)
        html = template.render(**base_content)  # またはvariantごとの形式に変換したdict

        with open(f"src/output_pages/{filename}", "w") as f:
            f.write(html)

        metadata[filename] = {"structure": variant}

# 保存
with open("src/metadata.json", "w") as f:
    json.dump(metadata, f, indent=2)