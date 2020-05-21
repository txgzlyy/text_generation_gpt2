from nameko.rpc import rpc
from rpc_run.rpc_config import MsBase, user_, uid_
from generate_tzxd import GenerateObj
from wisdoms.commons import success, revert, codes


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


if __name__ == "__main__":
    res = Gpt2().get_text({"data": {'star_str': "手风钻", 'length': 20, 'nsamples': 2}})
    print(res)
