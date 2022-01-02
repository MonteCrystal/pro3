import subprocess, os

from flask import request, jsonify

from server.app.init import app, db
from server.app.models.model import DataObj, Record, Query, Algorithm
from server.app.controllers.user import getfilename, getuid


def upload():
    cnt = request.form['cnt']
    files = []
    for i in range(int(cnt)):
        file = request.files['file' + str(i + 1)]
        filetype = gettype(file.content_type)
        filename = getfilename(filetype)

        dataObj = DataObj()
        dataObj.set(addr_front_to_back(filename), getuid(), filetype)# 后端存储位置f"../public/static/uploads/dataobjs/{uid}{oid}.{type.lower()}"
        dataObj.save(file)
        files.append({'filename':filename, 'id':dataObj.id})# 前端访问的：f"/static/uploads/dataobjs/{uid}{oid}.{type.lower()}"
    return jsonify({'code': 200, 'msg': 'success', 'filearr': files})


def addr_front_to_back(front):
    return f"../public{front}"


def gettype(mime):
    if mime == 'image/jpeg':
        return 'JPG'
    if mime == 'application/octet-streamg':
        return 'MP4'
    if mime == 'image/png':
        return 'PNG'
    if mime == 'image/gif':
        return 'GIF'
    if mime.split('/')[0] == 'text':
        return 'STR'
    return None


def generate_record():
    data = request.get_json(silent=True)
    img_ids = data['images']
    algo_ids = data['algos']

    record = Record()
    record.set(getuid())
    record.save()

    record_id = record.id

    for ipt_id in img_ids: # 这里用的是图片的id
        ipt_id = int(ipt_id)
        for algo_id in algo_ids: # 和算法的id
            algo_id = int(algo_id)
            query = Query()
            otpt_id = run_algo_on_ipt(algo_id, ipt_id)
            query.set(record_id, ipt_id, algo_id, otpt_id)
            query.save()
    return jsonify({'record_id': record_id})


def run_algo_on_ipt(algo_id, input_id):
    algo = db.session.query(Algorithm).filter(Algorithm.id == algo_id).first()
    algo_addr = f"../public{algo.address}"
    outetype = algo.output_type.lower()
    inpt_addr = db.session.query(DataObj.address).filter(DataObj.id == input_id).first()[0]
    otpt_addr = getfilename(outetype)

    dataObj = DataObj()
    dataObj.set(addr_front_to_back(otpt_addr), getuid(), outetype)
    dataObj.save()

    otpt_addr = otpt_addr.split('/')[-1]
    otpt_addr = f"../public/static/uploads/dataobjs/{otpt_addr}"
    subprocess.Popen(f'python {algo_addr} {inpt_addr} {otpt_addr}', cwd=os.getcwd())
    return dataObj.id

