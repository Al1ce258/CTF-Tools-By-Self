from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

class RSAEncryptor:
    def __init__(self, public_key_pem):
        """
        初始化加密器
        :param public_key_pem: 公钥字符串 (包含 -----BEGIN PUBLIC KEY----- 头尾)
        """
        # 导入公钥
        self.key = RSA.import_key(public_key_pem)
        # 创建 cipher 对象，使用 PKCS1_v1_5 填充 (这是 JSEncrypt 的默认填充方式)
        self.cipher = PKCS1_v1_5.new(self.key)

    def encrypt(self, message):
        """
        加密字符串
        :param message: 需要加密的明文字符串
        :return: Base64 编码的密文
        """
        if isinstance(message, str):
            message = message.encode('utf-8')
        
        # 执行加密
        encrypted_bytes = self.cipher.encrypt(message)
        
        # 转换为 Base64 字符串，方便传输
        encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')
        
        return encrypted_base64

# ================= 配置区域 =================

# 你提供的公钥 (已补全 PEM 格式头尾)
PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAg84CYczBEVWqxAR/4KdEpFoJ2Xj2JI4EOZPTGjO18ZGThhAN94AYemO99LkNqERr2ogwuS/M3zLaWzF/iwctHi7s84kopDUZE9iVIPLtTwc+nJeld7U5W4fvJ1zJN8l7sYiQ2qbhzUxiP7Tfg2OnXIosg3O/eWTmD5Yco249RodTVwj453ni9Wf57UgIsBUBepNeolpKRaH5tIpUsxT1DkqLEHKM3rflYVuApx7AXT7NYSzNIbRoFtzvcjZ0N9sxLzBeWcIYTSXTiMtG3pVngkL+U/TCLiXJU8Z2z/XwPjg/8D0YHunW3QwqztlW7+F6N7NfSAK7lVYXshv06EOcYQIDAQAB
-----END PUBLIC KEY-----"""

# ================= 运行示例 =================

if __name__ == "__main__":
    # 1. 初始化
    encryptor = RSAEncryptor(PUBLIC_KEY)
    
    # 2. 测试数据
    plain_text = "123456"  # 假设这是密码
    
    # 3. 加密
    cipher_text = encryptor.encrypt(plain_text)
    
    print(f"明文: {plain_text}")
    print(f"密文: {cipher_text}")
    print("-" * 30)