from data_pipeline.extract.github_client import GitHubClient

client = GitHubClient()

def fetch_prs(repo_name):
    endpoint = f"repos/{repo_name}/pulls"

    params = {"state": "all"}

    prs = client.get_all_pages(endpoint, params={"state": "all"}, max_pages=3)
    return prs