from yacs.config import CfgNode as CN
from train.moran_v2 import train_moran_v2
# 在这个位置扩充函数

function_dict = {

    'MORAN' : train_moran_v2,
    'Your Model Name' : 'Your Model Function'
}


parser = argparse.ArgumentParser()
parser.add_argument('--config_file', required=True, help='path to config file')
opt = parser.parse_args()


def read_config_file(config_file):
    # 用yaml重构配置文件
    f = open(config_file)
    result = CN.load_cfg(f)
    return result

if __name__ == '__main__':

    # 通过 '_' 区分调用模型的名称，并调用函数
    model_name = opt.config_file.split('_')[0]
    function = function_dict[model_name]

    # 读取配置文件
    result = read_config_file(config_file)

    # 调用函数
    function(result)

