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

# 旧版本数据模式
oldver = bytes([0x02, 0x09, 0x00, 0x04, 0x09, 0x00, 0x06, 0x09, 0x00])

# 新版本数据模式
newver = bytes([0x02, 0x09, 0x0a, 0x04, 0x09, 0x00, 0x06, 0x09, 0x1e])

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
                # 定位到偏移量0x31处
                file.seek(0x31)
                
                # 读取9字节数据
                buffer = file.read(LEN)
                if len(buffer) != LEN:
                    onerror(path, "读取文件失败")
                    continue
                
                # 比较数据是否匹配旧版本
                if buffer == oldver:
                    # 重新定位并写入新版本数据
                    file.seek(0x31)
                    file.write(newver)
                    print(f"{path}: 改好了")
                else:
                    print(f"{path}: 版本本来就是对的啊")
                    
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
