#!/usr/bin/env python3
"""修复路径问题 - 使用相对路径，本地和GitHub都能正常工作"""

import os

ROOT_DIR = r'f:\GithubDaiGou'

def fix_html_file(file_path, is_root_file):
    """修复单个HTML文件的路径"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if is_root_file:
        # 根目录文件：将 /xxx 改为 ./xxx
        replacements = [
            ('href="/_astro/', 'href="./_astro/'),
            ('src="/_astro/', 'src="./_astro/'),
            ('href="/favicon', 'href="./favicon'),
            ('href="/og-image', 'href="./og-image'),
            ('href="/blog/', 'href="./blog/'),
            ('href="/faq/', 'href="./faq/'),
            ('href="/pricing/', 'href="./pricing/'),
            ('href="/robots', 'href="./robots'),
            ('href="/sitemap', 'href="./sitemap'),
            ('href="/"', 'href="./"'),
            ('src="/favicon', 'src="./favicon'),
            ('content="/og-image', 'content="./og-image'),
        ]
    else:
        # 子目录文件：使用 ../ 返回上级目录
        replacements = [
            ('href="/_astro/', 'href="../_astro/'),
            ('src="/_astro/', 'src="../_astro/'),
            ('href="/favicon', 'href="../favicon'),
            ('href="/og-image', 'href="../og-image'),
            ('href="/blog/', 'href="../blog/'),
            ('href="/faq/', 'href="../faq/'),
            ('href="/pricing/', 'href="../pricing/'),
            ('href="/robots', 'href="../robots'),
            ('href="/sitemap', 'href="../sitemap'),
            ('href="/"', 'href="../"'),
            ('src="/favicon', 'src="../favicon'),
            ('content="/og-image', 'content="../og-image'),
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
                is_root = (root == ROOT_DIR)
                fix_html_file(file_path, is_root)
                fixed_count += 1
    
    print(f"\nDone! Fixed {fixed_count} files.")

if __name__ == '__main__':
    main()
