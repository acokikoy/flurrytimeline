""" flurryin.py - 1行ログ入力 """
from datetime import datetime

from flurrynote import add_note
from flurrynote import create_file
from flurrynote import load_notes


F_PATH = 'log.tsv'
F_ITEMS = ['created_on', 'body', 'tags', 'detail', 'main_task']


def main():
    # ファイルがなければ新規作成して1行目に項目行を書き込む。
    create_file()

    note = {}

    while 1:
        str_input = input("なんか気になった？: ")
        if str_input == 'q':
            break

        note['created_on'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if str_input.startswith('m '):
            # 「m 」から始まってたら、その文字列で "現在のメインタスク" を書き換える
            note['main_task'] = str_input[2:]
        else:
            note['body'] = str_input
            add_note(note) # 今回のログを記録

    print('お疲れ様でした。今日のふらり〜は次の通りです。\n','*'*20)
    notes = load_notes()
    prev_main_task = ''
    for note in notes:
        # メインタスクは切替わるタイミングで表示し、前回同様なら省略
        if prev_main_task != note['main_task']:
            print(note['main_task'], '-------------------')
            prev_main_task = note['main_task']

        print(f"\ton {note['created_on']}: {note['body']}")

if __name__ == '__main__':
    main()
