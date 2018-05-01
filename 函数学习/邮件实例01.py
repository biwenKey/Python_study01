#!/usr/bin/env python
# -*- coding:utf-8 -*-

def mail():
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    ret = True
    try:
        msg = MIMEText('biwenkey', 'plain', 'utf-8')
        msg['From'] = formataddr(["biwenkey", 'biwenkey@126.com'])
        msg['To'] = formataddr(["金必文", '2753081006@qq.com'])
        msg['Subject'] = "主题"
        server = smtplib.SMTP("smtp.126.com", 25)
        server.login("biwenkey@126.com", "jin1314520")
        server.sendmail('biwenkey@126.com', ['2753081006@qq.com', ], msg.as_string())
        server.quit()
    except:
        ret = False
    return ret

rr = mail()
if rr:
    print("发送成功")
else:
    print("发送失败")
