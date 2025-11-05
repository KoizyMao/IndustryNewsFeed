"""
主程序入口
整合新闻收集和邮件发送功能
"""
import logging
import sys
from datetime import datetime
from config import LOG_LEVEL, LOG_FILE
from news_collector import collect_all_news
from email_sender import send_email
from utils import filter_and_deduplicate_news


def setup_logging():
    """配置日志"""
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )


def main():
    """主函数"""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    logger.info("=" * 60)
    logger.info("开始执行自动化新闻订阅任务")
    logger.info(f"执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 60)
    
    try:
        # 1. 收集新闻
        logger.info("步骤1: 收集新闻...")
        all_news = collect_all_news()
        
        if not all_news:
            logger.warning("未收集到任何新闻")
            return
        
        logger.info(f"收集到 {len(all_news)} 条新闻")
        
        # 2. 筛选和去重
        logger.info("步骤2: 筛选AI/AIGC相关新闻并去重...")
        filtered_news = filter_and_deduplicate_news(all_news)
        
        if not filtered_news:
            logger.warning("筛选后没有AI/AIGC相关新闻")
            return
        
        logger.info(f"筛选后剩余 {len(filtered_news)} 条AI/AIGC相关新闻")
        
        # 3. 发送邮件
        logger.info("步骤3: 发送邮件...")
        success = send_email(filtered_news)
        
        if success:
            logger.info("任务执行成功！")
        else:
            logger.error("邮件发送失败")
            sys.exit(1)
        
        logger.info("=" * 60)
        logger.info("任务执行完成")
        logger.info("=" * 60)
        
    except KeyboardInterrupt:
        logger.info("用户中断程序")
        sys.exit(0)
    except Exception as e:
        logger.error(f"程序执行出错: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()

