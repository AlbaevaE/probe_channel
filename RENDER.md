# LLM Kyrgyz — Render Guide

## 1. Install dependencies

```bash
# macOS — system deps
brew install py-cairo pango pkg-config ffmpeg

# Python deps
pip3 install manim
```

## 2. Render (1080×1920, 60 fps — Instagram quality)

```bash
cd /Users/albaeva/probe_channel

# High quality (slow, production)
manim -pqh llm_kyrgyz.py LLM_Kyrgyz

# Medium quality (fast preview)
manim -pqm llm_kyrgyz.py LLM_Kyrgyz
```

Output lands in:
```
media/videos/llm_kyrgyz/1080p60/LLM_Kyrgyz.mp4
```

## 3. Individual scenes (for debugging)

```bash
manim -pqm llm_kyrgyz.py Scene1_Title
manim -pqm llm_kyrgyz.py Scene2_Tokens
manim -pqm llm_kyrgyz.py Scene3_Network
manim -pqm llm_kyrgyz.py Scene4_Prediction
manim -pqm llm_kyrgyz.py Scene5_Training
manim -pqm llm_kyrgyz.py Scene6_Outro
```

## 4. Instagram export tip

The script already sets 1080×1920 (9:16 vertical).  
After render, the MP4 is ready to upload directly to Reels.

## Scene timeline (~50 s)

| Scene | Duration | Content |
|-------|----------|---------|
| Scene1_Title      | 0–5 s   | "LLM деген эмне?" title card |
| Scene2_Tokens     | 5–14 s  | Text → tokenisation → vectors |
| Scene3_Network    | 14–25 s | Neural network layers pulsing |
| Scene4_Prediction | 25–36 s | Next-token prediction with probability bars |
| Scene5_Training   | 36–46 s | Training data (books, internet, code) |
| Scene6_Outro      | 46–50 s | Summary + subscribe call-to-action |
