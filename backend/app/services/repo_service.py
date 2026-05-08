from data_pipeline.extract.fetch_commits import fetch_commits
from data_pipeline.extract.fetch_prs import fetch_prs
from data_pipeline.extract.fetch_issues import fetch_issues
from data_pipeline.extract.fetch_contributors import fetch_contributors

from data_pipeline.utils.repo_parser import parse_github_url

from data_pipeline.load.load_postgres import (
    save_repository,
    save_commits,
    save_contributors,
    save_issues,
    save_prs
)

def process_repository(repo_url: str):
    try:
        print("\n========== STARTING REPO PROCESS ==========")

        repo_name = parse_github_url(repo_url)
        print(f"Parsed Repo: {repo_name}")

        print("\nFetching contributors...")
        contributors = fetch_contributors(repo_name)
        contributors_count = len(contributors) if contributors else 0
        print(f"Fetched contributors: {contributors_count}")

        print("\nFetching commits...")
        commits = fetch_commits(repo_name)
        commits_count = len(commits) if commits else 0
        print(f"Fetched commits: {commits_count}")

        print("\nFetching pull requests...")
        prs = fetch_prs(repo_name)
        prs_count = len(prs) if prs else 0
        print(f"Fetched PRs: {prs_count}")

        print("\nFetching issues...")
        issues = fetch_issues(repo_name)
        issues_count = len(issues) if issues else 0
        print(f"Fetched issues: {issues_count}")

        print("\nSaving repository...")
        repo_id = save_repository(repo_name, repo_url)
        print(f"Repository saved with ID: {repo_id}")

        print("\nSaving contributors...")
        save_contributors(contributors)
        print("Contributors saved successfully.")

        print("\nSaving commits...")
        save_commits(commits, repo_id)
        print("Commits saved successfully.")

        print("\nSaving pull requests...")
        save_prs(prs, repo_id)
        print("Pull requests saved successfully.")

        print("\nSaving issues...")
        save_issues(issues, repo_id)
        print("Issues saved successfully.")

        print("\n========== PROCESS COMPLETE ==========\n")

        return {
            "status": "success",
            "repository": repo_name,
            "contributors": contributors_count,
            "commits": commits_count,
            "pull_requests": prs_count,
            "issues": issues_count
        }

    except Exception as e:

        print("\n========== PROCESS FAILED ==========")
        print("ERROR IN PROCESS_REPOSITORY:")
        print(str(e))
        print("====================================\n")

        return {
            "status": "failed",
            "error": str(e)
        }