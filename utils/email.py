# 发送邮件
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(subject, file_info_list, receivers, mail_text):
    """
        发送邮件方法
        :param subject: 邮件名称
        :param file_info_list: 附件列表，格式: [{'path': '/tmp/', 'name': 'aaa.txt'}, .....]
        :param receivers: 收件人列表, 格式: ['aaa@xxx.com', 'bbb@xxx.com']
        :param mail_text: 正文部分
        :return:
    """
    username = 'xxx@xxx.cn'
    password = 'xxxxxx'
    sender = username

    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ';'.join(receivers)

    # 文字部分
    pure_text = MIMEText(mail_text, _subtype='plain', _charset='utf-8')
    msg.attach(pure_text)

    # 增加附件
    if file_info_list:
        for file_info in file_info_list:
            attachment = MIMEApplication(open(file_info['path'] + file_info['name'], 'rb').read())
            attachment.add_header('Content-Disposition', 'attachment', filename=file_info['name'])
            msg.attach(attachment)

    try:
        client = smtplib.SMTP()
        client.connect('smtp.exmail.qq.com')
        client.login(username, password)
        client.sendmail(sender, receivers, msg.as_string())
        client.quit()
        return True, '邮件发送成功！'
    except smtplib.SMTPRecipientsRefused:
        return False, 'Recipient refused'
    except smtplib.SMTPAuthenticationError as e:
        return False, str(e)
    except smtplib.SMTPSenderRefused:
        return False, 'Sender refused'
    except smtplib.SMTPException as e:
        return False, str(e)
    
# 发送邮件v2，用ssl
def send_email_v2(subject, file_info_list, receivers, mail_text):
    """
        发送邮件方法
        :param subject: 邮件名称
        :param file_info_list: 附件列表，格式: [{'path': '/tmp/', 'name': 'aaa.txt'}, .....]
        :param receivers: 收件人列表, 格式: ['aaa@xxx.com', 'bbb@xxx.com']
        :param mail_text: 正文部分
        :return:
    """
    username = 'xxx@xxx.cn'
    password = 'xxxxxx'
    sender = username

    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ';'.join(receivers)

    # 文字部分
    pure_text = MIMEText(mail_text, _subtype='plain', _charset='utf-8')
    msg.attach(pure_text)

    # 增加附件
    if file_info_list:
        for file_info in file_info_list:
            attachment = MIMEApplication(open(file_info['path'] + file_info['name'], 'rb').read())
            attachment.add_header('Content-Disposition', 'attachment', filename=file_info['name'])
            msg.attach(attachment)

    try:
        client = smtplib.SMTP_SSL('smtp.exmail.qq.com:465')
        client.login(username, password)
        client.sendmail(sender, receivers, msg.as_string())
        client.quit()
        return True, '邮件发送成功！'
    except smtplib.SMTPRecipientsRefused:
        return False, 'Recipient refused'
    except smtplib.SMTPAuthenticationError as e:
        return False, str(e)
    except smtplib.SMTPSenderRefused:
        return False, 'Sender refused'
    except smtplib.SMTPException as e:
        return False, str(e)