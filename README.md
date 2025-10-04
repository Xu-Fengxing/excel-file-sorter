## 🗂️ excel-file-sorter

一个轻量级的 Python 小工具，根据 Excel
表格中的文件名，自动分类同目录下的文件。
适合用于批量整理文件、匹配资源或管理素材等场景～✨

------------------------------------------------------------------------

### 💡 功能简介

-   选择一个 Excel 文件（A 列包含文件名，不带扩展名）\
-   扫描脚本所在目录的所有文件\
-   自动把文件分为两类：
    -   ✅ **匹配文件**：文件名在 Excel 列表中\
    -   🚫 **未匹配文件**：文件名不在 Excel 列表中\
-   程序会自动创建两个文件夹：
    -   `匹配文件/`
    -   `未匹配文件/`

------------------------------------------------------------------------

### 📦 使用方法

#### 一、准备工作

1.  安装好 [Python 3](https://www.python.org/downloads/)\

2.  安装依赖：

    ``` bash
    pip install pandas openpyxl
    ```

#### 二、运行脚本

1.  将脚本 `excel-file-sorter.py` 放在要分类的文件夹中。\

2.  双击运行脚本（或命令行运行）：

    ``` bash
    python excel-file-sorter.py
    ```

3.  弹窗中选择 Excel 文件。\

4.  等待分类完成，程序会提示：

        匹配文件：xx 个
        未匹配文件：xx 个

5.  查看生成的文件夹：

        匹配文件/
        未匹配文件/

------------------------------------------------------------------------

### 🧩 文件示例

Excel 文件（A列示例）： \| 文件名 \| \|--------\| \| cat_photo \| \|
dog_video \| \| travel_notes \|

脚本所在目录：

    📁 当前文件夹
     ┣ excel-file-sorter.py
     ┣ cat_photo.jpg
     ┣ dog_video.mp4
     ┣ other_image.png
     ┗ travel_notes.txt

运行后结果：

    📁 当前文件夹
     ┣ excel-file-sorter.py
     ┣ 📁 匹配文件
     ┃ ┣ cat_photo.jpg
     ┃ ┣ dog_video.mp4
     ┃ ┗ travel_notes.txt
     ┗ 📁 未匹配文件
        ┗ other_image.png

------------------------------------------------------------------------

### ⚙️ 可执行文件（可选）

想要做成一键双击运行的 `.exe` 程序可以用：

``` bash
pip install pyinstaller
pyinstaller -F -w excel-file-sorter.py
```

生成的 `excel-file-sorter.exe` 在 `dist` 文件夹中，可直接运行，无需
Python 环境。

------------------------------------------------------------------------

### 🐼 技术要点

-   使用 `tkinter` 实现图形化文件选择\
-   使用 `pandas` + `openpyxl` 读取 Excel\
-   使用 `shutil` 移动文件\
-   完全离线运行，无需网络
