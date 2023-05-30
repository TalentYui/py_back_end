import sys
import code
from OpenSSL import SSL

from flask import Flask,request,jsonify





root=Flask(__name__)






class __Autonomy__(object):
        """
        自定义变量的write方法
        """
        def __init__(self):
            """
            init
            """
            self._buff = ""

        def write(self, out_stream):
            """
            :param out_stream:
            :return:
            """
            self._buff += out_stream



@root.route('/', methods=['GET', 'POST'])

def index():
    
    varName = request.args.get('varName')
    stdin = request.args.get('stdin')
    print(varName,stdin)
    try:

        cppacdb = code.compile_command(varName, "<string>", "exec")
        

        current = sys.stdout
        accbbthg = __Autonomy__()
        
        sys.stdout = accbbthg

    
        exec(cppacdb,{'input': lambda prompt=stdin: prompt})

        
        sys.stdout = current

        # 打印缓冲区中的内容
        fuuoca=accbbthg._buff
        
        
        response = jsonify({'result': fuuoca})
        return response


    except Exception as e:
        return {'result': str(e)}



if __name__ =='__main__':
    root.run(host="0.0.0.0", port=443,  threaded=True, ssl_context=('C:/Users/Administrator/Desktop/VX/zsynb.online_bundle.crt','C:/Users/Administrator/Desktop/VX/zsynb.online.key') )
















