"""
Script to translate Chinese text in atom config.yaml files to English.
This script translates titles, comments, and tips in all component config files.
"""

import os
import yaml
import re
from pathlib import Path

# Common translations for atom configuration fields
TRANSLATIONS = {
    # Browser/Web related
    "浏览器对象": "Browser Object",
    "浏览器": "Browser",
    "元素拾取": "Element Picker",
    "拾取元素": "Pick Element",
    "拾取输入框": "Pick Input Box",
    "等待元素出现时间（秒）": "Wait Time for Element (seconds)",
    "超过该时间停止等待": "Stop waiting if timeout exceeded",
    "等待类型": "Wait Type",
    "等待出现或者等待消失": "Wait for appearance or disappearance",
    "等待结果": "Wait Result",
    "元素是否存在": "Element Exists",
    "输出元素是否存在，存在为true，不存在为false": "Output whether element exists, true if exists, false otherwise",
    "模拟人工点击": "Simulate Manual Click",
    "模拟人工输入": "Simulate Manual Input",
    "模拟人工操作方式点击，否则将根据拾取元素的自动化接口进行点击": "Simulate manual operation click, otherwise click via automation interface",
    "模拟人为操作方式输入，否则将根据元素的自动化接口进行输入": "Simulate manual operation input, otherwise input via automation interface",
    "辅助按键": "Auxiliary Key",
    "在点击时需要按下的键盘功能按键": "Keyboard function key to press when clicking",
    "点击键位": "Click Button",
    "选择模拟鼠标点击的方式": "Select mouse click simulation method",
    "输入类型": "Input Type",
    "选择填写输入框的方式": "Select input box filling method",
    "输入内容": "Input Content",
    "填写输入框的内容": "Content to fill in the input box",
    "焦点睡眠时间": "Focus Sleep Time",
    "焦点停顿时间(ms)": "Focus pause time (ms)",
    "按键输入间隔": "Key Input Interval",
    "输入内容输入的时间间隔(s)": "Time interval for input content (s)",
    "追加输入": "Append Input",
    "是否对输入框进行追加输入": "Whether to append input to the input box",
    "用户输入内容": "User Input Content",
    
    # General UI terms
    "选择要等待页面所在的浏览器对象": "Select the browser object where the page to wait for is located",
    "拾取需要等待的网页元素": "Pick the web element to wait for",
    "拾取需要操作的元素信息": "Pick the element information to operate on",
    "选择指定的网页元素所在的浏览器对象": "Select the browser object where the specified web element is located",
    
    # Screenshot related
    "截图保存路径": "Screenshot Save Path",
    "文件夹路径": "Folder Path",
    "图片名称": "Image Name",
    "携带后缀的名称比如图片.jpg": "Name with extension, e.g., image.jpg",
    "截图文件路径": "Screenshot File Path",
    
    # Scroll related
    "滚动目标": "Scroll Target",
    "选择网页窗口滚动条或指定网页上某个滚动条元素": "Select webpage window scrollbar or a specific scrollbar element on the page",
    "拾取滚动条": "Pick Scrollbar",
    "拾取需要在网页上滚动操作的滚动条元素": "Pick the scrollbar element to scroll on the webpage",
    "滚动方向": "Scroll Direction",
    "横向滚动位置": "Horizontal Scroll Position",
    "纵向滚动位置": "Vertical Scroll Position",
    "横向自定义滚动距离": "Horizontal Custom Scroll Distance",
    "纵向自定义滚动距离": "Vertical Custom Scroll Distance",
    "单位为屏幕的分辨率像素px，一般为0-9999之间的数值": "Unit is screen resolution pixels px, typically a value between 0-9999",
    
    # Loop related
    "起始位置": "Start Position",
    "结束位置": "End Position",
    "下标位置从0开始": "Index position starts from 0",
    "下标位置从0开始,-1代表循环至最后一个元素": "Index position starts from 0, -1 means loop to the last element",
    "循环项位置": "Loop Item Position",
    "默认变量可修改，用于遍历列表的变量索引数值": "Default variable (modifiable), variable index value for traversing list",
    "循环项": "Loop Item",
    "默认变量可修改，用于遍历列表的变量": "Default variable (modifiable), variable for traversing list",
    
    # Element operations
    "元素操作": "Element Operation",
    "属性名称": "Attribute Name",
    "元素信息": "Element Information",
    "输出变量": "Output Variable",
    "输出获取到的当前网页标题字符串": "Output the current webpage title string obtained",
    
    # Common verbs and actions
    "获取": "Get",
    "设置": "Set",
    "等待": "Wait",
    "点击": "Click",
    "输入": "Input",
    "填写": "Fill",
    "拾取": "Pick",
    "选择": "Select",
    "循环": "Loop",
    "输出": "Output",
    
    # Common words
    "文本": "Text",
    "内容": "Content",
    "路径": "Path",
    "时间": "Time",
    "位置": "Position",
    "距离": "Distance",
    "方向": "Direction",
    "类型": "Type",
    "名称": "Name",
    "对象": "Object",
    "结果": "Result",
    "列表": "List",
    "数组": "Array",
    "变量": "Variable",
    "参数": "Parameter",
    "配置": "Configuration",
    
    # Atoms titles - common patterns
    "等待元素（web）": "Wait for Element (Web)",
    "元素是否存在（web）": "Element Exists (Web)",
    "点击元素（web）": "Click Element (Web)",
    "填写输入框（web）": "Fill Input Box (Web)",
    "鼠标悬停在元素上（web）": "Mouse Hover on Element (Web)",
    "拾取元素截图（web）": "Pick Element Screenshot (Web)",
    "元素位置截图（web）": "Element Position Screenshot (Web)",
    "鼠标滚动网页": "Mouse Scroll Webpage",
    "元素置于可视区域（web）": "Element to Visible Area (Web)",
    "获取相似元素列表（web）": "Get Similar Elements List (Web)",
    "循环相似元素列表（web）": "Loop Similar Elements List (Web)",
    "获取元素文本内容（web）": "Get Element Text Content (Web)",
    "拾取滑块拖拽（web）": "Pick Slider Drag (Web)",
    
    # More specific patterns
    "悬停元素拾取": "Hover Element Picker",
    "拾取鼠标要悬停的元素": "Pick the element for mouse hover",
    "选择相似元素所在的浏览器对象": "Select the browser object where similar elements are located",
    "相似元素拾取": "Similar Element Picker",
    "在网页上拾取不同位置的两个相似元素": "Pick two similar elements at different positions on the webpage",
    "选择要获取文本的元素所在的浏览器对象": "Select the browser object where the element to get text is located",
    "选择要获取文本的元素位置": "Select the position of the element to get text",
    "选择要可视的元素所在的浏览器对象": "Select the browser object where the element to be visible is located",
    "拾取可视目标": "Pick Visible Target",
    "拾取需要可视的目标元素": "Pick the target element to be visible",
    "选择截图元素所在的浏览器对象": "Select the browser object where the screenshot element is located",
    "拾取需要截图的元素": "Pick the element to screenshot",
    "选择要滑动滚动条的网页所在浏览器对象": "Select the browser object where the webpage with scrollbar is located",
}


