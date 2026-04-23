from manim import *

# ---------- REELS FORMAT ----------
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#0f172a"

# ---------- COLORS ----------
BLUE_MAIN = "#60a5fa"
GREEN = "#34d399"
RED = "#f87171"
YELLOW = "#facc15"
WHITE_SOFT = "#e5e7eb"


def tx(text, size=0.6, color=WHITE_SOFT):
    return Text(
        text,
        font="DejaVu Sans",
        font_size=int(size * 80),
        color=color,
        line_spacing=0.9
    )


class PromptVideo(Scene):
    def construct(self):

        # ---------- TITLE ----------
        title = tx(
            "Prompt деген эмне?",
            0.8,
            BLUE_MAIN
        ).move_to([0, 3.8, 0])

        self.play(Write(title))
        self.wait(1)

        # ---------- QUESTION ----------
        question = tx(
            "AI менен сүйлөшкөндө\nсен эмне жазасың?",
            0.6
        ).move_to([0, 1.5, 0])

        self.play(FadeIn(question))
        self.wait(2)

        # ---------- PROMPT WORD ----------
        prompt_word = tx(
            "Ошол жазганың\nPROMPT деп аталат",
            0.7,
            GREEN
        ).move_to([0, -1, 0])

        self.play(Write(prompt_word))
        self.wait(3)

        self.play(
            FadeOut(question),
            FadeOut(prompt_word)
        )

        # ---------- BAD PROMPT ----------
        bad_title = tx(
            "Жаман prompt",
            0.7,
            RED
        ).move_to([0, 3.8, 0])

        bad_prompt = tx(
            "Мага текст жаз",
            0.7
        ).move_to([0, 1.5, 0])

        bad_ai = tx(
            "AI: Кандай текст?",
            0.6,
            YELLOW
        ).move_to([0, -0.5, 0])

        self.play(
            Transform(title, bad_title),
            FadeIn(bad_prompt)
        )

        self.wait(2)

        self.play(FadeIn(bad_ai))
        self.wait(3)

        self.play(
            FadeOut(bad_prompt),
            FadeOut(bad_ai)
        )

        # ---------- GOOD PROMPT ----------
        good_title = tx(
            "Жакшы prompt",
            0.7,
            GREEN
        ).move_to([0, 3.8, 0])

        good_prompt = tx(
            "10 жаштагы балага\nкара тешикти түшүндүр",
            0.65
        ).move_to([0, 1.5, 0])

        good_ai = tx(
            "AI: Кара тешик —\nабдан күчтүү гравитация...",
            0.55,
            YELLOW
        ).move_to([0, -1.2, 0])

        self.play(
            Transform(title, good_title),
            FadeIn(good_prompt)
        )

        self.wait(2)

        self.play(FadeIn(good_ai))
        self.wait(4)

        self.play(
            FadeOut(good_prompt),
            FadeOut(good_ai)
        )

        # ---------- CONCLUSION ----------
        final = tx(
            "AI кандай жооп берет\nсенин PROMPT'уңдан көз каранды",
            0.7,
            BLUE_MAIN
        ).move_to([0, 0, 0])

        self.play(
            FadeOut(title),
            Write(final)
        )

        self.wait(4)