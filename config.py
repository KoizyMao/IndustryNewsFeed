"""
配置文件模块
支持从环境变量或直接配置读取敏感信息
"""
import os
from typing import List

# SMTP配置（163邮箱）
SMTP_HOST = os.getenv('SMTP_HOST', 'smtp.163.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '465'))
SMTP_USERNAME = os.getenv('SMTP_USERNAME', '')  # 163邮箱地址
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '')  # 163邮箱授权码
SMTP_USE_TLS = True

# 收件人邮箱
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', '')  # 收件人邮箱地址

# NewsAPI配置
NEWS_API_KEY = os.getenv('NEWS_API_KEY', '')  # 可选，如果需要使用NewsAPI

# RSS订阅源列表（AI/AIGC相关新闻源）
RSS_FEEDS: List[str] = [
    'https://feeds.feedburner.com/oreilly/radar',  # O'Reilly Radar
    'https://www.theverge.com/rss/index.xml',  # The Verge
    'https://techcrunch.com/feed/',  # TechCrunch
    'https://rss.cnn.com/rss/edition.rss',  # CNN Technology
    'https://www.artificialintelligence-news.com/feed/',  # AI News
    'https://venturebeat.com/feed/',  # VentureBeat
    'https://www.wired.com/feed/rss',  # Wired
]

# AI/AIGC相关关键词（用于筛选新闻）
AI_KEYWORDS: List[str] = [
    'AI', 'AIGC', 'artificial intelligence', 'machine learning',
    '人工智能', '生成式AI', '生成式人工智能', '大模型',
    'GPT', 'ChatGPT', 'LLM', 'large language model',
    'deep learning', '深度学习', 'neural network', '神经网络',
    'AGI', 'artificial general intelligence', '通用人工智能',
    'computer vision', '计算机视觉', 'NLP', '自然语言处理',
    'reinforcement learning', '强化学习', 'transformer',
    'generative AI', '生成模型', 'diffusion model', '扩散模型',
    'multimodal', '多模态', 'robotics', '机器人',
]

# 新闻去重存储文件（可选，用于持久化去重）
DUPLICATE_CHECK_FILE = 'news_cache.json'

# 日志配置
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = 'news_feed.log'