def translate_text(text):
    """Translate Chinese text to English using the translation dictionary."""
    if not text or not isinstance(text, str):
        return text
    
    # Try exact match first
    if text in TRANSLATIONS:
        return TRANSLATIONS[text]
    
    # Try partial matches for common patterns
    translated = text
    for chinese, english in TRANSLATIONS.items():
        if chinese in translated:
            translated = translated.replace(chinese, english)
    
    # If still contains Chinese characters, return original (needs manual translation)
    if re.search(r'[\u4e00-\u9fa5]', translated):
        print(f"Warning: Untranslated text found: {text}")
        return text  # Return original for manual review
    
    return translated


def translate_config_item(item):
    """Recursively translate all string values in a config item."""
    if isinstance(item, dict):
        result = {}
        for key, value in item.items():
            if key in ['title', 'comment', 'tip']:
                result[key] = translate_text(value)
            else:
                result[key] = translate_config_item(value)
        return result
    elif isinstance(item, list):
        return [translate_config_item(i) for i in item]
    else:
        return item


def translate_config_file(file_path):
    """Translate a single config.yaml file."""
    print(f"\nTranslating: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        if not config or 'atomic' not in config:
            print(f"  Skipping - no 'atomic' section found")
            return
        
        # Translate the config
        translated_config = translate_config_item(config)
        
        # Create backup
        backup_path = str(file_path) + '.backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, allow_unicode=True, sort_keys=False)
        print(f"  Backup created: {backup_path}")
        
        # Write translated version
        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.dump(translated_config, f, allow_unicode=True, sort_keys=False)
        print(f"  Translation complete!")
        
    except Exception as e:
        print(f"  Error: {e}")


def main():
    """Main function to translate all config files."""
    base_path = Path(r"e:\astron-rpa\engine\components")
    
    # Find all config.yaml files
    config_files = list(base_path.glob("*/config.yaml"))
    
    print(f"Found {len(config_files)} config files to translate\n")
    print("=" * 60)
    
    for config_file in config_files:
        translate_config_file(config_file)
    
    print("\n" + "=" * 60)
    print("Translation complete!")
    print("\nNote: Please review files with 'Untranslated text' warnings")
    print("Backups have been created with .backup extension")


if __name__ == "__main__":
    main()
