#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Properly translate atomCommon JSON from atomCommon_original.json
Uses Python's JSON parser to handle UTF-8 encoding correctly
"""

import json
import re
import sys

# Comprehensive translation dictionary
TRANSLATIONS = {
    # Top-level categories
    "AI": "AI",
    "大模型": "Large Language Models",
    "网页自动化": "Web Automation",
    "数据库": "Database",
    "数据处理": "Data Processing",
    "对话框": "Dialog",
    "邮件": "Email",
    "加密": "Encryption",
    "Excel": "Excel",
    "输入": "Input",
    "网络": "Network",
    "开放接口": "Open API",
    "PDF": "PDF",
    "报表": "Report",
    "脚本": "Script",
    "软件": "Software",
    "系统": "System",
    "验证码": "Verification Code",
    "视觉": "Vision",
    "窗口": "Window",
    "桌面元素": "Desktop Element",
    "Word": "Word",
    "企业应用": "Enterprise Applications",
    "流程控制": "Flow Control",
    
    # AI subcategories
    "多轮会话": "Multi-turn Conversation",
    "单轮会话": "Single-turn Conversation",
    "知识问答": "Knowledge Q&A",
    "主题扩写": "Topic Expansion",
    "段落扩写": "Paragraph Expansion",
    "段落缩写": "Paragraph Abbreviation",
    "简历评分": "Resume Scoring",
    "职位关键词生成": "Job Keyword Generation",
    "合同要素提取": "Contract Element Extraction",
    "调用Dify流": "Call Dify Flow",
    
    # Browser Automation
    "浏览器": "Browser",
    "打开浏览器": "Open Browser",
    "关闭浏览器": "Close Browser",
    "网页元素": "Web Element",
    "等待元素（web）": "Wait for Element (Web)",
    "点击元素（web）": "Click Element (Web)",
    "填写输入框（web）": "Fill Input Box (Web)",
    "鼠标悬停在元素上（web）": "Hover Over Element (Web)",
    "拾取元素截图（web）": "Capture Element Screenshot (Web)",
    "元素位置截图（web）": "Element Position Screenshot (Web)",
    "鼠标滚动网页": "Scroll Webpage",
    "元素置于可视区域（web）": "Scroll Element into View (Web)",
    "获取相似元素列表（web）": "Get Similar Elements (Web)",
    "循环相似元素列表（web）": "Loop Similar Elements (Web)",
    "获取元素文本内容（web）": "Get Element Text (Web)",
    "拾取滑块拖拽（web）": "Drag Slider (Web)",
    "获取下拉框（web）": "Get Dropdown (Web)",
    "获取复选框（web）": "Get Checkbox (Web)",
    "操作下拉框（web）": "Operate Dropdown (Web)",
    "操作复选框（web）": "Operate Checkbox (Web)",
    "元素操作（web）": "Element Operations (Web)",
    "获取表格数据（web）": "Get Table Data (Web)",
    "数据抓取（web）": "Data Scraping (Web)",
    "获取元素对象（web）": "Get Element Object (Web)",
    "获取关联元素（web）": "Get Related Elements (Web)",
    "元素是否存在（web）": "Element Exists (Web)",
    "Js脚本": "JavaScript Script",
    "打开新网页": "Open New Page",
    "切换到已存在标签页": "Switch to Existing Tab",
    "等待页面加载完成": "Wait for Page Load",
    "停止加载网页": "Stop Page Loading",
    "刷新当前网页": "Refresh Page",
    "关闭网页": "Close Page",
    "网页截图": "Page Screenshot",
    "网页前进": "Page Forward",
    "网页后退": "Page Backward",
    "获取已打开的浏览器对象": "Get Opened Browser",
    "获取网页URL": "Get Page URL",
    "获取网页标题": "Get Page Title",
    "获取当前标签页ID": "Get Current Tab ID",
    "文件下载（web）": "File Download (Web)",
    "文件上传（web）": "File Upload (Web)",
    "设置Cookie": "Set Cookie",
    "获取Cookie": "Get Cookie",
    
    # Database operations
    "数据库连接": "Database Connection",
    "执行SQL": "Execute SQL",
    "查询数据": "Query Data",
    "插入数据": "Insert Data",
    "更新数据": "Update Data",
    "删除数据": "Delete Data",
    "关闭连接": "Close Connection",
    "MySQL": "MySQL",
    "SQL Server": "SQL Server",
    "Oracle": "Oracle",
    "PostgreSQL": "PostgreSQL",
    "SQLite": "SQLite",
    
    # Excel operations
    "打开Excel": "Open Excel",
    "关闭Excel": "Close Excel",
    "读取单元格": "Read Cell",
    "写入单元格": "Write Cell",
    "读取区域": "Read Range",
    "写入区域": "Write Range",
    "插入行": "Insert Row",
    "删除行": "Delete Row",
    "插入列": "Insert Column",
    "删除列": "Delete Column",
    "保存Excel": "Save Excel",
    "另存为": "Save As",
    "获取工作表": "Get Worksheet",
    "新建工作表": "Create Worksheet",
    "删除工作表": "Delete Worksheet",
    "复制工作表": "Copy Worksheet",
    "重命名工作表": "Rename Worksheet",
    "获取工作表列表": "Get Worksheet List",
    "激活工作表": "Activate Worksheet",
    "读取Excel文件": "Read Excel File",
    "写入Excel文件": "Write Excel File",
    "Excel另存为": "Excel Save As",
    "设置单元格样式": "Set Cell Style",
    "合并单元格": "Merge Cells",
    "取消合并单元格": "Unmerge Cells",
    
    # System operations
    "文件操作": "File Operations",
    "文件夹操作": "Folder Operations",
    "复制文件": "Copy File",
    "移动文件": "Move File",
    "删除文件": "Delete File",
    "重命名文件": "Rename File",
    "创建文件夹": "Create Folder",
    "删除文件夹": "Delete Folder",
    "压缩文件": "Compress Files",
    "解压文件": "Extract Files",
    "系统信息": "System Information",
    "环境变量": "Environment Variables",
    "注册表": "Registry",
    "命令行": "Command Line",
    "执行命令": "Execute Command",
    "PowerShell": "PowerShell",
    "获取文件列表": "Get File List",
    "文件是否存在": "File Exists",
    "文件夹是否存在": "Folder Exists",
    "获取文件属性": "Get File Attributes",
    "设置文件属性": "Set File Attributes",
    "读取文本文件": "Read Text File",
    "写入文本文件": "Write Text File",
    "追加文本文件": "Append Text File",
    "读取CSV文件": "Read CSV File",
    "写入CSV文件": "Write CSV File",
    "读取JSON文件": "Read JSON File",
    "写入JSON文件": "Write JSON File",
    "读取XML文件": "Read XML File",
    "写入XML文件": "Write XML File",
    "获取当前路径": "Get Current Path",
    "切换工作目录": "Change Directory",
    "打开文件夹": "Open Folder",
    "打开文件": "Open File",
    
    # Input operations
    "键盘输入": "Keyboard Input",
    "鼠标点击": "Mouse Click",
    "鼠标移动": "Mouse Move",
    "鼠标滚动": "Mouse Scroll",
    "组合键": "Hotkey",
    "模拟输入": "Simulated Input",
    "发送按键": "Send Keys",
    "等待按键": "Wait for Key",
    "鼠标左键": "Left Click",
    "鼠标右键": "Right Click",
    "鼠标双击": "Double Click",
    "鼠标拖拽": "Mouse Drag",
    "获取鼠标位置": "Get Mouse Position",
    "设置鼠标位置": "Set Mouse Position",
    
    # Window operations
    "窗口操作": "Window Operations",
    "激活窗口": "Activate Window",
    "关闭窗口": "Close Window",
    "最大化窗口": "Maximize Window",
    "最小化窗口": "Minimize Window",
    "还原窗口": "Restore Window",
    "移动窗口": "Move Window",
    "调整窗口大小": "Resize Window",
    "获取窗口信息": "Get Window Info",
    "获取窗口列表": "Get Window List",
    "窗口是否存在": "Window Exists",
    "等待窗口出现": "Wait for Window",
    "等待窗口消失": "Wait for Window Disappear",
    "获取窗口标题": "Get Window Title",
    "设置窗口标题": "Set Window Title",
    "置顶窗口": "Set Window Topmost",
    "取消置顶": "Unset Window Topmost",
    
    # Dialog operations
    "提示框": "Alert",
    "确认框": "Confirm",
    "输入框": "Input Box",
    "文件选择": "File Selection",
    "文件夹选择": "Folder Selection",
    "显示消息": "Show Message",
    "显示提示": "Show Alert",
    "显示确认": "Show Confirm",
    "显示输入": "Show Input",
    "选择文件": "Select File",
    "选择文件夹": "Select Folder",
    "颜色选择": "Color Picker",
    
    # Network operations
    "HTTP请求": "HTTP Request",
    "GET请求": "GET Request",
    "POST请求": "POST Request",
    "PUT请求": "PUT Request",
    "DELETE请求": "DELETE Request",
    "下载文件": "Download File",
    "上传文件": "Upload File",
    "FTP连接": "FTP Connection",
    "FTP上传": "FTP Upload",
    "FTP下载": "FTP Download",
    "FTP断开": "FTP Disconnect",
    "网络请求": "Network Request",
    "发送请求": "Send Request",
    "接收响应": "Receive Response",
    "设置请求头": "Set Headers",
    "设置超时": "Set Timeout",
    "设置代理": "Set Proxy",
    
    # Email operations
    "发送邮件": "Send Email",
    "接收邮件": "Receive Email",
    "读取邮件": "Read Email",
    "删除邮件": "Delete Email",
    "邮件附件": "Email Attachment",
    "连接邮箱": "Connect Mailbox",
    "断开邮箱": "Disconnect Mailbox",
    "SMTP": "SMTP",
    "POP3": "POP3",
    "IMAP": "IMAP",
    
    # Vision operations
    "图像识别": "Image Recognition",
    "OCR识别": "OCR Recognition",
    "文字识别": "Text Recognition",
    "图像查找": "Image Search",
    "颜色识别": "Color Recognition",
    "二维码识别": "QR Code Recognition",
    "条形码识别": "Barcode Recognition",
    "屏幕截图": "Screenshot",
    "图像拾取": "Image Capture",
    "图像查找点击": "Find and Click Image",
    "等待图像出现": "Wait for Image",
    "图像是否存在": "Image Exists",
    
    # PDF operations
    "读取PDF": "Read PDF",
    "提取文本": "Extract Text",
    "提取图片": "Extract Images",
    "PDF转换": "PDF Conversion",
    "合并PDF": "Merge PDF",
    "拆分PDF": "Split PDF",
    "PDF加密": "Encrypt PDF",
    "PDF解密": "Decrypt PDF",
    "PDF转Word": "PDF to Word",
    "PDF转Excel": "PDF to Excel",
    "PDF转图片": "PDF to Image",
    
    # Word operations
    "打开Word": "Open Word",
    "关闭Word": "Close Word",
    "读取文档": "Read Document",
    "写入文档": "Write Document",
    "保存文档": "Save Document",
    "另存为文档": "Save Document As",
    "读取段落": "Read Paragraph",
    "写入段落": "Write Paragraph",
    "插入图片": "Insert Image",
    "插入表格": "Insert Table",
    "替换文本": "Replace Text",
    "查找文本": "Find Text",
    
    # Encryption operations
    "MD5加密": "MD5 Encryption",
    "SHA加密": "SHA Encryption",
    "AES加密": "AES Encryption",
    "AES解密": "AES Decryption",
    "RSA加密": "RSA Encryption",
    "RSA解密": "RSA Decryption",
    "Base64编码": "Base64 Encoding",
    "Base64解码": "Base64 Decoding",
    "解密": "Decryption",
    "加密文件": "Encrypt File",
    "解密文件": "Decrypt File",
    
    # Data Processing operations
    "数据转换": "Data Conversion",
    "数据清洗": "Data Cleaning",
    "数据合并": "Data Merging",
    "数据拆分": "Data Splitting",
    "数据过滤": "Data Filtering",
    "数据排序": "Data Sorting",
    "数据去重": "Data Deduplication",
    "数据分组": "Data Grouping",
    "数据聚合": "Data Aggregation",
    "数据透视": "Data Pivot",
    "列表操作": "List Operations",
    "字典操作": "Dictionary Operations",
    "字符串操作": "String Operations",
    "数值运算": "Numeric Operations",
    "日期时间": "Date & Time",
    "正则表达式": "Regular Expression",
    "JSON处理": "JSON Processing",
    "XML处理": "XML Processing",
    "CSV处理": "CSV Processing",
    
    # Flow Control
    "条件判断": "Conditional",
    "循环": "Loop",
    "跳出循环": "Break Loop",
    "继续循环": "Continue Loop",
    "等待": "Wait",
    "延时": "Delay",
    "重试": "Retry",
    "异常处理": "Exception Handling",
    "日志记录": "Logging",
    "抛出异常": "Throw Exception",
    "捕获异常": "Catch Exception",
    "条件分支": "If-Else",
    "多条件分支": "Switch-Case",
    "循环列表": "For Each",
    "条件循环": "While Loop",
    "计数循环": "For Loop",
    "并行执行": "Parallel Execution",
    "串行执行": "Serial Execution",
    
    # Software operations
    "打开软件": "Open Software",
    "关闭软件": "Close Software",
    "软件自动化": "Software Automation",
    "启动程序": "Launch Program",
    "关闭程序": "Close Program",
    "程序是否运行": "Is Program Running",
    "等待程序启动": "Wait for Program",
    "结束进程": "Kill Process",
    "获取进程列表": "Get Process List",
    
    # Enterprise Applications
    "企业微信": "WeChat Work",
    "钉钉": "DingTalk",
    "飞书": "Feishu",
    
    # Report operations
    "生成报表": "Generate Report",
    "导出报表": "Export Report",
    
    # Script operations
    "Python脚本": "Python Script",
    "执行脚本": "Execute Script",
    "JavaScript脚本": "JavaScript Script",
    "运行Python": "Run Python",
    "运行JavaScript": "Run JavaScript",
    "运行命令": "Run Command",
    
    # OpenAPI operations
    "API调用": "API Call",
    "接口测试": "API Testing",
    "REST API": "REST API",
    
    # Desktop Element operations
    "元素识别": "Element Recognition",
    "元素点击": "Click Element",
    "元素输入": "Input Element",
    "获取元素属性": "Get Element Attribute",
    "设置元素属性": "Set Element Attribute",
    "等待元素": "Wait for Element",
    "元素是否存在": "Element Exists",
    "拾取元素": "Pick Element",
    
    # Verification Code
    "验证码识别": "Verify Code Recognition",
    "图片验证码": "Image Verification Code",
    "滑块验证码": "Slider Verification",
    
    # Common terms
    "变量": "Variables",
    "赋值": "Assignment",
    "变量类型": "Variable Type",
    "字符串": "String",
    "数字": "Number",
    "整数": "Integer",
    "浮点数": "Float",
    "布尔值": "Boolean",
    "列表": "List",
    "字典": "Dictionary",
    "对象": "Object",
    "空值": "Null",
    "真": "True",
    "假": "False",
}


def translate_text(text):
    """Translate Chinese text to English using the translation dictionary"""
    if not isinstance(text, str):
        return text
    
    # Direct lookup first
    if text in TRANSLATIONS:
        return TRANSLATIONS[text]
    
    # Try partial matches for compound phrases
    result = text
    for cn, en in sorted(TRANSLATIONS.items(), key=lambda x: -len(x[0])):
        if cn in result and cn != result:  # Don't replace if it's the whole string
            result = result.replace(cn, en)
    
    # If translation happened, return it
    if result != text:
        return result
    
    # Return original text if no translation found
    return text


def translate_json_recursive(obj, path=""):
    """Recursively translate all Chinese text in a JSON structure"""
    if isinstance(obj, dict):
        translated = {}
        for key, value in obj.items():
            new_path = f"{path}.{key}" if path else key
            
            # Translate specific fields
            if key in ['title', 'comment', 'tip', 'label', 'name', 'desc', 'description']:
                new_value = translate_text(value) if isinstance(value, str) else translate_json_recursive(value, new_path)
            else:
                new_value = translate_json_recursive(value, new_path)
            
            translated[key] = new_value
        return translated
    
    elif isinstance(obj, list):
        return [translate_json_recursive(item, f"{path}[{i}]") for i, item in enumerate(obj)]
    
    else:
        return obj


def main():
    print("Reading atomCommon_original.json...")
    
    # Read the extracted JSON file
    with open(r'e:\astron-rpa\docker\volumes\mysql\atomCommon_original.json', 'r', encoding='utf-8-sig') as f:
        atom_data = json.load(f)
    
    print(f"✓ JSON parsed successfully")
    print(f"  Keys: {list(atom_data.keys())}")
    print(f"  Total atom categories: {len(atom_data.get('atomicTree', []))}")
    
    # Translate the JSON
    print("\nTranslating JSON content...")
    translated_data = translate_json_recursive(atom_data)
    
    # Convert back to JSON string
    translated_json_str = json.dumps(translated_data, ensure_ascii=False, separators=(',', ':'))
    
    # Escape for SQL
    # Need to escape: \ becomes \\ and " becomes \" and ' becomes \'
    escaped_json = translated_json_str.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")
    
    # Generate new SQL INSERT statement
    new_sql = f"""INSERT INTO `c_atom_meta` VALUES (14,'root','atomCommon','{escaped_json}',0,'1','2025-10-14 09:14:46',1,'2025-10-14 09:14:46','1.0.1',NULL,'1000001');"""
    
    # Write to new file
    output_file = r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data_translated.sql'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_sql)
    
    print(f"\n✓ Successfully wrote translated SQL to: init_c_atom_meta_data_translated.sql")
    print(f"  Original JSON size: {len(json.dumps(atom_data, ensure_ascii=False))} bytes")
    print(f"  Translated JSON size: {len(translated_json_str)} bytes")
    
    # Also save the translated JSON for inspection
    json_output_file = r'e:\astron-rpa\docker\volumes\mysql\atomCommon_translated.json'
    with open(json_output_file, 'w', encoding='utf-8') as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=2)
    
    print(f"  Also saved pretty JSON to: atomCommon_translated.json")
    
    # Show a sample translation
    if 'atomicTree' in translated_data and len(translated_data['atomicTree']) > 0:
        first_category = translated_data['atomicTree'][0]
        print(f"\n✓ Sample translation:")
        print(f"  Category title: '{first_category.get('title')}'")
        if 'atomics' in first_category and len(first_category['atomics']) > 0:
            first_atom = first_category['atomics'][0]
            print(f"  First atom: '{first_atom.get('title')}'")


if __name__ == '__main__':
    main()
