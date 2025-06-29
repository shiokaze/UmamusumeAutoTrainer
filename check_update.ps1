if (-not (Test-Path -Path ".git" -PathType Container)) {
    # 不是从 git clone 下来的仓库，直接退出
    exit 1
}

$currentBranch = (git rev-parse --abbrev-ref HEAD).Trim()
if ($currentBranch -ne "dev") {
    Write-Host "[WARN] Your current branch is $currentBranch, which might not be the latest release. Please run 'git checkout dev' to switch to release branch" -ForegroundColor Yellow
    exit 1
}

try {
    git fetch origin | Out-Null
} catch {
    Write-Host "[WARN] Error pulling from origin：$_, upgrade terminated" -ForegroundColor Yellow
    exit 1
}

$localHash  = (git rev-parse HEAD).Trim()
$remoteHash = (git rev-parse origin/dev).Trim()

if ($localHash -ne $remoteHash) {
    Write-Host "`n[INFO] Update detected, please run 'git pull' to get latest release." -ForegroundColor Green
}
