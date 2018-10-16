# ！/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
正则化模块
'''

import re

# 顿号字符切割


def split_text(text):

    split_text = re.split('、', text)

    return split_text

# 当事人


def get_Prosecutor(text):
    pattern = re.compile("公诉机关(.+?)。")
    Prosecutor = pattern.findall(text)
    return Prosecutor


def get_province(text):

    pattern = re.compile('北京市|天津市|上海市|重庆市|河北省|山西省|辽宁省|吉林省|'
                                  '黑龙江省|江苏省|浙江省|安徽省|福建省|江西省|山东省|河南省|'
                                  '湖北省|湖南省|广东省|海南省|四川省|贵州省|云南省|陕西省|'
                                  '甘肃省|青海省|台湾省|内蒙古自治区|广西壮族自治区|西藏自治区|'
                                  '宁夏回族自治区|新疆维吾尔自治区|香港特别行政区|澳门特别行政区')
    province = pattern.findall(text)
    return province


def get_accused_person(text):
    pattern = re.compile('告人）{0,1}(.+?)[，。]')
    accused_person = pattern.findall(text)
    return accused_person


def get_gender(text):

    # pattern = re.compile('，男，|，男。|,男,|，女，|，女。|,女,')
    pattern = re.compile('[男女]')
    gender = pattern.findall(text)
    return gender


def get_born_date(text):
    pattern = re.compile('([\d]{4}年[\d]+月[\d]+日)出生')
    born_date = pattern.findall(text)
    return born_date


def get_birth_place(text):
    pattern = re.compile(r'，([\u4e00-\u9fa5]{2,20})人，|生[于地](.+?)，|住([\u4e00-\u9fa5]{2,20})。、')
    birth_place = pattern.findall(text)
    for (x, y, z) in birth_place:
        return x+y+z


def get_people(text):
    pattern = re.compile('，(汉族|蒙古族|回族|藏族|维吾尔族|苗族|彝族|壮族|布依族'
                                '|朝鲜族|满族|侗族|瑶族|白族|土家族|哈尼族|哈萨克族'
                                '|傣族|黎族|僳僳族|佤族|畲族|高山族|拉祜族|水族|东乡族'
                                '|纳西族|景颇族|柯尔克孜族|土族|达斡尔族|仫佬族|羌族'
                                '|布朗族|撒拉族|毛南族|仡佬族|锡伯族|阿昌族|普米族'
                                '|塔吉克族|怒族|乌孜别克族|俄罗斯族|鄂温克族|德昂族'
                                '|保安族|裕固族|京族|塔塔尔族|独龙族|鄂伦春族|赫哲族'
                                '|门巴族|珞巴族|基诺族)，')

    people = pattern.findall(text)
    return people


def get_edu_level(text):

    pattern = re.compile('，(博士|研究生文化|硕士|大学文化|本科文化|文化程度大学|文化程度本科|'
                            '大学本科|大专文化|文化程度大专|中专文化|文化程度中专|专科文化|'
                            '高中文化|文化程度高中|初中文化|文化程度初中|小学文化|文化程度小学|农民)，')
    edu_level = pattern.findall(text)
    return edu_level


def get_lawyer(text):

    # pattern = re.compile('辩护人.{1,4}，|辩护人.{1,4}、.{0,4}，|辩护人.{1,4}、.{0,4}、.{0,4}，')
    pattern = re.compile('辩护人(.+?)，')

    lawyer = pattern.findall(text)
    return lawyer


def get_law_firm(text):

    pattern = re.compile('[\u4e00-\u9fa5]{1,20}律师事务所|[\u4e00-\u9fa5]{1,20}援助中心律师')
    law_firm = pattern.findall(text)

    return law_firm

# 庭审程序说明


def get_Court_proceedings_time(text):
    pattern =  re.compile('于(.+?)[作向以]')
    Court_proceedings_time = pattern.findall(text)
    return Court_proceedings_time


# 庭审过程
def get_date(text):
    # pattern = re.compile('\d{4}年\d{1,2}月至\d{4}年\d{1,2}月|\d{4}年\d{1,2}月|\d{4}年\d{1,2}、\d{1,2}月|\d{4}年')
    pattern = re.compile(
    ''''' 
    \d{4}年\d{1,2}月、{0,1}\d{0,2}月{0,1}至\d{4}年\d{1,2}月、{0,1}\d{0,2}月{0,1}|
    \d{4}年\d{1,2}月至\d{4}年\d{1,2}月|  # year-month
    \d{4}年\d{0,2}月{0,1}至\d{4}年\d{0,2}月{0,1}|                    # year
    \d{4}年\d{0,2}月{0,1}\d{0,1}日{0,1}
    ''',
    re.VERBOSE)

    result = pattern.findall(text)
    return result


def get_money_number(text):
    pattern = re.compile('\d{1,20}.{0,1}\d{0,5}万{0,1}元')
    result = pattern.findall(text)
    return result



# 法院意见
#
# def get_court_opinion(text):
#     pattern = re.compile('述(.+？)。')
#
#     court_opinion = pattern.findall(text)
#     return court_opinion



# 判决结果
def get_judgment_result(text):

    pattern = re.compile('判决如下.+|裁定如下:.+|判处如下.+|判决:.+|'
                                        '如下判决:.+|判决书如下:.+|判决意见如下:.+|决定如下:.+')

    judgment_result = pattern.findall(text)

    return  judgment_result


def get_legal_basis(text):

    pattern = re.compile(r'依照(.+?)[之的]规定')

    legal_basis = pattern.findall(text)

    return legal_basis


def get_is_surrendere(text):

    pattern = re.compile('认定自首|处理自首')

    legal_basis = pattern.findall(text)

    return legal_basis

def get_accusation(text):

    pattern = re.compile('贪污罪|挪用公款罪|受贿罪|单位受贿罪|行贿罪|对单位行贿罪|介绍贿赂罪|单位行贿罪|巨额财产来源不明罪|隐瞒境外存款罪|私分国有资产罪|私分罚没财物罪')
    accusation = pattern.findall(text)
    return accusation


def get_court_opinion(text):
    pattern = re.compile('原判决{0,1}(.+?)。')
    court_opinion = pattern.findall(text)
    return court_opinion


"""
------- FUCTION -------
0 split_text(text)  顿号字符切割
1 get_Prosecutor(text)  (公诉机关)
2 get_province(text)
3 get_accused_person(text)  （获取被告）
4 get_gender(text)
5 get_born_date(text)
6 get_birth_place(text)
7 get_people(text)
8 get_edu_level(text)
9 get_lawyer(text)
10 get_law_firm(text)
11 get_judgment_result(text)
12 get_legal_basis(text)
13 get_is_surrendere(text)
14 get_paraclete(text)
16 get_accusation(text)
17 get_Court_proceedings_time(text)
18 get_court_opinion(text)
19 get_date(text)
20 get_money_number(text)

"""

if __name__ == '__main__':
    print('This is regex fuctions for openlaw!')