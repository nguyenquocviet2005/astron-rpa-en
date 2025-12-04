-- Translate atomCommon JSON content from Chinese to English
-- This script uses MySQL REPLACE to translate all Chinese text

USE rpa;

-- AI category
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"大模型"', '"title":"Large Language Models"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"多轮会话"', '"title":"Multi-turn Chat"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"单轮会话"', '"title":"Single-turn Chat"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"知识问答"', '"title":"Knowledge Q&A"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"主题扩写"', '"title":"Topic Expansion"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"段落扩写"', '"title":"Paragraph Expansion"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"段落缩写"', '"title":"Paragraph Abbreviation"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"简历评分"', '"title":"Resume Scoring"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"职位关键词生成"', '"title":"Job Keyword Generation"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"合同要素提取"', '"title":"Contract Element Extraction"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"调用Dify流程"', '"title":"Call Dify Workflow"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"调用星辰Agent流程"', '"title":"Call XingChen Agent Workflow"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"营业执照识别"', '"title":"Business License Recognition"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"身份证识别"', '"title":"ID Card Recognition"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"增值税发票识别"', '"title":"VAT Invoice Recognition"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"火车票识别"', '"title":"Train Ticket Recognition"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"出租车发票识别"', '"title":"Taxi Invoice Recognition"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"通用文字识别"', '"title":"General Text Recognition"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"验证码"', '"title":"Verification Code"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"通用数英验证码"', '"title":"General Alphanumeric Captcha"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"通用滑块验证码"', '"title":"General Slider Captcha"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"通用点击验证码"', '"title":"General Click Captcha"') WHERE atom_key = 'atomCommon';

-- Process Flow
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"流程"', '"title":"Process Flow"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"运行子流程"', '"title":"Run Sub-process"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"运行Python模块"', '"title":"Run Python Module"') WHERE atom_key = 'atomCommon';

-- Code Flow
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"代码流程"', '"title":"Code Flow"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"设置变量值"', '"title":"Set Variable Value"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"日志打印"', '"title":"Log Print"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"条件判断"', '"title":"Conditional Logic"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"IF条件"', '"title":"IF Condition"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"IF图像存在"', '"title":"IF Image Exists"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"IF文件夹存在"', '"title":"IF Folder Exists"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"IF文件存在"', '"title":"IF File Exists"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"IF窗口存在"', '"title":"IF Window Exists"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"ELSE IF条件"', '"title":"ELSE IF Condition"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"ELSE条件"', '"title":"ELSE Condition"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"循环"', '"title":"Loop"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"字典For循环"', '"title":"Dictionary For Loop"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"列表For循环"', '"title":"List For Loop"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"计数For循环"', '"title":"Count For Loop"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"循环Excel内容"', '"title":"Loop Excel Content"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"循环相似元素列表（web）"', '"title":"Loop Similar Elements (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"While循环"', '"title":"While Loop"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"退出循环（Break）"', '"title":"Break Loop"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"继续下次循环（Continue）"', '"title":"Continue Loop"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"错误处理"', '"title":"Error Handling"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"捕获异常（Try)"', '"title":"Try Exception"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"捕获异常（Finally)"', '"title":"Finally Exception"') WHERE atom_key = 'atomCommon';

