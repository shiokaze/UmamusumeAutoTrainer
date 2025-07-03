#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
import colorama

colorama.init()

RED    = "\033[91m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
GRAY   = "\033[90m"
RESET  = "\033[0m"

def print_error(msg):
    print(f"{RED}{msg}{RESET}")


def print_warn(msg):
    print(f"{YELLOW}{msg}{RESET}")


def print_info(msg):
    print(f"{GREEN}{msg}{RESET}")


def print_ok(msg):
    print(f"{GRAY}{msg}{RESET}")


def run_cmd(cmd):
    return subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True).strip()


def main():
    # 1. 检查 git 是否存在
    if shutil.which("git") is None:
        print_info("[INFO] 没有安装git, 跳过更新检查步骤")
        sys.exit(1)

    # 2. 检查 .git 目录（是否为 Git 仓库）
    if not os.path.isdir(".git"):
        print_info("[INFO] 当前路径不是git仓库, 跳过更新检查步骤")
        sys.exit(1)

    # 3. 获取当前分支并检查是否为 dev
    try:
        current_branch = run_cmd(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    except subprocess.CalledProcessError as e:
        print_error(f"[ERROR] 无法获取当前分支, 错误: {e.output}")
        sys.exit(1)

    if current_branch != "dev":
        print_warn(f"[WARN] 你当前的分支是 {current_branch}, 可能不是最新更新, 建议执行 'git checkout dev' 切换至发布分支")
        sys.exit(1)

    # 4. 拉取远程更新信息
    try:
        subprocess.check_call(["git", "fetch", "origin"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print_warn(f"[WARN] 获取远程仓库信息失败: {e}, 跳过更新检查")
        sys.exit(1)

    # 5. 获取本地和远程的提交哈希
    try:
        local_hash  = run_cmd(["git", "rev-parse", "HEAD"])
        remote_hash = run_cmd(["git", "rev-parse", "origin/dev"])
    except subprocess.CalledProcessError as e:
        print_error(f"[ERROR] 获取commit信息错误: {e.output}, 退出更新检查")
        sys.exit(1)

    # 6. 对比并提示
    if local_hash != remote_hash:
        print_info("\n[INFO] 检查到更新, 请执行 'git pull origin dev' 获取最新版本")
    else:
        print_ok("\n[OK] 当前文件为最新版本")


if __name__ == "__main__":
    main()
