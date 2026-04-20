"""
LLM explanation video in Kyrgyz — Instagram Reel (9:16), ~50 seconds
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
config.pixel_width       = 1080
config.pixel_height      = 1920
config.frame_width       = 9
config.frame_height      = 16


def tx(text, size=0.45, color=WHITE, **kw):
    """Regular text (Cyrillic-safe via Arial)."""
    return Text(text, font="Arial", font_size=int(size * 100),
                color=color, **kw)


def em(text, size=0.9, **kw):
    """Emoji text via Apple Color Emoji."""
    return Text(text, font="Apple Color Emoji", font_size=int(size * 100), **kw)


def neuron_circle(pos, radius=0.18, color=BLUE_1):
    return Circle(radius=radius, color=color,
                  fill_opacity=0.15, stroke_width=2).move_to(pos)


def make_network(layer_sizes, x_start=-2.1, y_center=-0.8,
                 layer_gap=1.35, y_gap=0.60):
    layers, edges = [], []
    xs = [x_start + i * layer_gap for i in range(len(layer_sizes))]
    for n, x in zip(layer_sizes, xs):
        top = (n - 1) / 2 * y_gap
        layers.append(VGroup(*[
            neuron_circle([x, y_center + top - j * y_gap, 0])
            for j in range(n)
        ]))
    for i in range(len(layers) - 1):
        eg = VGroup(*[
            Line(a.get_center(), b.get_center(),
                 stroke_width=0.6, stroke_color=BLUE_2, stroke_opacity=0.55)
            for a in layers[i] for b in layers[i + 1]
        ])
        edges.append(eg)
    return layers, edges


class LLM_Kyrgyz_Insta(Scene):
    def construct(self):

        # ─────────────────────────────────────────────────────────────────────
        # SCENE 1 · Title  (0–5 s)
        # ─────────────────────────────────────────────────────────────────────
        glow = Circle(radius=2.2, color=BLUE_1,
                      fill_opacity=0.06, stroke_opacity=0).shift(UP * 0.5)
        ring = Circle(radius=2.2, color=BLUE_1,
                      stroke_width=2, fill_opacity=0).shift(UP * 0.5)

        abbr     = tx("LLM",                  size=1.8,  color=BLUE_1  ).shift(UP * 1.2)
        full_en  = tx("Large Language Model", size=0.38, color=GREY_1  ).next_to(abbr,    DOWN, buff=0.25)
        full_ky  = tx("Чоң Тил Модели",       size=0.55, color=TEAL    ).next_to(full_en, DOWN, buff=0.30)
        question = tx("деген эмне?",           size=0.60, color=YELLOW_A).next_to(full_ky, DOWN, buff=0.20)

        self.play(FadeIn(glow), Create(ring, run_time=1.0))
        self.play(FadeIn(abbr, scale=0.8, run_time=1.0))
        self.play(FadeIn(full_en, shift=UP * 0.2),
                  FadeIn(full_ky, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(question, shift=UP * 0.15))
        self.wait(0.8)
        self.play(FadeOut(VGroup(glow, ring, abbr, full_en, full_ky, question)))

        # ─────────────────────────────────────────────────────────────────────
        # SCENE 2 · Tokens  (5–14 s)
        # ─────────────────────────────────────────────────────────────────────
        title2   = tx("Текст → Токендер", size=0.50, color=BLUE_1).to_edge(UP, buff=0.6)
        sentence = tx('"Мен үйгө барам"',  size=0.52, color=GREY_1).shift(UP * 3.0)

        self.play(FadeIn(title2, shift=DOWN * 0.20))
        self.play(FadeIn(sentence, shift=DOWN * 0.2))
        self.wait(0.3)

        words  = ["Мен", "үй", "гө",  "бар",  "ам"]
        colors = [BLUE_1, TEAL, YELLOW_A, PINK, TEAL]
        boxes  = VGroup()
        for w, c in zip(words, colors):
            lbl = tx(w, size=0.42, color=c)
            box = SurroundingRectangle(lbl, color=c, buff=0.18,
                                       corner_radius=0.10, stroke_width=1.8,
                                       fill_opacity=0.08, fill_color=c)
            boxes.add(VGroup(box, lbl))
        boxes.arrange(RIGHT, buff=0.18).shift(UP * 1.2)

        arrow = Arrow(sentence.get_bottom(), boxes.get_top(),
                      buff=0.15, color=GREY_2, stroke_width=2)
        self.play(GrowArrow(arrow))
        self.play(LaggedStart(*[FadeIn(b, shift=DOWN * 0.15) for b in boxes],
                              lag_ratio=0.18, run_time=1.3))

        note  = tx("Ар бир токен = бир сан", size=0.40, color=GREY_1).shift(DOWN * 0.2)
        ids   = VGroup(*[tx(str(1024 + i * 317), size=0.38, color=GREY_2)
                         for i in range(5)]).arrange(RIGHT, buff=0.42).next_to(note, DOWN, buff=0.35)
        embed = tx("токен → вектор ∈ R^4096", size=0.38, color=GREY_2).next_to(ids, DOWN, buff=0.35)

        self.play(FadeIn(note))
        self.play(LaggedStart(*[FadeIn(n) for n in ids], lag_ratio=0.15))
        self.play(FadeIn(embed, shift=UP * 0.1))
        self.wait(0.8)
        self.play(FadeOut(VGroup(title2, sentence, arrow, boxes, note, ids, embed)))

        # ─────────────────────────────────────────────────────────────────────
        # SCENE 3 · Neural network  (14–25 s)
        # ─────────────────────────────────────────────────────────────────────
        title3 = tx("Нейрондук Тармак", size=0.50, color=BLUE_1).to_edge(UP, buff=0.6)
        self.play(FadeIn(title3, shift=DOWN * 0.10))

        layers, edges = make_network([3, 5, 5, 3])
        lnames = ["Киргизуу", "Жашырын", "Жашырын", "Чыгаруу"]
        name_lbls = VGroup(*[
            tx(n, size=0.25, color=GREY_2).next_to(layers[i], DOWN, buff=0.25)
            for i, n in enumerate(lnames)
        ])

        for eg  in edges:  self.play(Create(eg, run_time=0.30), rate_func=linear)
        for lay in layers: self.play(LaggedStart(*[GrowFromCenter(n) for n in lay],
                                                 lag_ratio=0.10, run_time=0.45))
        self.play(FadeIn(name_lbls))

        for _ in range(2):
            for lay in layers:
                self.play(lay.animate.set_fill(YELLOW_A, opacity=0.55), run_time=0.15)
                self.play(lay.animate.set_fill(BLUE_1,   opacity=0.15), run_time=0.15)

        note3 = tx("Параметрлер: миллиарддар", size=0.40, color=TEAL).shift(DOWN * 3.8)
        self.play(FadeIn(note3, shift=UP * 0.15))
        self.wait(0.7)
        self.play(FadeOut(VGroup(title3, *layers, *edges, name_lbls, note3)))

        # ─────────────────────────────────────────────────────────────────────
        # SCENE 4 · Next-token prediction  (25–36 s)
        # ─────────────────────────────────────────────────────────────────────
        title4 = tx("Кийинки Сөздү Болжолдойт", size=0.42, color=BLUE_1).to_edge(UP, buff=0.6)
        self.play(FadeIn(title4, shift=DOWN * 0.10))

        prompt_words  = ["Мен", "китеп", "___"]
        prompt_colors = [BLUE_1, TEAL, GREY_2]
        prompt_boxes  = VGroup()
        for w, c in zip(prompt_words, prompt_colors):
            lbl = tx(w, size=0.35, color=c)
            box = SurroundingRectangle(lbl, color=c, buff=0.20,
                                       corner_radius=0.10, stroke_width=1.8,
                                       fill_opacity=0.08, fill_color=c)
            prompt_boxes.add(VGroup(box, lbl))
        prompt_boxes.arrange(RIGHT, buff=0.22).shift(UP * 2.8)

        self.play(LaggedStart(*[FadeIn(b) for b in prompt_boxes],
                              lag_ratio=0.20, run_time=0.9))

        candidates = [
            ("окуйм",    0.52, TEAL),
            ("жаздым",   0.28, BLUE_1),
            ("алдым",    0.12, YELLOW_A),
            ("таштадым", 0.08, PINK),
        ]
        bar_group = VGroup()
        for i, (word, prob, col) in enumerate(candidates):
            y   = 1.1 - i * 0.85
            bg  = Rectangle(width=4.0, height=0.38, fill_opacity=0.12,
                            fill_color=col, stroke_opacity=0).move_to([0.5, y, 0])
            bar = Rectangle(width=4.0 * prob, height=0.38,
                            fill_opacity=0.70, fill_color=col,
                            stroke_opacity=0).align_to(bg, LEFT)
            wlbl = tx(word,                  size=0.35, color=col   ).next_to(bg, LEFT,  buff=0.28)
            plbl = tx(f"{int(prob * 100)}%", size=0.34, color=GREY_1).next_to(bg, RIGHT, buff=0.15)
            bar_group.add(VGroup(bg, bar, wlbl, plbl))

        self.play(LaggedStart(*[FadeIn(g) for g in bar_group],
                              lag_ratio=0.18, run_time=1.2))

        winner = SurroundingRectangle(bar_group[0], color=TEAL,
                                      buff=0.08, corner_radius=0.08, stroke_width=2.5)
        chosen = tx("окуйм", size=0.40 , color=TEAL).next_to(prompt_boxes, RIGHT, buff=0.3)
        self.play(Create(winner), FadeIn(chosen), run_time=0.7)

        repeat = tx("... жана дагы, дагы, дагы ...", size=0.40, color=GREY_2).shift(DOWN * 2.5)
        self.play(FadeIn(repeat, shift=UP * 0.1))
        self.wait(0.8)
        self.play(FadeOut(VGroup(title4, prompt_boxes, bar_group,
                                  winner, chosen, repeat)))

        # ─────────────────────────────────────────────────────────────────────
        # SCENE 5 · Training  (36–46 s)
        # ─────────────────────────────────────────────────────────────────────
        title5 = tx("Кантип үйрөнөт?", size=0.50, color=BLUE_1).to_edge(UP, buff=0.6)
        self.play(FadeIn(title5, shift=DOWN * 0.10))

        # Icon squares instead of emoji (more reliable rendering)
        def icon_box(label_text, icon_color, pos):
            sq  = RoundedRectangle(corner_radius=0.3, width=1.6, height=1.6,
                                   fill_color=icon_color, fill_opacity=0.18,
                                   stroke_color=icon_color, stroke_width=2).move_to(pos)
            lbl = tx(label_text, size=0.38, color=icon_color).move_to(pos)
            return VGroup(sq, lbl)

        icon1 = icon_box("Китептер", TEAL,   LEFT * 2.8 + UP * 1.8)
        icon2 = icon_box("Интернет", BLUE_1,              UP * 1.8)
        icon3 = icon_box("Код",      YELLOW_A, RIGHT * 2.8 + UP * 1.8)

        self.play(LaggedStart(FadeIn(icon1, scale=0.5),
                              FadeIn(icon2, scale=0.5),
                              FadeIn(icon3, scale=0.5),
                              lag_ratio=0.20, run_time=0.9))

        # Brain circle
        brain_circ = Circle(radius=0.7, fill_color=PINK, fill_opacity=0.25,
                            stroke_color=PINK, stroke_width=2.5).shift(DOWN * 1.2)
        brain_lbl  = tx("ЖИ", size=0.55, color=PINK).move_to(brain_circ)
        brain      = VGroup(brain_circ, brain_lbl)

        arrs = VGroup(*[
            Arrow(ic[0].get_bottom(), brain_circ.get_top(),
                  buff=0.15, color=BLUE_2, stroke_width=2.5)
            for ic in [icon1, icon2, icon3]
        ])
        self.play(LaggedStart(*[GrowArrow(a) for a in arrs],
                              lag_ratio=0.15, run_time=0.8))
        self.play(GrowFromCenter(brain))

        stat = tx("Триллиондогон токен\nжүздөгөн GPU",
                  size=0.44, color=TEAL).shift(DOWN * 3.2)
        self.play(FadeIn(stat, shift=UP * 0.15))
        self.wait(0.8)
        self.play(FadeOut(VGroup(title5, icon1, icon2, icon3, arrs, brain, stat)))

        # ─────────────────────────────────────────────────────────────────────
        # SCENE 6 · Outro  (46–50 s)
        # ─────────────────────────────────────────────────────────────────────
        ring1 = Circle(radius=2.5, color=TEAL,   stroke_width=2,   fill_opacity=0).shift(UP * 0.8)
        ring2 = Circle(radius=1.8, color=BLUE_1, stroke_width=1.5, fill_opacity=0).shift(UP * 0.8)

        summary = [
            ("Текстти токендерге болот",    GREY_1),
            ("Векторлорго айлантат",        GREY_1),
            ("Кийинки токенди болжолдойт",  GREY_1),
            ("Триллиондогон мисалдан",      GREY_1),
            ("уйронуп LLM жаралат!",        GREY_1),
        ]
        lines  = VGroup(*[tx(txt, size=0.42, color=c) for txt, c in summary]
                        ).arrange(DOWN, buff=0.32).shift(DOWN * 0.8)
        # follow = tx("Жазылып кой!", size=0.52, color=PINK).to_edge(DOWN, buff=0.7)

        self.play(Create(ring1, run_time=0.8), Create(ring2, run_time=0.8))
        self.play(LaggedStart(*[FadeIn(l, shift=RIGHT * 0.2) for l in lines],
                              lag_ratio=0.22, run_time=1.8))
        # self.play(FadeIn(follow, scale=1.1))
        self.wait(1.2)
