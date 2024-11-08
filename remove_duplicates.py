#去掉重复的域名
def remove_duplicates(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        # 使用集合去重
        unique_lines = set(lines)

        # 写回文件
        with open(file_path, "w") as file:
            file.writelines(unique_lines)

        print("去重完成！")

    except Exception as e:
        print(f"发生错误：{e}")

remove_duplicates("available_domains.txt")