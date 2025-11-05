"""
邮件发送模块
支持生成HTML格式邮件并发送
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from typing import List, Dict
import logging
from datetime import datetime
from config import SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, SMTP_USE_TLS, RECIPIENT_EMAIL

logger = logging.getLogger(__name__)


def generate_email_html(news_list: List[Dict]) -> str:
    """生成HTML格式的邮件内容"""
    date_str = datetime.now().strftime('%Y年%m月%d日')
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: Arial, "Microsoft YaHei", sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            .container {{
                background-color: white;
                border-radius: 8px;
                padding: 30px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
            }}
            .summary {{
                background-color: #ecf0f1;
                padding: 15px;
                border-radius: 5px;
                margin-bottom: 20px;
                font-size: 14px;
            }}
            .news-item {{
                margin-bottom: 25px;
                padding-bottom: 20px;
                border-bottom: 1px solid #e0e0e0;
            }}
            .news-item:last-child {{
                border-bottom: none;
            }}
            .news-title {{
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 8px;
            }}
            .news-title a {{
                color: #2980b9;
                text-decoration: none;
            }}
            .news-title a:hover {{
                text-decoration: underline;
            }}
            .news-meta {{
                color: #7f8c8d;
                font-size: 12px;
                margin-bottom: 8px;
            }}
            .news-description {{
                color: #555;
                font-size: 14px;
                line-height: 1.5;
            }}
            .footer {{
                margin-top: 30px;
                padding-top: 20px;
                border-top: 1px solid #e0e0e0;
                text-align: center;
                color: #95a5a6;
                font-size: 12px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📰 AI/AIGC 行业新闻订阅 - {date_str}</h1>
            
            <div class="summary">
                <strong>今日共收集 {len(news_list)} 条AI/AIGC相关新闻</strong>
            </div>
    """
    
    for i, news in enumerate(news_list, 1):
        title = news.get('title', '无标题')
        url = news.get('url', '#')
        description = news.get('description', '暂无描述')
        source = news.get('source', '未知来源')
        published = news.get('published', '')
        
        # 格式化发布时间
        if published:
            try:
                if 'T' in published:
                    pub_date = datetime.fromisoformat(published.replace('Z', '+00:00'))
                    published_str = pub_date.strftime('%Y-%m-%d %H:%M')
                else:
                    published_str = published
            except:
                published_str = published
        else:
            published_str = '未知时间'
        
        html_content += f"""
            <div class="news-item">
                <div class="news-title">
                    {i}. <a href="{url}" target="_blank">{title}</a>
                </div>
                <div class="news-meta">
                    来源: {source} | 发布时间: {published_str}
                </div>
                <div class="news-description">
                    {description}
                </div>
            </div>
        """
    
    html_content += """
            <div class="footer">
                <p>本邮件由自动化新闻订阅系统生成</p>
                <p>如有问题，请联系系统管理员</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_content


def send_email(news_list: List[Dict], subject: str = None) -> bool:
    """发送邮件"""
    if not SMTP_USERNAME or not SMTP_PASSWORD:
        logger.error("SMTP用户名或密码未配置")
        return False
    
    if not RECIPIENT_EMAIL:
        logger.error("收件人邮箱未配置")
        return False
    
    if not news_list:
        logger.warning("新闻列表为空，不发送邮件")
        return False
    
    try:
        # 生成邮件内容
        html_content = generate_email_html(news_list)
        
        # 创建邮件
        msg = MIMEMultipart('alternative')
        msg['From'] = Header(SMTP_USERNAME, 'utf-8')
        msg['To'] = Header(RECIPIENT_EMAIL, 'utf-8')
        
        if subject is None:
            date_str = datetime.now().strftime('%Y-%m-%d')
            subject = f"AI/AIGC 行业新闻订阅 - {date_str} ({len(news_list)}条)"
        
        msg['Subject'] = Header(subject, 'utf-8')
        
        # 添加HTML内容
        html_part = MIMEText(html_content, 'html', 'utf-8')
        msg.attach(html_part)
        
        # 发送邮件
        logger.info(f"正在连接SMTP服务器 {SMTP_HOST}:{SMTP_PORT}")
        
        if SMTP_USE_TLS and SMTP_PORT == 465:
            # 使用SSL连接（163邮箱通常使用465端口）
            server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)
        else:
            # 使用TLS连接
            server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
            if SMTP_USE_TLS:
                server.starttls()
        
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, RECIPIENT_EMAIL, msg.as_string())
        server.quit()
        
        logger.info(f"邮件发送成功！收件人: {RECIPIENT_EMAIL}, 新闻数量: {len(news_list)}")
        return True
        
    except smtplib.SMTPAuthenticationError:
        logger.error("SMTP认证失败，请检查用户名和密码（授权码）")
        return False
    except smtplib.SMTPException as e:
        logger.error(f"SMTP错误: {e}")
        return False
    except Exception as e:
        logger.error(f"发送邮件时出错: {e}")
        return False

