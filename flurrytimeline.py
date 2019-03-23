""" flurrytimeline.py - ログのタイムライン表示 """
from datetime import datetime

from flurrynote import add_note, create_file, load_notes
from flurrynote import search_by_page, search_by_date, search_by_tag
from flurrynote import MAX_PER_PAGE


def show_timeline(notes, idx: list):
    """ 指定インデックスのログを表示する """
    for i in idx:
        print(f"on {notes[i]['created_on']}: {notes[i]['body']}")



def main():
    # タイムラインを表示して、コマンド待ち
    notes = load_notes()
    print(notes)

    # 一番最近のログ 20件を表示する
    idx_end = len(notes)
    idx_begin = idx_end - MAX_PER_PAGE
    if idx_begin < 0:
        idx_begin = 0

    show_timeline(notes, [x for x in range(idx_begin, idx_end)])


    while True:
        cmd_in = input('input command: [q]uit, [p]revious day, [n]ext day, [ID]modify data   ')
        cmd = cmd_in.strip()

        if cmd == 'q':
            print("Bye!")
            break

        if cmd == 'p':
            print("Prev 20")
            # 前の20件
            idx = search_by_page(notes, idx, dir='prev')
            show_timeline(notes, idx)
            continue

        if cmd == 'n':
            print("Next 20")
            # 次の20件
            idx = search_by_page(notes, idx, dir='next')
            show_timeline(notes, idx)
            continue

        if cmd == 't':
            print("tag")
            idx = search_by_tag(notes, tag="tag1")
            show_timeline(notes, idx)
            continue

        if cmd.isdecimal():
            pass


    # case [add_tag]:
    """ タグ追加 - 指定idのnoteにタグを追加する
        
        指定idのnoteを読み出す
        タグを付加して、noteを上書き保存する
        書き込みに成功したらTrueを返しておしまい
        
        Args:
            note_id (str)   : noteのid
            tags (str)      : tag1, tag2, tag3
        
        Returns:
            bool: True
        
    """


    # case [add detail]:
    """詳しい説明追加
    
    指定idのnoteに詳しい説明文を追加する
    
    Args:
        note_id(str) : noteのid
        detail(str) : 詳しい説明   
    
    Returns:
        bool: True成功
    
    """


    # case [select by tag]:
    """タグで抽出
    
    指定タグに合致するnoteを一覧する
    
    Args:
        tag (str): タグ
    
    Returns:
        notes: 条件に合うnoteをリストで返すとか？
    
    """



if __name__ == '__main__':
    api.run()
    main()
