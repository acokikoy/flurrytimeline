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
import logging
import os


# CONSTANTS
CSV_PATH = 'log.tsv'
CSV_ITEMS = ['created_on', 'body', 'tags', 'detail', 'main_task']
MAX_PER_PAGE = 5

def create_file(path=CSV_PATH):
    """ ファイルがなければ新規作成して1行目に項目行を書き込む。"""
    if not os.path.isfile(path):
        with open(path, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, CSV_ITEMS, delimiter='\t')
            writer.writeheader()


def load_notes(path=CSV_PATH):
    """ ファイルから全件読み出してdisc型のリストとして返す """
    with open(path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter='\t')
        notes = []
        for row in reader:
            notes.append(dict(row))
        return notes

def save_notes(notes, path=CSV_PATH):
    """ ファイルをnotesで上書き更新 """
    with open(path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, CSV_ITEMS, delimiter='\t')
        writer.writeheader()
        writer.writerow(notes)
    # logging.info("notes: ", notes)
    # logging.info("save_notes: ファイルに保存しました")


def add_note(note, path=CSV_PATH):
    """ 指定ファイルの末尾に、ログを1件追加する """
    with open(path, 'a', encoding='utf-8', newline='') as csv_file:
       writer = csv.DictWriter(csv_file, CSV_ITEMS, delimiter='\t')
       writer.writerow(note) # 今回のログを書き込む


def update_note(notes, id, note, path=CSV_PATH):
    """ 指定ファイルの指定レコードを上書き更新する
        ただし今は全件上書き更新している """
    notes[id] = note
    save_notes(notes)


def search_by_mode(notes, mode, mode_value):
    def _search_by_date(notes, str_date):
    # 指定日分のログを取り出す
        idx = []
        for i, note in enumerate(notes):
            if str_date in note['created_on']:
                idx.append(i)
            elif idx:
                return idx
        return idx


    def _search_by_page(notes, str_page):
        """ 指定範囲のログを取り出す """

        begin = int(str_page) * MAX_PER_PAGE
        end = begin + MAX_PER_PAGE

        if end > len(notes):
                end = len(notes)

        if begin > len(notes):
                begin = len(notes) - MAX_PER_PAGE

        return [x for x in range(begin, end)]


    def _search_by_tag(notes, tag):
        """ 指定タグのログを取り出す """
        idx = []
        for i, note in enumerate(notes):
            if tag in note['tags']:
                idx.append(i)
        return idx

    if mode == 'page':
        return _search_by_page(notes, mode_value)
    elif mode == 'date':
        return _search_by_date(notes, mode_value)
    elif mode == 'tag':
        return _search_by_tag(notes, mode_value)



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
