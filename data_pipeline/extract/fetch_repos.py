from data_pipeline.extract.github_client import GitHubClient

client = GitHubClient()

def fetch_repo(repo_name):
    data = client.get(f"repos/{repo_name}")
    return data