-- Web Automation
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"网页自动化"', '"title":"Web Automation"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"打开浏览器"', '"title":"Open Browser"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"关闭浏览器"', '"title":"Close Browser"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取已打开的浏览器对象"', '"title":"Get Opened Browser Object"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"元素是否存在（web）"', '"title":"Element Exists (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"等待元素（web）"', '"title":"Wait for Element (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"元素操作（web）"', '"title":"Element Operation (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"点击元素（web）"', '"title":"Click Element (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取元素文本内容（web）"', '"title":"Get Element Text (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"填写输入框（web）"', '"title":"Fill Input Box (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取复选框（web）"', '"title":"Get Checkbox (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"操作复选框（web）"', '"title":"Operate Checkbox (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取下拉框（web）"', '"title":"Get Dropdown (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"操作下拉框（web）"', '"title":"Operate Dropdown (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"拾取滑块拖拽（web）"', '"title":"Pick Slider Drag (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"鼠标悬停在元素上（web）"', '"title":"Mouse Hover on Element (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"拾取元素截图（web）"', '"title":"Pick Element Screenshot (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"元素位置截图（web）"', '"title":"Element Position Screenshot (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"元素置于可视区域（web）"', '"title":"Scroll Element into View (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取表格数据（web）"', '"title":"Get Table Data (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"数据抓取（web）"', '"title":"Data Scraping (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取相似元素列表（web）"', '"title":"Get Similar Elements (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取元素对象（web）"', '"title":"Get Element Object (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取关联元素（web）"', '"title":"Get Related Element (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"设置Cookie"', '"title":"Set Cookie"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取Cookie"', '"title":"Get Cookie"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"网页操作"', '"title":"Webpage Operations"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"打开新网页"', '"title":"Open New Webpage"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取当前标签页ID"', '"title":"Get Current Tab ID"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"切换到已存在标签页"', '"title":"Switch to Existing Tab"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"关闭网页"', '"title":"Close Webpage"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"刷新当前网页"', '"title":"Refresh Current Page"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"停止加载网页"', '"title":"Stop Loading Page"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"网页前进"', '"title":"Webpage Forward"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"网页后退"', '"title":"Webpage Backward"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"网页截图"', '"title":"Webpage Screenshot"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"鼠标滚动网页"', '"title":"Mouse Scroll Webpage"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取网页URL"', '"title":"Get Webpage URL"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取网页标题"', '"title":"Get Webpage Title"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"等待页面加载完成"', '"title":"Wait for Page Load"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"网页文件"', '"title":"Webpage Files"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"文件下载（web）"', '"title":"File Download (Web)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"文件上传（web）"', '"title":"File Upload (Web)"') WHERE atom_key = 'atomCommon';

-- Desktop Automation
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"桌面自动化"', '"title":"Desktop Automation"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"关闭程序"', '"title":"Close Program"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"打开程序"', '"title":"Open Program"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"点击元素（桌面）"', '"title":"Click Element (Desktop)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"元素截图（桌面）"', '"title":"Element Screenshot (Desktop)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"鼠标悬停元素（桌面）"', '"title":"Mouse Hover Element (Desktop)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"填写输入框（桌面）"', '"title":"Fill Input Box (Desktop)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取元素文本（桌面）"', '"title":"Get Element Text (Desktop)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取相似元素列表（桌面）"', '"title":"Get Similar Elements (Desktop)"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"窗口操作"', '"title":"Window Operations"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"置顶窗口"', '"title":"Pin Window"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"关闭窗口"', '"title":"Close Window"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"调整窗口大小"', '"title":"Resize Window"') WHERE atom_key = 'atomCommon';

-- Document Processing
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"文档处理"', '"title":"Document Processing"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取PDF文档页数"', '"title":"Get PDF Page Count"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"提取PDF文档文本"', '"title":"Extract PDF Text"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"合并PDF文件"', '"title":"Merge PDF Files"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"提取PDF文档图片"', '"title":"Extract PDF Images"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"抽取PDF指定页"', '"title":"Extract PDF Pages"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"提取PDF表格到Excel"', '"title":"Extract PDF Table to Excel"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"PDF页面转图片"', '"title":"PDF Page to Image"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"打开Word"', '"title":"Open Word"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"读取Word内容"', '"title":"Read Word Content"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"创建Word"', '"title":"Create Word"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"保存Word"', '"title":"Save Word"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"关闭Word"', '"title":"Close Word"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"插入文本到Word"', '"title":"Insert Text to Word"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"选择Word文本"', '"title":"Select Word Text"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"定位Word光标"', '"title":"Position Word Cursor"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"移动Word光标"', '"title":"Move Word Cursor"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"Word插入页/段落"', '"title":"Word Insert Page/Paragraph"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"Word插入超链接"', '"title":"Word Insert Hyperlink"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"Word插入图片"', '"title":"Word Insert Image"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"Word读取表格"', '"title":"Word Read Table"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"Word插入表格"', '"title":"Word Insert Table"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"Word删除内容"', '"title":"Word Delete Content"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"Word替换内容"', '"title":"Word Replace Content"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"Word创建批注"', '"title":"Word Create Comment"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"Word删除批注"', '"title":"Word Delete Comment"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"Word导出为PDF/TXT"', '"title":"Word Export to PDF/TXT"') WHERE atom_key = 'atomCommon';

-- Excel Processing
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"Excel处理"', '"title":"Excel Processing"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取Excel对象"', '"title":"Get Excel Object"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"打开Excel"', '"title":"Open Excel"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"关闭Excel"', '"title":"Close Excel"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"保存Excel"', '"title":"Save Excel"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"读取Excel单元格"', '"title":"Read Excel Cell"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"读取Excel行"', '"title":"Read Excel Row"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"读取Excel列"', '"title":"Read Excel Column"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"写入Excel单元格"', '"title":"Write Excel Cell"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"写入Excel行"', '"title":"Write Excel Row"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"写入Excel列"', '"title":"Write Excel Column"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取Excel表单"', '"title":"Get Excel Sheet"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"新增Excel表单"', '"title":"Add Excel Sheet"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"删除Excel表单"', '"title":"Delete Excel Sheet"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"激活Excel表单"', '"title":"Activate Excel Sheet"') WHERE atom_key = 'atomCommon';

-- Data Processing
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"数据处理"', '"title":"Data Processing"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"字符串处理"', '"title":"String Processing"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"字符串拼接"', '"title":"String Concatenation"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"字符串截取"', '"title":"String Substring"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"字符串替换"', '"title":"String Replace"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"字符串分割"', '"title":"String Split"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"字符串格式化"', '"title":"String Format"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"去除空白字符"', '"title":"Remove Whitespace"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取字符串长度"', '"title":"Get String Length"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"正则匹配"', '"title":"Regex Match"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"列表处理"', '"title":"List Processing"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"添加列表元素"', '"title":"Add List Element"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"删除列表元素"', '"title":"Delete List Element"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取列表元素"', '"title":"Get List Element"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"列表排序"', '"title":"Sort List"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"列表去重"', '"title":"Remove List Duplicates"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取列表长度"', '"title":"Get List Length"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"字典处理"', '"title":"Dictionary Processing"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"添加字典键值对"', '"title":"Add Dictionary Key-Value"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"删除字典键值对"', '"title":"Delete Dictionary Key-Value"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取字典值"', '"title":"Get Dictionary Value"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取字典所有键"', '"title":"Get All Dictionary Keys"') WHERE atom_key = 'atomCommon';

-- Mouse & Keyboard
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"鼠标键盘"', '"title":"Mouse & Keyboard"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"鼠标左键单击"', '"title":"Mouse Left Click"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"鼠标右键单击"', '"title":"Mouse Right Click"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"鼠标双击"', '"title":"Mouse Double Click"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"鼠标移动"', '"title":"Mouse Move"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"鼠标拖拽"', '"title":"Mouse Drag"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"鼠标滚动"', '"title":"Mouse Scroll"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取鼠标位置"', '"title":"Get Mouse Position"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"发送快捷键"', '"title":"Send Hotkey"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"输入文本"', '"title":"Input Text"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"发送按键"', '"title":"Send Key"') WHERE atom_key = 'atomCommon';

-- System
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"系统"', '"title":"System"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"延时等待"', '"title":"Delay Wait"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"执行CMD命令"', '"title":"Execute CMD Command"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"执行Powershell命令"', '"title":"Execute PowerShell Command"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取环境变量"', '"title":"Get Environment Variable"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"设置环境变量"', '"title":"Set Environment Variable"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取剪贴板内容"', '"title":"Get Clipboard Content"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"设置剪贴板内容"', '"title":"Set Clipboard Content"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"获取当前时间"', '"title":"Get Current Time"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"时间格式化"', '"title":"Format Time"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"时间计算"', '"title":"Time Calculation"') WHERE atom_key = 'atomCommon';

-- File Operations
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"文件操作"', '"title":"File Operations"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"创建文件夹"', '"title":"Create Folder"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"删除文件夹"', '"title":"Delete Folder"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"复制文件夹"', '"title":"Copy Folder"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"移动文件夹"', '"title":"Move Folder"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"重命名文件夹"', '"title":"Rename Folder"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"遍历文件夹"', '"title":"Traverse Folder"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"创建文件"', '"title":"Create File"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"删除文件"', '"title":"Delete File"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"复制文件"', '"title":"Copy File"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"移动文件"', '"title":"Move File"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"重命名文件"', '"title":"Rename File"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"读取文本文件"', '"title":"Read Text File"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"写入文本文件"', '"title":"Write Text File"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"读取CSV文件"', '"title":"Read CSV File"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"写入CSV文件"', '"title":"Write CSV File"') WHERE atom_key = 'atomCommon';

-- Network
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"网络"', '"title":"Network"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"HTTP请求"', '"title":"HTTP Request"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"下载文件"', '"title":"Download File"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"上传文件"', '"title":"Upload File"') WHERE atom_key = 'atomCommon';

-- Email
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"邮件"', '"title":"Email"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"发送邮件"', '"title":"Send Email"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"接收邮件"', '"title":"Receive Email"') WHERE atom_key = 'atomCommon';

-- Database
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"数据库"', '"title":"Database"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"连接数据库"', '"title":"Connect Database"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"断开数据库"', '"title":"Disconnect Database"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"执行SQL查询"', '"title":"Execute SQL Query"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"执行SQL更新"', '"title":"Execute SQL Update"') WHERE atom_key = 'atomCommon';

-- Image Processing
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"图像处理"', '"title":"Image Processing"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"等待图片出现"', '"title":"Wait for Image"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"图片是否存在"', '"title":"Image Exists"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"点击图片"', '"title":"Click Image"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"找图位置"', '"title":"Find Image Position"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"找图点击"', '"title":"Find and Click Image"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"全屏截图"', '"title":"Full Screenshot"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"区域截图"', '"title":"Region Screenshot"') WHERE atom_key = 'atomCommon';

-- Dialogue & Input
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"对话框"', '"title":"Dialogue Box"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"消息框"', '"title":"Message Box"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"输入框"', '"title":"Input Box"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"文件选择框"', '"title":"File Selection Box"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"文件夹选择框"', '"title":"Folder Selection Box"') WHERE atom_key = 'atomCommon';

-- OpenAPI
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"OpenAPI"', '"title":"OpenAPI"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"title":"调用OpenAPI"', '"title":"Call OpenAPI"') WHERE atom_key = 'atomCommon';

-- Additional common terms
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"desc":"大模型"', '"desc":"Large Language Models"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"desc":"网页自动化"', '"desc":"Web Automation"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"desc":"桌面自动化"', '"desc":"Desktop Automation"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"desc":"流程"', '"desc":"Process Flow"') WHERE atom_key = 'atomCommon';
UPDATE c_atom_meta SET atom_content = REPLACE(atom_content, '"desc":"代码流程"', '"desc":"Code Flow"') WHERE atom_key = 'atomCommon';

SELECT 'Translation completed - All atomCommon text translated to English' as status;
