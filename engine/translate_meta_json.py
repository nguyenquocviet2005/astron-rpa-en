#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch translate all meta.json files in engine/components/astronverse-*/
"""

import json
import os
import glob
from pathlib import Path

# Reuse the same translation dictionary
TRANSLATIONS = {
    # (same as the previous script - I'll just reference the key translations)
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
    
    # Browser element operations
    "浏览器对象": "Browser Object",
    "元素拾取": "Pick Element",
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
    
    # Common field translations
    "浏览器对象": "Browser Object",
    "选择指定的网页元素所在的浏览器对象": "Select the browser object where the specified web element is located",
    "元素拾取": "Pick Element",
    "拾取需要等待的网页元素": "Pick the web element to wait for",
    "等待类型": "Wait Type",
    "等待出现或者等待消失": "Wait for appearance or disappearance",
    "等待元素出现": "Wait for Element to Appear",
    "等待元素消失": "Wait for Element to Disappear",
    "等待元素出现时间（秒）": "Wait Time for Element (seconds)",
    "超过该时间停止等待": "Stop waiting after this time",
    "等待结果": "Wait Result",
    "输出元素是否出现/消失，出现/消失为true，反之为false": "Output whether element appeared/disappeared, true if appeared/disappeared, false otherwise",
    
    "拾取元素": "Pick Element",
    "拾取需要操作的元素信息": "Pick the element information to operate on",
    "模拟人工点击": "Simulate Manual Click",
    "模拟人工点击是模拟人为操作方式点击，否则将根据拾取元素的自动化接口进行点击": "Simulated manual click mimics human operation, otherwise uses automation interface",
    "是": "Yes",
    "否": "No",
    "辅助按键": "Auxiliary Key",
    "在点击时需要按下的键盘功能按键": "Keyboard function key to press while clicking",
    "无": "None",
    "点击键位": "Click Type",
    "选择模拟鼠标点击的方式": "Select the mouse click simulation method",
    "左击": "Left Click",
    "双击": "Double Click",
    "右击": "Right Click",
    
    "拾取输入框": "Pick Input Box",
    "拾取需要填写内容的输入框元素": "Pick the input box element to fill",
    "模拟人工输入": "Simulate Manual Input",
    "模拟人工输入是模拟人为操作方式输入，否则将根据元素的自动化接口进行输入": "Simulated manual input mimics human operation, otherwise uses automation interface",
    "输入类型": "Input Type",
    "选择填写输入框的方式": "Select the method to fill the input box",
    "键盘输入": "Keyboard Input",
    "剪贴板": "Clipboard",
    "输入内容": "Input Content",
    "填写输入框的内容": "Content to fill in the input box",
    "焦点睡眠时间": "Focus Sleep Time",
    "焦点停顿时间(ms)": "Focus pause time (ms)",
    "按键输入间隔": "Key Input Interval",
    "输入内容输入的时间间隔(s)": "Time interval between input content (s)",
    "追加输入": "Append Input",
    "是否对输入框进行追加输入": "Whether to append input to the input box",
    "追加": "Append",
    "覆盖": "Overwrite",
    "用户输入内容": "User Input Content",
    
    "悬停元素拾取": "Pick Element to Hover",
    "拾取鼠标要悬停的元素": "Pick the element for mouse to hover over",
    
    "截图保存路径": "Screenshot Save Path",
    "文件夹路径": "Folder Path",
    "图片名称": "Image Name",
    "携带后缀的名称比如图片.jpg": "Name with extension, e.g., image.jpg",
    "截图文件路径": "Screenshot File Path",
    
    "滚动目标": "Scroll Target",
    "选择网页窗口滚动条或指定网页上某个滚动条元素": "Select webpage window scrollbar or a specific scrollbar element",
    "窗口": "Window",
    "自定义目标": "Custom Target",
    "拾取滚动条": "Pick Scrollbar",
    "拾取需要在网页上滚动操作的滚动条元素": "Pick scrollbar element for scrolling on webpage",
    "滚动方向": "Scroll Direction",
    "横向": "Horizontal",
    "纵向": "Vertical",
    "横向滚动位置": "Horizontal Scroll Position",
    "最左": "Leftmost",
    "最右": "Rightmost",
    "自定义": "Custom",
    "横向自定义滚动距离": "Custom Horizontal Scroll Distance",
    "单位为屏幕的分辨率像素px，一般为0-9999之间的数值": "Unit is screen resolution pixels (px), usually between 0-9999",
    "纵向滚动位置": "Vertical Scroll Position",
    "顶部": "Top",
    "底部": "Bottom",
    "纵向自定义滚动距离": "Custom Vertical Scroll Distance",
    
    "拾取可视目标": "Pick Visible Target",
    "拾取需要可视的目标元素": "Pick the target element to make visible",
    
    "相似元素拾取": "Pick Similar Elements",
    "在网页上拾取不同位置的两个相似元素": "Pick two similar elements at different positions on the webpage",
    "元素操作": "Element Operation",
    "获取元素对象": "Get Element Object",
    "获取元素文本内容": "Get Element Text",
    "获取元素源代码": "Get Element HTML",
    "获取元素值": "Get Element Value",
    "获取元素链接地址": "Get Element Link",
    "获取元素属性": "Get Element Attribute",
    "获取元素位置": "Get Element Position",
    "获取元素选中状态": "Get Element Selection Status",
    "属性名称": "Attribute Name",
    "元素信息": "Element Information",
    
    "起始位置": "Start Position",
    "下标位置从0开始": "Index position starts from 0",
    "结束位置": "End Position",
    "下标位置从0开始,-1代表循环至最后一个元素": "Index starts from 0, -1 means loop to last element",
    "循环项位置": "Loop Item Position",
    "默认变量可修改，用于遍历列表的变量索引数值": "Default variable can be modified, index value for list iteration",
    "循环项": "Loop Item",
    "默认变量可修改，用于遍历列表的变量": "Default variable can be modified, variable for list iteration",
    
    "选择要获取文本的元素所在的浏览器对象": "Select browser object where the element is located",
    "选择要获取文本的元素位置": "Select element position to get text from",
    "输出变量": "Output Variable",
    "输出获取到的当前网页标题字符串": "Output the current page title string",
    
    # More common translations
    "打开浏览器": "Open Browser",
    "关闭浏览器": "Close Browser",
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
}


def translate_text(text):
    """Translate Chinese text to English"""
    if not isinstance(text, str):
        return text
    
    # Direct lookup
    if text in TRANSLATIONS:
        return TRANSLATIONS[text]
    
    # Partial replacement
    result = text
    for cn, en in sorted(TRANSLATIONS.items(), key=lambda x: -len(x[0])):
        if cn in result:
            result = result.replace(cn, en)
    
    return result if result != text else text


def translate_json_recursive(obj):
    """Recursively translate JSON structure"""
    if isinstance(obj, dict):
        translated = {}
        for key, value in obj.items():
            # Translate specific fields
            if key in ['title', 'comment', 'tip', 'label', 'name']:
                new_value = translate_text(value) if isinstance(value, str) else translate_json_recursive(value)
            else:
                new_value = translate_json_recursive(value)
            translated[key] = new_value
        return translated
    
    elif isinstance(obj, list):
        return [translate_json_recursive(item) for item in obj]
    
    else:
        return obj


def main():
    # Find all meta.json files
    components_dir = Path(r'e:\astron-rpa\engine\components')
    meta_files = list(components_dir.glob('astronverse-*/meta.json'))
    
    print(f"Found {len(meta_files)} meta.json files to translate\n")
    
    translated_count = 0
    for meta_file in sorted(meta_files):
        component_name = meta_file.parent.name
        print(f"Processing: {component_name}/meta.json")
        
        try:
            # Read the meta.json file
            with open(meta_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Translate
            translated_data = translate_json_recursive(data)
            
            # Write back
            with open(meta_file, 'w', encoding='utf-8') as f:
                json.dump(translated_data, f, ensure_ascii=False, indent=2)
            
            print(f"  ✓ Translated {component_name}")
            translated_count += 1
            
        except Exception as e:
            print(f"  ✗ ERROR in {component_name}: {e}")
    
    print(f"\n✓ Successfully translated {translated_count}/{len(meta_files)} meta.json files")


if __name__ == '__main__':
    main()
