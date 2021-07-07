# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http.response import  HttpResponse

from django.shortcuts import render_to_response
import json
import os

def request(request):
    return HttpResponse('return_json')
    # reqs = request.get_full_path()
    # req = reqs.split('.json')[0].split('&')[-1]
    # url = '/Users/v_stxiao/Desktop/server_mock/templates/mock' + req + '.json'
    # jsonp = ['callback=', 'xiaoshuntao']
    # for i in jsonp:
    #     if i in req:
    #         callback_int = req.split('callback=')[1].split('&')[0]
    #         open_path = open(url, 'r')
    #         open_json = open_path.read()
    #         for_mat = json.loads(json.dumps(open_json))
    #         return_json = for_mat.replace((for_mat.split('(')[0]), callback_int)
    #         return HttpResponse(return_json)
    #     else:
    #         return render_to_response(url, content_type='application/json')
