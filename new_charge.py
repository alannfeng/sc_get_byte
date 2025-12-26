#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件版本修改工具 - Python 3实现
功能：检查并修改文件在偏移量0x31处的9字节版本数据
"""

import sys
import os

# 定义数据长度
LEN = 9

# # 旧版本数据模式
# oldver = bytes([0x02, 0x09, 0x00, 0x04, 0x09, 0x00, 0x06, 0x09, 0x00])

# 新版本数据模式
newver1 = bytes([0x02, 0x09, 0x0a, 0x04, 0x09, 0x00, 0x06, 0x09, 0x1e, 0x08, 0x09, 0xf8, 0xd7, 0x0b, 0x0a, 0x09, 0xf8, 0xd7, 0x0b])
newver2 = bytes([0xf8, 0xd7, 0x0b])

def onerror(path, error_msg):
    """错误处理函数"""
    print(f"{path}: 不行，{error_msg}")

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("给点录像啊")
        return
    
    for i in range(1, len(sys.argv)):
        path = sys.argv[i]
        
        try:
            # 以读写二进制模式打开文件
            with open(path, "r+b") as file:
                
                # 修改从0x31开始19字节数据
                file.seek(0x31)
                file.write(newver1)
                print(f"{path}: newver1改好了")

                # 修改从0x67开始3字节数据
                file.seek(0x67)
                file.write(newver2)
                print(f"{path}: newver2改好了")
            
                    
        except FileNotFoundError:
            onerror(path, "文件不存在")
        except PermissionError:
            onerror(path, "权限不足")
        except IOError as e:
            onerror(path, f"IO错误: {e}")
        except Exception as e:
            onerror(path, f"未知错误: {e}")
    
    print("可以把我关了")
    input()  # 等待用户输入

if __name__ == "__main__":
    main()
