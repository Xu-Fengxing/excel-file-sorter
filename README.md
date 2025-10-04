# excel-file-sorter

一个轻量级的 Python 脚本，用来根据 Excel 表格中的文件名自动分类当前文件夹下的文件。

## 使用方法

1. 下载 `excel-file-sorter.py`。  
2. 把它放到需要分类的文件夹里。  
3. 双击运行脚本。  
4. 在弹出的窗口中选择 Excel 文件（A列包含文件名，不含扩展名）。  
5. 程序会自动创建两个文件夹：  
   - `匹配文件`：文件名出现在 Excel 表格中  
   - `未匹配文件`：文件名未出现在 Excel 表格中  

## 示例

原始文件夹：
cat.jpg
dog.mp4
tree.png
list.xlsx
excel-file-sorter.py

css
复制代码

Excel 文件内容（A列）：
cat
tree

复制代码

运行后：
📁 匹配文件
┣ cat.jpg
┗ tree.png
📁 未匹配文件
┗ dog.mp4

markdown
复制代码

## 环境要求

- Python 3.x（推荐 3.7+）  
- 依赖：`pandas`, `openpyxl`  
- 支持 Windows、macOS、Linux
