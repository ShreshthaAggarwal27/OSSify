from data_pipeline.extract.github_client import GitHubClient

client = GitHubClient()

def fetch_contributors(repo_name):
    endpoint = f"repos/{repo_name}/contributors"
    contributors = client.get_all_pages(endpoint)
    return contributors