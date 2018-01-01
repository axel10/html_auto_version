import os
import re
import uuid


def file_extension(path):
    return os.path.splitext(path)[1]


basePath = "D:\\auto_version\\html"
html_list = []


def find_html(path):
    files = os.listdir(path=path)

    for item in files:
        abs_path = os.path.join(path, item)
        if not os.path.isdir(abs_path) and file_extension(abs_path) == ".html":
            html_list.append(abs_path)

        if (os.path.isdir(abs_path)):
            find_html(abs_path)


def deal_html(html_list):
    for html_path in html_list:
        html_file = open(html_path, "r+")
        content = html_file.read()
        # print(html_file.read())
        # res = re.sub(r'<link (.*) href="(.*)\.css".*>',r'<link \1 href="\2\.css?v=1"\3>',content)
        res1 = re.sub(r'<link (.*) href="(.*)\.css.*"(.*)>', lambda x: '<link ' + x.group(1) + ' href="' + x.group(
            2) + '.css?v=' + uuid.uuid1().hex + '"' + x.group(3) + '>', content)
        res2 = re.sub(r'<script src="(.*)\.js.*"></script>',
                      lambda x: '<script src="' + x.group(1) + '.js?v=' + uuid.uuid1().hex + '"></script>', res1)
        html_file.seek(0)
        html_file.truncate()
        html_file.write(res2)
        html_file.close()


if __name__ == '__main__':
    find_html(basePath)
    deal_html(html_list)
