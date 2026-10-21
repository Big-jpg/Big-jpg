#!/usr/bin/env python3
"""Create a read-only snapshot of a GitHub account's followers."""
import csv
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USER = os.environ.get("TARGET_USER", "Big-jpg")
TOKEN = os.environ.get("GH_TOKEN", "")
OUT = Path("follower-audit")


def api(path):
    url = "https://api.github.com" + path
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "follower-audit",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN
    request = urllib.request.Request(url, headers=headers)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=25) as response:
                return json.load(response)
        except urllib.error.HTTPError as err:
            if err.code in (429, 500, 502, 503, 504) and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            raise RuntimeError(f"GitHub API request failed: {path} (HTTP {err.code})") from err
    raise RuntimeError(f"GitHub API request failed after retries: {path}")


def followers():
    result = []
    page = 1
    while True:
        segment = api(
            f"/users/{urllib.parse.quote(USER, safe='')}/followers"
            f"?per_page=100&page={page}"
        )
        if not isinstance(segment, list):
            raise RuntimeError("Expected a list from the followers endpoint")
        result.extend(segment)
        if len(segment) < 100:
            return result
        page += 1


def main():
    now = datetime.now(timezone.utc)
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []

    for entry in followers():
        login = entry["login"]
        details = api("/users/" + urllib.parse.quote(login, safe=""))
        created = datetime.fromisoformat(details["created_at"].replace("Z", "+00:00"))
        rows.append({
            "username": login,
            "profile": details["html_url"],
            "created_at_utc": details["created_at"],
            "account_age_days": (now - created).days,
            "public_repos": details.get("public_repos", 0),
            "followers": details.get("followers", 0),
            "following": details.get("following", 0),
            "account_type": details.get("type", "Unknown"),
        })

    rows.sort(key=lambda r: (r["account_age_days"], r["username"].lower()))
    columns = [
        "username", "profile", "created_at_utc", "account_age_days",
        "public_repos", "followers", "following", "account_type",
    ]

    with (OUT / "followers.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

    snapshot = {"captured_at_utc": now.isoformat(), "target_user": USER, "followers": rows}
    (OUT / "followers.json").write_text(
        json.dumps(snapshot, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        f"# Follower audit — {USER}",
        "",
        f"Captured: {now:%Y-%m-%d %H:%M UTC}  ",
        f"Total followers: **{len(rows)}**",
        "",
        "Sorted by account age, newest first. Account age alone does not indicate bot activity.",
        "",
        "| Profile | Created (UTC) | Age (days) | Public repos | Followers | Following |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| [{row['username']}]({row['profile']}) "
            f"| {row['created_at_utc'][:10]} "
            f"| {row['account_age_days']} "
            f"| {row['public_repos']} "
            f"| {row['followers']} "
            f"| {row['following']} |"
        )

    (OUT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Audited {len(rows)} followers for {USER}")


if __name__ == "__main__":
    main()
