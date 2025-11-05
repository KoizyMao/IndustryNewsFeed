"""
工具函数模块
包含去重、筛选等辅助功能
"""
import json
import hashlib
import os
from typing import List, Dict, Set
from datetime import datetime, timedelta
from config import AI_KEYWORDS, DUPLICATE_CHECK_FILE


def generate_news_hash(title: str, url: str) -> str:
    """生成新闻的唯一哈希值，用于去重"""
    content = f"{title}|{url}".lower().strip()
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def load_seen_news() -> Set[str]:
    """加载已见过的新闻哈希集合"""
    if not os.path.exists(DUPLICATE_CHECK_FILE):
        return set()
    
    try:
        with open(DUPLICATE_CHECK_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # 清理30天前的记录
            cutoff_date = datetime.now() - timedelta(days=30)
            seen_news = set()
            for item in data.get('news', []):
                news_date = datetime.fromisoformat(item['date'])
                if news_date > cutoff_date:
                    seen_news.add(item['hash'])
            return seen_news
    except Exception:
        return set()


def save_seen_news(seen_hashes: Set[str]):
    """保存已见过的新闻哈希集合"""
    try:
        existing_data = {'news': []}
        if os.path.exists(DUPLICATE_CHECK_FILE):
            with open(DUPLICATE_CHECK_FILE, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        
        # 添加新的哈希记录
        cutoff_date = datetime.now() - timedelta(days=30)
        news_list = existing_data.get('news', [])
        
        # 清理旧记录
        news_list = [
            item for item in news_list 
            if datetime.fromisoformat(item['date']) > cutoff_date
        ]
        
        # 添加新的记录
        current_date = datetime.now().isoformat()
        for hash_val in seen_hashes:
            if not any(item['hash'] == hash_val for item in news_list):
                news_list.append({
                    'hash': hash_val,
                    'date': current_date
                })
        
        existing_data['news'] = news_list
        
        with open(DUPLICATE_CHECK_FILE, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"保存新闻缓存时出错: {e}")


def is_ai_related(title: str, description: str = '') -> bool:
    """判断新闻是否与AI/AIGC相关"""
    text = f"{title} {description}".lower()
    return any(keyword.lower() in text for keyword in AI_KEYWORDS)


def filter_and_deduplicate_news(news_list: List[Dict]) -> List[Dict]:
    """筛选AI相关新闻并去重"""
    seen_hashes = load_seen_news()
    filtered_news = []
    new_hashes = set()
    
    for news in news_list:
        # 检查是否与AI相关
        title = news.get('title', '')
        description = news.get('description', '')
        
        if not is_ai_related(title, description):
            continue
        
        # 生成哈希并去重
        url = news.get('url', '')
        news_hash = generate_news_hash(title, url)
        
        if news_hash not in seen_hashes:
            filtered_news.append(news)
            new_hashes.add(news_hash)
    
    # 更新已见过的新闻集合
    if new_hashes:
        seen_hashes.update(new_hashes)
        save_seen_news(seen_hashes)
    
    # 按日期排序（最新的在前）
    filtered_news.sort(key=lambda x: x.get('published', ''), reverse=True)
    
    return filtered_news


def clean_html_text(text: str) -> str:
    """清理HTML标签，提取纯文本"""
    from bs4 import BeautifulSoup
    if not text:
        return ''
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text(strip=True)

