import os, requests
from github import Github

token = os.getenv("GITHUB_TOKEN")
gh    = Github(token)

OUT_DIR = "gdd_md_all"
os.makedirs(OUT_DIR, exist_ok=True)

queries = ['"Game Design Document" extension:md', 'filename:GameDesignDocument.md', 'filename:GDD.md']
seen = set()

for q in queries:
    for item in gh.search_code(q, order="desc"):
        repo = item.repository
        branch = repo.default_branch
        relpath = item.path                # örn. "docs/GDD.md"
        raw_url = f"https://raw.githubusercontent.com/{repo.full_name}/{branch}/{relpath}"
        if raw_url in seen: continue
        seen.add(raw_url)

        # Kaydedeceğimiz klasör: OUT_DIR/<owner_repo>/
        repo_folder = os.path.join(OUT_DIR, repo.full_name.replace("/", "_"))
        os.makedirs(repo_folder, exist_ok=True)

        # Orijinal dizin yapısını da koruyabilirsiniz:
        # local_path = os.path.join(repo_folder, relpath)
        # os.makedirs(os.path.dirname(local_path), exist_ok=True)

        filename = os.path.basename(relpath)
        outfp = os.path.join(repo_folder, filename)

        r = requests.get(raw_url)
        if r.status_code == 200:
            with open(outfp, "wb") as f:
                f.write(r.content)
            print(f"✔ {repo.full_name} → {filename}")
        else:
            print(f"✖ {r.status_code}: {raw_url}")
