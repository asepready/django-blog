#!/usr/bin/env python
# encoding: utf-8

from core.utils import send_email
from core.utils import get_current_site
import logging

logger = logging.getLogger(__name__)


def send_comment_email(comment):
    site = get_current_site().domain
    subject = 'Thanks for your comment'
    article_url = "https://{site}{path}".format(
        site=site, path=comment.article.get_absolute_url())
    html_content = """
                   <p>Thank you for your comment on this site</p>
                   You can visit
                   <a href="%s" rel="bookmark">%s</a>
                   To see your comments,
                   Thank you again!
                   <br />
                   If the above link cannot be opened, please copy this link to your browser.
                   %s
                   """ % (article_url, comment.article.title, article_url)
    tomail = comment.author.email
    send_email([tomail], subject, html_content)
    try:
        if comment.parent_comment:
            html_content = """
                    You are <a href="%s" rel="bookmark">%s</a> S comments <br/> %s <br/> Received a reply. Go and have a look
                    <br/>
                    If the above link cannot be opened, please copy this link to your browser.
                    %s
                    """ % (article_url, comment.article.title, comment.parent_comment.body, article_url)
            tomail = comment.parent_comment.author.email
            send_email([tomail], subject, html_content)
    except Exception as e:
        logger.error(e)
