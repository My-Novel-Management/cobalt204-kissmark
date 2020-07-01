# -*- coding: utf-8 -*-
"""Config: The zebra-bra
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # zebrabra
        ("emi", "槙坂,笑美", 16, "female", "高校生", "me:わたし:S:わたし:ken:ケンさん:yumi:遊美:kmam:リアさん:masa:鈴村マサト"),
        ("ken", "陣野,ケン", 21, "male", "アパレル経営", "me:オレ:emi:エミちゃん:masa:マサ"),
        ("masa", "鈴村,マサト", 27, "male", "カメラマン", "me:俺:ken:ケン"),
        ("yumi", "武田,遊美", 16, "female", "高校生", "me:あたし:emi:エミ"),
        ("mother", "槙坂,母", 40, "female", "パート", "me:私:emi:笑美"),
        ("mamken", "陣野,リア", 42, "female", "パート", "me:私i:ken:ケン:emi:笑美ちゃん"),
        ("teacher", "先生", 50, "male", "高校教師", "me:私"),
        ("murata", "村田,健吾", 67, "male", "農家", "me:僕"),
        # kissmark
        ("hana", "蜂須賀,花", 20, "male", "大学生", "me:俺"),
        ("mizukawa", "水川", 20, "female", "大学生", "me:わたし"),
        ("mitsu", "ミッツ", 11, "female", "小学生", "me:わたし"),
        ("kitami", "喜多見", 24, "male", "大学生", "me:オレ"),
        )

STAGES = (
        # zebra
        ("Chiba", "千葉県"),
        ("hometown", "袖ケ浦市"),
        ## Area
        ("myhome", "槙坂家"),
        ("kenapart", "ケンのアパート"),
        ("hisshop", "ケンの店"),
        ("temple", "巌詠寺"),
        ## Part
        ("myroom", "笑美の部屋"),
        ("living", "リビング"),
        ("dyning", "食堂"),
        ("classroom", "教室"),
        ("studio", "撮影スタジオ"),
        # kissmark
        ("ks_univ", "北海道大学"),
        ("ks_home", "花のアパート"),
        ("ks_ramen", "大学前ラーメン店"),
        ("oncorridor", "廊下"),
        )

DAYS = (
        # main
        ("current", "現在"),
        # Zebra
        ("marason", "マラソン大会", 10,25, 2019),
        ("getzebra", "ゼブラブラ入手日"),
        ("camera", "撮影日"),
        # kissmark
        ("ks_shogaku", "小学生時代")
        )

ITEMS = (
        # Zebra
        ("zebrabra", "ゼブラブラ"),
        )

INFOS = (
        # Zebra
        ("brandname", "KenKen"),
        ("Ilove", "アイラブシマウマ"),
        )


FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }

