# -*- coding: utf-8 -*-
# @Author  : Dali

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


class Test_Email():
    def __init__(self,filename):

        self.mail_addr=filename #发送邮件的地址
        self.smtpserver='smtp.sina.com'#发送邮件的服务器
        self.user='1334029448li@sina.com' # 发送邮箱的用户/密码
        self.password='123456Li'
        self.sender='1334029448li@sina.com' # 发送邮件
        self.receiver=['1334029448@qq.com','wojiangyaoaini@qq.com'] # 接受邮件的用户
        self.subject='中秋节' # 发送邮件主题

    #把报告路径拿到，报告名称切出来
    def report_name(self):
        mail_name = str(self.mail_addr)
        repost_name1 = mail_name.split("\\")
        return repost_name1[-1]

    #发送邮件的附件
    def send_email(self):
        sendfile = open(self.mail_addr, 'rb').read()
        att = MIMEText(sendfile, "plain", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        # att["Content-Disposition"]="attachment;filename =report_name"
        att.add_header('Content-Disposition', 'attachment', filename=self.report_name())
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = Header(self.subject, 'utf-8')
        msgRoot['From'] = Header(self.user)
        msgRoot.attach(att)

        smtp = smtplib.SMTP()
        smtp.connect(self.smtpserver)
        # 用户登录并发送邮件
        smtp.login(self.user, self.password)
        smtp.sendmail(self.sender, self.receiver, msgRoot.as_string())
        smtp.quit()


if __name__ == '__main__':
    mail_addr = r'D:\class_project\class_40\class_40_ui_frame\report\2021_12_29_15_00_24test.html'
    test_email= Test_Email(mail_addr)
    test_email.send_email()
