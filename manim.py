from manim import *
import pandas as pd

config.background_color = WHITE




class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

pwr_blender = [0, 0, 0, 0, 0, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pwr_stove = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 0, 2500, 2500, 2500, 0, 2500, 2500, 2500, 0, 2500, 2500, 2500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pwr_kettle = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2100, 2100, 2100, 2100, 2100, 2100, 2100, 2100, 2100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pwr_other = [245, 215, 213, 224, 233, 216, 260, 232, 245, 240, 240, 260, 280, 249, 235, 255, 250, 270, 268, 275, 260, 242, 202, 221, 204, 217, 230, 221, 231, 217, 232, 242, 232, 228, 245, 204, 200, 246, 243, 215, 250, 241, 237, 205, 233, 208, 250, 200, 207, 233]

CBLUE = "#3257A8"
CRED = "#9D0003"
CGREEN = "#30A490"

class CreateGraph(Scene):
    def construct(self):
        # Daten aus Excel-Datei einlesen
        pwr_total = [a + b + c + d for a, b, c, d in zip(pwr_blender, pwr_stove, pwr_kettle, pwr_other)]
        x_scale = 12
        x_spacing = 5

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
        # Jede Serie nacheinander animieren
        #for series, color in zip([pwr_blender, pwr_stove, pwr_kettle, pwr_other], [BLUE, GREEN, RED, GREY]):
        #    plotted_graph = graph.plot(lambda x: series[int(x)], color=color, use_smoothing=False)
        #    self.play(Write(plotted_graph))
        #    self.wait(1)

        # 1. Erstellen und Anzeigen der Summe aller vier Serien
        plotted_total_2 = graph.plot(lambda x: pwr_total[min(int(x / x_scale), len(pwr_total)-1)], color="#D5D5D5")
        plotted_total = graph.plot(lambda x: pwr_total[min(int(x / x_scale), len(pwr_total)-1)], color=BLACK)
        self.play(Write(plotted_total_2), Write(plotted_total))
        self.wait(2)

        # 2. Transformieren Sie die Summe in (Summe-pwr_blender) und pwr_blender
        pwr_sum_minus_blender = [total - blender for total, blender in zip(pwr_total, pwr_blender)]
        plotted_sum_minus_blender = graph.plot(lambda x: pwr_sum_minus_blender[min(int(x / x_scale), len(pwr_sum_minus_blender)-1)], color=BLACK)
        plotted_blender = graph.plot(lambda x: pwr_blender[min(int(x / x_scale), len(pwr_blender)-1)], color=CBLUE, use_smoothing=False)


        # Finden Sie den ersten und letzten Nicht-Null-Wert in der Datenreihe
        non_zero_indices = [i for i, value in enumerate(pwr_blender) if value != 0]
        x_min = non_zero_indices[0]
        x_max = non_zero_indices[-1]
        area_under_blender = graph.get_area(plotted_blender, color=GREY, opacity=0.5, x_range=[x_min, x_max])
        text_blender = Text("Mixer").scale(0.7).next_to(graph,RIGHT).set_color(CBLUE)

        self.play(Create(plotted_blender), Create(text_blender))
        self.bring_to_front(graph.x_axis)
        self.wait(1)
        
        self.play(Indicate(plotted_blender))

        self.wait(2)
        self.play(Transform(plotted_total, plotted_sum_minus_blender))
        self.wait(2)

        # 3. Transformieren Sie die Summe in (Summe-pwr_blender-pwr_stove), pwr_blender und pwr_stove
        pwr_sum_minus_blender_stove = [sum_minus_blender - stove for sum_minus_blender, stove in zip(pwr_sum_minus_blender, pwr_stove)]
        plotted_sum_minus_blender_stove = graph.plot(lambda x: pwr_sum_minus_blender_stove[min(int(x / x_scale), len(pwr_sum_minus_blender_stove)-1)], color=BLACK)
        plotted_stove = graph.plot(lambda x: pwr_stove[min(int(x / x_scale), len(pwr_stove)-1)], color=CRED, use_smoothing=False)
        area_under_stove = graph.get_area(plotted_sum_minus_blender_stove, color=GREY, opacity=0.5)
        text_stove = Text("Backofen").scale(0.7).next_to(text_blender,DOWN).set_color(CRED)

        self.play(Create(plotted_stove), Create(text_stove))
        self.bring_to_front(graph.x_axis)
        self.wait(0.3)
        self.play(Indicate(plotted_stove))
        self.wait(1)
        self.remove(plotted_total)
        self.play(Transform(plotted_sum_minus_blender, plotted_sum_minus_blender_stove, replace_mobject_with_target_in_scene=True))
        self.wait(2)

        # 4. Transformieren Sie die Summe in (pwr_sum_minus_blender_stove - pwr_kettle), pwr_blender, pwr_stove und pwr_kettle
        pwr_sum_minus_blender_stove_kettle = [sum_minus_blender_stove - kettle for sum_minus_blender_stove, kettle in zip(pwr_sum_minus_blender_stove, pwr_kettle)]
        plotted_sum_minus_blender_stove_kettle = graph.plot(lambda x: pwr_sum_minus_blender_stove_kettle[min(int(x / x_scale), len(pwr_sum_minus_blender_stove_kettle)-1)], color=BLACK)
        plotted_kettle = graph.plot(lambda x: pwr_kettle[min(int(x / x_scale), len(pwr_kettle)-1)], color=CGREEN, use_smoothing=False)
        area_under_kettle = graph.get_area(plotted_sum_minus_blender_stove_kettle, color=GREY, opacity=0.5)
        text_kettle = Text("Wasserkocher").scale(0.7).next_to(text_stove,DOWN).set_color(CGREEN)

        self.play(Create(plotted_kettle), Create(text_kettle))
        self.bring_to_front(graph.x_axis)
        self.wait(0.3)
        self.play(Indicate(plotted_kettle))
        self.wait(1)
        self.remove(plotted_sum_minus_blender_stove)
        self.play(Transform(plotted_sum_minus_blender_stove, plotted_sum_minus_blender_stove_kettle, replace_mobject_with_target_in_scene=True))
        self.wait(2)

        self.play(Uncreate(plotted_sum_minus_blender_stove_kettle), Uncreate(plotted_total_2))
