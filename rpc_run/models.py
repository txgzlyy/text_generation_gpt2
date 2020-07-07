from elasticsearch_dsl import Document, Text, Keyword, Integer, Nested, Date
from rpc_run.rpc_config import ES_PASS, ES_NAME, ES_HOST
from elasticsearch_dsl.connections import connections

connect = connections.create_connection(hosts=[ES_HOST], http_auth=(ES_NAME, ES_PASS))


class GnerateDoc(Document):
    '''
    文档自动生成所保存的生成文档
    '''
    user_id = Integer(fields={'keyword': Keyword()})
    user_phone = Text(fields={'keyword': Keyword()})
    doc_tittle = Text(fields={'keyword': Keyword()})
    doc_body = Text()
    doc_status = Text(fields={'keyword': Keyword()})
    create_time = Date()
    update_time = Date()

    class Index:
        name = "generate_doc"


if __name__ == "__main__":
    # GnerateDoc.init()

    res = GnerateDoc().get(id="1i0oKHMBXo6QS--SixFv")
    a = hasattr(res, "doc_status")
    print(a)
