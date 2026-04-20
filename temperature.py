"""
AI Temperature — Instagram Reel (~50s)
Style: 3Blue1Brown inspired
Language: Kyrgyz
"""

from manim import *

# ─────────────────────────────────────────────
# Palette
# ─────────────────────────────────────────────

BG       = "#0F0F1A"
BLUE_1   = "#4AABDB"
BLUE_2   = "#2A6FA8"
TEAL     = "#3DCFB6"
YELLOW_A = "#FFD166"
PINK     = "#EF476F"
GREY_1   = "#CCCCCC"
GREY_2   = "#888888"

config.background_color = BG
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

SAFE_TOP = 3.8
SAFE_BOTTOM = -3.8


def tx(text, size=0.42, color=WHITE):
    return Text(
        text,
        font="Arial",
        font_size=int(size * 80),
        color=color
    )


# ─────────────────────────────────────────────
# Scene
# ─────────────────────────────────────────────

class Temperature_Reel(Scene):

    def construct(self):

        # ─────────────────────────────────
        # SCENE 1 — Hook
        # ─────────────────────────────────

        title = VGroup(
            tx("AI эмне үчүн",0.55,BLUE_1),
            tx("ар башка жооп берет?",0.55,BLUE_1),
        ).arrange(DOWN, buff=0.25)

        self.play(FadeIn(title, shift=DOWN*0.4))
        self.wait(2)

        self.play(title.animate.to_edge(UP, buff=1.4))

        # ─────────────────────────────────
        # SCENE 2 — Question
        # ─────────────────────────────────

        question = VGroup(
            tx("Суроо",0.45,GREY_1),
            tx('"Бүгүн аба ырайы кандай?"',0.48,TEAL)
        ).arrange(DOWN, buff=0.3)

        question.move_to([0,1.6,0])

        self.play(FadeIn(question))

        answers = VGroup(
            tx("Жооп: Күн жылуу.",0.42,BLUE_1),
            tx("Жооп: Күн жылуу, шамал бар.",0.42,BLUE_1)
        ).arrange(DOWN, buff=0.5)

        answers.move_to([0,-1.2,0])

        self.play(LaggedStart(*[FadeIn(a) for a in answers], lag_ratio=0.3))

        self.wait(2)

        self.play(FadeOut(answers))

        # ─────────────────────────────────
        # SCENE 3 — Probabilities
        # ─────────────────────────────────

        title2 = tx("AI варианттарды билет",0.55,BLUE_1)
        title2.to_edge(UP, buff=1.4)

        self.play(
            FadeOut(title),
            FadeIn(title2)
        )

        options = [
            ("жылуу",0.6,TEAL),
            ("салкын",0.25,BLUE_1),
            ("жамгыр",0.15,YELLOW_A),
        ]

        bars = VGroup()

        for word,prob,color in options:

            bg = Rectangle(
                width=4,
                height=0.45,
                fill_opacity=0.15,
                fill_color=color,
                stroke_opacity=0
            )

            bar = Rectangle(
                width=4*prob,
                height=0.45,
                fill_color=color,
                fill_opacity=0.8,
                stroke_opacity=0
            ).align_to(bg,LEFT)

            label = tx(word,0.42,color).next_to(bg,LEFT,buff=0.35)
            prob_label = tx(f"{int(prob*100)}%",0.35,GREY_1).next_to(bg,RIGHT)

            bars.add(VGroup(bg,bar,label,prob_label))

        bars.arrange(DOWN,buff=0.2)
        bars.move_to([0,-0.2,0])

        self.play(LaggedStart(*[FadeIn(b) for b in bars],lag_ratio=0.25))

        self.wait(2)

        self.play(FadeOut(bars))
        self.play(FadeOut(question))

        # ─────────────────────────────────
        # SCENE 4 — Temperature slider
        # ─────────────────────────────────

        title3 = tx("Temperature",0.65,TEAL)
        subtitle = tx("AI канчалык креативдүү болот",0.42,GREY_1)

        header = VGroup(title3,subtitle).arrange(DOWN,buff=0.10)
        header.to_edge(UP,buff=1.4)

        self.play(
            FadeOut(title2),
            FadeIn(header)
        )

        line = Line(LEFT*3,RIGHT*3,color=GREY_2)

        dot = Dot(color=PINK).move_to(line.get_left())

        labels = VGroup(
            tx("0.2",0.35,GREY_1).next_to(line,LEFT),
            tx("2.0",0.35,GREY_1).next_to(line,RIGHT),
        )

        slider = VGroup(line,dot,labels)

        slider.move_to([0,-0.6,0])

        self.play(Create(line))
        self.play(FadeIn(dot))
        self.play(FadeIn(labels))

        self.play(dot.animate.move_to(line.get_center()),run_time=1.5)
        self.play(dot.animate.move_to(line.get_right()),run_time=1.5)

        self.wait(1)

        self.play(FadeOut(slider))

        # ─────────────────────────────────
        # SCENE 5 — Example
        # ─────────────────────────────────

        title4 = tx("Температура жоопту өзгөртөт",0.45,BLUE_1)
        title4.to_edge(UP,buff=1.4)

        self.play(
            FadeOut(header),
            FadeIn(title4)
        )

        examples = VGroup(

            tx("Temp 0 → Мен алма жейм",0.37,TEAL),
            tx("Temp 1 → Мен кызыл алма жейм",0.37,BLUE_1),
            tx("Temp 2 → Мен галактикалык алма жейм 🚀",0.37,YELLOW_A),

        )

        examples.arrange(DOWN,buff=0.9)
        examples.move_to([0,-0.4,0])

        self.play(LaggedStart(*[FadeIn(e) for e in examples],lag_ratio=0.3))

        self.wait(2)

        self.play(FadeOut(examples))

        # ─────────────────────────────────
        # SCENE 6 — Outro
        # ─────────────────────────────────

        summary = VGroup(

            tx("Temperature",0.7,TEAL),
            tx("AI канчалык",0.45,GREY_1),
            tx("креативдүү болорун",0.45,GREY_1),
            tx("чечет",0.45,GREY_1)

        )

        summary.arrange(DOWN,buff=0.25)
        summary.move_to([0,-0.2,0])

        self.play(
            FadeOut(title4),
            LaggedStart(*[FadeIn(t,shift=UP*0.2) for t in summary],lag_ratio=0.25)
        )

        self.wait(2)