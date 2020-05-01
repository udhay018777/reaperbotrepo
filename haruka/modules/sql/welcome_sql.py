import threading
from typing import Union

from sqlalchemy import Column, String, Boolean, UnicodeText, Integer, BigInteger

from haruka.modules.helper_funcs.msg_types import Types
from haruka.modules.sql import SESSION, BASE

DEFAULT_WELCOME = "Hey {first}, how are you?"
DEFAULT_GOODBYE = "Nice knowing ya!"


class Welcome(BASE):
    __tablename__ = "welcome_pref"
    chat_id = Column(String(14), primary_key=True)
    should_welcome = Column(Boolean, default=True)
    should_goodbye = Column(Boolean, default=True)

    custom_content = Column(UnicodeText, default=None)
    custom_welcome = Column(UnicodeText, default=DEFAULT_WELCOME)
    welcome_type = Column(Integer, default=Types.TEXT.value)

    custom_content_leave = Column(UnicodeText, default=None)
    custom_leave = Column(UnicodeText, default=DEFAULT_GOODBYE)
    leave_type = Column(Integer, default=Types.TEXT.value)

    clean_welcome = Column(BigInteger)

    def __init__(self, chat_id, should_welcome=True, should_goodbye=True):
        self.chat_id = chat_id
        self.should_welcome = should_welcome
        self.should_goodbye = should_goodbye

    def __repr__(self):
        return "<Chat {} should Welcome new users: {}>".format(
            self.chat_id, self.should_welcome)
