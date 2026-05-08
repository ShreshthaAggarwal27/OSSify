from data_pipeline.extract.github_client import GitHubClient

client = GitHubClient()

def fetch_issues(repo_name):
    endpoint = f"repos/{repo_name}/issues"

    params = {"state": "all"}

    issues = client.get(endpoint, params={
        "state": "all",
        "per_page": 10
    })
    issues = [issue for issue in issues if "pull_request" not in issue]

    return issues