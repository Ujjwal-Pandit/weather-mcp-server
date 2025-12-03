# Git Setup and Push Script
# Run this script to initialize git and prepare for GitHub push

Write-Host "Git Setup for Weather MCP Server" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is available
try {
    $gitVersion = git --version 2>&1
    Write-Host "✓ Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Git not found. Please install Git first:" -ForegroundColor Red
    Write-Host "  winget install Git.Git" -ForegroundColor Yellow
    Write-Host "  Or download from: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

# Check if already a git repo
if (Test-Path .git) {
    Write-Host "✓ Git repository already initialized" -ForegroundColor Green
} else {
    Write-Host "Initializing git repository..." -ForegroundColor Yellow
    git init
    Write-Host "✓ Repository initialized" -ForegroundColor Green
}

Write-Host ""
Write-Host "Adding files to git..." -ForegroundColor Yellow
git add .

Write-Host ""
Write-Host "Current status:" -ForegroundColor Cyan
git status

Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Review the files to be committed (above)" -ForegroundColor White
Write-Host "2. Commit the changes:" -ForegroundColor White
Write-Host "   git commit -m 'Task 1: Weather MCP server implementation'" -ForegroundColor Yellow
Write-Host ""
Write-Host "3. Create a repository on GitHub (if not already created)" -ForegroundColor White
Write-Host "4. Add remote and push:" -ForegroundColor White
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git" -ForegroundColor Yellow
Write-Host "   git branch -M main" -ForegroundColor Yellow
Write-Host "   git push -u origin main" -ForegroundColor Yellow
Write-Host ""

