import json
import re

# Chinese to English translations for UI text
TRANSLATIONS = {
    # Main categories
    "大模型": "Large Language Models",
    "验证码": "Verification Code",
    "流程": "Process",
    "代码流程": "Code Flow",
    "条件判断": "Conditional",
    "循环": "Loop",
    "错误处理": "Error Handling",
    "网页自动化": "Web Automation",
    "桌面自动化": "Desktop Automation",
    "窗口操作": "Window Operations",
    "文档处理": "Document Processing",
    "鼠标键盘": "Mouse & Keyboard",
    "数据处理": "Data Processing",
    "数学操作": "Math Operations",
    "字符串操作": "String Operations",
    "列表操作": "List Operations",
    "字典操作": "Dictionary Operations",
    "时间操作": "Time Operations",
    "操作系统": "Operating System",
    "文件操作": "File Operations",
    "文件夹操作": "Folder Operations",
    "压缩/解压": "Compress/Decompress",
    "系统命令": "System Commands",
    "截图": "Screenshot",
    "剪切板": "Clipboard",
    "加解密/编解码": "Encryption/Encoding",
    "网络": "Network",
    "邮件": "Email",
    "CV图像": "CV Image",
    "对话框": "Dialog",
    "自定义脚本": "Custom Script",
    "卓越中心": "Excellence Center",
    "飞书": "Feishu",
    "网页操作": "Page Operations",
    "网页文件": "Web File",
    
    # Atom titles - AI
    "多轮会话": "Multi-turn Conversation",
    "单轮会话": "Single-turn Conversation",
    "知识问答": "Knowledge Q&A",
    "主题扩写": "Topic Expansion",
    "段落扩写": "Paragraph Expansion",
    "段落缩写": "Paragraph Abbreviation",
    "简历评分": "Resume Scoring",
    "职位关键词生成": "Job Keyword Generation",
    "合同要素提取": "Contract Element Extraction",
    "调用Dify工作流": "Call Dify Workflow",
    "调用Dify对话流": "Call Dify Chatflow",
    "调用星辰Agent流程": "Call XingChen Agent Flow",
    
    # OCR
    "营业执照识别": "Business License Recognition",
    "身份证识别": "ID Card Recognition",
    "增值税发票识别": "VAT Invoice Recognition",
    "火车票识别": "Train Ticket Recognition",
    "出租车发票识别": "Taxi Invoice Recognition",
    "通用文字识别": "General Text Recognition",
    
    # Verification
    "通用数英验证码": "General Alphanumeric Captcha",
    "通用滑块验证码": "General Slider Captcha",
    "通用点击验证码": "General Click Captcha",
    
    # Process
    "运行子流程": "Run Sub-process",
    "运行Python模块": "Run Python Module",
    
    # Code flow
    "设置变量值": "Set Variable Value",
    "日志打印": "Log Print",
    "IF条件": "IF Condition",
    "IF图像存在": "IF Image Exists",
    "IF文件夹存在": "IF Folder Exists",
    "IF文件存在": "IF File Exists",
    "IF窗口存在": "IF Window Exists",
    "ELSE IF条件": "ELSE IF Condition",
    "ELSE条件": "ELSE Condition",
    "字典For循环": "Dictionary For Loop",
    "列表For循环": "List For Loop",
    "计数For循环": "Count For Loop",
    "循环Excel内容": "Loop Excel Content",
    "循环相似元素列表（web）": "Loop Similar Elements (Web)",
    "While循环": "While Loop",
    "退出循环（Break）": "Exit Loop (Break)",
    "继续下次循环（Continue）": "Continue Next Loop (Continue)",
    "捕获异常（Try)": "Catch Exception (Try)",
    "捕获异常（Finally)": "Catch Exception (Finally)",
    
    # Web automation
    "打开浏览器": "Open Browser",
    "关闭浏览器": "Close Browser",
    "获取已打开的浏览器对象": "Get Opened Browser Objects",
    "元素是否存在（web）": "Element Exists (Web)",
    "等待元素（web）": "Wait for Element (Web)",
    "元素操作（web）": "Element Operations (Web)",
    "点击元素（web）": "Click Element (Web)",
    "获取元素文本内容（web）": "Get Element Text (Web)",
    "填写输入框（web）": "Fill Input Box (Web)",
    "获取复选框（web）": "Get Checkbox (Web)",
    "操作复选框（web）": "Operate Checkbox (Web)",
    "获取下拉框（web）": "Get Dropdown (Web)",
    "操作下拉框（web）": "Operate Dropdown (Web)",
    "拾取滑块拖拽（web）": "Pick Slider Drag (Web)",
    "鼠标悬停在元素上（web）": "Mouse Hover Element (Web)",
    "拾取元素截图（web）": "Pick Element Screenshot (Web)",
    "元素位置截图（web）": "Element Position Screenshot (Web)",
    "元素置于可视区域（web）": "Scroll Element to View (Web)",
    "获取表格数据（web）": "Get Table Data (Web)",
    "数据抓取（web）": "Data Scraping (Web)",
    "获取相似元素列表（web）": "Get Similar Elements (Web)",
    "获取元素对象（web）": "Get Element Object (Web)",
    "获取关联元素（web）": "Get Related Elements (Web)",
    "设置Cookie": "Set Cookie",
    "获取Cookie": "Get Cookie",
    "打开新网页": "Open New Page",
    "获取当前标签页ID": "Get Current Tab ID",
    "切换到已存在标签页": "Switch to Existing Tab",
    "关闭网页": "Close Page",
    "刷新当前网页": "Refresh Current Page",
    "停止加载网页": "Stop Loading Page",
    "网页前进": "Page Forward",
    "网页后退": "Page Backward",
    "网页截图": "Page Screenshot",
    "鼠标滚动网页": "Mouse Scroll Page",
    "获取网页URL": "Get Page URL",
    "获取网页标题": "Get Page Title",
    "等待页面加载完成": "Wait for Page Load",
    "文件下载（web）": "File Download (Web)",
    "文件上传（web）": "File Upload (Web)",
    
    # Desktop automation
    "关闭程序": "Close Program",
    "打开程序": "Open Program",
    "点击元素（桌面）": "Click Element (Desktop)",
    "元素截图（桌面）": "Element Screenshot (Desktop)",
    "鼠标悬停元素（桌面）": "Mouse Hover Element (Desktop)",
    "填写输入框（桌面）": "Fill Input Box (Desktop)",
    "获取元素文本（桌面）": "Get Element Text (Desktop)",
    "获取相似元素列表（桌面）": "Get Similar Elements (Desktop)",
    "置顶窗口": "Pin Window to Top",
    "关闭窗口": "Close Window",
    "调整窗口大小": "Resize Window",
    
    # PDF
    "获取PDF文档页数": "Get PDF Page Count",
    "提取PDF文档文本": "Extract PDF Text",
    "合并PDF文件": "Merge PDF Files",
    "提取PDF文档图片": "Extract PDF Images",
    "抽取PDF指定页": "Extract PDF Pages",
    "提取PDF表格到Excel": "Extract PDF Table to Excel",
    "PDF页面转图片": "PDF Page to Image",
    
    # Word
    "打开Word": "Open Word",
    "读取Word内容": "Read Word Content",
    "创建Word": "Create Word",
    "保存Word": "Save Word",
    "关闭Word": "Close Word",
    "插入文本到Word": "Insert Text to Word",
    "选择Word文本": "Select Word Text",
    "定位Word光标": "Position Word Cursor",
    "移动Word光标": "Move Word Cursor",
    "Word插入页/段落": "Word Insert Page/Paragraph",
    "Word插入超链接": "Word Insert Hyperlink",
    "Word插入图片": "Word Insert Image",
    "Word读取表格": "Word Read Table",
    "Word插入表格": "Word Insert Table",
    "Word删除内容": "Word Delete Content",
    "Word替换内容": "Word Replace Content",
    "Word创建批注": "Word Create Comment",
    "Word删除批注": "Word Delete Comment",
    "Word导出为PDF/TXT": "Word Export to PDF/TXT",
    
    # Excel
    "打开Excel": "Open Excel",
    "添加Excel工作表": "Add Excel Worksheet",
    "获取已打开的Excel对象": "Get Opened Excel Objects",
    "创建Excel": "Create Excel",
    "保存Excel": "Save Excel",
    "关闭Excel": "Close Excel",
    "写入Excel": "Write to Excel",
    "读取Excel内容": "Read Excel Content",
    "设置单元格格式": "Set Cell Format",
    "复制Excel单元格": "Copy Excel Cell",
    "粘贴Excel单元格": "Paste Excel Cell",
    "删除Excel单元格": "Delete Excel Cell",
    "获取Excel工作表名称": "Get Excel Sheet Names",
    "清除Excel区域内容": "Clear Excel Range",
    "插入Excel行或列": "Insert Excel Row/Column",
    "获取Excel行数": "Get Excel Row Count",
    "获取Excel列数": "Get Excel Column Count",
    "获取Excel第一个可用行": "Get Excel First Available Row",
    "获取Excel第一个可用列": "Get Excel First Available Column",
    "设置Excel行高": "Set Excel Row Height",
    "设置Excel列宽": "Set Excel Column Width",
    "获取Excel单元格颜色": "Get Excel Cell Color",
    "合并或拆分Excel单元格": "Merge/Split Excel Cells",
    "移动Excel工作表": "Move Excel Worksheet",
    "删除Excel工作表": "Delete Excel Worksheet",
    "重命名Excel工作表": "Rename Excel Worksheet",
    "复制Excel工作表": "Copy Excel Worksheet",
    "查找或替换Excel内容": "Find/Replace Excel Content",
    "插入Excel图片": "Insert Excel Image",
    "插入Excel公式": "Insert Excel Formula",
    "创建Excel批注": "Create Excel Comment",
    "删除Excel批注": "Delete Excel Comment",
    "Excel区域文本转数字": "Excel Text to Number",
    "Excel区域数字转文本": "Excel Number to Text",
    
    # Mouse & Keyboard
    "键盘输入": "Keyboard Input",
    "鼠标点击": "Mouse Click",
    "鼠标滚动": "Mouse Scroll",
    "鼠标移动": "Mouse Move",
    "鼠标拖拽": "Mouse Drag",
    "获取鼠标位置": "Get Mouse Position",
    "键盘模拟按键": "Keyboard Simulate Key",
    
    # Data Processing - Math
    "生成随机数": "Generate Random Number",
    "四舍五入": "Round Number",
    "自增自减": "Increment/Decrement",
    "获取绝对值": "Get Absolute Value",
    "数学计算": "Math Calculation",
    
    # Data Processing - String
    "文本提取内容": "Extract Text Content",
    "文本替换内容": "Replace Text Content",
    "列表聚合为文本": "List to Text",
    "文本分割为列表": "Text to List",
    "文本合并": "Merge Text",
    "文本补齐至固定长度": "Pad Text to Length",
    "文本去除两侧空格": "Trim Text Spaces",
    "截取固定长度文本": "Substring Fixed Length",
    "更改文本大小写": "Change Text Case",
    "获取文本长度": "Get Text Length",
    "JSON字符串互转": "JSON String Convert",
    "其他格式转文本": "Other Format to Text",
    "文本转其他格式": "Text to Other Format",
    
    # Data Processing - List
    "创建新列表": "Create New List",
    "清空列表": "Clear List",
    "列表插入值": "List Insert Value",
    "列表修改值": "List Modify Value",
    "获取值在列表位置": "Get Value Position in List",
    "列表删除值": "List Remove Value",
    "列表排序": "List Sort",
    "列表随机打乱顺序": "List Shuffle",
    "剔除列表中的多项": "Remove Multiple from List",
    "列表反转": "List Reverse",
    "列表合并": "List Merge",
    "列表去重": "List Remove Duplicates",
    "获取两个列表的重复项": "Get List Duplicates",
    "根据索引获取列表值": "Get List Value by Index",
    "获取列表长度": "Get List Length",
    
    # Data Processing - Dict
    "创建新字典": "Create New Dictionary",
    "字典设置值": "Dictionary Set Value",
    "字典删除值": "Dictionary Delete Value",
    "字典获取值": "Dictionary Get Value",
    "获取字典所有键": "Get Dictionary All Keys",
    "获取字典所有值": "Get Dictionary All Values",
    
    # Data Processing - Time
    "获取当前时间": "Get Current Time",
    "设置时间": "Set Time",
    "时间对象转时间戳": "DateTime to Timestamp",
    "时间戳转时间对象": "Timestamp to DateTime",
    "获取时间差": "Get Time Difference",
    "输出指定格式时间文本": "Output Formatted Time",
    
    # File Operations
    "创建文件": "Create File",
    "写入文件": "Write File",
    "读取文件": "Read File",
    "复制文件": "Copy File",
    "移动文件": "Move File",
    "重命名文件": "Rename File",
    "删除文件": "Delete File",
    "查找文件": "Find File",
    "等待文件": "Wait for File",
    "获取文件编码类型": "Get File Encoding",
    "获取文件信息": "Get File Info",
    "获取文件列表": "Get File List",
    "上传文件至共享文件夹": "Upload to Shared Folder",
    "从共享文件夹下载文件": "Download from Shared Folder",
    
    # Folder Operations
    "创建文件夹": "Create Folder",
    "打开文件夹": "Open Folder",
    "复制文件夹": "Copy Folder",
    "移动文件夹": "Move Folder",
    "重命名文件夹": "Rename Folder",
    "清空文件夹": "Clear Folder",
    "删除文件夹": "Delete Folder",
    "获取文件夹列表": "Get Folder List",
    
    # Compress
    "压缩": "Compress",
    "解压": "Decompress",
    
    # System
    "运行或打开": "Run or Open",
    "获取进程PID": "Get Process PID",
    "终止进程": "Terminate Process",
    "屏幕截图": "Screen Screenshot",
    "复制到剪切板": "Copy to Clipboard",
    "清空剪切板": "Clear Clipboard",
    "获取剪切板": "Get Clipboard",
    
    # Encryption
    "SHA加密": "SHA Encryption",
    "MD5加密": "MD5 Encryption",
    "对称解密": "Symmetric Decryption",
    "对称加密": "Symmetric Encryption",
    "Base64解码": "Base64 Decode",
    "Base64编码": "Base64 Encode",
    
    # Network
    "发送邮件": "Send Email",
    "接收邮件": "Receive Email",
    "HTTP请求": "HTTP Request",
    "HTTP下载": "HTTP Download",
    "创建FTP连接": "Create FTP Connection",
    "关闭FTP连接": "Close FTP Connection",
    "获取工作目录(FTP)": "Get Work Directory (FTP)",
    "切换工作目录(FTP)": "Change Work Directory (FTP)",
    "创建文件夹(FTP)": "Create Folder (FTP)",
    "获取文件/文件夹(FTP)": "Get File/Folder (FTP)",
    "上传文件/文件夹(FTP)": "Upload File/Folder (FTP)",
    "重命名文件/文件夹(FTP)": "Rename File/Folder (FTP)",
    "下载文件/文件夹(FTP)": "Download File/Folder (FTP)",
    "删除文件/文件夹(FTP)": "Delete File/Folder (FTP)",
    
    # CV
    "点击图像": "Click Image",
    "鼠标悬浮在图像上": "Mouse Hover on Image",
    "等待图像": "Wait for Image",
    "图像输入框输入": "Image Input Box Input",
    
    # Dialog
    "消息提示框": "Message Dialog",
    "输入对话框": "Input Dialog",
    "选择对话框": "Select Dialog",
    "日期时间选择框": "DateTime Picker",
    "文件选择对话框": "File Select Dialog",
    "自定义对话框": "Custom Dialog",
    
    # Script
    "JS脚本": "JS Script",
    
    # Remote
    "获取共享变量": "Get Shared Variable",
    
    # Feishu
    "连接到多维表格": "Connect to Multi-sheet",
    "列出记录（筛选）": "List Records (Filtered)",
    "列出记录（指定）": "List Records (Specified)",
    "创建记录": "Create Record",
    "更新记录": "Update Record",
    "删除记录": "Delete Record",
    "列出数据表": "List Data Tables",
    "新增数据表": "Add Data Table",
    "删除数据表": "Delete Data Table",
    "重命名数据表": "Rename Data Table",
    "列出字段": "List Fields",
    "新增字段": "Add Field",
    "更新字段": "Update Field",
    "删除字段": "Delete Field",
    "连接数据表": "Connect to Table",
    "获取工作表信息": "Get Worksheet Info",
    "设置筛选器": "Set Filter",
    "获取筛选结果": "Get Filter Result",
    "读取工作表数据": "Read Worksheet Data",
    "写入数据": "Write Data",
    
    # Common Advanced Parameters
    "打印输出变量值": "Print Output Variable Value",
    "是": "Yes",
    "否": "No",
    "执行前延迟(秒)": "Delay Before Execution (sec)",
    "执行后延迟(秒)": "Delay After Execution (sec)",
    "执行异常时": "On Execution Error",
    "退出": "Exit",
    "跳过": "Skip",
    "重试": "Retry",
    "重试次数(次)": "Retry Count",
    "重试间隔(秒)": "Retry Interval (sec)",
    
    # Types
    "任意值": "Any Value",
    "任何值": "Any Value",
    "数值": "Number",
    "整数": "Integer",
    "布尔值": "Boolean",
    "字符串": "String",
    "列表": "List",
    "字典": "Dictionary",
    "文件路径": "File Path",
    "文件夹路径": "Folder Path",
    "日期时间": "DateTime",
    "地址": "URL",
    "元素": "Element",
    "网页元素": "Web Element",
    "桌面元素": "Desktop Element",
    "图像元素": "Image Element",
    "密码": "Password",
    "飞书对象": "Feishu Object",
    "对话框输出结果": "Dialog Output Result",
    "浏览器对象": "Browser Object",
    "Word对象": "Word Object",
    "Excel对象": "Excel Object",
    
    # Type functions
    "转文本": "To Text",
    "取整数部分": "Get Integer Part",
    "转整数": "To Integer",
    "转数值": "To Number",
    "删除两端空格": "Trim Spaces",
    "列表第": "List Item",
    "项": "Item",
    "列表倒数第": "List Item from End",
    "列表长度": "List Length",
    "字典键": "Dictionary Key",
    "的值": "Value",
    "字典包含元素个数": "Dictionary Element Count",
    "根目录": "Root Directory",
    "父目录": "Parent Directory",
    "文件名称": "File Name",
    "文件名称(不带扩展名)": "File Name (No Extension)",
    "文件扩展名": "File Extension",
    "获取年份": "Get Year",
    "获取月份": "Get Month",
    "获取日": "Get Day",
    "获取小时": "Get Hour",
    "获取分钟": "Get Minute",
    "获取秒": "Get Second",
    "获取周几": "Get Weekday",
    "获取周数": "Get Week Number",
    "该网页的地址": "Page URL",
    "该网页的标题": "Page Title",
    "文件所在位置": "File Location",
    "第一个可用行": "First Available Row",
    
    # Remaining Chinese text - use Unicode curly quotes like the original
    "\u201c你好\u201d": "\u201cHello\u201d",  # Chinese curly quotes with Chinese -> curly quotes with English
    "对象": "Object",
    "到第": " to ",
    
    # Keep some as-is for template values - these need escaped quotes in JSON
    "true或者false": "true or false",
    "小明": "John",
}

def translate_text(text):
    """Translate Chinese text to English"""
    if text in TRANSLATIONS:
        return TRANSLATIONS[text]
    return text

def translate_in_string(s):
    """Replace all Chinese phrases in a string with English translations"""
    result = s
    # Sort by length descending to replace longer phrases first
    for cn, en in sorted(TRANSLATIONS.items(), key=lambda x: -len(x[0])):
        result = result.replace(cn, en)
    return result

# Read the original SQL-escaped JSON
with open(r'e:\astron-rpa\docker\volumes\mysql\original_raw.txt', 'r', encoding='utf-8') as f:
    original_escaped = f.read()

# Translate the text while keeping the SQL escaping intact
translated_escaped = translate_in_string(original_escaped)

print(f"Original length: {len(original_escaped)}")
print(f"Translated length: {len(translated_escaped)}")
print(f"\nFirst 200 chars:\n{translated_escaped[:200]}")
print(f"\nLast 200 chars:\n{translated_escaped[-200:]}")

# Save translated SQL-escaped string
with open(r'e:\astron-rpa\docker\volumes\mysql\translated_escaped.txt', 'w', encoding='utf-8') as f:
    f.write(translated_escaped)

print("\n✓ Saved translated SQL-escaped string")
