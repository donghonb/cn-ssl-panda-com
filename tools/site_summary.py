"""
Site Summary Generator
"""

import os
import json

# Sample site data with keywords, tags, and descriptions
SITE_DATA = {
    "site_url": "https://cn-ssl-panda.com",
    "keywords": ["熊猫体育", "体育赛事", "在线娱乐", "体育投注"],
    "tags": ["sports", "entertainment", "ssl-secured", "panda"],
    "description": "一个专注于体育赛事和在线娱乐的平台，提供多种体育项目的资讯与互动服务。"
}

def load_site_info() -> dict:
    """Load site information from embedded data."""
    return SITE_DATA

def validate_url(url: str) -> bool:
    """Basic URL validation."""
    return url.startswith("http://") or url.startswith("https://")

def format_summary(data: dict) -> str:
    """Generate a structured summary from site data."""
    lines = []
    lines.append("=" * 50)
    lines.append("站点摘要报告")
    lines.append("=" * 50)
    lines.append(f"站点URL: {data.get('site_url', 'N/A')}")
    lines.append(f"核心关键词: {', '.join(data.get('keywords', []))}")
    lines.append(f"相关标签: {', '.join(data.get('tags', []))}")
    lines.append(f"简要说明: {data.get('description', 'N/A')}")
    lines.append("=" * 50)
    return "\n".join(lines)

def export_to_markdown(data: dict, filepath: str = "site_summary.md") -> str:
    """Export summary to a markdown file."""
    md_lines = [
        "# 站点摘要",
        "",
        f"**URL**: [{data.get('site_url', '')}]({data.get('site_url', '')})",
        "",
        "## 关键词",
        "",
    ]
    for kw in data.get("keywords", []):
        md_lines.append(f"- {kw}")
    md_lines.append("")
    md_lines.append("## 标签")
    md_lines.append("")
    for tag in data.get("tags", []):
        md_lines.append(f"- `{tag}`")
    md_lines.append("")
    md_lines.append("## 说明")
    md_lines.append("")
    md_lines.append(data.get("description", ""))
    md_lines.append("")
    md_lines.append("---")
    md_lines.append(f"*生成于 {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")

    content = "\n".join(md_lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath

def main():
    """Main entry point for generating site summary."""
    print("正在生成站点摘要...\n")
    info = load_site_info()

    # Validate URL before proceeding
    if not validate_url(info.get("site_url", "")):
        print("错误：站点URL格式无效。")
        return

    # Print summary to console
    summary = format_summary(info)
    print(summary)

    # Export to markdown file
    md_file = export_to_markdown(info)
    print(f"\nMarkdown 摘要已导出至: {os.path.abspath(md_file)}")

if __name__ == "__main__":
    main()