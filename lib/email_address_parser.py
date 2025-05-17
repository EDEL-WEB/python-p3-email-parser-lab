# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, strArg:str):
        self.string = strArg

    def parse(self):
        matched = []
        emailPattern = r"[a-z.]+[a-z0-9]+@[a-z]+\.[a-z+]"
        mailList = self.separate()
        email = re.compile(emailPattern)
        for mail in mailList:
            if email.match(mail):
                matched.append(mail)

        matched.sort()  
        return matched
    
    def separate(self):
        mails = []
        pos = 0
        for i in range(len(self.string)):
            if self.string[i] == " " or self.string[i] == ",":
                mail = self.string[pos:i]
                pos = i + 1
                mails.append(mail)
            elif  i == len(self.string) - 1:
                mail = self.string[pos:i+1]
                mails.append(mail)
        return mails

parser = EmailAddressParser("talk@talk.com john.jones@flatironschool.com alexa@amazon.com")
parser.parse()