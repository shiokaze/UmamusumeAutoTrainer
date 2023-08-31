$Env:PIP_DISABLE_PIP_VERSION_CHECK = 1
$Env:PIP_NO_CACHE_DIR = 1

function InstallFail {
    Write-Output "install failed"
    Read-Host | Out-Null ;
    Exit
}


function Check {
    param (
        $ErrorInfo
    )
    if (!($?)) {
        Write-Output $ErrorInfo
        InstallFail
    }
}


if (!(Test-Path -Path "venv")) {
    Write-Output "creating venv..."
    python -m venv venv
    Check "Failed to create a virtual environment. Please check whether python is installed and whether the python version is the 64-bit version of python 3.10, or whether the python directory is in the environment variable PATH."
}


.\venv\Scripts\activate
Check "activate venv failed"

pip install pyelftools==0.29 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pdf2docx==0.5.6 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install --upgrade -r requirements.txt -i https://mirror.baidu.com/pypi/simple

Write-Output "install complete"
Read-Host | Out-Null ;
