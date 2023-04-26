from dataclasses import dataclass


@dataclass
class OperatorSearchInfo:
    name: str = ''
    level: int = 0
    skill: str = ''
    skin_key: str = ''
    voice_key: str = ''
    story_key: str = ''
    skill_index: int = 0


class InitData:
    sp_type = {
        1: '自动回复',
        2: '攻击回复',
        4: '受击回复',
        8: '被动'
    }
    class_type = {
        1: '先锋',
        2: '近卫',
        3: '重装',
        4: '狙击',
        5: '术师',
        6: '辅助',
        7: '医疗',
        8: '特种'
    }
    skill_type = {
        0: '被动',
        1: '手动触发',
        2: '自动触发'
    }
    skill_level = {
        1: '等级1',
        2: '等级2',
        3: '等级3',
        4: '等级4',
        5: '等级5',
        6: '等级6',
        7: '等级7',
        8: '专精1',
        9: '专精2',
        10: '专精3'
    }
    skill_index_list = {
        '1技能': 1, '2技能': 2, '3技能': 3
    }
    skill_level_list = {
        '精1': -1, '精英1': -1,
        '精2': -2, '精英2': -2,
        '1级': 1, '等级1': 1,
        '2级': 2, '等级2': 2,
        '3级': 3, '等级3': 3,
        '4级': 4, '等级4': 4,
        '5级': 5, '等级5': 5,
        '6级': 6, '等级6': 6,
        '7级': 7, '等级7': 7,
        '专1': 8, '专精1': 8,
        '专2': 9, '专精2': 9,
        '专3': 10, '专精3': 10
    }
    potential_rank = {
        1: '一',
        2: '丅',
        3: '上',
        4: '止',
        5: '正'
    }
    keyword = [
        '模组', '资料', '简历'
    ]
    skins = [
        '皮肤', '服装', '衣服', '时装', '立绘'
    ]
    voices = [
        '任命助理', '任命队长', '编入队伍', '问候', '闲置',
        '交谈1', '交谈2', '交谈3', '晋升后交谈1', '晋升后交谈2',
        '信赖提升后交谈1', '信赖提升后交谈2', '信赖提升后交谈3',
        '精英化晋升1', '精英化晋升2',
        '行动出发', '行动失败', '行动开始', '3星结束行动', '4星结束行动', '非3星结束行动',
        '选中干员1', '选中干员2', '部署1', '部署2', '作战中1', '作战中2', '作战中3', '作战中4',
        '戳一下', '信赖触摸', '干员报到', '进驻设施', '观看作战记录', '标题'
    ]
    ignore_keywords = [
        '兔兔山',
        '兔兔夕'
    ]
