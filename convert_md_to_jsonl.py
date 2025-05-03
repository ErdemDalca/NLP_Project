# convert_md_to_jsonl.py
import os, json

INPUT_DIR  = "gdd_md_all"
OUTPUT_FILE = "gdd_input.jsonl"

count = 0
with open(OUTPUT_FILE, "w", encoding="utf-8") as fout:
    for repo_folder in os.listdir(INPUT_DIR):
        repo_path = os.path.join(INPUT_DIR, repo_folder)
        if not os.path.isdir(repo_path):
            continue
        for file in os.listdir(repo_path):
            if file.lower().endswith(".md"):
                file_path = os.path.join(repo_path, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    raw_text = f.read()
                record = {
                    "id": f"{repo_folder}_{os.path.splitext(file)[0]}",
                    "source": file_path,
                    "date": None,
                    "url": None,
                    "raw_text": raw_text
                }
                fout.write(json.dumps(record, ensure_ascii=False) + "\n")
                count += 1

print(f"✅ Generated {count} records into {OUTPUT_FILE}")
