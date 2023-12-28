import os
from git import Repo

# 本地仓库路径
local_repo_path = r"C:\Users\JasminL\Desktop\pythonProject"

# 检查是否存在 Git 仓库，如果不存在则初始化
if not os.path.exists(os.path.join(local_repo_path, ".git")):
    Repo.init(local_repo_path)

# 初始化本地仓库
repo = Repo(local_repo_path)

# 远程仓库 URL（使用 SSH）
remote_repo_url = 'git@github.com:MasterL-min/pythongit-learning.git'

# 添加并提交 main.py 文件
repo.index.add(['main.py'])
repo.index.commit("first commit with main.py")

# 创建并切换到 main 分支
repo.head.reference = repo.create_head('main')
repo.head.reset(index=True, working_tree=True)

# 检查远程仓库是否已存在
try:
    origin = repo.remote('origin')
    print("Remote 'origin' already exists.")
except ValueError:
    # 添加远程仓库（使用个人访问令牌）
    origin = repo.create_remote('origin', url=remote_repo_url)
    print("Remote 'origin' created.")

# 推送到远程仓库
push_result = origin.push(refspec='refs/heads/main:refs/heads/main')
print(f"Push result: {push_result}")

