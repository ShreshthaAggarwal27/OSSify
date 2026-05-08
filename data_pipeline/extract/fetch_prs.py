from data_pipeline.extract.github_client import GitHubClient

client = GitHubClient()

def fetch_prs(repo_name):
    endpoint = f"repos/{repo_name}/pulls"

    params = {"state": "all"}

    prs = client.get(endpoint, params={
            "state": "all",
            "per_page": 10
    })
    return prs