""" Flurry Timeline - 1行ログ処理 """
from datetime import datetime
import csv
import os


# import flurrynote

F_PATH = 'log.tsv'
F_ITEMS = ['created_on', 'body', 'tags', 'detail']


def main():    
    while 1:
        str_input = input("なんか気になった？: ")
        if str_input == 'q':
            break

        note = {}
        note['created_on'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        note['body'] = str_input

        is_file = os.path.isfile(F_PATH)  # ファイルの存在判定用

        with open(F_PATH, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, F_ITEMS, delimiter='\t')
            if not is_file:
                # 新規ファイルなら、項目名を1行目に書き込む
            	writer.writeheader()

            writer.writerow(note) # 今回のログを記録


    with open(F_PATH, 'r', encoding='utf-8') as f:
        print('お疲れ様でした。今日のふらり〜は次の通りです。\n','*'*20)
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            print(row)

if __name__ == '__main__':
    main()
