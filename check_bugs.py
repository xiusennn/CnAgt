#!/usr/bin/env python3
"""检测所有HTML文件中的路径问题和潜在BUG"""

import os
import re

ROOT_DIR = r'f:\GithubDaiGou'

def check_html_file(file_path):
    """检查单个HTML文件"""
    issues = []
    
    # 尝试多种编码读取文件
    content = None
    for encoding in ['utf-8', 'gbk', 'gb2312', 'latin-1']:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
    
    if content is None:
        return [f"无法读取文件: {file_path}"]
    
    # 检查是否还有 _astro 路径
    if '/_astro/' in content or '/CnAgt/_astro/' in content:
        issues.append("仍然包含 _astro 路径")
    
    # 检查 assets 路径是否正确
    if '/assets/' not in content and 'stylesheet' in content:
        issues.append("缺少 assets 路径引用")
    
    # 检查是否有未闭合的标签
    open_tags = len(re.findall(r'<(?!/|!|br|hr|img|input|meta|link)[a-zA-Z][^>]*[^/]>', content))
    close_tags = len(re.findall(r'</[a-zA-Z][^>]*>', content))
    # 注意：这不是精确检查，只是粗略估计
    
    # 检查 JavaScript 函数是否完整
    if 'function' in content:
        # 检查是否有未闭合的函数
        open_braces = content.count('{')
        close_braces = content.count('}')
        if open_braces != close_braces:
            issues.append(f"JavaScript 大括号不匹配: {{ = {open_braces}, }} = {close_braces}")
    
    # 检查是否有未闭合的引号
    single_quotes = content.count("'") - content.count("\\'")
    double_quotes = content.count('"') - content.count('\\"')
    if single_quotes % 2 != 0:
        issues.append("可能存在未闭合的单引号")
    if double_quotes % 2 != 0:
        issues.append("可能存在未闭合的双引号")
    
    return issues

def main():
    """主函数"""
    print("开始检测HTML文件...\n")
    
    total_issues = 0
    
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                issues = check_html_file(file_path)
                
                if issues:
                    print(f"文件: {file_path}")
                    for issue in issues:
                        print(f"  ⚠️  {issue}")
                    print()
                    total_issues += len(issues)
                else:
                    print(f"✅ {file_path} - 无问题")
    
    print(f"\n总计发现 {total_issues} 个问题")
    
    if total_issues == 0:
        print("🎉 所有文件检测通过！")

if __name__ == '__main__':
    main()
