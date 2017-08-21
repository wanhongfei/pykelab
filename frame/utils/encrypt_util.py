#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/20 21:18
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : encrypt_util.py
# @Software: PyCharm
import base64
import hashlib

from django.contrib.auth.hashers import make_password

MD5 = "md5"
SHA1 = "sha1"
SHA224 = "sha224"
SHA256 = "sha256"
SHA384 = "sha384"
SHA512 = "sha512"
ALGORITHM_DICT = {
    MD5: hashlib.md5(),
    SHA1: hashlib.sha1(),
    SHA224: hashlib.sha224(),
    SHA256: hashlib.sha384(),
    SHA384: hashlib.sha512(),
}


def encode_base64(s):
    '''
    base64加密
    :param s:
    :return:
    '''
    return base64.encodestring(str(s))


def decode_base64(s):
    '''
    base64解密
    :param s:
    :return:
    '''
    return base64.decode(str(s))


def encode(s, algorithm=MD5):
    '''
    支持以上不可逆算法加密
    :param s:
    :param algorithm:
    :return:
    '''
    algorithm = str(algorithm).lower().strip()
    m = ALGORITHM_DICT[algorithm]
    m.update(str(s))
    return m.hexdigest()


def make_pbkdf2_sha256_passwd(pwd):
    '''
    django 默认自带加密
    :param pwd:
    :return:
    '''
    return str(make_password(str(pwd), None, 'pbkdf2_sha256'))


def check_pbkdf2_sha256_passwd(pwd, epwd):
    '''
    django 默认自带加密检测
    :param pwd:
    :param epwd:
    :return:
    '''
    return str(make_password(str(pwd), str(epwd)))


from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class AESEncoder(object):
    '''
    aes 加密算法
    '''

    def __init__(self, key):
        self.key = hashlib.md5(key).hexdigest()
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        if len(text) % 16 != 0:
            text = text + str((16 - len(text) % 16) * '0')
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0').rstrip('0')
