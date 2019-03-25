""" Flurry Notes 
notes: 1ログ分がdict型で、それのリスト（暫定）
notes = [
    {
      'created_on': '2019-02-16 16:40:00',
      'body': '本文', 
      'tags': 'python, foo, bar', 
      'detail': '詳しい内容', 
      'main_task': '本来やってたメインタスク'
    }.
    { ...
    }
]
idx: 表示対象noteのインデックスをリストで入れてる
idx = [0, 1, 2, 3, 6]
"""
import csv
from datetime import datetime, timedelta
import os


# CONSTANTS
CSV_PATH = 'log.tsv'
CSV_ITEMS = ['created_on', 'body', 'tags', 'detail', 'main_task']
MAX_PER_PAGE = 5

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
    """ ファイルから全件読み出してdisc型のリストとして返す """
    with open(CSV_PATH, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter='\t')
        notes = []
        for row in reader:
            notes.append(dict(row))
        return notes


def update_notes(path):
    """ notesを指定パスのファイルに書き出し保存する """
    print("ファイルに保存しました")



def search_by_date(notes, str_date):
# 指定日分のログを取り出す
    idx = []
    for i, note in enumerate(notes):
        if str_date in note['created_on']:
            idx.append(i)
        elif idx:
            return idx

    return idx


def search_by_page(notes, page):
    """ 指定範囲のログを取り出す """

    begin = page * MAX_PER_PAGE
    end = begin + MAX_PER_PAGE

    if end > len(notes):
            end = len(notes)

    if begin > len(notes):
            begin = len(notes) - MAX_PER_PAGE

    return [x for x in range(begin, end)]

def search_by_tag(notes, tag):
    """ 指定タグのログを取り出す """
    idx = []
    for i, note in enumerate(notes):
        if tag in note['tags']:
            idx.append(i)
    return idx


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
