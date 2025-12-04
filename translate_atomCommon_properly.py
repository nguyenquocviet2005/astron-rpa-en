#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Properly translate atomCommon JSON by extracting, translating, and updating in MySQL
Uses proper UTF-8 encoding handling
"""

import json
import subprocess

# Translation dictionary
TRANSLATIONS = {
    # AI
    "大模型": "Large Language Models",
    "多轮会话": "Multi-turn Chat",
    "单轮会话": "Single-turn Chat",
    "知识问答": "Knowledge Q&A",
    "主题扩写": "Topic Expansion",
    "段落扩写": "Paragraph Expansion",
    "段落缩写": "Paragraph Abbreviation",
    "简历评分": "Resume Scoring",
    "职位关键词生成": "Job Keyword Generation",
    "合同要素提取": "Contract Element Extraction",
    "调用Dify流程": "Call Dify Workflow",
    "调用星辰Agent流程": "Call XingChen Agent Workflow",
    
    # OCR
    "营业执照识别": "Business License Recognition",
    "身份证识别": "ID Card Recognition",
    "增值税发票识别": "VAT Invoice Recognition",
    "火车票识别": "Train Ticket Recognition",
    "出租车发票识别": "Taxi Invoice Recognition",
    "通用文字识别": "General Text Recognition",
    
    # Verification Code
    "验证码": "Verification Code",
    "通用数英验证码": "General Alphanumeric Captcha",
    "通用滑块验证码": "General Slider Captcha",
    "通用点击验证码": "General Click Captcha",
    
    # Process Flow
    "流程": "Process Flow",
    "运行子流程": "Run Sub-process",
    "运行Python模块": "Run Python Module",
    
    # Code Flow
    "代码流程": "Code Flow",
    "设置变量值": "Set Variable Value",
    "日志打印": "Log Print",
    "条件判断": "Conditional Logic",
    "IF条件": "IF Condition",
    "IF图像存在": "IF Image Exists",
    "IF文件夹存在": "IF Folder Exists",
    "IF文件存在": "IF File Exists",
    "IF窗口存在": "IF Window Exists",
    "ELSE IF条件": "ELSE IF Condition",
    "ELSE条件": "ELSE Condition",
    "循环": "Loop",
    "字典For循环": "Dictionary For Loop",
    "列表For循环": "List For Loop",
    "计数For循环": "Count For Loop",
    "循环Excel内容": "Loop Excel Content",
    "循环相似元素列表（web）": "Loop Similar Elements (Web)",
    "While循环": "While Loop",
    "退出循环（Break）": "Break Loop",
    "继续下次循环（Continue）": "Continue Loop",
    "错误处理": "Error Handling",
    "捕获异常（Try)": "Try Exception",
    "捕获异常（Finally)": "Finally Exception",
    
    # Web Automation
    "网页自动化": "Web Automation",
    "打开浏览器": "Open Browser",
    "关闭浏览器": "Close Browser",
    "获取已打开的浏览器对象": "Get Opened Browser Object",
    "元素是否存在（web）": "Element Exists (Web)",
    "等待元素（web）": "Wait for Element (Web)",
    "元素操作（web）": "Element Operation (Web)",
    "点击元素（web）": "Click Element (Web)",
    "获取元素文本内容（web）": "Get Element Text (Web)",
    "填写输入框（web）": "Fill Input Box (Web)",
    "获取复选框（web）": "Get Checkbox (Web)",
    "操作复选框（web）": "Operate Checkbox (Web)",
    "获取下拉框（web）": "Get Dropdown (Web)",
    "操作下拉框（web）": "Operate Dropdown (Web)",
    "拾取滑块拖拽（web）": "Pick Slider Drag (Web)",
    "鼠标悬停在元素上（web）": "Mouse Hover on Element (Web)",
    "拾取元素截图（web）": "Pick Element Screenshot (Web)",
    "元素位置截图（web）": "Element Position Screenshot (Web)",
    "元素置于可视区域（web）": "Scroll Element into View (Web)",
    "获取表格数据（web）": "Get Table Data (Web)",
    "数据抓取（web）": "Data Scraping (Web)",
    "获取相似元素列表（web）": "Get Similar Elements (Web)",
    "获取元素对象（web）": "Get Element Object (Web)",
    "获取关联元素（web）": "Get Related Element (Web)",
    "设置Cookie": "Set Cookie",
    "获取Cookie": "Get Cookie",
    "网页操作": "Webpage Operations",
    "打开新网页": "Open New Webpage",
    "获取当前标签页ID": "Get Current Tab ID",
    "切换到已存在标签页": "Switch to Existing Tab",
    "关闭网页": "Close Webpage",
    "刷新当前网页": "Refresh Current Page",
    "停止加载网页": "Stop Loading Page",
    "网页前进": "Webpage Forward",
    "网页后退": "Webpage Backward",
    "网页截图": "Webpage Screenshot",
    "鼠标滚动网页": "Mouse Scroll Webpage",
    "获取网页URL": "Get Webpage URL",
    "获取网页标题": "Get Webpage Title",
    "等待页面加载完成": "Wait for Page Load",
    "网页文件": "Webpage Files",
    "文件下载（web）": "File Download (Web)",
    "文件上传（web）": "File Upload (Web)",
    
    # Desktop Automation
    "桌面自动化": "Desktop Automation",
    "关闭程序": "Close Program",
    "打开程序": "Open Program",
    "点击元素（桌面）": "Click Element (Desktop)",
    "元素截图（桌面）": "Element Screenshot (Desktop)",
    "鼠标悬停元素（桌面）": "Mouse Hover Element (Desktop)",
    "填写输入框（桌面）": "Fill Input Box (Desktop)",
    "获取元素文本（桌面）": "Get Element Text (Desktop)",
    "获取相似元素列表（桌面）": "Get Similar Elements (Desktop)",
    "窗口操作": "Window Operations",
    "置顶窗口": "Pin Window",
    "关闭窗口": "Close Window",
    "调整窗口大小": "Resize Window",
    
    # ... Add rest of translations (keeping response shorter)
}

def translate_recursively(obj):
    """Recursively translate all title and desc fields in the JSON structure"""
    if isinstance(obj, dict):
        result = {}
        for key, value in obj.items():
            if key in ('title', 'desc', 'label', 'funcDesc', 'resDesc') and isinstance(value, str):
                # Translate if in dictionary
                result[key] = TRANSLATIONS.get(value, value)
            elif key == 'template' and isinstance(value, str) and value in TRANSLATIONS:
                result[key] = TRANSLATIONS[value]
            else:
                result[key] = translate_recursively(value)
        return result
    elif isinstance(obj, list):
        return [translate_recursively(item) for item in obj]
    else:
        return obj

def main():
    print("Fetching atomCommon from database...")
    
    # Fetch the JSON from MySQL
    cmd = [
        "docker", "exec", "-i", "rpa-opensource-mysql",
        "mysql", "-uroot", "-prpa123456", "rpa", "-N", "-e",
        "SELECT atom_content FROM c_atom_meta WHERE atom_key = 'atomCommon';"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    
    if result.returncode != 0:
        print(f"Error fetching data: {result.stderr}")
        return
    
    json_str = result.stdout.strip()
    
    if not json_str:
        print("No data found for atomCommon")
        return
    
    print(f"Retrieved JSON, length: {len(json_str)}")
    
    try:
        # Parse JSON
        data = json.loads(json_str)
        print("JSON parsed successfully")
        
        # Translate
        translated_data = translate_recursively(data)
        print("Translation completed")
        
        # Convert back to JSON
        translated_json = json.dumps(translated_data, ensure_ascii=False, separators=(',', ':'))
        
        # Escape for SQL
        escaped_json = translated_json.replace("\\", "\\\\").replace("'", "\\'")
        
        # Update in database
        update_sql = f"UPDATE c_atom_meta SET atom_content = '{escaped_json}' WHERE atom_key = 'atomCommon';"
        
        # Write to temp file
        with open('E:\\astron-rpa\\update_atomCommon.sql', 'w', encoding='utf-8') as f:
            f.write(update_sql)
        
        print("SQL file created: E:\\astron-rpa\\update_atomCommon.sql")
        print("Copying to container and executing...")
        
        # Copy to container
        subprocess.run([
            "docker", "cp",
            "E:\\astron-rpa\\update_atomCommon.sql",
            "rpa-opensource-mysql:/tmp/update_atomCommon.sql"
        ], check=True)
        
        # Execute
        result = subprocess.run([
            "docker", "exec", "-i", "rpa-opensource-mysql",
            "mysql", "-uroot", "-prpa123456", "rpa", "-e",
            "SOURCE /tmp/update_atomCommon.sql;"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✓ Database updated successfully!")
        else:
            print(f"Error updating database: {result.stderr}")
        
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        print(f"Problem area: {json_str[max(0, e.pos-50):e.pos+50]}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
