from manim import config, Scene, Circle, Rectangle, Polygon, Create, Axes, Transform, Write, Text, Indicate, Tex, Uncreate, FadeIn, FadeOut, MoveToTarget, DashedLine
from manim import DEGREES, UP, DOWN, LEFT, RIGHT
from manim import WHITE, BLACK, PINK, GREY, BLUE, RED
from manim import *   # noqa: F403
import pandas as pd

config.background_color = WHITE


pwr_blender = [0, 0, 0, 0, 0, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pwr_stove = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 0, 2500, 2500, 2500, 0, 2500, 2500, 2500, 0, 2500, 2500, 2500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pwr_kettle = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2100, 2100, 2100, 2100, 2100, 2100, 2100, 2100, 2100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pwr_other = [245, 215, 213, 224, 233, 216, 260, 232, 245, 240, 240, 260, 280, 249, 235, 255, 250, 270, 268, 275, 260, 242, 202, 221, 204, 217, 230, 221, 231, 217, 232, 242, 232, 228, 245, 204, 200, 246, 243, 215, 250, 241, 237, 205, 233, 208, 250, 200, 207, 233]
pwr_total = [a + b + c + d for a, b, c, d in zip(pwr_blender, pwr_stove, pwr_kettle, pwr_other)]
x_scale = 12
x_spacing = 5


CBLUE = "#3257A8"
CRED = "#9D0003"
CGREEN = "#30A490"
CDARKGREEN = "#192E40"
CACCENT = "#ff9179"

class CreateGraph(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_graph()
        self.add_labels()
        self.add_data()

    def create_graph(self):
        self.graph = Axes(
            x_range=[0, x_scale * (len(pwr_total)), (x_scale * x_spacing) // 2],
            y_range=[0, max(pwr_total) + 500, 500],
            x_length=9,
            y_length=5.5,
            axis_config={
                "color": BLACK,
                "tip_width": 0.2,
                "tip_height": 0.2,
                "font_size": 24
            }
        )

    def add_labels(self):
        x_numbers = self.graph.get_x_axis().add_numbers([i for i in range(0, x_scale * len(pwr_total), x_scale * x_spacing)])
        y_numbers = self.graph.get_y_axis().add_numbers([i for i in range(0, int(max(pwr_total)) + 500, 1000)])

        for label in x_numbers:
            label.set_color(BLACK)
        for label in y_numbers:
            label.set_color(BLACK)

        self.x_label = self.graph.get_x_axis_label(Tex("Zeit in Sekunden").scale(0.65), edge=DOWN, direction=DOWN, buff=0.25).set_color(BLACK)
        self.y_label = self.graph.get_y_axis_label(Tex("Leistung in Watt").scale(0.65).rotate(90 * DEGREES), edge=LEFT, direction=LEFT, buff=0.25).set_color(BLACK)

    def add_data(self):
        self.plotted_total_0 = self.graph.plot(lambda x: pwr_total[min(int(x / x_scale), len(pwr_total)-1)], color="#D5D5D5")
        self.plotted_total_1 = self.graph.plot(lambda x: pwr_total[min(int(x / x_scale), len(pwr_total)-1)], color=BLACK)


class CreateGraph_orig(Scene):
    def construct(self):


        # Erstellen Sie ein Diagramm mit den Datenpunkten
        graph = Axes(
            x_range=[0, x_scale * (len(pwr_total)), (x_scale * x_spacing) // 2],  # Multiplizieren Sie die X-Werte mit 5
            y_range=[0, max(pwr_total) + 500, 500],
            x_length=9,
            y_length=5.5,
            axis_config=
                {
                    "color": BLACK,
                    "tip_width": 0.2,
                    "tip_height": 0.2,
                    "font_size": 24
                }
        )

        # Beschriftungen hinzufügen
        x_values = [x_scale * i for i in range(0, len(pwr_blender), x_spacing)]  # Multiplizieren Sie die X-Werte mit 5
        x_numbers = graph.get_x_axis().add_numbers([i for i in range(0, x_scale * len(pwr_total), x_scale * x_spacing)])
        y_numbers = graph.get_y_axis().add_numbers([i for i in range(0, int(max(pwr_total)) + 500, 1000)])

        # Setzen Sie die Farbe der Achsenbeschriftungen auf Schwarz
        for label in x_numbers:
            label.set_color(BLACK)
        for label in y_numbers:
            label.set_color(BLACK)

        # Achsentitel hinzufügen
        x_label = graph.get_x_axis_label(Tex("Zeit in Sekunden").scale(0.65), edge=DOWN, direction=DOWN, buff=0.25).set_color(BLACK)
        y_label = graph.get_y_axis_label(Tex("Leistung in Watt").scale(0.65).rotate(90 * DEGREES), edge=LEFT, direction=LEFT, buff=0.25).set_color(BLACK)

        # Alles zur Szene hinzufügen und animieren

        self.play(Create(graph), Write(x_label), Write(y_label))
        self.wait(0.5)

        # 1. Erstellen und Anzeigen der Summe aller vier Serien
        plotted_total_0 = graph.plot(lambda x: pwr_total[min(int(x / x_scale), len(pwr_total)-1)], color="#D5D5D5")
        plotted_total_1 = graph.plot(lambda x: pwr_total[min(int(x / x_scale), len(pwr_total)-1)], color=BLACK)
        self.play(Create(plotted_total_0), Create(plotted_total_1), run_time=3)
        self.wait(2)

        # 2. Transformieren Sie die Summe in (Summe-pwr_blender) und pwr_blender
        pwr_sum_minus_blender = [total - blender for total, blender in zip(pwr_total, pwr_blender)]
        plotted_total_2 = graph.plot(lambda x: pwr_sum_minus_blender[min(int(x / x_scale), len(pwr_sum_minus_blender)-1)], color=BLACK)
        plotted_blender = graph.plot(lambda x: pwr_blender[min(int(x / x_scale), len(pwr_blender)-1)], color=CBLUE, use_smoothing=False)
        plotted_blender_original = plotted_blender.copy()

        # Finden Sie den ersten und letzten Nicht-Null-Wert in der Datenreihe
        non_zero_indices = [i for i, value in enumerate(pwr_blender) if value != 0]
        x_min = non_zero_indices[0]
        x_max = non_zero_indices[-1]
        
        area_under_blender = graph.get_area(plotted_blender, color=CBLUE, opacity=0.5, x_range=[(x_min) * x_scale, (x_max+1) * x_scale])
        text_blender = Text("Mixer").scale(0.7).next_to(graph,UR).set_color(CBLUE)



        self.play(Create(plotted_blender), Write(text_blender), Create(area_under_blender), run_time=2)
        self.bring_to_front(graph.x_axis)
        self.wait(1)
        self.play(Indicate(area_under_blender))
        self.wait(2)
        self.play(FadeOut(area_under_blender))

        plotted_blender_under_text = plotted_blender.copy().scale(0.2).next_to(text_blender, DOWN)
        self.play(Transform(plotted_total_1, plotted_total_2), Transform(plotted_blender, plotted_blender_under_text))
        
        
        self.wait(2)

        # 3. Transformieren Sie die Summe in (Summe-pwr_blender-pwr_stove), pwr_blender und pwr_stove
        pwr_sum_minus_blender_stove = [sum_minus_blender - stove for sum_minus_blender, stove in zip(pwr_sum_minus_blender, pwr_stove)]
        plotted_sum_minus_blender_stove = graph.plot(lambda x: pwr_sum_minus_blender_stove[min(int(x / x_scale), len(pwr_sum_minus_blender_stove)-1)], color=BLACK)
        plotted_stove = graph.plot(lambda x: pwr_stove[min(int(x / x_scale), len(pwr_stove)-1)], color=CRED, use_smoothing=False)
        plotted_stove_original = plotted_stove.copy()
        
        text_stove = Text("Herdplatte").scale(0.7).next_to(plotted_blender,DOWN).set_color(CRED)



        self.play(Create(plotted_stove), Write(text_stove), run_time=2)
        self.bring_to_front(graph.x_axis)
        self.wait(0.3)
        self.play(Indicate(plotted_stove))
        self.wait(1)
        self.remove(plotted_total_1)
        
        plotted_stove_under_text = plotted_stove.copy().scale(0.2).next_to(text_stove, DOWN)
        self.play(Transform(plotted_total_2, plotted_sum_minus_blender_stove, replace_mobject_with_target_in_scene=True), 
                  Transform(plotted_stove, plotted_stove_under_text))
        self.wait(2)

        # 4. Transformieren Sie die Summe in (pwr_sum_minus_blender_stove - pwr_kettle), pwr_blender, pwr_stove und pwr_kettle
        pwr_sum_minus_blender_stove_kettle = [sum_minus_blender_stove - kettle for sum_minus_blender_stove, kettle in zip(pwr_sum_minus_blender_stove, pwr_kettle)]
        plotted_sum_minus_blender_stove_kettle = graph.plot(lambda x: pwr_sum_minus_blender_stove_kettle[min(int(x / x_scale), len(pwr_sum_minus_blender_stove_kettle)-1)], color=BLACK)
        plotted_kettle = graph.plot(lambda x: pwr_kettle[min(int(x / x_scale), len(pwr_kettle)-1)], color=CGREEN, use_smoothing=False)
        plotted_kettle_original = plotted_kettle.copy()

        text_kettle = Text("Wasserkocher").scale(0.7).next_to(plotted_stove,DOWN).set_color(CGREEN)

        self.play(Create(plotted_kettle), Write(text_kettle), run_time=2)
        self.bring_to_front(graph.x_axis)
        self.wait(0.3)
        self.play(Indicate(plotted_kettle))
        self.wait(1)
        self.remove(plotted_sum_minus_blender_stove)
        
        plotted_kettle_under_text = plotted_kettle.copy().scale(0.2).next_to(text_kettle, DOWN)
        self.play(Transform(plotted_sum_minus_blender_stove, plotted_sum_minus_blender_stove_kettle, replace_mobject_with_target_in_scene=True), 
                  Transform(plotted_kettle, plotted_kettle_under_text))
        self.wait(2)
        
        self.play(Uncreate(plotted_sum_minus_blender_stove_kettle), 
                  Uncreate(plotted_total_0),
                  Transform(plotted_blender_under_text, plotted_blender_original)                  
        )
        
        self.play(Transform(plotted_stove_under_text, plotted_stove_original))
        self.play(Transform(plotted_kettle_under_text, plotted_kettle_original))
        self.bring_to_front(graph.x_axis)
        self.wait(2)


        # Funktion, die den maximalen Wert der drei Serien für einen gegebenen x-Wert zurückgibt
        def max_value_function(x):
            index = min(int(x / x_scale), len(pwr_blender)-1)
            return max(pwr_blender[index], pwr_stove[index], pwr_kettle[index])

        # Erstellen Sie eine Linie für den maximalen Wert der drei Serien
        max_value_line = graph.plot(max_value_function, color=CACCENT, use_smoothing=False)  # Die Farbe ist hier nicht wichtig, da wir nur den Bereich darunter füllen wollen

        plotted_x_min = 5 * x_scale
        plotted_x_max = 38 * x_scale

        # Vertikale Linien an den X-Werten 60 und 450 erstellen
        y_min, y_max = graph.y_range[0], graph.y_range[1]
        left_line = DashedLine(start=graph.c2p(plotted_x_min, y_min), end=graph.c2p(plotted_x_min, y_max), color=BLACK)
        right_line = DashedLine(start=graph.c2p(plotted_x_max, y_min), end=graph.c2p(plotted_x_max, y_max), color=BLACK)

        # Bereich zwischen den Linien füllen
        marked_area = graph.get_area(max_value_line, x_range=[plotted_x_min, plotted_x_max], color=CDARKGREEN, opacity=0.9)
        # Fügen Sie den Bereich zur Szene hinzu (ohne Animation)
        self.add(marked_area)

        # Führen Sie dann Ihre anderen Animationen durch
        self.play(Create(left_line), 
                  Create(right_line),
                  FadeOut(plotted_blender_under_text),
                  FadeOut(plotted_stove_under_text),
                  FadeOut(plotted_kettle_under_text),
                  Create(max_value_line),
                  FadeIn(marked_area),
                  FadeOut(plotted_blender), 
                  FadeOut(plotted_stove), 
                  FadeOut(plotted_kettle),
                  FadeOut(right_line),
                  FadeOut(left_line),
                  FadeOut(text_blender), 
                  FadeOut(text_stove), 
                  FadeOut(text_kettle)
                )

        adl_text = Text('ADL "Kochen"', font_size=36).next_to(plotted_stove_original, UP * 2).set_color(BLACK)
        adl_text.shift(LEFT * 0.5)  # Verschiebt den Text um 0.5 Einheiten nach links. Sie können den Wert anpassen.
        self.play(Write(adl_text))
        
        

        self.wait(3)
        #self.play()

        
        # Koordinaten für die Ecken des Rechtecks ermitteln
        bottom_left = graph.c2p(plotted_x_min, 2000)
        top_left = graph.c2p(plotted_x_min, 2500)
        bottom_right = graph.c2p(plotted_x_max, 2000)
        top_right = graph.c2p(plotted_x_max, 2500)

        # Rechteck mit den ermittelten Koordinaten erstellen
        adl = Polygon(bottom_left, top_left, top_right, bottom_right, fill_color=CDARKGREEN, fill_opacity=0.9, color=CACCENT)
        adl_border = Polygon(bottom_left, top_left, top_right, bottom_right, fill_color=CDARKGREEN, fill_opacity=0, color=CACCENT)

        # x-Achse neu positionieren
        graph.x_axis.generate_target()
        graph.x_axis.target.shift(UP * 2)  # Verschieben Sie die x-Achse um 2.75 Einheiten nach oben. Sie können diesen Wert anpassen.
        
        # y-Achse ausblenden
        self.play(FadeOut(graph.y_axis), FadeOut(y_numbers), FadeOut(y_label), FadeOut(x_label), Transform(marked_area, adl), Transform(max_value_line, adl_border), MoveToTarget(graph.x_axis), adl_text.animate.shift(DOWN * 0.25))

        
        self.wait(3)


class CreateADL(Scene):
    def construct(self):

        # Erstellen Sie ein Diagramm mit den Datenpunkten
        graph = Axes(
            x_range=[0, x_scale * (len(pwr_total)), (x_scale * x_spacing) // 2],  # Multiplizieren Sie die X-Werte mit 5
            y_range=[0, max(pwr_total) + 500, 500],
            x_length=9,
            y_length=5.5,
            axis_config=
                {
                    "color": BLACK,
                    "tip_width": 0.2,
                    "tip_height": 0.2,
                    "font_size": 24
                }
        )

        # Beschriftungen hinzufügen
        x_values = [x_scale * i for i in range(0, len(pwr_blender), x_spacing)]  # Multiplizieren Sie die X-Werte mit 5
        x_numbers = graph.get_x_axis().add_numbers([i for i in range(0, x_scale * len(pwr_total), x_scale * x_spacing)])
        y_numbers = graph.get_y_axis().add_numbers([i for i in range(0, int(max(pwr_total)) + 500, 1000)])

        # Setzen Sie die Farbe der Achsenbeschriftungen auf Schwarz
        for label in x_numbers:
            label.set_color(BLACK)
        for label in y_numbers:
            label.set_color(BLACK)

        # Achsentitel hinzufügen
        x_label = graph.get_x_axis_label(Tex("Zeit in Sekunden").scale(0.65), edge=DOWN, direction=DOWN, buff=0.25).set_color(BLACK)
        y_label = graph.get_y_axis_label(Tex("Leistung in Watt").scale(0.65).rotate(90 * DEGREES), edge=LEFT, direction=LEFT, buff=0.25).set_color(BLACK)

        # 1. Erstellen und Anzeigen der Summe aller vier Serien
        plotted_total_0 = graph.plot(lambda x: pwr_total[min(int(x / x_scale), len(pwr_total)-1)], color="#D5D5D5")
        plotted_total_1 = graph.plot(lambda x: pwr_total[min(int(x / x_scale), len(pwr_total)-1)], color=BLACK)


        # 2. Transformieren Sie die Summe in (Summe-pwr_blender) und pwr_blender
        pwr_sum_minus_blender = [total - blender for total, blender in zip(pwr_total, pwr_blender)]
        plotted_total_2 = graph.plot(lambda x: pwr_sum_minus_blender[min(int(x / x_scale), len(pwr_sum_minus_blender)-1)], color=BLACK)
        plotted_blender = graph.plot(lambda x: pwr_blender[min(int(x / x_scale), len(pwr_blender)-1)], color=CBLUE, use_smoothing=False)
        plotted_blender_original = plotted_blender.copy()

        # Finden Sie den ersten und letzten Nicht-Null-Wert in der Datenreihe
        non_zero_indices = [i for i, value in enumerate(pwr_blender) if value != 0]
        x_min = non_zero_indices[0]
        x_max = non_zero_indices[-1]
        
        area_under_blender = graph.get_area(plotted_blender, color=CBLUE, opacity=0.5, x_range=[(x_min) * x_scale, (x_max+1) * x_scale])
        text_blender = Text("Mixer").scale(0.7).next_to(graph,UR).set_color(CBLUE)
        plotted_blender_under_text = plotted_blender.copy().scale(0.2).next_to(text_blender, DOWN)

        # 3. Transformieren Sie die Summe in (Summe-pwr_blender-pwr_stove), pwr_blender und pwr_stove
        pwr_sum_minus_blender_stove = [sum_minus_blender - stove for sum_minus_blender, stove in zip(pwr_sum_minus_blender, pwr_stove)]
        plotted_sum_minus_blender_stove = graph.plot(lambda x: pwr_sum_minus_blender_stove[min(int(x / x_scale), len(pwr_sum_minus_blender_stove)-1)], color=BLACK)
        plotted_stove = graph.plot(lambda x: pwr_stove[min(int(x / x_scale), len(pwr_stove)-1)], color=CRED, use_smoothing=False)
        plotted_stove_original = plotted_stove.copy()
        
        text_stove = Text("Herdplatte").scale(0.7).next_to(plotted_blender_under_text,DOWN).set_color(CRED)
        plotted_stove_under_text = plotted_stove.copy().scale(0.2).next_to(text_stove, DOWN)

        # 4. Transformieren Sie die Summe in (pwr_sum_minus_blender_stove - pwr_kettle), pwr_blender, pwr_stove und pwr_kettle
        pwr_sum_minus_blender_stove_kettle = [sum_minus_blender_stove - kettle for sum_minus_blender_stove, kettle in zip(pwr_sum_minus_blender_stove, pwr_kettle)]
        plotted_sum_minus_blender_stove_kettle = graph.plot(lambda x: pwr_sum_minus_blender_stove_kettle[min(int(x / x_scale), len(pwr_sum_minus_blender_stove_kettle)-1)], color=BLACK)
        plotted_kettle = graph.plot(lambda x: pwr_kettle[min(int(x / x_scale), len(pwr_kettle)-1)], color=CGREEN, use_smoothing=False)
        plotted_kettle_original = plotted_kettle.copy()

        text_kettle = Text("Wasserkocher").scale(0.7).next_to(plotted_stove_under_text,DOWN).set_color(CGREEN)
        plotted_kettle_under_text = plotted_kettle.copy().scale(0.2).next_to(text_kettle, DOWN)
        
        self.add(graph)
        self.add(x_label)
        self.add(y_label)
        self.add(plotted_total_0)
        self.add(text_blender)
        self.add(text_stove)
        self.add(text_kettle)
        self.add(plotted_blender_under_text)
        self.add(plotted_stove_under_text)
        self.add(plotted_kettle_under_text)
        self.add(plotted_sum_minus_blender_stove_kettle)
        
        
        
        
        self.play(Uncreate(plotted_sum_minus_blender_stove_kettle), 
                  Uncreate(plotted_total_0),
                  Transform(plotted_blender_under_text, plotted_blender_original)                  
        )
        
        self.play(Transform(plotted_stove_under_text, plotted_stove_original))
        self.play(Transform(plotted_kettle_under_text, plotted_kettle_original))
        self.bring_to_front(graph.x_axis)
        self.wait(2)


        # Funktion, die den maximalen Wert der drei Serien für einen gegebenen x-Wert zurückgibt
        def max_value_function(x):
            index = min(int(x / x_scale), len(pwr_blender)-1)
            return max(pwr_blender[index], pwr_stove[index], pwr_kettle[index])

        # Erstellen Sie eine Linie für den maximalen Wert der drei Serien
        max_value_line = graph.plot(max_value_function, color=CACCENT, use_smoothing=False)  # Die Farbe ist hier nicht wichtig, da wir nur den Bereich darunter füllen wollen

        plotted_x_min = 5 * x_scale
        plotted_x_max = 38 * x_scale

        # Vertikale Linien an den X-Werten 60 und 450 erstellen
        y_min, y_max = graph.y_range[0], graph.y_range[1]
        left_line = DashedLine(start=graph.c2p(plotted_x_min, y_min), end=graph.c2p(plotted_x_min, y_max), color=BLACK)
        right_line = DashedLine(start=graph.c2p(plotted_x_max, y_min), end=graph.c2p(plotted_x_max, y_max), color=BLACK)

        # Bereich zwischen den Linien füllen
        marked_area = graph.get_area(max_value_line, x_range=[plotted_x_min, plotted_x_max], color=CDARKGREEN, opacity=0.9)
        # Fügen Sie den Bereich zur Szene hinzu (ohne Animation)
        self.add(marked_area)

        # Führen Sie dann Ihre anderen Animationen durch
        self.play(Create(left_line), 
                  Create(right_line),
                  FadeOut(plotted_blender_under_text),
                  FadeOut(plotted_stove_under_text),
                  FadeOut(plotted_kettle_under_text),
                  Create(max_value_line),
                  FadeIn(marked_area),
                  FadeOut(plotted_blender), 
                  FadeOut(plotted_stove), 
                  FadeOut(plotted_kettle),
                  FadeOut(right_line),
                  FadeOut(left_line),
                  FadeOut(text_blender), 
                  FadeOut(text_stove), 
                  FadeOut(text_kettle)
                )

        adl_text = Text('ADL "Kochen"', font_size=36).next_to(plotted_stove_original, UP * 2).set_color(BLACK)
        adl_text.shift(LEFT * 0.5)  # Verschiebt den Text um 0.5 Einheiten nach links. Sie können den Wert anpassen.
        self.play(Write(adl_text))
        
        

        self.wait(3)
        
        # Koordinaten für die Ecken des Rechtecks ermitteln
        bottom_left = graph.c2p(plotted_x_min, 2000)
        top_left = graph.c2p(plotted_x_min, 2500)
        bottom_right = graph.c2p(plotted_x_max, 2000)
        top_right = graph.c2p(plotted_x_max, 2500)

        # Rechteck mit den ermittelten Koordinaten erstellen
        adl = Polygon(bottom_left, top_left, top_right, bottom_right, fill_color=CDARKGREEN, fill_opacity=0.9, color=CACCENT)
        adl_border = Polygon(bottom_left, top_left, top_right, bottom_right, fill_color=CDARKGREEN, fill_opacity=0, color=CACCENT)

        # x-Achse neu positionieren
        graph.x_axis.generate_target()
        graph.x_axis.target.shift(UP * 2)  # Verschieben Sie die x-Achse um 2.75 Einheiten nach oben. Sie können diesen Wert anpassen.
        
        # y-Achse ausblenden
        self.play(FadeOut(graph.y_axis), FadeOut(y_numbers), FadeOut(y_label), FadeOut(x_label), Transform(marked_area, adl), Transform(max_value_line, adl_border), MoveToTarget(graph.x_axis), adl_text.animate.shift(DOWN * 0.25))

        
        self.wait(3)
        
        
        
class DisaggregateGraph(Scene):
    def construct(self):
        graph_scene = CreateGraph()

        self.add(graph_scene.graph)
        self.add(graph_scene.x_label)
        self.add(graph_scene.y_label)
        self.add(graph_scene.plotted_total_0)
        self.add(graph_scene.plotted_total_1)


        # 2. Transformieren Sie die Summe in (Summe-pwr_blender) und pwr_blender
        pwr_sum_minus_blender = [total - blender for total, blender in zip(pwr_total, pwr_blender)]
        plotted_total_2 = graph_scene.graph.plot(lambda x: pwr_sum_minus_blender[min(int(x / x_scale), len(pwr_sum_minus_blender)-1)], color=BLACK)
        plotted_blender = graph_scene.graph.plot(lambda x: pwr_blender[min(int(x / x_scale), len(pwr_blender)-1)], color=CBLUE, use_smoothing=False)

        # Finden Sie den ersten und letzten Nicht-Null-Wert in der Datenreihe
        non_zero_indices = [i for i, value in enumerate(pwr_blender) if value != 0]
        x_min = non_zero_indices[0]
        x_max = non_zero_indices[-1]
        
        area_under_blender = graph_scene.graph.get_area(plotted_blender, color=CBLUE, opacity=0.5, x_range=[(x_min) * x_scale, (x_max+1) * x_scale])
        text_blender = Text("Mixer").scale(0.7).next_to(graph_scene.graph,UR).set_color(CBLUE)

        # Animation für 1. Haushaltsgerät (Mixer)
        self.play(Create(plotted_blender), Write(text_blender), Create(area_under_blender), run_time=2)
        self.bring_to_front(graph_scene.graph.x_axis)
        self.wait(1)
        self.play(Indicate(area_under_blender))
        self.wait(2)
        self.play(FadeOut(area_under_blender))

        plotted_blender_under_text = plotted_blender.copy().scale(0.2).next_to(text_blender, DOWN)
        self.play(Transform(graph_scene.plotted_total_1, plotted_total_2), Transform(plotted_blender, plotted_blender_under_text))
        
        
        self.wait(2)

        # Animation für 2. Haushaltsgerät (Herdplatte)
        pwr_sum_minus_blender_stove = [sum_minus_blender - stove for sum_minus_blender, stove in zip(pwr_sum_minus_blender, pwr_stove)]
        plotted_sum_minus_blender_stove = graph_scene.graph.plot(lambda x: pwr_sum_minus_blender_stove[min(int(x / x_scale), len(pwr_sum_minus_blender_stove)-1)], color=BLACK)
        plotted_stove = graph_scene.graph.plot(lambda x: pwr_stove[min(int(x / x_scale), len(pwr_stove)-1)], color=CRED, use_smoothing=False)
        
        text_stove = Text("Herdplatte").scale(0.7).next_to(plotted_blender,DOWN).set_color(CRED)



        self.play(Create(plotted_stove), Write(text_stove), run_time=2)
        self.bring_to_front(graph_scene.graph.x_axis)
        self.wait(0.3)
        self.play(Indicate(plotted_stove))
        self.wait(1)
        self.remove(graph_scene.plotted_total_1)
        
        plotted_stove_under_text = plotted_stove.copy().scale(0.2).next_to(text_stove, DOWN)
        self.play(Transform(plotted_total_2, plotted_sum_minus_blender_stove, replace_mobject_with_target_in_scene=True), 
                  Transform(plotted_stove, plotted_stove_under_text))
        self.wait(2)

        # 4. Transformieren Sie die Summe in (pwr_sum_minus_blender_stove - pwr_kettle), pwr_blender, pwr_stove und pwr_kettle
        pwr_sum_minus_blender_stove_kettle = [sum_minus_blender_stove - kettle for sum_minus_blender_stove, kettle in zip(pwr_sum_minus_blender_stove, pwr_kettle)]
        plotted_sum_minus_blender_stove_kettle = graph_scene.graph.plot(lambda x: pwr_sum_minus_blender_stove_kettle[min(int(x / x_scale), len(pwr_sum_minus_blender_stove_kettle)-1)], color=BLACK)
        plotted_kettle = graph_scene.graph.plot(lambda x: pwr_kettle[min(int(x / x_scale), len(pwr_kettle)-1)], color=CGREEN, use_smoothing=False)

        text_kettle = Text("Wasserkocher").scale(0.7).next_to(plotted_stove,DOWN).set_color(CGREEN)


        # Animation für 3. Haushaltsgerät (Wasserkocher)
        self.play(Create(plotted_kettle), Write(text_kettle), run_time=2)
        self.bring_to_front(graph_scene.graph.x_axis)
        self.wait(0.3)
        self.play(Indicate(plotted_kettle))
        self.wait(1)
        self.remove(plotted_sum_minus_blender_stove)
        
        plotted_kettle_under_text = plotted_kettle.copy().scale(0.2).next_to(text_kettle, DOWN)
        self.play(Transform(plotted_sum_minus_blender_stove, plotted_sum_minus_blender_stove_kettle, replace_mobject_with_target_in_scene=True), 
                  Transform(plotted_kettle, plotted_kettle_under_text))
        
        




class DrawGraph(Scene):
    def construct(self):
        graph = CreateGraph()
        
        self.play(Create(graph.graph), Write(graph.x_label), Write(graph.y_label))
        self.play(Create(graph.plotted_total_0), Create(graph.plotted_total_1), run_time=3)       
