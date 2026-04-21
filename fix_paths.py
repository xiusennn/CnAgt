#!/usr/bin/env python3
"""修复GitHub Pages路径问题 - 使用带仓库名的绝对路径"""

import os

ROOT_DIR = r'f:\GithubDaiGou'
REPO_NAME = 'CnAgt'

def fix_html_file(file_path):
    """修复单个HTML文件的路径"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 将所有相对路径和绝对路径统一替换为带仓库名的路径
    replacements = [
        ('href="./_astro/', f'href="/{REPO_NAME}/_astro/'),
        ('src="./_astro/', f'src="/{REPO_NAME}/_astro/'),
        ('href="/_astro/', f'href="/{REPO_NAME}/_astro/'),
        ('src="/_astro/', f'src="/{REPO_NAME}/_astro/'),
        ('href="./favicon', f'href="/{REPO_NAME}/favicon'),
        ('href="/favicon', f'href="/{REPO_NAME}/favicon'),
        ('src="./favicon', f'src="/{REPO_NAME}/favicon'),
        ('src="/favicon', f'src="/{REPO_NAME}/favicon'),
        ('href="./og-image', f'href="/{REPO_NAME}/og-image'),
        ('href="/og-image', f'href="/{REPO_NAME}/og-image'),
        ('content="./og-image', f'content="/{REPO_NAME}/og-image'),
        ('content="/og-image', f'content="/{REPO_NAME}/og-image'),
        ('href="./blog/', f'href="/{REPO_NAME}/blog/'),
        ('href="/blog/', f'href="/{REPO_NAME}/blog/'),
        ('href="./faq/', f'href="/{REPO_NAME}/faq/'),
        ('href="/faq/', f'href="/{REPO_NAME}/faq/'),
        ('href="./pricing/', f'href="/{REPO_NAME}/pricing/'),
        ('href="/pricing/', f'href="/{REPO_NAME}/pricing/'),
        ('href="./robots', f'href="/{REPO_NAME}/robots'),
        ('href="/robots', f'href="/{REPO_NAME}/robots'),
        ('href="./sitemap', f'href="/{REPO_NAME}/sitemap'),
        ('href="/sitemap', f'href="/{REPO_NAME}/sitemap'),
        ('href="./"', f'href="/{REPO_NAME}/"'),
        ('href="/"', f'href="/{REPO_NAME}/"'),
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed: {file_path}")

def main():
    """主函数"""
    fixed_count = 0
    
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                fix_html_file(file_path)
                fixed_count += 1
    
    print(f"\nDone! Fixed {fixed_count} files.")

if __name__ == '__main__':
    main()
