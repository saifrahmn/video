from manimlib import *

class Cigarette(Scene):
    def construct(self):
        cigarette = ImageMobject("cigraette.png").scale(2)
        self.play(FadeIn(cigarette))
        self.wait(1)
        
        cigarette_label = Text("Life as a Cigarette", font="Arial").scale(1.5).next_to(cigarette, DOWN)
        self.play(FadeIn(cigarette_label))
        self.wait(1)

        pleasure_text = Text("Initial pleasure, excitement, and danger", font="Arial").next_to(cigarette, UP)
        self.play(Write(pleasure_text))
        self.wait(1)

        addiction_text = Text("Addiction makes it hard to quit", font="Arial").next_to(pleasure_text, DOWN)
        self.play(Write(addiction_text))
        self.wait(1)

        challenges_text = Text("Unexpected challenges and difficulties", font="Arial").next_to(addiction_text, DOWN)
        self.play(Write(challenges_text))
        self.wait(1)

        impact_text = Text("Our actions and choices impact those around us", font="Arial").next_to(challenges_text, DOWN)
        self.play(Write(impact_text))
        self.wait(1)

        enjoyment_text = Text("Despite the harm, still enjoyable", font="Arial").next_to(impact_text, DOWN)
        self.play(Write(enjoyment_text))
        self.wait(1)

        self.play(FadeOut(cigarette), FadeOut(cigarette_label), FadeOut(pleasure_text), FadeOut(addiction_text), FadeOut(challenges_text), FadeOut(impact_text), FadeOut(enjoyment_text))
        self.wait(1)
