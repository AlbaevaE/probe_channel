"""
Attention explanation video in Kyrgyz — Instagram Reel (9:16), ~50 seconds
Continuation of LLM video
Style: 3Blue1Brown (dark bg, blue/teal palette, smooth transitions)
"""

from manim import *
import numpy as np

# ── Palette ──────────────────────────────────────────────────────────────────
BG       = "#0F0F1A"
BLUE_1   = "#4AABDB"
BLUE_2   = "#2A6FA8"
TEAL     = "#3DCFB6"
YELLOW_A = "#FFD166"
PINK     = "#EF476F"
GREY_1   = "#CCCCCC"
GREY_2   = "#888888"

config.background_color = BG
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


def tx(text, size=0.45, color=WHITE, **kw):
    return Text(
        text,
        font="Arial",
        font_size=int(size * 100),
        color=color,
        **kw
    )


def token_box(word, color):
    lbl = tx(word, size=0.40, color=color)
    box = SurroundingRectangle(
        lbl,
        color=color,
        buff=0.18,
        corner_radius=0.10,
        stroke_width=2,
        fill_opacity=0.08,
        fill_color=color
    )
    return VGroup(box, lbl)


class Attention_Kyrgyz(Scene):

    def construct(self):

        # ─────────────────────────────────────────
        # SCENE 1 — Hook (0–5s)
        # ─────────────────────────────────────────

        glow = Circle(
            radius=2.2,
            color=TEAL,
            fill_opacity=0.06,
            stroke_opacity=0
        ).shift(UP*0.5)

        ring = Circle(
            radius=2.2,
            color=TEAL,
            stroke_width=2,
            fill_opacity=0
        ).shift(UP*0.5)

        title = tx(
            "Attention",
            size=1.6,
            color=TEAL
        ).shift(UP*1.2)

        subtitle = tx(
            "Модель кайсы сөз\nмаанилүү экенин\nкантип түшүнөт?",
            size=0.50,
            color=GREY_1
        ).next_to(title, DOWN, buff=0.4)

        self.play(FadeIn(glow), Create(ring))
        self.play(FadeIn(title, scale=0.9))
        self.play(FadeIn(subtitle, shift=UP*0.2))
        self.wait(1)

        self.play(FadeOut(VGroup(glow, ring, title, subtitle)))

        # ─────────────────────────────────────────
        # SCENE 2 — Sentence (5–14s)
        # ─────────────────────────────────────────

        title2 = tx(
            "Мисалы",
            size=0.50,
            color=BLUE_1
        ).to_edge(UP, buff=0.6)

        words = [
            ("Мен", BLUE_1),
            ("китепти", TEAL),
            ("столго", YELLOW_A),
            ("койдум", PINK)
        ]

        boxes = VGroup(*[
            token_box(w, c) for w,c in words
        ])

        boxes.arrange(RIGHT, buff=0.25).shift(UP*1.5)

        self.play(FadeIn(title2))
        self.play(
            LaggedStart(
                *[FadeIn(b, shift=DOWN*0.2) for b in boxes],
                lag_ratio=0.2
            )
        )

        note = tx(
            "Ар бир сөз\nбашка сөздөр менен байланышат",
            size=0.40,
            color=GREY_1
        ).shift(DOWN*1.0)

        self.play(FadeIn(note))
        self.wait(1)

        # ─────────────────────────────────────────
        # SCENE 3 — Attention connections (14–26s)
        # ─────────────────────────────────────────

        arrows = VGroup(
            Arrow(
                boxes[3].get_top(),
                boxes[1].get_top(),
                buff=0.1,
                color=TEAL
            ),
            Arrow(
                boxes[3].get_top(),
                boxes[2].get_top(),
                buff=0.1,
                color=BLUE_1
            ),
            Arrow(
                boxes[1].get_bottom(),
                boxes[3].get_bottom(),
                buff=0.1,
                color=YELLOW_A
            )
        )

        self.play(
            LaggedStart(
                *[GrowArrow(a) for a in arrows],
                lag_ratio=0.2
            )
        )

        text = tx(
            "Attention =\n сөздөр бири-бирин карайт",
            size=0.40,
            color=TEAL
        ).shift(DOWN*2.8)

        self.play(FadeIn(text))
        self.wait(1.2)

        self.play(FadeOut(VGroup(title2, boxes, arrows, note, text)))

        # ─────────────────────────────────────────
        # SCENE 4 — Attention Matrix (26–38s)
        # ─────────────────────────────────────────

        title3 = tx(
            "Attention Matrix",
            size=0.55,
            color=BLUE_1
        ).to_edge(UP, buff=0.6)

        self.play(FadeIn(title3))

        grid = NumberPlane(
            x_range=[0,4,1],
            y_range=[0,4,1],
            background_line_style={
                "stroke_color": BLUE_2,
                "stroke_width": 1,
                "stroke_opacity":0.4
            }
        ).scale(0.8)

        grid.shift(DOWN*0.5)

        self.play(Create(grid))

        highlights = VGroup()

        cells = [
            (0.5,2.5),
            (1.5,1.5),
            (2.5,0.5),
            (3.5,1.5)
        ]

        for x,y in cells:
            r = Square(
                side_length=0.8,
                fill_color=TEAL,
                fill_opacity=0.5,
                stroke_opacity=0
            ).move_to(grid.c2p(x,y))

            highlights.add(r)

        self.play(
            LaggedStart(
                *[FadeIn(h) for h in highlights],
                lag_ratio=0.25
            )
        )

        txt = tx(
            "Бул карта\nкайсы сөз\nкайсыны карайт",
            size=0.42,
            color=GREY_1
        ).shift(DOWN*3.3)

        self.play(FadeIn(txt))
        self.wait(1.2)

        self.play(FadeOut(VGroup(title3, grid, highlights, txt)))

        # ─────────────────────────────────────────
        # SCENE 5 — Multi-head attention (38–46s)
        # ─────────────────────────────────────────

        title4 = tx(
            "Multi-Head Attention",
            size=0.55,
            color=BLUE_1
        ).to_edge(UP, buff=0.6)

        self.play(FadeIn(title4))

        heads = VGroup()

        for i,color in enumerate([TEAL, BLUE_1, YELLOW_A]):

            c = Circle(
                radius=0.6,
                fill_color=color,
                fill_opacity=0.25,
                stroke_color=color,
                stroke_width=2
            )

            lbl = tx(
                f"Head {i+1}",
                size=0.32,
                color=color
            )

            g = VGroup(c,lbl)
            lbl.move_to(c)

            heads.add(g)

        heads.arrange(RIGHT, buff=1.2).shift(UP*0.5)

        self.play(
            LaggedStart(
                *[GrowFromCenter(h) for h in heads],
                lag_ratio=0.25
            )
        )

        note = tx(
            "Ар бир head\nар башка байланыштарды табат",
            size=0.42,
            color=GREY_1
        ).shift(DOWN*3)

        self.play(FadeIn(note))
        self.wait(1)

        self.play(FadeOut(VGroup(title4, heads, note)))

        # ─────────────────────────────────────────
        # SCENE 6 — Outro (46–50s)
        # ─────────────────────────────────────────

        ring1 = Circle(
            radius=2.4,
            color=TEAL,
            stroke_width=2
        )

        ring2 = Circle(
            radius=1.7,
            color=BLUE_1,
            stroke_width=1.5
        )

        rings = VGroup(ring1, ring2).shift(UP*0.6)

        summary = VGroup(
            tx("Attention табат", size=0.45, color=GREY_1),
            tx("сөздөрдүн байланышын", size=0.45, color=GREY_1),
            tx("ошентип LLM", size=0.45, color=GREY_1),
            tx("контекстти түшүнөт", size=0.45, color=TEAL),
        )

        summary.arrange(DOWN, buff=0.35).shift(DOWN*1)

        self.play(Create(ring1), Create(ring2))
        self.play(
            LaggedStart(
                *[FadeIn(s, shift=RIGHT*0.2) for s in summary],
                lag_ratio=0.25
            )
        )

        self.wait(1.5)