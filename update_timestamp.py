import datetime
import re
print("Updating README.md with the current timestamp...")

# 读取 README.md
with open("README.md", "r") as f:
    content = f.read()

# 生成当前时间（支持时区）
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC%z")

# 替换占位符
new_content = re.sub(
    r"<!-- AUTO_UPDATE_TIME -->", 
    f"`{now}`", 
    content
)

# 写回文件
with open("README.md", "w") as f:
    f.write(new_content)

print(f"README.md has been updated with the current timestamp: {now}")
