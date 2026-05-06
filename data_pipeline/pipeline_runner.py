from extract.fetch_commits import fetch_commits
from extract.fetch_prs import fetch_prs
from extract.fetch_issues import fetch_issues
from extract.fetch_contributors import fetch_contributors
from utils.repo_parser import parse_github_url


if __name__ == "__main__":
    url = input("Enter GitHub Repo URL: ")

    try:
        repo = parse_github_url(url)
    except Exception as e:
        print("Invalid URL:", e)
        exit()

    print(f"\nProcessing repo: {repo}\n")

    commits = fetch_commits(repo)
    prs = fetch_prs(repo)
    issues = fetch_issues(repo)
    contributors = fetch_contributors(repo)

    print("\nSummary:")
    print("Commits:", len(commits))
    print("PRs:", len(prs))
    print("Issues:", len(issues))
    print("Contributors:", len(contributors))