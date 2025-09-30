param([string]$Branch = "main")
$ErrorActionPreference = "Stop"

# Đặt working dir về root repo
Set-Location -Path (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location -Path (Resolve-Path "..")

# 1) Có thay đổi không?
$dirty = git status --porcelain
if ([string]::IsNullOrWhiteSpace($dirty)) {
  Write-Host "[auto_push] No changes to commit."
  exit 0
}