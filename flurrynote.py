""" Flurry Notes 
notesはdict型（暫定）
notes = {
      'created_on': 2019-02-16 16:40:00,
      'body': '本文', 
      'tags': 'python, foo, bar', 
      'detail': '詳しい内容', 
      'main_task': '本来やってたメインタスク'
    }
"""
import csv
import os


# CONSTANTS
CSV_PATH = 'log.tsv'
CSV_ITEMS = ['created_on', 'body', 'tags', 'detail', 'main_task']

def create_file():
    """ ファイルがなければ新規作成して1行目に項目行を書き込む。"""
    if not os.path.isfile(CSV_PATH):
        with open(CSV_PATH, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, CSV_ITEMS, delimiter='\t')
            writer.writeheader()

def add_note(note):
    """ 指定ファイルに、ログを一件追加する """
    with open(CSV_PATH, 'a', encoding='utf-8', newline='') as csv_file:
       writer = csv.DictWriter(csv_file, CSV_ITEMS, delimiter='\t')
       writer.writerow(note) # 今回のログを書き込む


def load_notes():
    """ ファイルから読み出してdisc型のリストとして返す """
    with open(CSV_PATH, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter='\t')
        notes = []
        for row in reader:
            notes.append(dict(row))
        return notes


def update_notes(path):
    """ notesを指定パスのファイルに書き出し保存する """
    print("ファイルに保存しました")

# class FlurryNote:
#     """
#     fn = FlurryNote(body)
#         fn.id (int)　・・・一意な通し番号。編集用に使う
#         fn.body (str) = body
#         fn.c_date (datetime)
#         fn.tags (str)
#         fn.detail (str)
#     """
#     last_num = 0

#     def __init__(self, body, c_date=None, tags='', detail=''):
#         """ 一意なidを発行する, c_dateが無指定なら現在時刻をセットして、tagとdetailも初期化する """
#         FlurryNote.last_num += 1
#         self.id = FlurryNote.last_num

#         icsv_file c_date is None:
#             self.c_date = datetime.now()
#         else:
#             self.c_date = c_date

#         self.body = body
#         self.tags = tags
#         self.detail = detail



#     def edit_note(self, body, tags, detail):
#         """ 本文、タグ、詳細メモを上書き編集 """
#         self.body = body
#         self.tags = tags
#         self.detail = detail
