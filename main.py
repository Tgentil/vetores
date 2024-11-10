from manim import *
import numpy as np
import os

class Introducao(Scene):
    def construct(self):
        titulo = Text("Introdução a Vetores", font_size=48)
        self.play(Write(titulo))
        self.wait(10)
        self.play(FadeOut(titulo))


class OQueSaoVetores(Scene):
    def construct(self):
        # Título da Cena
        titulo = Text("O que são Vetores?", font_size=48)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # Introdução ao conceito de vetor
        definicao = Text(
            "Vetores são grandezas com\nmagnitude, direção e sentido.",
            font_size=36
        )
        self.play(Write(definicao))
        self.wait(3)
        self.play(FadeOut(definicao))

        # Representação geométrica
        plano = NumberPlane()
        self.play(Create(plano))
        self.wait(1)

        vetor = Arrow(ORIGIN, [3, 2, 0], color=YELLOW)
        vetor_label = MathTex(r'\vec{v}', color=YELLOW).next_to(vetor.get_end(), UP)

        self.play(GrowArrow(vetor), Write(vetor_label))
        self.wait(1)

        # Mostrar magnitude (comprimento do vetor)
        magnitude_brace = Brace(vetor, direction=vetor.copy().rotate(PI/2).get_unit_vector())
        magnitude_text = magnitude_brace.get_tex(r"|\vec{v}|")
        self.play(Create(magnitude_brace), Write(magnitude_text))
        self.wait(2)

        # Mostrar direção e sentido
        direction_label = Text("Direção e Sentido", font_size=24, color=BLUE)
        direction_label.next_to(vetor.get_center(), RIGHT)
        self.play(Indicate(vetor, scale_factor=1.1, color=BLUE), Write(direction_label))
        self.wait(2)
        self.play(FadeOut(direction_label))
        self.wait(1)

        # Remover o plano cartesiano para focar nos vetores
        self.play(FadeOut(plano, magnitude_text))
        self.wait(0.5)

        # Vetores equivalentes (mesma magnitude, direção e sentido)
        vetor_equiv = Arrow(LEFT*5 + DOWN*3, LEFT*2 + DOWN, color=YELLOW)
        vetor_equiv_label = MathTex(r'\vec{v}', color=YELLOW).next_to(vetor_equiv.get_end(), UP)
        self.play(GrowArrow(vetor_equiv), Write(vetor_equiv_label))
        self.wait(1)
        
        # Mostrar magnitude do segundo vetor
        magnitude_brace_equiv = Brace(vetor_equiv, direction=vetor_equiv.copy().rotate(PI/2).get_unit_vector())
        self.play(Create(magnitude_brace_equiv))
        self.wait(2)

        # Destacar que os vetores são equivalentes
        self.play(Indicate(VGroup(vetor, vetor_label), scale_factor=1.1))
        self.play(Indicate(VGroup(vetor_equiv, vetor_equiv_label), scale_factor=1.1))
        self.wait(2)

        # Pausa para explicar sobre vetores equivalentes
        self.wait(3)

        # Limpar os vetores após a comparação
        self.play(FadeOut(VGroup(vetor, vetor_label, vetor_equiv, vetor_equiv_label, magnitude_brace, magnitude_brace_equiv)))
        self.wait(1)

        # Trazer de volta o plano cartesiano
        self.play(Create(plano))
        self.wait(5)

        # Operações com vetores (adição)
        vetor_u = Arrow(ORIGIN, RIGHT*3, color=RED)
        vetor_u_label = MathTex(r'\vec{v}', color=RED).next_to(vetor_u.get_end(), DOWN)
        vetor_v = Arrow(ORIGIN, UP*3, color=GREEN)
        vetor_v_label = MathTex(r'\vec{c}', color=GREEN).next_to(vetor_v.get_end(), LEFT)
        vetor_result = Arrow(ORIGIN, RIGHT*3 + UP*3, color=ORANGE)
        vetor_result_label = MathTex(r'\vec{v}+\vec{c}', color=ORANGE).next_to(vetor_result.get_end(), UP)

        self.play(GrowArrow(vetor_u), Write(vetor_u_label))
        self.wait(11)
        self.play(GrowArrow(vetor_v), Write(vetor_v_label))
        self.wait(11)
        self.play(GrowArrow(vetor_result), Write(vetor_result_label))
        self.wait(5)

        # Mostrar que vetor_result é a soma de vetor_u e vetor_v
        self.play(Indicate(vetor_result, scale_factor=1.1))
        self.wait(10)

        # Limpar a cena
        self.play(
            FadeOut(VGroup(
                plano, vetor_u, vetor_u_label, vetor_v, vetor_v_label, vetor_result, vetor_result_label
            ))
        )
        self.wait(1)


