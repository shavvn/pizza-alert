import sys
import urllib2
import smtplib
from bs4 import BeautifulSoup


region_list = ['dc', 'nyc', 'philly', 'baltimore']
test_list = ['test']


def get_email_list(region):
    email_list = []
    fp = open('/home/shang/pizza-alert/' + region + '.csv', 'r')
    if fp is not None:
        for line in fp:
            email_list.append(line)
        fp.close()
    else:
        return None
    return email_list


def get_html_file(region):
    raw_url = 'http://ispizzahalfprice.com/'
    final_url = raw_url+region
    html_file = urllib2.urlopen(final_url).read()
    return html_file


def get_promo_code(html_input):
    soup = BeautifulSoup(html_input, 'html.parser')
    verdict_tag = soup.find('section', {'class': 'verdict'})
    promo_code = None
    for tag in verdict_tag.find_all('p'):
        if "Yes" in tag.get_text():
            if "Use code" in tag.get_text():
                promo_code = tag.find('strong').get_text()
                break
    return promo_code


def send_email(region, promo_code):
    gmail_user = 'dummy_email'
    gmail_pwd = 'password'
    from_addr = 'dummy_email'
    to_addr = ['mygmail.com']  # always send to myself to make sure it's working
    cc_addr = ['']  # meant to be empty
    bcc_addr = get_email_list(region)
    subject = 'Half Price Pizza in ' + region.upper() + ' with Code: ' + promo_code
    text = 'Yay! Pizza is half price today! Promotion Code is '+promo_code\
           + '\r\n Click the link below to order:\r\n'\
           + 'http://order.papajohns.com/\r\n'\
           + '(Use the promotion code when check out)'
    # Prepare actual message
    message = "from: %s\r\n" % from_addr\
              + "to: %s\r\n" % to_addr \
              + "cc: %s\r\n" % ", ".join(cc_addr)\
              + "Subject: %s\r\n" % subject\
              + "\r\n"\
              + text
    to_addrs = [to_addr] + bcc_addr
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587) #or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(from_addr, to_addrs, message)
        server.close()
        print 'successfully sent the mail to ' + region + ' users!'
    except:
        print 'failed to send mail'


if __name__ == '__main__':
    # no arguments, iterate all regions
    if len(sys.argv) == 1:
        for region in region_list:
            html_file = get_html_file(region)
            promo_code = get_promo_code(html_file)
            if promo_code is not None:  # promo code not None
                send_email(region, promo_code)
    elif len(sys.argv) == 2 and sys.argv[1] == 'test':
        region = 'test'
        promo_code = 'TEST50'
        send_email(region, promo_code)
    else:
        print('Invalid arguments!')
        exit(0)


