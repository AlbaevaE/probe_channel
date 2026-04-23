from manim import *

# Vertical Reels config
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#0E1117"


# 3Blue1Brown-style palette
TITLE_COLOR = "#FFE66D"
TEXT_COLOR = "#F5F5F5"
ACCENT_BLUE = "#58C4DD"
ACCENT_YELLOW = "#FFD166"
ACCENT_GREEN = "#83C167"
ACCENT_PINK = "#FC6255"
ACCENT_PURPLE = "#C77DFF"
MUTED = "#6C757D"
SAFE_TOP = 5
SAFE_BOTTOM = -5.5

class TokenizationReel(Scene):
    def construct(self):
        self.scene_1_hook()
        self.scene_2_problem()
        self.scene_3_analogy()
        self.scene_4_cut_the_sentence()
        self.scene_5_subword_tokens()
        self.scene_6_tokens_to_numbers()
        self.scene_7_vocabulary()
        self.scene_8_full_pipeline()
        self.scene_9_summary()

    # -----------------------------------------------------------
    # Scene 1 — Hook: "Токен деген эмне?"
    # -----------------------------------------------------------
    def scene_1_hook(self):
        q_mark = Text("?", font_size=260, color=ACCENT_YELLOW, weight=BOLD)
        q_mark.set_stroke(width=0)

        title = Text("Токен", font_size=120, color=TITLE_COLOR, weight=BOLD)
        subtitle = Text("деген эмне?", font_size=72, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.35)

        hint = Text(
            "AI текстти кантип түшүнөт?",
            font_size=44,
            color=ACCENT_BLUE,
        )
        hint.next_to(subtitle, DOWN, buff=0.8)

        self.play(FadeIn(q_mark, scale=0.6), run_time=0.8)
        self.wait(0.4)
        self.play(
            q_mark.animate.scale(0.35).to_edge(UP, buff=1.2).set_opacity(0.4),
            run_time=0.8,
        )
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.6)
        self.wait(1.8)

        self.play(
            FadeOut(q_mark),
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(hint),
            run_time=0.6,
        )

    # -----------------------------------------------------------
    # Scene 2 — The problem: AI does not read like humans
    # -----------------------------------------------------------
    def scene_2_problem(self):
        human_label = Text("Адам", font_size=44, color=ACCENT_GREEN)
        human_label.move_to([0, SAFE_TOP, 0])

        sentence = Text(
            "Мен алманы жедим",
            font_size=64,
            color=TEXT_COLOR,
        )
        sentence.next_to(human_label, DOWN, buff=0.8)

        eye = Circle(radius=0.35, color=ACCENT_GREEN, fill_opacity=0.2)
        pupil = Dot(radius=0.12, color=ACCENT_GREEN)
        eye_group = VGroup(eye, pupil).next_to(sentence, DOWN, buff=0.6)

        read_note = Text(
            "Бүт сүйлөмдү бир көрө алат",
            font_size=36,
            color=MUTED,
        ).next_to(eye_group, DOWN, buff=0.4)

        self.play(FadeIn(human_label), run_time=0.5)
        self.play(Write(sentence), run_time=1.2)
        self.play(FadeIn(eye_group), run_time=0.4)
        self.play(FadeIn(read_note), run_time=0.4)
        self.wait(1.2)

        # Transform into the AI side
        ai_label = Text("AI", font_size=44, color=ACCENT_PINK).move_to(human_label)

        robot_body = RoundedRectangle(
            width=1.6, height=1.8, corner_radius=0.25,
            color=ACCENT_PINK, fill_opacity=0.15,
        )
        robot_eye_l = Dot(radius=0.1, color=ACCENT_PINK).shift(LEFT * 0.35 + UP * 0.2)
        robot_eye_r = Dot(radius=0.1, color=ACCENT_PINK).shift(RIGHT * 0.35 + UP * 0.2)
        robot_mouth = Line(LEFT * 0.25, RIGHT * 0.25, color=ACCENT_PINK).shift(DOWN * 0.3)
        robot = VGroup(robot_body, robot_eye_l, robot_eye_r, robot_mouth)
        robot.next_to(sentence, DOWN, buff=0.8)

        confused = Text("???", font_size=48, color=ACCENT_PINK)
        confused.next_to(robot, UP, buff=0.2)

        fail_note = Text(
            "Тамгаларды түз түшүнбөйт",
            font_size=36,
            color=MUTED,
        ).next_to(robot, DOWN, buff=0.4)

        self.play(
            Transform(human_label, ai_label),
            FadeOut(eye_group),
            FadeOut(read_note),
            run_time=0.6,
        )
        self.play(FadeIn(robot), run_time=0.5)
        self.play(Write(confused), run_time=0.5)
        self.play(FadeIn(fail_note), run_time=0.4)
        self.wait(1.8)

        self.play(
            FadeOut(human_label),
            FadeOut(sentence),
            FadeOut(robot),
            FadeOut(confused),
            FadeOut(fail_note),
            run_time=0.6,
        )

    # -----------------------------------------------------------
    # Scene 3 — Analogy: cut the apple
    # -----------------------------------------------------------
    def scene_3_analogy(self):
        top = Text(
            "Бир чоң алманы жута албайсың —",
            font_size=40,
            color=TEXT_COLOR,
        ).move_to([0, SAFE_TOP, 0])

        bottom = Text(
            "адегенде кесип аласың.",
            font_size=40,
            color=TEXT_COLOR,
        ).next_to(top, DOWN, buff=0.2)

        apple = Circle(radius=1.0, color=ACCENT_PINK, fill_opacity=0.9)
        leaf = Triangle(color=ACCENT_GREEN, fill_opacity=1).scale(0.2)
        leaf.move_to(apple.get_top() + UP * 0.1 + RIGHT * 0.15)
        apple_group = VGroup(apple, leaf).shift(DOWN * 0.5)

        self.play(FadeIn(top), FadeIn(bottom), run_time=0.6)
        self.play(GrowFromCenter(apple_group), run_time=0.8)
        self.wait(0.8)

        # Cut the apple
        knife_line = Line(
            apple.get_center() + UP * 1.4,
            apple.get_center() + DOWN * 1.4,
            color=ACCENT_BLUE, stroke_width=8,
        )
        self.play(Create(knife_line), run_time=0.4)
        self.play(FadeOut(knife_line), run_time=0.2)

        left_half = apple.copy().set_color(ACCENT_PINK)
        right_half = apple.copy().set_color(ACCENT_PINK)
        self.remove(apple_group)
        self.add(left_half, right_half, leaf)
        self.play(
            left_half.animate.shift(LEFT * 0.8),
            right_half.animate.shift(RIGHT * 0.8),
            leaf.animate.shift(RIGHT * 0.8),
            run_time=0.5,
        )

        # Cut again into four
        piece_1 = left_half.copy()
        piece_2 = left_half.copy()
        piece_3 = right_half.copy()
        piece_4 = right_half.copy()
        self.remove(left_half, right_half)
        self.add(piece_1, piece_2, piece_3, piece_4)
        self.play(
            piece_1.animate.shift(LEFT * 0.6).scale(0.7),
            piece_2.animate.shift(LEFT * 0.2).scale(0.7),
            piece_3.animate.shift(RIGHT * 0.2).scale(0.7),
            piece_4.animate.shift(RIGHT * 0.6).scale(0.7),
            leaf.animate.shift(UP * 0.3).scale(0.7),
            run_time=0.6,
        )

        conclusion = Text(
            "AI да текстти ушундай кесет.",
            font_size=42,
            color=ACCENT_YELLOW,
            weight=BOLD,
        ).to_edge(DOWN, buff=2.0)

        self.play(Write(conclusion), run_time=0.9)
        self.wait(1.8)

        self.play(
            FadeOut(top),
            FadeOut(bottom),
            FadeOut(piece_1),
            FadeOut(piece_2),
            FadeOut(piece_3),
            FadeOut(piece_4),
            FadeOut(leaf),
            FadeOut(conclusion),
            run_time=0.6,
        )

    # -----------------------------------------------------------
    # Scene 4 — Cut a sentence into word tokens
    # -----------------------------------------------------------
    def scene_4_cut_the_sentence(self):
        header = Text(
            "Мисалы: сүйлөмдү кесели",
            font_size=40,
            color=ACCENT_BLUE,
        ).move_to([0, SAFE_TOP, 0])

        sentence = Text(
            "Мен мектепке бара жатам",
            font_size=60,
            color=TEXT_COLOR,
        )

        self.play(FadeIn(header), run_time=0.5)
        self.play(Write(sentence), run_time=1.2)
        self.wait(0.5)

        # Split into word tokens
        words = ["Мен", "мектепке", "бара", "жатам"]
        colors = [ACCENT_BLUE, ACCENT_YELLOW, ACCENT_GREEN, ACCENT_PURPLE]

        token_texts = VGroup(
            *[
                Text(w, font_size=48, color=c, weight=BOLD)
                for w, c in zip(words, colors)
            ]
        ).arrange(RIGHT, buff=0.35)

        # Shrink in two rows so they fit vertical frame
        row1 = VGroup(token_texts[0], token_texts[1]).arrange(RIGHT, buff=0.35)
        row2 = VGroup(token_texts[2], token_texts[3]).arrange(RIGHT, buff=0.35)
        rows = VGroup(row1, row2).arrange(DOWN, buff=0.5)

        self.play(FadeOut(sentence), run_time=0.3)
        self.play(
            LaggedStart(
                *[FadeIn(t, shift=DOWN * 0.4) for t in token_texts],
                lag_ratio=0.2,
            ),
            run_time=1.3,
        )

        # Boxes around each token
        boxes = VGroup(
            *[
                SurroundingRectangle(t, buff=0.18, color=t.color, corner_radius=0.15)
                for t in token_texts
            ]
        )
        self.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.15), run_time=1.0)

        label = Text(
            "Ар бир кесек — бул ТОКЕН",
            font_size=44,
            color=ACCENT_YELLOW,
            weight=BOLD,
        ).move_to([0, SAFE_BOTTOM, 0])
        self.play(Write(label), run_time=0.9)
        self.wait(2.0)

        self.play(
            FadeOut(header),
            FadeOut(label),
            *[FadeOut(b) for b in boxes],
            run_time=0.5,
        )

        # keep token_texts for the next scene, fade them out cleanly instead
        self.play(FadeOut(token_texts), run_time=0.4)

    # -----------------------------------------------------------
    # Scene 5 — Sub-word tokens: words split smaller
    # -----------------------------------------------------------
    def scene_5_subword_tokens(self):
        header = Text(
            "Кээде сөз андан да кичине болот",
            font_size=38,
            color=ACCENT_BLUE,
        ).move_to([0, SAFE_TOP, 0])

        word = Text("мектепке", font_size=80, color=ACCENT_YELLOW, weight=BOLD)
        self.play(FadeIn(header), run_time=0.4)
        self.play(Write(word), run_time=0.9)
        self.wait(0.5)

        # Split into "мектеп" + "ке"
        part1 = Text("мектеп", font_size=70, color=ACCENT_GREEN, weight=BOLD)
        part2 = Text("ке", font_size=70, color=ACCENT_PINK, weight=BOLD)
        parts = VGroup(part1, part2).arrange(RIGHT, buff=0.4)

        self.play(Transform(word, parts), run_time=1.0)

        box1 = SurroundingRectangle(part1, buff=0.18, color=ACCENT_GREEN, corner_radius=0.15)
        box2 = SurroundingRectangle(part2, buff=0.18, color=ACCENT_PINK, corner_radius=0.15)
        self.play(Create(box1), Create(box2), run_time=0.6)

        note1 = Text("көп колдонулат", font_size=32, color=ACCENT_GREEN)
        note1.next_to(box1, DOWN, buff=0.35)
        note2 = Text("жөндөмө", font_size=32, color=ACCENT_PINK)
        note2.next_to(box2, DOWN, buff=0.35)

        self.play(FadeIn(note1), FadeIn(note2), run_time=0.5)
        self.wait(1.0)

        explain = Text(
            "AI сөздөрдү легодой чогултат.",
            font_size=38,
            color=ACCENT_YELLOW,
        ).move_to([0, SAFE_BOTTOM, 0])

        self.play(Write(explain), run_time=0.9)
        self.wait(2.0)

        self.play(
            FadeOut(header),
            FadeOut(word),
            FadeOut(box1),
            FadeOut(box2),
            FadeOut(note1),
            FadeOut(note2),
            FadeOut(explain),
            run_time=0.6,
        )

    # -----------------------------------------------------------
    # Scene 6 — Tokens to numbers
    # -----------------------------------------------------------
    def scene_6_tokens_to_numbers(self):
        header = Text(
            "Ар бир токенге — өзүнүн саны",
            font_size=40,
            color=ACCENT_BLUE,
        ).move_to([0, SAFE_TOP, 0])
        self.play(FadeIn(header), run_time=0.5)

        pairs = [
            ("Мен",    "42",    ACCENT_BLUE),
            ("мектеп", "1523",  ACCENT_YELLOW),
            ("ке",     "7",     ACCENT_PINK),
            ("бара",   "318",   ACCENT_GREEN),
            ("жатам",  "2904",  ACCENT_PURPLE),
        ]

        rows = VGroup()
        for tok, num, color in pairs:
            t = Text(tok, font_size=44, color=color, weight=BOLD)
            arrow = Arrow(
                start=LEFT * 0.3, end=RIGHT * 0.3,
                buff=0, color=MUTED, stroke_width=5,
                max_tip_length_to_length_ratio=0.35,
            )
            n = Text(num, font_size=44, color=TEXT_COLOR)
            row = VGroup(t, arrow, n).arrange(RIGHT, buff=0.4)
            rows.add(row)

        rows.arrange(DOWN, buff=0.45).move_to(ORIGIN)

        # Align all arrows to a common center column for a clean look
        for row in rows:
            row[0].align_to(rows[0][0], RIGHT)
            row[2].align_to(rows[0][2], LEFT)

        self.play(
            LaggedStart(
                *[FadeIn(r, shift=RIGHT * 0.3) for r in rows],
                lag_ratio=0.15,
            ),
            run_time=1.8,
        )
        self.wait(1.2)

        caption = Text(
            "AI үчүн текст — бул сандар.",
            font_size=40,
            color=ACCENT_YELLOW,
            weight=BOLD,
        ).to_edge(DOWN, buff=1.8)
        self.play(Write(caption), run_time=0.9)
        self.wait(2.0)

        self.play(FadeOut(header), FadeOut(rows), FadeOut(caption), run_time=0.5)

    # -----------------------------------------------------------
    # Scene 7 — Vocabulary: huge dictionary of tokens
    # -----------------------------------------------------------
    def scene_7_vocabulary(self):
        header = Text(
            "AI'нин токен сөздүгү",
            font_size=44,
            color=ACCENT_BLUE,
            weight=BOLD,
        ).move_to([0, SAFE_TOP, 0])
        self.play(FadeIn(header), run_time=0.5)

        # A list that looks like a dictionary
        entries_data = [
            ("0",      "<башы>"),
            ("1",      "<бош>"),
            ("42",     "Мен"),
            ("318",    "бара"),
            ("1523",   "мектеп"),
            ("2904",   "жатам"),
            ("...",    "..."),
            ("49998",  "күн"),
            ("49999",  "түн"),
        ]

        lines = VGroup()
        for num, tok in entries_data:
            n = Text(num, font_size=32, color=MUTED)
            t = Text(tok, font_size=34, color=TEXT_COLOR)
            line = VGroup(n, t).arrange(RIGHT, buff=0.6)
            lines.add(line)

        lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22).move_to(ORIGIN)

        frame = SurroundingRectangle(
            lines, buff=0.45, color=MUTED, corner_radius=0.2, stroke_width=3
        )

        self.play(Create(frame), run_time=0.6)
        self.play(
            LaggedStart(*[FadeIn(l, shift=UP * 0.2) for l in lines], lag_ratio=0.08),
            run_time=1.5,
        )
        self.wait(0.8)

        big_number = Text(
            "≈ 50 000 токен",
            font_size=50,
            color=ACCENT_YELLOW,
            weight=BOLD,
        ).move_to([0, SAFE_BOTTOM, 0])

        self.play(Write(big_number), run_time=0.9)
        self.wait(1.8)

        self.play(
            FadeOut(header),
            FadeOut(frame),
            FadeOut(lines),
            FadeOut(big_number),
            run_time=0.6,
        )

    # -----------------------------------------------------------
    # Scene 8 — Full pipeline: text → tokens → numbers → AI
    # -----------------------------------------------------------
    def scene_8_full_pipeline(self):
        header = Text(
            "Баары кантип иштейт?",
            font_size=44,
            color=ACCENT_BLUE,
            weight=BOLD,
        ).move_to([0, SAFE_TOP, 0])
        self.play(FadeIn(header), run_time=0.5)

        # Step 1 — raw text
        txt = Text("«Салам, дүйнө!»", font_size=46, color=TEXT_COLOR)
        step1_label = Text("1. Текст", font_size=30, color=MUTED).next_to(txt, UP, buff=0.25)
        group1 = VGroup(step1_label, txt).move_to(UP * 3.5)

        # Step 2 — tokens
        tokens = VGroup(
            Text("Салам", font_size=40, color=ACCENT_BLUE, weight=BOLD),
            Text(",", font_size=40, color=ACCENT_GREEN, weight=BOLD),
            Text("дүйнө", font_size=40, color=ACCENT_YELLOW, weight=BOLD),
            Text("!", font_size=40, color=ACCENT_PINK, weight=BOLD),
        ).arrange(RIGHT, buff=0.25)
        step2_label = Text("2. Токендер", font_size=30, color=MUTED).next_to(tokens, UP, buff=0.25)
        group2 = VGroup(step2_label, tokens).move_to(UP * 1.3)

        # Step 3 — numbers
        numbers = VGroup(
            Text("78",   font_size=40, color=ACCENT_BLUE),
            Text("15",   font_size=40, color=ACCENT_GREEN),
            Text("2041", font_size=40, color=ACCENT_YELLOW),
            Text("9",    font_size=40, color=ACCENT_PINK),
        ).arrange(RIGHT, buff=0.4)
        step3_label = Text("3. Сандар", font_size=30, color=MUTED).next_to(numbers, UP, buff=0.25)
        group3 = VGroup(step3_label, numbers).move_to(DOWN * 0.9)

        # Step 4 — AI brain
        brain = RoundedRectangle(
            width=3.2, height=1.6, corner_radius=0.4,
            color=ACCENT_PURPLE, fill_opacity=0.2,
        )
        brain_label = Text("AI", font_size=46, color=ACCENT_PURPLE, weight=BOLD)
        brain_label.move_to(brain.get_center())
        step4_label = Text("4. AI ойлонот", font_size=30, color=MUTED).next_to(brain, UP, buff=0.25)
        group4 = VGroup(step4_label, brain, brain_label).move_to(DOWN * 3.2)

        arrow1 = Arrow(group1.get_bottom(), group2.get_top(), color=MUTED, buff=0.1, stroke_width=5)
        arrow2 = Arrow(group2.get_bottom(), group3.get_top(), color=MUTED, buff=0.1, stroke_width=5)
        arrow3 = Arrow(group3.get_bottom(), group4.get_top(), color=MUTED, buff=0.1, stroke_width=5)

        self.play(FadeIn(group1), run_time=0.5)
        self.play(GrowArrow(arrow1), run_time=0.4)
        self.play(FadeIn(group2, shift=UP * 0.2), run_time=0.6)
        self.play(GrowArrow(arrow2), run_time=0.4)
        self.play(FadeIn(group3, shift=UP * 0.2), run_time=0.6)
        self.play(GrowArrow(arrow3), run_time=0.4)
        self.play(FadeIn(group4, shift=UP * 0.2), run_time=0.6)

        # Pulse the AI brain
        self.play(
            brain.animate.set_fill(ACCENT_PURPLE, opacity=0.5),
            run_time=0.4,
        )
        self.play(
            brain.animate.set_fill(ACCENT_PURPLE, opacity=0.2),
            run_time=0.4,
        )
        self.wait(1.6)

        self.play(
            FadeOut(header),
            FadeOut(group1), FadeOut(group2), FadeOut(group3), FadeOut(group4),
            FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3),
            run_time=0.6,
        )

    # -----------------------------------------------------------
    # Scene 9 — Summary takeaway
    # -----------------------------------------------------------
    def scene_9_summary(self):
        line1 = Text("Текст", font_size=72, color=TEXT_COLOR, weight=BOLD)
        arrow_a = Text("→", font_size=72, color=MUTED)
        line2 = Text("Токен", font_size=72, color=ACCENT_YELLOW, weight=BOLD)
        arrow_b = Text("→", font_size=72, color=MUTED)
        line3 = Text("Сан", font_size=72, color=ACCENT_BLUE, weight=BOLD)

        row = VGroup(line1, arrow_a, line2, arrow_b, line3).arrange(RIGHT, buff=0.3)
        row.scale(0.9)

        self.play(Write(line1), run_time=0.6)
        self.play(FadeIn(arrow_a), Write(line2), run_time=0.8)
        self.play(FadeIn(arrow_b), Write(line3), run_time=0.8)

        final = Text(
            "Мына ушинтип AI\nтексти түшүнөт.",
            font_size=50,
            color=ACCENT_GREEN,
            weight=BOLD,
            line_spacing=1.2,
        )
        final.next_to(row, DOWN, buff=1.2)

        self.play(FadeIn(final, shift=UP * 0.3), run_time=0.9)