class VetoresEmDimensoesMaiores(ThreeDScene):
    def construct(self):
        # Título da Cena
        titulo = Text("Vetores em Dimensões Maiores", font_size=48)
        self.add_fixed_in_frame_mobjects(titulo)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))
        self.remove_fixed_in_frame_mobjects(titulo)

        # Transição de 2D para 3D
        texto_2d = Text("Espaço 2D", font_size=36)
        texto_2d.to_edge(UP)
        self.add_fixed_in_frame_mobjects(texto_2d)
        self.play(Write(texto_2d))

        plano = NumberPlane()
        vetor_2d = Arrow(ORIGIN, RIGHT * 2 + UP * 1, color=YELLOW)
        label_2d = MathTex(r'\vec{v}_{2D}').next_to(vetor_2d.get_end(), UP)

        self.play(Create(plano))
        self.play(GrowArrow(vetor_2d), Write(label_2d))
        self.wait(10)

        self.play(FadeOut(plano), FadeOut(vetor_2d), FadeOut(label_2d))
        self.play(FadeOut(texto_2d))
        self.remove_fixed_in_frame_mobjects(texto_2d)

        # Espaço 3D
        texto_3d = Text("Espaço 3D", font_size=36)
        texto_3d.to_edge(UP)
        self.add_fixed_in_frame_mobjects(texto_3d)
        self.play(Write(texto_3d))

        axes = ThreeDAxes()

        # Ajuste da orientação da câmera para o vetor 3D
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES, distance=5)
        vetor_3d = Arrow3D(ORIGIN, [2, 1, 2], color=YELLOW)
        label_3d = MathTex(r'\vec{v}_{3D}').next_to(vetor_3d.get_end(), UP)

        self.play(Create(axes))
        self.play(Create(vetor_3d), Write(label_3d))
        self.wait(2)

        # Adicionar rotação suave da câmera para enfatizar a profundidade
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(15)
        self.stop_ambient_camera_rotation()

        self.play(FadeOut(axes), FadeOut(vetor_3d), FadeOut(label_3d))
        self.play(FadeOut(texto_3d))
        self.remove_fixed_in_frame_mobjects(texto_3d)
        self.wait(6)
        
                # Espaços de Alta Dimensionalidade
        texto_hd = Text("Espaços de Alta Dimensionalidade", font_size=36)
        texto_hd.to_edge(UP)
        self.add_fixed_in_frame_mobjects(texto_hd)
        self.play(Write(texto_hd))
        self.wait(15)
        self.play(FadeOut(texto_hd))

        # Ajuste da orientação da câmera para os pontos aleatórios
        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)

        # Criar e exibir pontos aleatórios em 3D
        num_pontos = 200
        axes_hd = ThreeDAxes()
        self.play(Create(axes_hd))

        pontos = VGroup(*[
            Dot(
                point=[np.random.uniform(-5, 5), np.random.uniform(-5, 5), np.random.uniform(-5, 5)],
                radius=0.05,
                color=BLUE
            ) for _ in range(num_pontos)
        ])

        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(LaggedStartMap(FadeIn, pontos, lag_ratio=0.005, run_time=3))
        self.wait(2)

        # Mostrar que os pontos representam vetores em alta dimensionalidade
        texto_pontos = Text(
            "Pontos representando vetores em alta dimensionalidade",
            font_size=24
        )
        texto_pontos.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(texto_pontos)
        self.play(Write(texto_pontos))
        self.wait(15)

        # Limpar a cena
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(pontos), FadeOut(axes_hd))
        self.remove_fixed_in_frame_mobjects(texto_pontos)
        self.play(FadeOut(texto_pontos))
        self.wait(1)


class WordEmbeddings:
    def __init__(self):
        # Definindo embeddings simplificados para visualização
        self.embeddings = {
            "Paris": np.array([2, 3]),
            "França": np.array([1, 2]),
            "Itália": np.array([4, 2]),
            "Roma": np.array([5, 3]),
        }
    
    def get_vector(self, word):
        return self.embeddings.get(word, np.array([0, 0]))

