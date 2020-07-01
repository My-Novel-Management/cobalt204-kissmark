#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "The kissmark"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from config import ASSET
# import scenes
from scenes import Apart


################################################################
#
#   1. Story memo
#   2. Story structure
#   3. Plot
#   4. Conte
#   5. Draft
#
################################################################

# Constant
TITLE = "キスマーク"
OUTLINE = "コバルト短編小説新人賞２０４回もう一歩作品"
MAJOR, MINOR, MICRO = 1, 0, 0


# Episodes
def ep_intro(w: World):
    return w.episode("冒頭",
            Apart.dislike(w),
            )

def ep_ramen(w: World):
    return w.episode("ラーメン屋",
            Apart.telephone(w),
            Apart.ramen(w),
            )

def ep_oldstory(w: World):
    return w.episode("昔話",
            Apart.oldtalk(w),
            )

def ep_univ(w: World):
    return w.episode("大学生",
            Apart.goto_univ(w),
            )

def ep_kissmark(w: World):
    return w.episode("キスマーク",
            Apart.kissmark(w),
            w.symbol("（了）"),
            )


def ch_main(w: World):
    return w.chapter('main',
            ep_intro(w),
            ep_ramen(w),
            ep_oldstory(w),
            ep_univ(w),
            ep_kissmark(w),
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(ASSET)
    return w.run(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

