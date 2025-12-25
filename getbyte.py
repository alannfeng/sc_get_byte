#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
读取文件从0x31位置开始的16个字节数据，并分别打印每个字节
"""

def read_bytes_from_offset(file_path, offset=0x31, length=32):
    """
    从指定文件的偏移位置读取指定长度的字节数据
    
    Args:
        file_path (str): 要读取的文件路径
        offset (int): 起始偏移位置（十六进制，默认0x31）
        length (int): 要读取的字节数（默认16）
    """
    try:
        with open(file_path, 'rb') as file:
            # 定位到指定偏移位置
            file.seek(offset)
            
            # 读取指定长度的字节数据
            data = file.read(length)
            
            if len(data) < length:
                print(f"警告：文件从偏移0x{offset:x}开始只有{len(data)}个字节，不足{length}个字节")
            
            print(f"从文件 '{file_path}' 偏移0x{offset:x}处读取到的{len(data)}个字节数据：")
            print("=" * 50)
            
            # 分别打印每个字节
            for i, byte in enumerate(data):
                # 十六进制格式
                hex_value = f"0x{byte:02x}"
                # 十进制格式
                dec_value = str(byte)
                # ASCII字符（如果可打印）
                ascii_char = chr(byte) if 32 <= byte <= 126 else '.'
                
                print(f"字节 {i:2d}: 偏移0x{offset + i:02x} | 十六进制: {hex_value:4s} | 十进制: {dec_value:3s} | ASCII: {ascii_char}")
            
            print("=" * 50)
            
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在")
    except PermissionError:
        print(f"错误：没有权限读取文件 '{file_path}'")
    except Exception as e:
        print(f"读取文件时发生错误：{e}")


def main():
    """主函数"""
    print("文件字节读取工具")
    print("功能：读取文件从0x31位置开始的16个字节数据")
    print("-" * 40)
    
    # 获取用户输入的文件路径
    file_path = input("请输入要读取的文件路径：").strip()
    
    if not file_path:
        print("未输入文件路径，程序退出")
        return
    
    # 读取并显示字节数据
    read_bytes_from_offset(file_path)


if __name__ == "__main__":
    main()
