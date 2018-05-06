#!/usr/bin/env python
# -*- coding:utf-8 -*-
def email(p,text):
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = formataddr(["biwenkey", 'biwenkey@126.com'])
    msg['To'] = formataddr(["金必文", p])
    msg['Subject'] = "主题"

    server = smtplib.SMTP("smtp.126.com", 25)
    server.login("biwenkey@126.com", "jin1314520")
    server.sendmail('biwenkey@126.com', [p, ], msg.as_string())
    server.quit()


email("2753081006@qq.com","ok")

