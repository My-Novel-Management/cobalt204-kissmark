#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from config import ASSET
# import scenes
# from scenes import xxx


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
TITLE = "作品タイトル"
OUTLINE = "あらすじ"


# Episodes
def ep_xxx(w: World):
    return w.episode('episode_title',
            outline="description")


def ch_main(w: World):
    return w.chapter('main',
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_version(0,0,1)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(ASSET)
    return w.run(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

