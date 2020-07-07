from datetime import datetime
from nameko.rpc import rpc
from rpc_run.rpc_config import MsBase, user_, uid_, ES_HOST, ES_NAME, ES_PASS
from rpc_run.models import GnerateDoc
from generate import GenerateObj
from wisdoms.commons import success, revert, codes
from wisdoms.es_db import EsSearch
from elasticsearch_dsl import Q, search

es = EsSearch(ES_HOST, http_auth=(ES_NAME, ES_PASS))


class Gpt2(MsBase):
    name = "Gpt2App"

    @rpc
    def get_text(self, req):
        '''
        向手机发送验证码
        :param req:
        :return:
        '''
        data = req["data"]
        # 生成验证码
        res = GenerateObj.main(**data)
        return success(res)

    @rpc
    @user_
    def create_doc(self, req):
        '''
        创建文档
        :param req:
        :return:
        '''
        user = req["user"]
        data = req["data"]
        g_doc = GnerateDoc()
        data["user_id"] = user.get("id")
        data["user_phone"] = user.get("account")

        for d in data:
            if data.get(d) is not None:
                setattr(g_doc, d, data.get(d))
        g_doc.create_time = str(datetime.now())
        g_doc.save()

        return success()

    @rpc
    @user_
    def update_doc(self, req):
        '''
        更新文档
        :param req:
        :return:
        '''
        user = req["user"]
        data = req["data"]
        index_id = data.get("index_id")
        g_doc = GnerateDoc().get(index_id)
        if g_doc.user_id != user.get("id"):
            return revert(codes.ERROR, desc="没权限修改")

        for d in data:
            if data.get(d) is not None:
                if hasattr(g_doc, d):
                    setattr(g_doc, d, data.get(d))
        g_doc.update_time = str(datetime.now())
        g_doc.save()

        return success()

    @rpc
    @user_
    def get_mydoc(self, req):
        '''
        获取文档
        :param req:
        :return:
        '''
        user = req["user"]
        data = req["data"]
        uid = user.get('id')

        res = es.es_search(GnerateDoc.Index.name, user_id=uid, **data)

        return success(res)


if __name__ == "__main__":
    res = Gpt2().get_text({"data": {'star_str': "手风钻", 'length': 20, 'nsamples': 2}})
    print(res)
