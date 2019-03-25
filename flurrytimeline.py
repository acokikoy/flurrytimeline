""" flurrytimeline.py - ログのタイムライン表示 """
from datetime import datetime
import logging

import responder

from flurrynote import load_notes
from flurrynote import search_by_page, search_by_date, search_by_tag
from flurrynote import MAX_PER_PAGE

notes = load_notes()
api = responder.API()


@api.route("/")
@api.route("/page")
def show_timeline(req, resp):
    # 一番最近のログ 20件を表示する
    idx_end = len(notes)
    idx_begin = idx_end - MAX_PER_PAGE
    if idx_begin < 0:
        idx_begin = 0
    
    resp.html = api.template(
                'index.html', 
                tmpl_notes = notes, 
                tmpl_idx   = [x for x in range(idx_begin, idx_end)], 
                tmpl_page  = 0
                )


# http://127.0.0.1:5042/p/2
@api.route("/p/{str_page}")
def show_by_page(req, resp, *, str_page):
    resp.html = api.template(
                'index.html', 
                tmpl_notes = notes, 
                tmpl_idx   = search_by_page(notes, int(str_page)), 
                tmpl_page  = str_page
                )

# http://127.0.0.1:5042/d/2019-03-19
@api.route("/d/{str_date}")
def show_by_date(req, resp, *, str_date):
    resp.html = api.template(
                'by_date.html', 
                tmpl_notes = notes, 
                tmpl_idx   = search_by_date(notes, str_date), 
                tmpl_date  = str_date
                )


def main():
    api.run()

    # タイムラインを表示して、コマンド待ち
    # notes = load_notes()
    # show_timeline(notes, [x for x in range(idx_begin, idx_end)])

    # while True:
    #     cmd_in = input('input command: [q]uit, [p]revious day, [n]ext day, [ID]modify data   ')
    #     cmd = cmd_in.strip()

    #     if cmd == 'q':
    #         print("Bye!")
    #         break

    #     if cmd == 'p':
    #         print("Prev 20")
    #         # 前の20件
    #         idx = search_by_page(notes, idx, dir='prev')
    #         show_timeline(notes, idx)
    #         continue

    #     if cmd == 'n':
    #         print("Next 20")
    #         # 次の20件
    #         idx = search_by_page(notes, idx, dir='next')
    #         show_timeline(notes, idx)
    #         continue

    #     if cmd == 't':
    #         print("tag")
    #         idx = search_by_tag(notes, tag="tag1")
    #         show_timeline(notes, idx)
    #         continue

    #     if cmd.isdecimal():
    #         pass


if __name__ == '__main__':
    main()
