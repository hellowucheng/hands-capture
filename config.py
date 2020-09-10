
class config(object):

    def __init__(self):

        # 共13种手势, 名称如下, 录制前将self.label设置为对应名称, 且请保证录制视频时务必只做单种手势
        """
        'zuoshou',
        'youshou',
        'shuangshou',
        'liu',
        'hezhang',
        'rock',
        'ok',
        'dianzan',
        'kaiqiang',
        'qitao',
        'baoquan',
        'bixin',
        'shizhi' """
        self.label = 'rock'

        # 0: 左手  1: 右手 2:双手 请保证单手和双手分别录制视频
        self.mode = 0

        # 下面的参数不用改
        self.name_dict = ['_shitou',
                          '_jiandao',
                          '_bu',
                          '_liu',
                          '_hezhang',
                          '_rock',
                          '_ok',
                          '_dianzan',
                          '_kaiqiang',
                          '_qitao',
                          '_baoquan',
                          '_bixin',
                          '_shizhi']
        self.color_map = [(255, 0, 0), (0, 0, 255)]

        self.video_path = 'Homemade_Hand/' + self.label + '.avi'
        self.save_path = 'Homemade_Hand/_' + self.label + '/'
        self.boxes_path = 'Homemade_Hand/_' + self.label + '/' + self.label + '_boxes.pickle'

args = config()