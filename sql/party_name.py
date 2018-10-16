# ！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Copyright 2018 The Author. All Rights Reversed.
------------------------------------------------------------
File Name:
Author : zhangtao
Time:
Description：
------------------------------------------------------------
"""
import openpyxl

import re
import regex_openlaw as openlaw

def party_IE(text_string):
    list_temp = []
    text = re.split('、[上被]', text_string)
    if len(text) >= 1:
        for i in range(1, len(text)):
            names = openlaw.get_accused_person(text[i])

            if len(names) == 1:
                people = openlaw.get_people(text[i])
                if people == []:
                    people = None
                else:
                    people = people[0]
                province = openlaw.get_province(text[i])
                if province == []:
                    province = None
                else:
                    province = province[0]

                gender = openlaw.get_gender(text[i])
                if gender == []:
                    gender = None
                else:
                    gender = gender[0]
                edu_level = openlaw.get_edu_level(text[i])
                if edu_level == []:
                    edu_level = None
                else:
                    edu_level = edu_level[0]
                birth_place = openlaw.get_birth_place(text[i])

                if birth_place != None:
                    birth_place = birth_place[0]
                born_date = openlaw.get_born_date(text[i])
                if born_date == []:
                    born_date = None
                else:
                    born_date = born_date[0]
                lawyer = openlaw.get_lawyer(text[i])
                law_firm = openlaw.get_law_firm(text[i])

                if len(lawyer) != 0:
                    if len(lawyer) == len(law_firm):
                        for lawyer_num in range(len(lawyer)):

                            list_temp.append([names, people, province, gender, edu_level, birth_place ,born_date ,lawyer[lawyer_num], law_firm[lawyer_num]])
                else:
                    list_temp.append([names, people, province, gender, edu_level, birth_place, born_date, None, None])



    else:
        list_temp = [None, None, None, None, None, None, None, None, None]

    return list_temp


if __name__ == '__main__':
    temp_str = '公诉机关广西壮族自治区天峨县人民检察院。、被告人陈毓焕，男。、因涉嫌贪污罪，于2013年3月25日被刑事拘留，同年4月8日被逮捕，同年6月21日天峨县人民检察院对其取保候审。、现住天峨县六排镇城东路275号。、辩护人班华进，男，天峨县法律援助中心律师。、被告人姚胜军，男。、因涉嫌贪污罪于2013年3月25日被刑事拘留，同年4月8日被逮捕，同年6月4日天峨县人民检察院对其取保候审。、现住天峨县政府大院。、被告人梁保成，男。、因涉嫌贪污罪于2013年3月29日被刑事拘留，同年4月8日被逮捕，同年5月3日天峨县人民检察院对其取保候审，现住大化县岩滩镇东杠村先下屯24号。、被告人曾运进，男。、因涉嫌贪污罪于2013年3月29日被刑事拘留，同月11日天峨县人民检察院对其取保候审。、现住天峨县更新乡更新街。'
    print(party_IE(temp_str))