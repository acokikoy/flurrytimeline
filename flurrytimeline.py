""" flurrytimeline.py - ログのタイムライン表示 """
from datetime import datetime

from flurrynote import add_note
from flurrynote import create_file
from flurrynote import load_notes


def main():
    # 今日1日分か、なければ直近のタイムライン20件を表示して、コマンド待ち
    notes = load_notes()

    target_notes = []
    str_today = datetime.today().strftime('%Y-%m-%d')

    for note in notes:
        # 本日のログを取り出す
        if str_today in note['created_on']:
            target_notes.append(note)

    if target_notes == []:
        # 本日のログが存在しないなら直近20件を使う
        MAX_LEN = 20

        if len(notes) < MAX_LEN:
            start = 0
        else:
            start = len(notes) - MAX_LEN

        target_notes = notes[start:]

    for note in target_notes:
        print(f"\ton {note['created_on']}: {note['body']}")


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
    pass

    # case [add detail]:
    """詳しい説明追加
    
    指定idのnoteに詳しい説明文を追加する
    
    Args:
        note_id(str) : noteのid
        detail(str) : 詳しい説明   
    
    Returns:
        bool: True成功
    
    """
    pass

    # case [select by tag]:
    """タグで抽出
    
    指定タグに合致するnoteを一覧する
    
    Args:
        tag (str): タグ
    
    Returns:
        notes: 条件に合うnoteをリストで返すとか？
    
    """






    pass


if __name__ == '__main__':
    main()
