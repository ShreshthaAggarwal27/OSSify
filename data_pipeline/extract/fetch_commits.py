from data_pipeline.extract.github_client import GitHubClient

client = GitHubClient()

def fetch_commits(repo_name):
    endpoint = f"repos/{repo_name}/commits"
    commits = client.get(endpoint, params={"per_page": 50})
    return commits