""" Flurry Timeline - 1行ログ処理 """
from datetime import datetime
import csv
import os


# import flurrynote

F_PATH = 'log.tsv'
F_ITEMS = ['created_on', 'body', 'tags', 'detail', 'main_task']


def main():
    # ファイルがなければ新規作成して1行目に項目行を書き込む。
    if not os.path.isfile(F_PATH):
       with open(F_PATH, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, F_ITEMS, delimiter='\t')
            writer.writeheader()

    """
    note:
        'created_on':   ログ時刻, 
        'body':         ログ本文, 
        'main_task':    ログ時点で行なっていたメインタスク
    """    
    note = {}

    while 1:
        str_input = input("なんか気になった？: ")
        if str_input == 'q':
            break

        note['created_on'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if str_input.startswith('m '):
            # 「m 」から始まってたら現在のメインタスクを書き換える
            note['main_task'] = str_input[2:]
        else:
            note['body'] = str_input

            with open(F_PATH, 'a', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, F_ITEMS, delimiter='\t')
                writer.writerow(note) # 今回のログを記録


    with open(F_PATH, 'r', encoding='utf-8') as f:
        print('お疲れ様でした。今日のふらり〜は次の通りです。\n','*'*20)
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            print(row)

if __name__ == '__main__':
    main()
