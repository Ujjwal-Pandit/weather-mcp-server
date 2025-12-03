# PowerShell script to set up Claude Desktop configuration
# Run this script to configure Claude Desktop to use the weather MCP server

$projectPath = (Get-Location).Path
$claudeConfigPath = "$env:AppData\Claude\claude_desktop_config.json"
$configDir = Split-Path $claudeConfigPath

Write-Host "Setting up Claude Desktop configuration..." -ForegroundColor Cyan
Write-Host "Project path: $projectPath" -ForegroundColor Gray

# Create Claude config directory if it doesn't exist
if (-not (Test-Path $configDir)) {
    New-Item -ItemType Directory -Path $configDir -Force | Out-Null
    Write-Host "✓ Created Claude config directory" -ForegroundColor Green
}

# Create or update config
$config = @{
    mcpServers = @{
        weather = @{
            command = "uv"
            args = @(
                "--directory",
                $projectPath,
                "run",
                "weather.py"
            )
        }
    }
}

# If config exists, merge with existing
if (Test-Path $claudeConfigPath) {
    Write-Host "✓ Found existing Claude Desktop config, merging..." -ForegroundColor Yellow
    try {
        $existing = Get-Content $claudeConfigPath -Raw | ConvertFrom-Json
        if ($existing.mcpServers) {
            if ($existing.mcpServers.weather) {
                Write-Host "⚠ Weather server already configured. Updating..." -ForegroundColor Yellow
                $existing.mcpServers.weather = $config.mcpServers.weather
            } else {
                $existing.mcpServers | Add-Member -MemberType NoteProperty -Name "weather" -Value $config.mcpServers.weather -Force
            }
            $config = $existing
        } else {
            $existing | Add-Member -MemberType NoteProperty -Name "mcpServers" -Value $config.mcpServers -Force
            $config = $existing
        }
    } catch {
        Write-Host "⚠ Error reading existing config, creating new one..." -ForegroundColor Yellow
    }
}

# Write config
$jsonConfig = $config | ConvertTo-Json -Depth 10
Set-Content -Path $claudeConfigPath -Value $jsonConfig

Write-Host ""
Write-Host "✓ Claude Desktop configuration created/updated!" -ForegroundColor Green
Write-Host "  Location: $claudeConfigPath" -ForegroundColor Gray
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Fully quit Claude Desktop (right-click system tray icon → Quit)" -ForegroundColor White
Write-Host "2. Restart Claude Desktop" -ForegroundColor White
Write-Host "3. Look for the 'Search and tools' icon in Claude Desktop" -ForegroundColor White
Write-Host "4. Test by asking: 'What are the weather alerts in California?'" -ForegroundColor White
Write-Host ""

