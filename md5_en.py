import hashlib
import os

def md5_32(text):
    """
    计算字符串的 32位 MD5 值
    """
    # 1. 将字符串编码为 bytes (utf-8)
    # 2. 计算 md5
    # 3. 返回 16 进制字符串 (hexdigest 默认就是 32 位小写)
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def process_file(input_filename, output_filename):
    if not os.path.exists(input_filename):
        print(f"❌ 错误：找不到源文件 '{input_filename}'")
        return

    print(f"🚀 正在读取文件：{input_filename} ...")
    
    try:
        with open(input_filename, 'r', encoding='utf-8') as f_in, \
             open(output_filename, 'w', encoding='utf-8') as f_out:
            
            count = 0
            for line in f_in:
                # 去除每行首尾的空白字符（换行符、空格等）
                # 如果不加 strip()，加密结果会包含换行符，导致哈希值不同
                clean_line = line.strip()
                
                # 如果是空行，可以选择跳过或处理，这里选择跳过
                if not clean_line:
                    continue
                
                # 计算 MD5
                encrypted_text = md5_32(clean_line)
                
                # 写入新文件，并补上换行符
                f_out.write(encrypted_text + '\n')
                count += 1
                
                # 可选：在控制台打印进度（如果文件很大，可以注释掉下面这行）
                # print(f"处理中: {clean_line} -> {encrypted_text}")

        print(f"✅ 成功！共处理了 {count} 行数据。")
        print(f"📄 结果已保存在：{output_filename}")

    except Exception as e:
        print(f"❌ 发生未知错误：{e}")

if __name__ == "__main__":
    source_file = 'm.txt'
    result_file = 'md5_result.txt'
    process_file(source_file, result_file)