class ExemploParisRoma(Scene):
    def construct(self):
        # Instanciar os embeddings
        embeddings = WordEmbeddings()
        
        # Vetores das palavras
        paris_vec = embeddings.get_vector("Paris")
        franca_vec = embeddings.get_vector("França")
        italia_vec = embeddings.get_vector("Itália")
        roma_vec = embeddings.get_vector("Roma")
        
        # Planos e eixos
        plane = NumberPlane(
            x_range=[0, 9, 1],
            y_range=[0, 9, 1],
            background_line_style={"stroke_color": GREY_A, "stroke_width": 1}
        )
        self.add(plane)
        
        # Criar vetores
        paris_arrow = self.create_vector(paris_vec, color=BLUE, label="Paris")
        franca_arrow = self.create_vector(franca_vec, color=GREEN, label="França")
        italia_arrow = self.create_vector(italia_vec, color=PINK, label="Itália")
        roma_arrow = self.create_vector(roma_vec, color=RED, label="Roma")
        
        # Desenhar 'Paris' e 'França'
        self.play(GrowArrow(paris_arrow), Write(paris_arrow.label))
        self.wait(1)
        self.play(GrowArrow(franca_arrow), Write(franca_arrow.label))
        self.wait(1)
        
        # Criar e desenhar vetor de diferença entre 'França' e 'Paris'
        paris_franca_diff = Arrow(
            start=franca_arrow.get_end(),
            end=paris_arrow.get_end(),
            buff=0,
            color=YELLOW,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        paris_franca_diff_label = Text("Diferença", font_size=20, color=YELLOW).next_to(paris_franca_diff.get_center(), UP)
        self.play(GrowArrow(paris_franca_diff), Write(paris_franca_diff_label))
        self.wait(1)
        
        # Desenhar 'Itália' e 'Roma'
        self.play(GrowArrow(italia_arrow), Write(italia_arrow.label))
        self.wait(1)
        self.play(GrowArrow(roma_arrow), Write(roma_arrow.label))
        self.wait(1)
        
        # Criar e desenhar vetor de diferença entre 'Itália' e 'Roma'
        roma_italia_diff = Arrow(
            start=italia_arrow.get_end(),
            end=roma_arrow.get_end(),
            buff=0,
            color=YELLOW,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        roma_italia_diff_label = Text("Diferença", font_size=20, color=YELLOW).next_to(roma_italia_diff.get_center(), UP)
        self.play(GrowArrow(roma_italia_diff), Write(roma_italia_diff_label))
        self.wait(1)
        
        # Destacar que os vetores de diferença são similares
        self.play(
            Indicate(paris_franca_diff, scale_factor=1.2),
            Indicate(roma_italia_diff, scale_factor=1.2),
            run_time=2
        )
        self.wait(10)
        
        # Conclusão
        self.play(
            FadeOut(VGroup(
                paris_arrow, paris_arrow.label,
                franca_arrow, franca_arrow.label,
                paris_franca_diff, paris_franca_diff_label,
                italia_arrow, italia_arrow.label,
                roma_arrow, roma_arrow.label,
                roma_italia_diff, roma_italia_diff_label
            ))
        )
        self.wait(1)
    
    def create_vector(self, vector, color=WHITE, label=""):
        if len(vector) == 2:
            vector = np.array([vector[0], vector[1], 0])
        arrow = Arrow(
            start=ORIGIN,
            end=vector,
            buff=0,
            color=color,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        label_mob = Text(label, font_size=24).next_to(arrow.get_end(), UP)
        arrow.label = label_mob
        return arrow

class Conclusao(Scene):
    def construct(self):
        titulo = Text("Conclusão", font_size=48)
        self.play(Write(titulo))
        self.wait(10)
        self.play(FadeOut(titulo))

# Executar as cenas
if __name__ == "__main__":
    # os.system("manim -pql main.py Introducao")
    # os.system("manim -pql main.py OQueSaoVetores")
    os.system("manim -pql main.py VetoresEmDimensoesMaiores")
    # os.system("manim -pql main.py ExemploParisRoma")
    # os.system("manim -pql main.py Conclusao")