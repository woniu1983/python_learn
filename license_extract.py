# -*- coding: UTF-8 -*-
'''
  尝试从文件夹目录下，提取各个库模块的开源协议，并存储到csv文件中
'''

import time
import os

def parse_license(dirname, license_dir_path):
    license_path1 = license_dir_path + "/" + "LICENSE"
    license_path2 = license_dir_path + "/" + "LICENSE.md"
    license_path3 = license_dir_path + "/" + "LICENSE.txt"
    license_path4 = license_dir_path + "/" + "README"
    license_path5 = license_dir_path + "/" + "README.md"
    license_path6 = license_dir_path + "/" + "README.txt"
    license_path7 = license_dir_path + "/" + "package.json"

    license_search_files = []
    if os.path.exists(license_path1):
        license_search_files.append(license_path1)
    if os.path.exists(license_path2):
        license_search_files.append(license_path2)
    if os.path.exists(license_path3):
        license_search_files.append(license_path3)
    if os.path.exists(license_path4):
        license_search_files.append(license_path4)
    if os.path.exists(license_path5):
        license_search_files.append(license_path5)
    if os.path.exists(license_path6):
        license_search_files.append(license_path6)
    if os.path.exists(license_path7):
        license_search_files.append(license_path7)
    
    if len(license_search_files) == 0:
        print("%s License file not found" % (dirname))
        return
    license = ''
    for license_path in license_search_files:
        print("license_path=", license_path)
        try:
            f = open(license_path, 'r', encoding='utf-8')

            # 1： 一次性读取整个文件
            # print(f.read())

            # 2： 通过for-in循环逐行读取
            for line in f:
                if 'MIT ' in line.upper():
                    print("%s License is %s" % (dirname, 'MIT'))
                    license = 'MIT'
                    break
                if '\"MIT\"' in line.upper():
                    print("%s License is %s" % (dirname, 'MIT'))
                    license = 'MIT'
                    break
                elif 'APACHE' in line.upper():
                    print("%s License is %s" % (dirname, 'Apache v2'))
                    license = 'Apache v2'
                    break
                elif 'BSD ' in line.upper():
                    print("%s License is %s" % (dirname, 'BSD'))
                    license = 'BSD'
                    break
                elif '\"BSD\"' in line.upper():
                    print("%s License is %s" % (dirname, 'BSD'))
                    license = 'BSD'
                    break
                elif 'BSD-3' in line.upper():
                    print("%s License is %s" % (dirname, 'BSD'))
                    license = 'BSD'
                    break
                elif 'BSD-2' in line.upper():
                    print("%s License is %s" % (dirname, 'BSD'))
                    license = 'BSD'
                    break
                elif 'ISC ' in line.upper():
                    print("%s License is %s" % (dirname, 'ISC'))
                    license = 'ISC'
                    break
                elif '\"ISC\"' in line.upper():
                    print("%s License is %s" % (dirname, 'ISC'))
                    license = 'ISC'
                    break
                elif 'LGPL ' in line.upper():
                    print("%s License is %s" % (dirname, 'LGPL'))
                    license = 'LGPL'
                    break
                else:
                    continue
            print()
        except FileNotFoundError:
            print('无法打开指定的文件!', license_path)
        except LookupError:
            print('指定了未知的编码!', license_path)
        except UnicodeDecodeError:
            print('读取文件时解码错误!', license_path)
        except Exception:
            # print('读取文件时解码错误!', license_path)
            print('str(Exception):\t', str(Exception))
            # print 'str(e):\t\t', str(e)
        else:
            f.close()

        if(license == ''):
            print('----------Not found')
        else:
            return license
    

def main():
    dir = "C:/node_modules/"
    cdirs = os.listdir(dir)
    outfile = open('C:/desktop/新建文件夹/license.csv', "w+", encoding='utf-8')
    for cdir in cdirs:
        # print(dir+cdir)
        if cdir == ".bin":
            continue
        else:
            license = parse_license(cdir, dir+cdir)
            outfile.writelines("%s %s %s %s" % (cdir, ',', license, '\n'))

    outfile.close()

if __name__ == '__main__':
    main()
