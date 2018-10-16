# ！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
© Copyright 2018 The Author. All Rights Reversed.
------------------------------------------------------------
File Name: 
Author : zhangtao 
Time:
Description：
------------------------------------------------------------
"""
from regex_openlaw import *


def extraction(table, i):



    # 标题 table.cell(i, 1).value
    title = table.cell(i, 1).value

    # 案号 table.cell(i, 2).value
    case_number = table.cell(i, 2).value

    # 案件类型 table.cell(i, 3).value
    case_type = table.cell(i, 3).value

    # 庭审程序 table.cell(i, 4).value
    procedure_of_court_trial = table.cell(i, 4).value

    # 案由 table.cell(i, 5).value
    cause_of_action = table.cell(i, 5).value

    # 文书类型 table.cell(i, 6).value
    Document_type = table.cell(i, 6).value

    # 法院 table.cell(i, 7).value
    court = table.cell(i, 7).value

    # 判决日期 table.cell(i, 8).value
    judgment_date = table.cell(i, 8).value

    # 原告 table.cell(i, 9).value
    plaintiff = table.cell(i, 9).value

    # 被告 table.cell(i, 9).value
    defendant = table.cell(i, 10).value

    # 法官 table.cell(i, 12).value
    judge = table.cell(i, 12).value

    # 审判长 table.cell(i, 13).value
    presiding_judge = table.cell(i, 13).value

    # 审判员 table.cell(i, 14).value
    judicial_officer = table.cell(i, 14).value

    # 书记员 table.cell(i, 15).value
    court_clerk = table.cell(i, 15).value

    # 头部 # table.cell(i, 16).value

    # 当事人(party) table.cell(i, 18).value
    # Prosecutor province accused_person gender born_date birth_place people edu_level lawyer law_firm

    party = str(table.cell(i, 18).value)

    party_Prosecutor = get_Prosecutor(party)
    party_province = get_province(party)
    party_gender = get_gender(party)
    party_born_date = get_born_date(party)
    party_birth_place = get_birth_place(party)
    party_people = get_people(party)
    party_edu_level = get_edu_level(party)
    party_lawyer = get_lawyer(party)
    party_faw_firm = get_law_firm(party)


    # 庭审程序说明(Explanation_of_trial_procedure) table.cell(i, 21).value
    Explanation_of_trial_procedure = table.cell(i, 21).value




    #Explanation_of_trial_procedure = table.cell(i, 20).value

    # 庭审过程(Trial_process) table.cell(i, 22).value
    #Trial_process = table.cell(i, 22).value

    # 法院意见 table.cell(i, 28).value
    # 判决结果 table.cell(i, 29).value
    # 法院意见 table.cell(i, 30).value


    return title, case_number, case_type, procedure_of_court_trial, cause_of_action, Document_type, court, judgment_date, plaintiff, defendant, judge, presiding_judge, judicial_officer, court_clerk, party_Prosecutor, party_province, party_gender, party_born_date, party_birth_place, party_people, party_edu_level, party_lawyer, party_faw_firm
