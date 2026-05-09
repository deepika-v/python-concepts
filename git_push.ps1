# Interactive git push helper for this repository
#
# This script prompts for the remote URL and branch, then pushes using
# a one-time override of git credential helper so you can choose the
# account credentials at push time without deleting saved credentials.

$remote = Read-Host "Enter git remote name or URL (leave blank for origin)"
if ([string]::IsNullOrWhiteSpace($remote)) {
    $remote = "origin"
}

$branch = Read-Host "Enter branch to push (leave blank for master)"
if ([string]::IsNullOrWhiteSpace($branch)) {
    $branch = "master"
}

Write-Host "Pushing branch '$branch' to '$remote'..."

# Use an empty credential helper for this push so Git will prompt for credentials
# instead of silently reusing stored HTTPS credentials.
git -c credential.helper= push $remote $branch
