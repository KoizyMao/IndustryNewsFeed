"""
新闻收集模块
支持RSS订阅源和新闻API两种方式收集新闻
"""
import feedparser
import requests
from typing import List, Dict
from datetime import datetime
import logging
from config import RSS_FEEDS, NEWS_API_KEY
from utils import clean_html_text

logger = logging.getLogger(__name__)


def collect_rss_news() -> List[Dict]:
    """从RSS订阅源收集新闻"""
    all_news = []
    
    for feed_url in RSS_FEEDS:
        try:
            logger.info(f"正在获取RSS源: {feed_url}")
            feed = feedparser.parse(feed_url)
            
            if feed.bozo and feed.bozo_exception:
                logger.warning(f"RSS源解析失败 {feed_url}: {feed.bozo_exception}")
                continue
            
            for entry in feed.entries[:20]:  # 每个源最多取20条
                try:
                    title = entry.get('title', '').strip()
                    link = entry.get('link', '').strip()
                    description = entry.get('description', '') or entry.get('summary', '')
                    description = clean_html_text(description)
                    
                    # 处理发布时间
                    published = ''
                    if hasattr(entry, 'published_parsed') and entry.published_parsed:
                        published = datetime(*entry.published_parsed[:6]).isoformat()
                    elif hasattr(entry, 'published'):
                        published = entry.published
                    
                    if title and link:
                        all_news.append({
                            'title': title,
                            'url': link,
                            'description': description[:300],  # 限制描述长度
                            'published': published,
                            'source': feed.feed.get('title', feed_url)
                        })
                except Exception as e:
                    logger.error(f"处理RSS条目时出错: {e}")
                    continue
            
            logger.info(f"从 {feed_url} 获取了 {len(feed.entries)} 条新闻")
            
        except Exception as e:
            logger.error(f"获取RSS源 {feed_url} 时出错: {e}")
            continue
    
    logger.info(f"RSS源总共收集了 {len(all_news)} 条新闻")
    return all_news


def collect_api_news() -> List[Dict]:
    """从NewsAPI收集新闻"""
    if not NEWS_API_KEY:
        logger.warning("未配置NEWS_API_KEY，跳过API新闻收集")
        return []
    
    all_news = []
    
    try:
        # NewsAPI搜索AI相关新闻
        keywords = ['artificial intelligence', 'AI', 'machine learning', 'GPT', 'ChatGPT']
        
        for keyword in keywords[:2]:  # 限制关键词数量避免请求过多
            try:
                url = 'https://newsapi.org/v2/everything'
                params = {
                    'q': keyword,
                    'language': 'en',
                    'sortBy': 'publishedAt',
                    'pageSize': 20,
                    'apiKey': NEWS_API_KEY
                }
                
                logger.info(f"正在从NewsAPI获取关键词: {keyword}")
                response = requests.get(url, params=params, timeout=10)
                response.raise_for_status()
                
                data = response.json()
                articles = data.get('articles', [])
                
                for article in articles:
                    title = article.get('title', '').strip()
                    url_link = article.get('url', '').strip()
                    description = clean_html_text(article.get('description', ''))
                    published = article.get('publishedAt', '')
                    source = article.get('source', {}).get('name', 'Unknown')
                    
                    if title and url_link:
                        all_news.append({
                            'title': title,
                            'url': url_link,
                            'description': description[:300],
                            'published': published,
                            'source': source
                        })
                
                logger.info(f"从NewsAPI获取关键词 {keyword} 得到 {len(articles)} 条新闻")
                
            except Exception as e:
                logger.error(f"获取NewsAPI关键词 {keyword} 时出错: {e}")
                continue
        
        logger.info(f"NewsAPI总共收集了 {len(all_news)} 条新闻")
        
    except Exception as e:
        logger.error(f"NewsAPI请求出错: {e}")
    
    return all_news


def collect_all_news() -> List[Dict]:
    """收集所有来源的新闻"""
    logger.info("开始收集新闻...")
    
    rss_news = collect_rss_news()
    api_news = collect_api_news()
    
    # 合并所有新闻
    all_news = rss_news + api_news
    
    logger.info(f"总共收集了 {len(all_news)} 条新闻")
    return all_news

