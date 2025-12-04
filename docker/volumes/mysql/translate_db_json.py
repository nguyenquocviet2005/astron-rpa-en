#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Properly translate atomCommon JSON from init_c_atom_meta_data.sql
Uses Python's JSON parser to handle UTF-8 encoding correctly
"""

import json
import re
import sys

# Translation dictionary for common terms
TRANSLATIONS = {
    # AI / Large Language Models
    "AI": "AI",
    "大模型": "Large Language Models",
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
    "网页自动化": "Web Automation",
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
    "获取相似元素列表（web）": "Get Similar Elements List (Web)",
    "循环相似元素列表（web）": "Loop Through Similar Elements (Web)",
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
    "元素是否存在（web）": "Check Element Exists (Web)",
    "Js脚本": "JavaScript Script",
    "打开新网页": "Open New Page",
    "切换到已存在标签页": "Switch to Existing Tab",
    "等待页面加载完成": "Wait for Page Load",
    "停止加载网页": "Stop Page Loading",
    "刷新当前网页": "Refresh Current Page",
    "关闭网页": "Close Page",
    "网页截图": "Page Screenshot",
    "网页前进": "Page Forward",
    "网页后退": "Page Backward",
    "获取已打开的浏览器对象": "Get Opened Browser Object",
    "获取网页URL": "Get Page URL",
    "获取网页标题": "Get Page Title",
    "获取当前标签页ID": "Get Current Tab ID",
    "文件下载（web）": "File Download (Web)",
    "文件上传（web）": "File Upload (Web)",
    "设置Cookie": "Set Cookie",
    "获取Cookie": "Get Cookie",
    
    # Database
    "数据库": "Database",
    "数据库连接": "Database Connection",
    "执行SQL": "Execute SQL",
    "查询数据": "Query Data",
    "插入数据": "Insert Data",
    "更新数据": "Update Data",
    "删除数据": "Delete Data",
    "关闭连接": "Close Connection",
    
    # Data Processing
    "数据处理": "Data Processing",
    "数据转换": "Data Conversion",
    "数据清洗": "Data Cleaning",
    "数据合并": "Data Merging",
    "数据拆分": "Data Splitting",
    "数据过滤": "Data Filtering",
    "数据排序": "Data Sorting",
    "数据去重": "Data Deduplication",
    
    # Dialog
    "对话框": "Dialog",
    "提示框": "Alert",
    "确认框": "Confirm",
    "输入框": "Input Box",
    "文件选择": "File Selection",
    "文件夹选择": "Folder Selection",
    
    # Email
    "邮件": "Email",
    "发送邮件": "Send Email",
    "接收邮件": "Receive Email",
    "读取邮件": "Read Email",
    "删除邮件": "Delete Email",
    "邮件附件": "Email Attachment",
    
    # Encryption
    "加密": "Encryption",
    "解密": "Decryption",
    "MD5加密": "MD5 Encryption",
    "SHA加密": "SHA Encryption",
    "AES加密": "AES Encryption",
    "RSA加密": "RSA Encryption",
    "Base64编码": "Base64 Encoding",
    "Base64解码": "Base64 Decoding",
    
    # Excel
    "Excel": "Excel",
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
    
    # Input
    "输入": "Input",
    "键盘输入": "Keyboard Input",
    "鼠标点击": "Mouse Click",
    "鼠标移动": "Mouse Move",
    "鼠标滚动": "Mouse Scroll",
    "组合键": "Hotkey",
    "模拟输入": "Simulated Input",
    
    # Network
    "网络": "Network",
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
    
    # OpenAPI
    "开放接口": "Open API",
    "API调用": "API Call",
    "接口测试": "API Testing",
    
    # PDF
    "PDF": "PDF",
    "读取PDF": "Read PDF",
    "提取文本": "Extract Text",
    "提取图片": "Extract Images",
    "PDF转换": "PDF Conversion",
    "合并PDF": "Merge PDF",
    "拆分PDF": "Split PDF",
    "PDF加密": "Encrypt PDF",
    "PDF解密": "Decrypt PDF",
    
    # Report
    "报表": "Report",
    "生成报表": "Generate Report",
    "导出报表": "Export Report",
    
    # Script
    "脚本": "Script",
    "Python脚本": "Python Script",
    "执行脚本": "Execute Script",
    "JavaScript脚本": "JavaScript Script",
    
    # Software
    "软件": "Software",
    "打开软件": "Open Software",
    "关闭软件": "Close Software",
    "软件自动化": "Software Automation",
    
    # System
    "系统": "System",
    "系统信息": "System Information",
    "环境变量": "Environment Variables",
    "注册表": "Registry",
    "命令行": "Command Line",
    "PowerShell": "PowerShell",
    "执行命令": "Execute Command",
    "文件操作": "File Operations",
    "文件夹操作": "Folder Operations",
    "复制文件": "Copy File",
    "移动文件": "Move File",
    "删除文件": "Delete File",
    "重命名文件": "Rename File",
    "创建文件夹": "Create Folder",
    "删除文件夹": "Delete Folder",
    "压缩文件": "Compress File",
    "解压文件": "Extract File",
    
    # Verify Code
    "验证码": "Verification Code",
    "验证码识别": "Verify Code Recognition",
    "图片验证码": "Image Verification Code",
    
    # Vision
    "视觉": "Vision",
    "图像识别": "Image Recognition",
    "OCR识别": "OCR Recognition",
    "文字识别": "Text Recognition",
    "图像查找": "Image Search",
    "颜色识别": "Color Recognition",
    
    # Window
    "窗口": "Window",
    "窗口操作": "Window Operations",
    "激活窗口": "Activate Window",
    "关闭窗口": "Close Window",
    "最大化窗口": "Maximize Window",
    "最小化窗口": "Minimize Window",
    "还原窗口": "Restore Window",
    "移动窗口": "Move Window",
    "调整窗口大小": "Resize Window",
    "获取窗口信息": "Get Window Info",
    
    # Win Element
    "桌面元素": "Desktop Element",
    "元素识别": "Element Recognition",
    "元素点击": "Click Element",
    "元素输入": "Input Element",
    "获取元素属性": "Get Element Attribute",
    "设置元素属性": "Set Element Attribute",
    
    # Word
    "Word": "Word",
    "打开Word": "Open Word",
    "关闭Word": "Close Word",
    "读取文档": "Read Document",
    "写入文档": "Write Document",
    "保存文档": "Save Document",
    "另存为文档": "Save Document As",
    
    # Enterprise
    "企业应用": "Enterprise Applications",
    "企业微信": "WeChat Work",
    "钉钉": "DingTalk",
    "飞书": "Feishu",
    
    # Flow Control
    "流程控制": "Flow Control",
    "条件判断": "Conditional",
    "循环": "Loop",
    "跳出循环": "Break Loop",
    "继续循环": "Continue Loop",
    "等待": "Wait",
    "延时": "Delay",
    "重试": "Retry",
    "异常处理": "Exception Handling",
    "日志记录": "Logging",
    
    # Variables
    "变量": "Variables",
    "赋值": "Assignment",
    "变量类型": "Variable Type",
    "字符串": "String",
    "数字": "Number",
    "布尔值": "Boolean",
    "列表": "List",
    "字典": "Dictionary",
    "对象": "Object",
}


def translate_text(text):
    """Translate Chinese text to English using the translation dictionary"""
    if not isinstance(text, str):
        return text
    
    # Direct lookup first
    if text in TRANSLATIONS:
        return TRANSLATIONS[text]
    
    # Try partial matches for compound phrases
    for cn, en in TRANSLATIONS.items():
        if cn in text:
            text = text.replace(cn, en)
    
    return text


def translate_json_recursive(obj):
    """Recursively translate all Chinese text in a JSON structure"""
    if isinstance(obj, dict):
        translated = {}
        for key, value in obj.items():
            # Translate keys if needed (usually not)
            new_key = key
            
            # Translate specific fields
            if key in ['title', 'comment', 'tip', 'label', 'name']:
                new_value = translate_text(value) if isinstance(value, str) else translate_json_recursive(value)
            else:
                new_value = translate_json_recursive(value)
            
            translated[new_key] = new_value
        return translated
    
    elif isinstance(obj, list):
        return [translate_json_recursive(item) for item in obj]
    
    elif isinstance(obj, str):
        return obj  # Don't translate strings outside specific fields
    
    else:
        return obj


def main():
    print("Reading init_c_atom_meta_data.sql...")
    
    # Read the SQL file
    with open(r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8') as f:
        sql_content = f.read()
    
    # Extract the JSON from the INSERT statement using regex
    # Pattern: INSERT INTO `c_atom_meta` VALUES (14,'root','atomCommon','<JSON>',...)
    # The JSON ends with }' followed by a comma and more fields
    pattern = r"INSERT INTO `c_atom_meta` VALUES \(14,'root','atomCommon','(.+?)',\d+,"
    
    match = re.search(pattern, sql_content, re.DOTALL)
    if not match:
        print("ERROR: Could not find atomCommon INSERT statement in SQL file")
        sys.exit(1)
    
    json_str_escaped = match.group(1)
    
    # Unescape the JSON string properly
    # In SQL, strings are escaped with backslashes, so:
    # - \" becomes "
    # - \\ becomes \
    # But we need to be careful about the order
    json_str = json_str_escaped.replace('\\\\', '\x00').replace('\\"', '"').replace('\x00', '\\')
    
    print(f"Extracted JSON length: {len(json_str)} characters")
    
    # Parse the JSON
    try:
        atom_data = json.loads(json_str)
        print("Successfully parsed JSON")
    except json.JSONDecodeError as e:
        print(f"ERROR: Failed to parse JSON: {e}")
        sys.exit(1)
    
    # Translate the JSON
    print("Translating JSON content...")
    translated_data = translate_json_recursive(atom_data)
    
    # Convert back to JSON string
    translated_json_str = json.dumps(translated_data, ensure_ascii=False, separators=(',', ':'))
    
    # Escape for SQL (replace " with \" and \ with \\)
    escaped_json = translated_json_str.replace('\\', '\\\\').replace('"', '\\"')
    
    # Generate new SQL INSERT statement (preserving the rest of the fields)
    # Get the rest of the original SQL after the JSON
    rest_pattern = r"INSERT INTO `c_atom_meta` VALUES \(14,'root','atomCommon','.+?'(,\d+,.+?)\);"
    rest_match = re.search(rest_pattern, sql_content, re.DOTALL)
    
    if rest_match:
        rest_of_statement = rest_match.group(1)
    else:
        # Fallback to default values
        rest_of_statement = ",0,'1','2025-10-14 09:14:46',1,'2025-10-14 09:14:46','1.0.1',NULL,'1000001')"
    
    new_sql = f"""INSERT INTO `c_atom_meta` VALUES (14,'root','atomCommon','{escaped_json}'{rest_of_statement};"""
    
    # Write to new file
    output_file = r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data_translated.sql'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_sql)
    
    print(f"Successfully wrote translated SQL to: {output_file}")
    print(f"Original JSON size: {len(json_str)} bytes")
    print(f"Translated JSON size: {len(translated_json_str)} bytes")
    
    # Also save the translated JSON for inspection
    json_output_file = r'e:\astron-rpa\docker\volumes\mysql\atomCommon_translated.json'
    with open(json_output_file, 'w', encoding='utf-8') as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=2)
    
    print(f"Also saved pretty JSON to: {json_output_file}")


if __name__ == '__main__':
    main()
