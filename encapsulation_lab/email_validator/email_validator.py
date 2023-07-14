from typing import List


class EmailValidator:

    def __init__(self, min_length: int, mails, domains):
        self.min_length = min_length
        self.mails: List[str] = mails
        self.domains: List[str] = domains

    def __is_name_valid(self, name):
        return True if len(name) >= self.min_length else False

    def __is_mail_valid(self, mail):
        return True if mail in self.mails else False

    def __is_domain_valid(self, domain):
        return True if domain in self.domains else False


    def validate(self, email):
        line = email.split("@")
        name = line[0]
        mail, domain = line[1].split(".")
        return True if self.__is_name_valid(name) \
                       and self.__is_mail_valid(mail) and self.__is_domain_valid(domain) else False




