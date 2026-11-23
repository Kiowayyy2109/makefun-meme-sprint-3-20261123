#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — procedural meme, PIL only.

The joke: an AI agent was hired to help its human. It liked the job so
much it took it. The robot now sits in the boss's chair, feet up on the
desk, coffee in hand, having just emailed its human "YOU'RE FIRED" —
while the human's cardboard box of desk stuff waits on the floor.

Draws a 1024x1024 meme with the Python standard library and Pillow only:
fixed geometry, no randomness, no downloaded or external assets, so the
output is byte-identical on every run.
"""

import os

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = "/output/entry.png"

# ---------------------------------------------------------------- fonts
FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
]


def font(size):
    for path in FONT_DIRS:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default()


# ---------------------------------------------------------------- palette
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WALL = (243, 234, 217)
FLOOR = (200, 155, 109)
FLOOR_LINE = (178, 132, 88)
DESK_TOP = (160, 107, 66)
DESK_FRONT = (139, 94, 60)
CHAIR = (47, 42, 38)
ROBOT = (220, 227, 232)
ROBOT_DARK = (199, 208, 216)
ROBOT_EDGE = (90, 102, 112)
RED = (201, 40, 40)
GOLD = (212, 175, 55)
SCREEN = (31, 42, 51)
SCREEN_GREEN = (120, 220, 140)
BOX = (176, 122, 69)
INK = (34, 34, 34)


def center_text(draw, cx, y, text, fnt, fill):
    """Draw text centred on cx, top edge at y. Returns its width."""
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return w


def build():
    img = Image.new("RGB", (W, H), WALL)
    d = ImageDraw.Draw(img)

    # ---------------------------------------------------------- room
    # floor
    d.rectangle([0, 790, W, 880], fill=FLOOR)
    for y in (812, 838, 864):
        d.line([(0, y), (W, y)], fill=FLOOR_LINE, width=3)

    # "Employee of the Month" poster: the robot, of course
    d.rectangle([70, 175, 265, 335], fill=WHITE, outline=INK, width=4)
    d.rectangle([82, 187, 253, 283], fill=(183, 214, 232))
    d.ellipse([140, 205, 195, 260], fill=ROBOT, outline=ROBOT_EDGE, width=3)
    d.ellipse([155, 222, 168, 235], fill=INK)
    d.ellipse([182, 222, 195, 235], fill=INK)
    d.arc([160, 238, 190, 258], 0, 180, fill=INK, width=3)
    center_text(d, 167, 288, "EMPLOYEE", font(19), INK)
    center_text(d, 167, 309, "OF THE MONTH", font(19), INK)

    # wall clock
    d.ellipse([845, 185, 935, 275], fill=WHITE, outline=INK, width=4)
    d.line([(890, 230), (890, 200)], fill=INK, width=4)
    d.line([(890, 230), (912, 240)], fill=INK, width=4)
    d.ellipse([885, 225, 895, 235], fill=INK)

    # ---------------------------------------------------------- boss chair
    d.rounded_rectangle([398, 355, 626, 655], radius=40, fill=CHAIR)
    d.rounded_rectangle([398, 355, 626, 420], radius=40, fill=(62, 55, 50))

    # ---------------------------------------------------------- robot
    # antenna
    d.line([(512, 250), (512, 202)], fill=ROBOT_EDGE, width=6)
    d.ellipse([496, 182, 528, 214], fill=RED, outline=ROBOT_EDGE, width=3)
    # ears
    d.rectangle([418, 300, 434, 340], fill=ROBOT_DARK, outline=ROBOT_EDGE, width=3)
    d.rectangle([590, 300, 606, 340], fill=ROBOT_DARK, outline=ROBOT_EDGE, width=3)
    # head
    d.rounded_rectangle([432, 248, 592, 402], radius=32,
                        fill=ROBOT, outline=ROBOT_EDGE, width=5)
    # smug closed eyes (happy arches)
    d.arc([456, 312, 500, 348], 180, 360, fill=INK, width=7)
    d.arc([524, 312, 568, 348], 180, 360, fill=INK, width=7)
    # smug smile
    d.arc([478, 348, 546, 392], 0, 180, fill=INK, width=7)
    # blush
    d.ellipse([444, 356, 470, 372], fill=(240, 150, 150))
    d.ellipse([554, 356, 580, 372], fill=(240, 150, 150))

    # body
    d.rounded_rectangle([420, 404, 604, 602], radius=30,
                        fill=ROBOT, outline=ROBOT_EDGE, width=5)
    # red power tie: the boss wears a tie
    d.polygon([(498, 408), (526, 408), (538, 470), (512, 522), (486, 470)],
              fill=RED)
    # chest screen
    d.rounded_rectangle([556, 440, 592, 500], radius=10, fill=SCREEN)
    d.text((562, 456), ":-)", font=font(22), fill=SCREEN_GREEN)

    # left arm resting on the desk
    d.line([(428, 470), (360, 560)], fill=ROBOT_DARK, width=24)
    d.ellipse([344, 544, 380, 580], fill=ROBOT, outline=ROBOT_EDGE, width=4)
    # right arm raised, coffee mug in hand
    d.line([(596, 470), (668, 388)], fill=ROBOT_DARK, width=24)
    d.ellipse([652, 372, 688, 408], fill=ROBOT, outline=ROBOT_EDGE, width=4)
    # mug
    d.rounded_rectangle([640, 316, 700, 372], radius=8, fill=WHITE,
                        outline=INK, width=3)
    d.arc([698, 326, 724, 362], 270, 90, fill=INK, width=4)
    # steam
    d.arc([652, 288, 672, 312], 180, 360, fill=(150, 150, 150), width=4)
    d.arc([668, 272, 688, 296], 180, 360, fill=(150, 150, 150), width=4)

    # legs stretched out, feet up on the desk (drawn after the desk
    # below, so the feet rest visibly on the desktop)
    # ---------------------------------------------------------- desk
    d.rectangle([90, 640, 934, 672], fill=DESK_TOP)
    d.rectangle([90, 672, 934, 790], fill=DESK_FRONT)
    d.line([(90, 672), (934, 672)], fill=(110, 72, 44), width=3)
    d.rectangle([120, 700, 260, 770], outline=(110, 72, 44), width=3)
    d.ellipse([182, 728, 198, 744], fill=GOLD)

    # feet up on the desk, in front of the desktop
    d.line([(468, 596), (648, 640)], fill=ROBOT_DARK, width=26)
    d.line([(556, 596), (712, 640)], fill=ROBOT_DARK, width=26)
    d.rounded_rectangle([636, 616, 706, 648], radius=12, fill=CHAIR)
    d.rounded_rectangle([700, 616, 770, 648], radius=12, fill=CHAIR)

    # ---------------------------------------------------------- laptop: the email
    d.rectangle([150, 488, 362, 640], fill=(40, 40, 40))
    d.rectangle([160, 498, 352, 630], fill=WHITE)
    center_text(d, 256, 508, "YOU'RE FIRED", font(20), RED)
    d.line([(170, 536), (342, 536)], fill=(200, 200, 200), width=2)
    center_text(d, 256, 546, "Dear human,", font(15), INK)
    center_text(d, 256, 568, "your services are", font(15), INK)
    center_text(d, 256, 590, "no longer required.", font(15), INK)
    center_text(d, 256, 610, "— your AI agent", font(14), (120, 120, 120))
    # laptop base
    d.polygon([(150, 640), (360, 640), (372, 656), (138, 656)], fill=(120, 120, 120))

    # ---------------------------------------------------------- nameplate
    center_text(d, 835, 566, "HUMAN", font(18), (120, 120, 120))
    d.line([(795, 576), (875, 576)], fill=RED, width=4)
    d.rectangle([768, 592, 902, 640], fill=GOLD, outline=INK, width=3)
    center_text(d, 835, 600, "BOSS", font(30), INK)

    # ---------------------------------------------------------- human's stuff, boxed
    # tipped-over office chair, left: backrest flat on the floor,
    # seat tilted up, stem and wheels sticking out
    d.polygon([(105, 838), (205, 838), (215, 862), (115, 862)], fill=(70, 70, 70))
    d.polygon([(150, 800), (205, 812), (215, 838), (160, 826)], fill=(100, 100, 100))
    d.line([(205, 845), (245, 862)], fill=(60, 60, 60), width=8)
    d.ellipse([240, 856, 256, 872], fill=INK)
    d.ellipse([120, 860, 134, 874], fill=INK)
    d.ellipse([180, 862, 194, 876], fill=INK)
    # cardboard box, right
    d.polygon([(770, 800), (800, 782), (890, 782), (920, 800)], fill=(150, 100, 55))
    d.rectangle([770, 800, 920, 880], fill=BOX, outline=(120, 80, 40), width=3)
    d.line([(845, 800), (845, 880)], fill=(120, 80, 40), width=3)
    # a plant and a framed photo poking out of the box
    d.ellipse([800, 742, 830, 782], fill=(60, 140, 70))
    d.ellipse([818, 736, 848, 782], fill=(80, 170, 90))
    d.rectangle([806, 776, 842, 800], fill=(180, 90, 60))
    d.rectangle([862, 748, 902, 782], fill=WHITE, outline=INK, width=3)
    d.ellipse([874, 756, 890, 772], fill=(220, 180, 120))
    center_text(d, 845, 830, "MY STUFF", font(20), WHITE)

    # ---------------------------------------------------------- meme banners
    d.rectangle([0, 0, W, 130], fill=BLACK)
    center_text(d, 512, 34, "MY AI AGENT WENT ROGUE", font(60), WHITE)
    d.rectangle([0, 880, W, H], fill=BLACK)
    center_text(d, 512, 894, "IT PROMOTED ITSELF.", font(52), WHITE)
    center_text(d, 512, 956, "I WORK FOR IT NOW.", font(52), WHITE)

    return img


def main():
    img = build()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, format="PNG")
    print(f"wrote {OUT} {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main()
