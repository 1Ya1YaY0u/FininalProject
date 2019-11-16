from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
# import re
 
 
class PrpCrypt(object):
 
    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC

    def padding(self, text):
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            # \0 backspace
            # text = text + ('\0' * add)
            p_text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            # text = text + ('\0' * add)
            p_text = text + ('\0' * add).encode('utf-8')
        return p_text

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。
    # text is byte object
    def encrypt(self, text):
        # text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        text = self.padding(text)
        # length = 16
        # count = len(text)
        # if count < length:
        #     add = (length - count)
        #     # \0 backspace
        #     # text = text + ('\0' * add)
        #     text = text + ('\0' * add).encode('utf-8')
        # elif count > length:
        #     add = (length - (count % length))
        #     # text = text + ('\0' * add)
        #     text = text + ('\0' * add).encode('utf-8')
        self.ciphertext = cryptor.encrypt(text)
        # print('self.ciphertext', self.ciphertext)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串(bytes object)
        print('encrypt result', b2a_hex(self.ciphertext))
        return b2a_hex(self.ciphertext)
 
    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        # print(text)
        # length = 16
        # count = len(text)
        # if count < length:
        #     add = (length - count)
        #     # \0 backspace
        #     # text = text + ('\0' * add)
        #     text = text + ('\0' * add).encode('utf-8')
        # elif count > length:
        #     add = (length - (count % length))
        #     # text = text + ('\0' * add)
        #     # text = text + b2a_hex(('\0' * add).encode('utf-8'))
        #     text = text + ('\0' * add).encode('utf-8')
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        # print(text)
        plain_text = cryptor.decrypt(a2b_hex(text))
        # print(plain_text)
        # plain_text = plain_text[0:plain_text.find(b'\\')]
        # return re.sub(r'\x.*$', '', plain_text)
        print('decrypt result', plain_text.rstrip(b'\x00'))
        return plain_text.rstrip(b'\x00')
        # print(plain_text)
        # return bytes.decode(plain_text).rstrip('\0')
 
 
if __name__ == '__main__':
    pc = PrpCrypt('keyskeyskeyskeys')  # 初始化密钥
    e = pc.encrypt(b"testtesttest")  # 加密
    d = pc.decrypt(e)  # 解密
    print("加密:", e)
    print("解密:", d)
    print(d.decode('utf-8'))