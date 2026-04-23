from manim import *
import random

# ── Palette ──────────────────────────────────────────────────────────────────
BG       = "#0F0F1A"
BLUE_1   = "#4AABDB"
BLUE_2   = "#2A6FA8"
TEAL     = "#3DCFB6"
YELLOW_A = "#FFD166"
PINK     = "#EF476F"
GREY_1   = "#CCCCCC"
GREY_2   = "#888888"
SAFE_TOP = 5.1
SAFE_BOTTOM = -5.7

# Vertical configuration for Instagram Reels
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def tx(text, size=0.45, color=WHITE, **kw):
    return Text(
        text,
        font="Arial",
        # font_size=int(size * 100),
        color=color,
        **kw
    )



class AIHallucination(Scene):
    def construct(self):

        # -----------------------
        # Scene 1 — Title
        # -----------------------

        title = tx("AI галлюцинациясы деген эмне?", font_size=40)

        subtitle = tx(
            "AI кээде туура эмес жооп ойлоп табат",
            font_size=30
        ).next_to(title, DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(3)

        self.play(FadeOut(title), FadeOut(subtitle))

        # -----------------------
        # Scene 2 — Prompt
        # -----------------------

        prompt = tx(
            'Суроо: "Айдын борборунда эмне бар?"',
            font_size=35,
            color=BLUE_1
        )

        self.play(Write(prompt))
        self.wait(2)

        answer = tx(
            "AI: Айдын ичинде чоң кристалл бар",
            font_size=35,
            color=YELLOW_A
        ).next_to(prompt, DOWN)

        self.play(FadeIn(answer))
        self.wait(2)

        warning = tx(
            "Бул туура эмес жооп",
            font_size=36
        ).next_to(answer, DOWN)

        self.play(FadeIn(warning))
        self.wait(2)

        self.play(
            FadeOut(prompt),
            FadeOut(answer),
            FadeOut(warning)
        )

        # -----------------------
        # Scene 3 — Prediction idea
        # -----------------------

        text = tx(
            "LLM чындыкты текшербейт",
            font_size=40
        )

        self.play(Write(text))
        self.wait(2)

        next_text = tx(
            "Ал кийинки сөздү болжолдойт",
            font_size=40,
            color=TEAL
        ).next_to(text, DOWN)

        self.play(FadeIn(next_text))
        self.wait(2)

        self.play(FadeOut(text), FadeOut(next_text))

        # ------------------------------------------------
        # Scene 4 — Probability distribution
        # ------------------------------------------------

        title2 = tx(
            "Кийинки сөздүн мүмкүнчүлүктөрү",
            font_size=40
        ).move_to([0, SAFE_TOP, 0])

        self.play(Write(title2))

        words = ["таш", "металл", "кристалл", "жер"]
        probs = [0.32, 0.27, 0.23, 0.18]

        labels = VGroup(*[
            Text(w, font_size=30) for w in words
        ])

        # labels.arrange(RIGHT, buff=1.2)
        # labels.shift(DOWN*4)

        bars = VGroup()

        for p in probs:
            bar = Rectangle(
                height=p*6,
                width=0.8
            )
            bars.add(bar)

        # bars.arrange(RIGHT, buff=1.5)
        # bars.align_to(labels, DOWN)
        bars.arrange(RIGHT, buff=1.5)
        bars.shift(DOWN*1.5)

        labels.arrange(RIGHT, buff=1.5)
        labels.next_to(bars, DOWN, buff=0.5)

        self.play(
            LaggedStart(*[GrowFromEdge(bar, DOWN) for bar in bars], lag_ratio=0.2)
        )

        self.play(FadeIn(labels))

        prob_text = VGroup(*[
            Text(f"{p:.2f}", font_size=28).next_to(bar, UP)
            for p, bar in zip(probs, bars)
        ])

        self.play(FadeIn(prob_text))

        self.wait(2)

        explanation = Text(
            "AI бул мүмкүнчүлүктөрдөн тандайт",
            font_size=36
        ).move_to([0, SAFE_BOTTOM, 0])

        self.play(FadeIn(explanation))
        self.wait(2)

        # ------------------------------------------------
        # Scene 5 — Sampling
        # ------------------------------------------------

        dot = Dot(radius=0.12)
        dot.move_to(UP*4)

        self.play(FadeIn(dot))

        target_bar = random.choice(bars)

        self.play(
            dot.animate.move_to(target_bar.get_top() + UP*0.3),
            run_time=2
        )

        highlight = SurroundingRectangle(target_bar)

        self.play(Create(highlight))

        result = Text(
            "Кээде туура эмес сөз тандалышы мүмкүн",
            font_size=36
        ).to_edge(DOWN)

        self.play(Transform(explanation, result))

        self.wait(3)

        self.play(
            FadeOut(bars),
            FadeOut(labels),
            FadeOut(prob_text),
            FadeOut(dot),
            FadeOut(highlight),
            FadeOut(title2),
            FadeOut(explanation)
        )

        # ------------------------------------------------
        # Scene 6 — Embedding space confusion
        # ------------------------------------------------

        plane = NumberPlane()
        plane.scale(0.8)

        self.play(Create(plane))

        words2 = ["ай", "таш", "металл", "кристалл", "жер"]

        positions = [
            LEFT*2 + UP,
            RIGHT*2,
            LEFT*1.5 + DOWN,
            RIGHT*1.2 + UP*1.5,
            DOWN*2
        ]

        word_objs = VGroup()

        for w, p in zip(words2, positions):
            t = Text(w, font_size=32)
            t.move_to(p)
            word_objs.add(t)

        self.play(FadeIn(word_objs))

        self.wait(2)

        self.play(
            *[
                w.animate.shift(
                    RIGHT*random.uniform(-1.5,1.5) +
                    UP*random.uniform(-1.5,1.5)
                )
                for w in word_objs
            ],
            run_time=3
        )

        confusion = Text(
            "Маалымат жетишсиз болгондо",
            font_size=40
        ).move_to([0, SAFE_TOP, 0])

        confusion2 = Text(
            "маанилер аралашып кетиши мүмкүн",
            font_size=40
        ).next_to(confusion, DOWN)

        self.play(FadeIn(confusion))
        self.play(FadeIn(confusion2))

        self.wait(3)

        self.play(
            FadeOut(plane),
            FadeOut(word_objs),
            FadeOut(confusion),
            FadeOut(confusion2)
        )

        # ------------------------------------------------
        # Scene 7 — Final message
        # ------------------------------------------------

        final1 = Text(
            "AI галлюцинациясы",
            font_size=72
        )

        final2 = Text(
            "ишенимдүү угулат",
            font_size=48
        ).next_to(final1, DOWN)

        final3 = Text(
            "бирок дайыма эле туура эмес",
            font_size=48
        ).next_to(final2, DOWN)

        self.play(Write(final1))
        self.play(FadeIn(final2))
        self.play(FadeIn(final3))

        self.wait(4)