import zipfile, os, re

docx_path = "wordd.docx"  # <-- поменяй

with zipfile.ZipFile(docx_path, 'r') as z:
    z.printdir()
    # сохранить в папку ./unpacked
    z.extractall("unpacked")

# поиск по xml-файлам на предмет флагов / необычных строк
pattern = re.compile(rb'bctf\{.*?\}|FLAG\{.*?\}|flag\s*[:\-].{1,80}', re.IGNORECASE)

for root, _, files in os.walk("unpacked"):
    for fname in files:
        path = os.path.join(root, fname)
        try:
            data = open(path, "rb").read()
        except Exception:
            continue
        if pattern.search(data):
            print("MATCH in", path)
            for m in pattern.finditer(data):
                print("  ->", m.group(0))
        # распечатать небольшие текстовые куски, чтобы увидеть явные ascii
        txt = re.findall(rb'[\x20-\x7E]{6,}', data)  # подряд ascii >=6 символов
        if txt:
            print(path, "contains ascii fragments:", txt[:5])
