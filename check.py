#!/usr/bin/env python3
"""检测所有HTML文件中的CSS引用是否正确"""

import os

ROOT_DIR = r'f:\GithubDaiGou'
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')

# 获取assets文件夹中实际的CSS文件名
actual_css_files = set()
for f in os.listdir(ASSETS_DIR):
    if f.endswith('.css'):
        actual_css_files.add(f)

print("actual css files in assets folder:")
for f in sorted(actual_css_files):
    print(f"  - {f}")

# 检查所有HTML文件
print("\nchecking html files...")
issues = []

for root, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            
            content = None
            for encoding in ['utf-8', 'gbk', 'latin-1']:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            
            if content is None:
                issues.append(f"cannot read: {file_path}")
                continue
            
            # 检查是否引用了不存在的CSS文件
            import re
            css_refs = re.findall(r'href="[^"]*\.css"', content)
            for ref in css_refs:
                # 提取文件名
                filename = ref.split('/')[-1].replace('href="', '').replace('"', '')
                if filename not in actual_css_files:
                    issues.append(f"{file_path}: references non-existent css file '{filename}'")
            
            # 检查是否还有旧的文件名格式
            if '@' in content and '.css' in content:
                issues.append(f"{file_path}: still contains @ in css reference")
            
            if '_astro' in content:
                issues.append(f"{file_path}: still contains _astro reference")

if issues:
    print("\nissues found:")
    for issue in issues:
        print(f"  - {issue}")
else:
    print("\nall css references are correct!")
