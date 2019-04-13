""" flurrytimeline.py - ログのタイムライン表示 """
from datetime import datetime
import logging
import time
import urllib

import responder

from flurrynote import load_notes, update_note
from flurrynote import search_by_mode
from flurrynote import MAX_PER_PAGE

notes = load_notes()
api = responder.API()


@api.route("/")
def show_timeline(req, resp):
    # 一番最近のログ 20件を表示する
    idx_end = len(notes)
    idx_begin = idx_end - MAX_PER_PAGE
    if idx_begin < 0:
        idx_begin = 0
    
    resp.html = api.template('index.html', 
                tmpl_notes = notes, 
                tmpl_idx   = [x for x in range(idx_begin, idx_end)], 
                tmpl_mode  = 'page',
                tmpl_mode_value = '0'
                )


# http://127.0.0.1:5042/p/2
@api.route("/p/{str_page}")
def show_by_page(req, resp, *, str_page):
    resp.html = api.template('index.html', 
                tmpl_notes = notes, 
                tmpl_idx   = search_by_mode(notes, mode='page', mode_value=str_page), 
                tmpl_mode  = 'page',
                tmpl_mode_value = str_page
                )

# http://127.0.0.1:5042/d/2019-03-19
@api.route("/d/{str_date}") 
def show_by_date(req, resp, *, str_date):
    resp.html = api.template('index.html', 
                tmpl_notes = notes, 
                tmpl_idx   = search_by_mode(notes, mode='date', mode_value=str_date), 
                tmpl_mode  = 'date',
                tmpl_mode_value  = str_date
                )

# http://127.0.0.1:5042/t/TAG
@api.route("/t/{str_tag}") 
def show_by_tag(req, resp, *, str_tag):
    resp.html = api.template('index.html', 
                tmpl_notes = notes, 
                tmpl_idx   = search_by_mode(notes, mode='tag', mode_value=str_tag), 
                tmpl_mode  = 'tag',
                tmpl_mode_value  = str_tag
                )


# http://127.0.0.1:5042/update
@api.route("/update")
async def update(req, resp):
    # await req.text=> id=5&tags=tag5&detail=detail5
    # qs_d=> {"id": ["12"], "tags": ["tag12"], "detail": ["detail12"]}
    qs_d = urllib.parse.parse_qs(await req.text)

    id = int(qs_d['id'][0])
    note = notes[id]
    note['tags'] = qs_d['tags'][0]
    note['detail'] = qs_d['detail'][0]
    update_note(notes, id, note)

    mode = qs_d['mode'][0]
    mode_value = qs_d['mode_value'][0]

    resp.html = api.template(
                'update.html', 
                tmpl_notes = notes,
                tmpl_updated_id = id,
                tmpl_idx   = search_by_mode(notes, mode, mode_value),
                tmpl_mode  = mode,
                tmpl_mode_value  = mode_value
                )


def main():
    api.run()


if __name__ == '__main__':
    main()
