import os
import shutil
import pandas as pd
from tkinter import Tk, filedialog, messagebox

def main():
    # 关闭主窗口
    root = Tk()
    root.withdraw()
    root.update()

    # 选择 Excel 文件
    excel_path = filedialog.askopenfilename(
        title="请选择Excel文件",
        filetypes=[("Excel 文件", "*.xlsx;*.xls")]
    )

    if not excel_path:
        messagebox.showinfo("提示", "未选择Excel文件，程序已退出。")
        return

    try:
        # 读取Excel第一列数据
        df = pd.read_excel(excel_path, usecols=[0], header=None)
        excel_names = df.iloc[:, 0].dropna().astype(str).tolist()
        excel_names_set = set(excel_names)

        # 当前脚本目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        matched_dir = os.path.join(current_dir, "匹配文件")
        unmatched_dir = os.path.join(current_dir, "未匹配文件")

        os.makedirs(matched_dir, exist_ok=True)
        os.makedirs(unmatched_dir, exist_ok=True)

        # 遍历当前目录下所有文件
        files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]

        matched_count = 0
        unmatched_count = 0

        for file in files:
            if file.endswith(".py"):
                continue  # 跳过脚本本身

            filename_no_ext = os.path.splitext(file)[0]
            src_path = os.path.join(current_dir, file)

            if filename_no_ext in excel_names_set:
                shutil.move(src_path, os.path.join(matched_dir, file))
                matched_count += 1
            else:
                shutil.move(src_path, os.path.join(unmatched_dir, file))
                unmatched_count += 1

        messagebox.showinfo(
            "分类完成",
            f"分类完成！\n\n匹配文件：{matched_count} 个\n未匹配文件：{unmatched_count} 个"
        )

    except Exception as e:
        messagebox.showerror("错误", f"发生错误：\n{e}")

if __name__ == "__main__":
    main()