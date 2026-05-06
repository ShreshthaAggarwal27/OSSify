def parse_github_url(url: str):
    if not url:
        raise ValueError("Empty URL")

    if "github.com" not in url:
        raise ValueError("Not a Github URL")

    parts = url.strip().rstrip("/").split("/")

    if len(parts) < 5:
        raise ValueError("Invalid GitHub URL")

    try:
        owner = parts[-2]
        repo = parts[-1]
    except:
        raise ValueError("Invalid format")

    return f"{owner}/{repo}"