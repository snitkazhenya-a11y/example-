import re
def clean_html(input_file, output_file="cleaned.txt"):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    text = re.sub(r"<script.*?>.*?</script>", "", text, flags=re.DOTALL)
    text = re.sub(r"<style.*?>.*?</style>", "", text, flags=re.DOTALL)
    clean_text = re.sub(r"<[^>]+>", "", text)
    lines = clean_text.splitlines()
    lines = [line.strip() for line in lines if line.strip()]
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
input_path = r"D:\Project\draft (1).html"
output_path = r"D:\Project\cleaned.txt"

clean_html(input_path, output_path)