import pygame

pygame.init()

largura = 1200
altura = 700

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("PYQUIZ")
cena = "inicio"
pontuacao = 0


def transition(cena, x_range, y_range, prox_cena):
    if x_range[0] <= mouse[0] <= x_range[1] and y_range[0] <= mouse[1] <= y_range[1]:
        return prox_cena
    return cena

def render_text(texto, x, y, size=150, color=(255, 255, 255)):
    font = pygame.font.Font(None, size)
    text_surface = font.render(texto, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    tela.blit(text_surface, text_rect)

loop = True

while loop:

    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if cena == 'inicio':
                cena = transition(cena, (533, 533 + 558), (337, 337 + 118), 'tela2')
                cena = transition(cena, (530, 530 + 580), (490, 490 + 120), 'creditos')

            elif cena == 'creditos':
                cena = transition(cena, (23, 23 + 99), (608, 608 + 73), 'inicio')
                cena = transition(cena, (1038, 1038 + 90), (27, 27 + 90), 'sobre')

            elif cena == 'sobre':
                cena = transition(cena, (23, 23 + 99), (608, 608 + 73), 'creditos')

            elif cena == 'tela2':
                cena = transition(cena, (1015, 1015 + 162), (590, 590 + 70), 'menu')
                cena = transition(cena, (18, 18 + 104), (598, 598 + 80), 'inicio')

            elif cena == 'menu':
                cena = transition(cena, (103, 103 + 457), (297, 297 + 90), 'pergunta2')
                cena = transition(cena, (617, 617 + 447), (297, 297 + 90), 'funcao1')

            elif cena == 'pergunta2':
                cena = transition(cena, (761, 761 + 322), (122, 122 + 801), 'erro2')
                cena = transition(cena, (761, 761 + 322), (292, 292 + 147), 'erro2')
                cena = transition(cena, (761, 761 + 322), (461, 461 + 144), 'acerto2')

            elif cena == 'acerto2':
                cena = transition(cena, (1062, 1062 + 127), (595, 595 + 91), 'pergunta3')

            elif cena == 'erro2':
                cena = transition(cena, (1062, 1062 + 127), (595, 595 + 91), 'pergunta3')

            elif cena == 'pergunta3':
                cena = transition(cena, (762, 762 + 323), (124, 124 + 147), 'acerto3')
                cena = transition(cena, (762, 762 + 323), (461, 461 + 147), 'erro3')
                cena = transition(cena, (762, 762 + 323), (291, 291 + 149), 'erro3')

            elif cena == 'acerto3':
                cena = transition(cena, (1061, 1061 + 128), (591, 591 + 96), 'pergunta4')

            elif cena == 'erro3':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'pergunta4')

            elif cena == 'pergunta4':
                cena = transition(cena, (763, 763 + 323), (463, 463 + 147), 'erro4')
                cena = transition(cena, (762, 762 + 323), (125, 125 + 145), 'acerto4')
                cena = transition(cena, (762, 762 + 323), (291, 291 + 149), 'erro4')

            elif cena == 'acerto4':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'pergunta5')

            elif cena == 'erro4':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'pergunta5')

            elif cena == 'pergunta5':
                cena = transition(cena, (763, 763 + 323), (463, 463 + 147), 'erro5')
                cena = transition(cena, (762, 762 + 323), (125, 125 + 145), 'erro5')
                cena = transition(cena, (762, 762 + 323), (291, 291 + 149), 'acerto5')

            elif cena == 'acerto5':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'pergunta6')

            elif cena == 'erro5':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'pergunta6')

            elif cena == 'pergunta6':
                cena = transition(cena, (763, 763 + 323), (463, 463 + 147), 'acerto6')
                cena = transition(cena, (762, 762 + 323), (125, 125 + 145), 'erro6')
                cena = transition(cena, (762, 762 + 323), (291, 291 + 149), 'erro6')

            elif cena == 'acerto6':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'pergunta7')

            elif cena == 'erro6':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'pergunta7')

            elif cena == 'pergunta7':
                cena = transition(cena, (766, 766 + 327), (291, 291 + 149), 'erro7')
                cena = transition(cena, (762, 762 + 323), (125, 125 + 145), 'acerto7')
                cena = transition(cena, (762, 762 + 323), (463, 463 + 147), 'erro7')

            elif cena == 'acerto7':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'pergunta8')

            elif cena == 'erro7':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'pergunta8')

            elif cena == 'pergunta8':
                cena = transition(cena, (766, 766 + 327), (291, 291 + 149), 'acerto8')
                cena = transition(cena, (762, 762 + 323), (125, 125 + 145), 'erro8')
                cena = transition(cena, (762, 762 + 323), (463, 463 + 147), 'erro8')

            elif cena == 'acerto8':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'pergunta9')

            elif cena == 'erro8':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'pergunta9')

            elif cena == 'pergunta9':
                cena = transition(cena, (766, 766 + 327), (291, 291 + 149), 'acerto9')
                cena = transition(cena, (762, 762 + 323), (125, 125 + 145), 'erro9')
                cena = transition(cena, (762, 762 + 323), (463, 463 + 147), 'erro9')

            elif cena == 'acerto9':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'pergunta10')

            elif cena == 'erro9':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'pergunta10')

            elif cena == 'pergunta10':
                cena = transition(cena, (766, 766 + 327), (291, 291 + 149), 'erro10')
                cena = transition(cena, (762, 762 + 323), (125, 125 + 145), 'erro10')
                cena = transition(cena, (762, 762 + 323), (463, 463 + 147), 'acerto10')

            elif cena == 'acerto10':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'menu11')

            elif cena == 'erro10':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'menu11')

            elif cena == 'menu11':
                cena = transition(cena, (617, 617 + 447), (297, 297 + 90), 'funcao1')

            elif cena == 'funcao1':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'acertofun1')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errofun1')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errofun1')

            elif cena == 'errofun1':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'funcao2')

            elif cena == 'acertofun1':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'funcao2')

            elif cena == 'funcao2':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errofun2')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errofun2')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'acertofun2')

            elif cena == 'errofun2':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'funcao3')

            elif cena == 'acertofun2':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'funcao3')

            elif cena == 'funcao3':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errofun3')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'acertofun3')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errofun3')

            elif cena == 'errofun3':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'funcao4')

            elif cena == 'acertofun3':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'funcao4')

            elif cena == 'funcao4':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errofun4')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errofun4')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'acertofun4')

            elif cena == 'errofun4':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'funcao5')

            elif cena == 'acertofun4':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'funcao5')

            elif cena == 'funcao5':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'acertofun5')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errofun5')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errofun5')

            elif cena == 'errofun5':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'funcao6')

            elif cena == 'acertofun5':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'funcao6')

            elif cena == 'funcao6':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errofun6')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'acertofun6')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errofun6')

            elif cena == 'errofun6':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'funcao7')

            elif cena == 'acertofun6':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'funcao7')

            elif cena == 'funcao7':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errofun7')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errofun7')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'acertofun7')

            elif cena == 'errofun7':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'funcao8')

            elif cena == 'acertofun7':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'funcao8')

            elif cena == 'funcao8':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'acertofun8')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errofun8')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errofun8')

            elif cena == 'errofun8':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'funcao9')

            elif cena == 'acertofun8':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'funcao9')

            elif cena == 'funcao9':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errofun9')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errofun9')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'acertofun9')

            elif cena == 'errofun9':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'funcao10')

            elif cena == 'acertofun9':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'funcao10')

            elif cena == 'funcao10':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errofun10')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'acertofun10')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errofun10')

            elif cena == 'errofun10':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'menu12')

            elif cena == 'acertofun10':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'menu12')

            elif cena == 'menu12':
                cena = transition(cena, (621, 621 + 441), (457, 457 + 86), 'repeticao1')

            elif cena == 'repeticao1':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errorep1')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'acertorep1')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errorep1')

            elif cena == 'errorep1':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'repeticao2')

            elif cena == 'acertorep1':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'repeticao2')

            elif cena == 'repeticao2':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errorep2')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errorep2')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'acertorep2')

            elif cena == 'errorep2':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'repeticao3')

            elif cena == 'acertorep2':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'repeticao3')

            elif cena == 'repeticao3':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errorep3')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'acertorep3')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errorep3')

            elif cena == 'errorep3':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'repeticao4')

            elif cena == 'acertorep3':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'repeticao4')

            elif cena == 'repeticao4':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'acertorep4')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errorep4')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errorep4')

            elif cena == 'errorep4':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'repeticao5')

            elif cena == 'acertorep4':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'repeticao5')

            elif cena == 'repeticao5':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'acertorep5')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errorep5')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errorep5')

            elif cena == 'errorep5':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'repeticao6')

            elif cena == 'acertorep5':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'repeticao6')

            elif cena == 'repeticao6':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errorep6')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'acertorep6')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errorep6')

            elif cena == 'errorep6':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'repeticao7')

            elif cena == 'acertorep6':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'repeticao7')

            elif cena == 'repeticao7':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errorep7')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errorep7')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'acertorep7')

            elif cena == 'errorep7':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'repeticao8')

            elif cena == 'acertorep7':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'repeticao8')

            elif cena == 'repeticao8':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errorep8')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'acertorep8')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'acertorep8')

            elif cena == 'errorep8':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'repeticao9')

            elif cena == 'acertorep8':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'repeticao9')

            elif cena == 'repeticao9':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errorep9')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'acertorep9')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errorep9')

            elif cena == 'errorep9':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'repeticao10')

            elif cena == 'acertorep9':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'repeticao10')

            elif cena == 'repeticao10':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'acertorep10')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errorep10')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errorep10')

            elif cena == 'errorep10':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'menu13')

            elif cena == 'acertorep10':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'menu13')

            elif cena == 'menu13':
                cena = transition(cena, (117, 117 + 443), (459, 459 + 87), 'decisao1')

            elif cena == 'decisao1':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errodec1')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'acertodec1')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errodec1')

            elif cena == 'errodec1':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'decisao2')

            elif cena == 'acertodec1':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'decisao2')

            elif cena == 'decisao2':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errodec2')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errodec2')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'acertodec2')

            elif cena == 'errodec2':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'decisao3')

            elif cena == 'acertodec2':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'decisao3')

            elif cena == 'decisao3':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'acertodec3')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errodec3')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errodec3')

            elif cena == 'errodec3':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'decisao4')

            elif cena == 'acertodec3':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'decisao4')

            elif cena == 'decisao4':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errodec4')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'acertodec4')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errodec4')

            elif cena == 'errodec4':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'decisao5')

            elif cena == 'acertodec4':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'decisao5')

            elif cena == 'decisao5':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errodec5')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errodec5')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'acertodec5')

            elif cena == 'errodec5':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'decisao6')

            elif cena == 'acertodec5':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'decisao6')

            elif cena == 'decisao6':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'acertodec6')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errodec6')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errodec6')

            elif cena == 'errodec6':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'decisao7')

            elif cena == 'acertodec6':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'decisao7')

            elif cena == 'decisao7':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errodec7')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errodec7')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'acertodec7')

            elif cena == 'errodec7':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'decisao8')

            elif cena == 'acertodec7':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'decisao8')

            elif cena == 'decisao8':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errodec8')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errodec8')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'acertodec8')

            elif cena == 'errodec8':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'decisao9')

            elif cena == 'acertodec8':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'decisao9')

            elif cena == 'decisao9':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'acertodec9')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errodec9')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'errodec9')

            elif cena == 'errodec9':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'decisao10')

            elif cena == 'acertodec9':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'decisao10')

            elif cena == 'decisao10':
                cena = transition(cena, (762, 762 + 323), (123, 123 + 145), 'errodec10')
                cena = transition(cena, (762, 762 + 323), (459, 459 + 149), 'errodec10')
                cena = transition(cena, (762, 762 + 323), (292, 292 + 148), 'acertodec10')

            elif cena == 'errodec10':
                cena = transition(cena, (1062, 1062 + 126), (592, 592 + 95), 'menu14')

            elif cena == 'acertodec10':
                cena = transition(cena, (1061, 1061 + 127), (593, 593 + 96), 'menu14')

            elif cena == 'menu14':
                cena = transition(cena, (1034, 1034 + 100), (46, 46 + 99), 'pontuacao_tela')

            elif cena == 'pontuacao_tela':
                cena = transition(cena, (70, 70 + 107), (51, 51 + 105), 'inicio')

    if cena == 'pontuacao_tela':
        pontuacao_tela = pygame.image.load("pontuacao_tela.png")
        tela.blit(pontuacao_tela, (0, 0))
        render_text(f'{pontuacao}', largura // 2, altura // 2)

    elif cena == 'menu14':
        menu14 = pygame.image.load("menu1.4.png")
        tela.blit(menu14, (0, 0))

    elif cena == 'acertodec10':
        acertodec10 = pygame.image.load("acertodec10.png")
        tela.blit(acertodec10, (0, 0))
        pontuacao += 50

    elif cena == 'errodec10':
        errodec10 = pygame.image.load("errodec10.png")
        tela.blit(errodec10, (0, 0))
        pontuacao -= 25

    elif cena == 'decisao10':
        decisao10 = pygame.image.load("decisao10.png")
        tela.blit(decisao10, (0, 0))

    elif cena == 'acertodec9':
        acertodec9 = pygame.image.load("acertodec9.png")
        tela.blit(acertodec9, (0, 0))
        pontuacao += 50

    elif cena == 'errodec9':
        errodec9 = pygame.image.load("errodec9.png")
        tela.blit(errodec9, (0, 0))
        pontuacao -= 25

    elif cena == 'decisao9':
        decisao9 = pygame.image.load("decisao9.png")
        tela.blit(decisao9, (0, 0))

    elif cena == 'acertodec8':
        acertodec8 = pygame.image.load("acertodec8.png")
        tela.blit(acertodec8, (0, 0))
        pontuacao += 50

    elif cena == 'errodec8':
        errodec8 = pygame.image.load("errodec8.png")
        tela.blit(errodec8, (0, 0))
        pontuacao -= 25

    elif cena == 'decisao8':
        decisao8 = pygame.image.load("decisao8.png")
        tela.blit(decisao8, (0, 0))

    elif cena == 'acertodec7':
        acertodec7 = pygame.image.load("acertodec7.png")
        tela.blit(acertodec7, (0, 0))
        pontuacao += 50

    elif cena == 'errodec7':
        errodec7 = pygame.image.load("errodec7.png")
        tela.blit(errodec7, (0, 0))
        pontuacao -= 25

    elif cena == 'decisao7':
        decisao7 = pygame.image.load("decisao7.png")
        tela.blit(decisao7, (0, 0))

    elif cena == 'acertodec6':
        acertodec6 = pygame.image.load("acertodec6.png")
        tela.blit(acertodec6, (0, 0))
        pontuacao += 50

    elif cena == 'errodec6':
        errodec6 = pygame.image.load("errodec6.png")
        tela.blit(errodec6, (0, 0))
        pontuacao -= 25

    elif cena == 'decisao6':
        decisao6 = pygame.image.load("decisao6.png")
        tela.blit(decisao6, (0, 0))

    elif cena == 'acertodec5':
        acertodec5 = pygame.image.load("acertodec5.png")
        tela.blit(acertodec5, (0, 0))
        pontuacao += 50

    elif cena == 'errodec5':
        errodec5 = pygame.image.load("errodec5.png")
        tela.blit(errodec5, (0, 0))
        pontuacao -= 25

    elif cena == 'decisao5':
        decisao5 = pygame.image.load("decisao5.png")
        tela.blit(decisao5, (0, 0))

    elif cena == 'acertodec4':
        acertodec4 = pygame.image.load("acertodec4.png")
        tela.blit(acertodec4, (0, 0))
        pontuacao += 50

    elif cena == 'errodec4':
        errodec4 = pygame.image.load("errodec4.png")
        tela.blit(errodec4, (0, 0))
        pontuacao -= 25

    elif cena == 'decisao4':
        decisao4 = pygame.image.load("decisao4.png")
        tela.blit(decisao4, (0, 0))

    elif cena == 'acertodec3':
        acertodec3 = pygame.image.load("acertodec3.png")
        tela.blit(acertodec3, (0, 0))
        pontuacao += 50

    elif cena == 'errodec3':
        errodec3 = pygame.image.load("errodec3.png")
        tela.blit(errodec3, (0, 0))
        pontuacao -= 25

    elif cena == 'decisao3':
        decisao3 = pygame.image.load("decisao3.png")
        tela.blit(decisao3, (0, 0))

    elif cena == 'acertodec2':
        acertodec2 = pygame.image.load("acertodec2.png")
        tela.blit(acertodec2, (0, 0))
        pontuacao += 50

    elif cena == 'errodec2':
        errodec2 = pygame.image.load("errodec2.png")
        tela.blit(errodec2, (0, 0))
        pontuacao -= 25

    elif cena == 'decisao2':
        decisao2 = pygame.image.load("decisao2.png")
        tela.blit(decisao2, (0, 0))

    elif cena == 'acertodec1':
        acertodec1 = pygame.image.load("acertodec1.png")
        tela.blit(acertodec1, (0, 0))
        pontuacao += 50

    elif cena == 'errodec1':
        errodec1 = pygame.image.load("errodec1.png")
        tela.blit(errodec1, (0, 0))
        pontuacao -= 25

    elif cena == 'decisao1':
        decisao1 = pygame.image.load("decisao1.png")
        tela.blit(decisao1, (0, 0))

    elif cena == 'menu13':
        menu13 = pygame.image.load("menu1.3.png")
        tela.blit(menu13, (0, 0))

    elif cena == 'acertorep10':
        acertorep10 = pygame.image.load("acertorep10.png")
        tela.blit(acertorep10, (0, 0))
        pontuacao += 50

    elif cena == 'errorep10':
        errorep10 = pygame.image.load("errorep10.png")
        tela.blit(errorep10, (0, 0))
        pontuacao -= 25

    elif cena == 'repeticao10':
        repeticao10 = pygame.image.load("repeticao10.png")
        tela.blit(repeticao10, (0, 0))

    elif cena == 'acertorep9':
        acertorep9 = pygame.image.load("acertorep9.png")
        tela.blit(acertorep9, (0, 0))
        pontuacao += 50

    elif cena == 'errorep9':
        errorep9 = pygame.image.load("errorep9.png")
        tela.blit(errorep9, (0, 0))
        pontuacao -= 25

    elif cena == 'repeticao9':
        repeticao9 = pygame.image.load("repeticao9.png")
        tela.blit(repeticao9, (0, 0))

    elif cena == 'acertorep8':
        acertorep8 = pygame.image.load("acertorep8.png")
        tela.blit(acertorep8, (0, 0))
        pontuacao += 50

    elif cena == 'errorep8':
        errorep8 = pygame.image.load("errorep8.png")
        tela.blit(errorep8, (0, 0))
        pontuacao -= 25

    elif cena == 'repeticao8':
        repeticao8 = pygame.image.load("repeticao8.png")
        tela.blit(repeticao8, (0, 0))

    elif cena == 'acertorep7':
        acertorep7 = pygame.image.load("acertorep7.png")
        tela.blit(acertorep7, (0, 0))
        pontuacao += 50

    elif cena == 'errorep7':
        errorep7 = pygame.image.load("errorep7.png")
        tela.blit(errorep7, (0, 0))
        pontuacao -= 25

    elif cena == 'repeticao7':
        repeticao7 = pygame.image.load("repeticao7.png")
        tela.blit(repeticao7, (0, 0))

    elif cena == 'acertorep6':
        acertorep6 = pygame.image.load("acertorep6.png")
        tela.blit(acertorep6, (0, 0))
        pontuacao += 50

    elif cena == 'errorep6':
        errorep6 = pygame.image.load("errorep6.png")
        tela.blit(errorep6, (0, 0))
        pontuacao -= 25

    elif cena == 'repeticao6':
        repeticao6 = pygame.image.load("repeticao6.png")
        tela.blit(repeticao6, (0, 0))

    elif cena == 'acertorep5':
        acertorep5 = pygame.image.load("acertorep5.png")
        tela.blit(acertorep5, (0, 0))
        pontuacao += 50

    elif cena == 'errorep5':
        errorep5 = pygame.image.load("errorep5.png")
        tela.blit(errorep5, (0, 0))
        pontuacao -= 25

    elif cena == 'repeticao5':
        repeticao5 = pygame.image.load("repeticao5.png")
        tela.blit(repeticao5, (0, 0))

    elif cena == 'acertorep4':
        acertorep4 = pygame.image.load("acertorep4.png")
        tela.blit(acertorep4, (0, 0))
        pontuacao += 50

    elif cena == 'errorep4':
        errorep4 = pygame.image.load("errorep4.png")
        tela.blit(errorep4, (0, 0))
        pontuacao -= 25

    elif cena == 'repeticao4':
        repeticao4 = pygame.image.load("repeticao4.png")
        tela.blit(repeticao4, (0, 0))

    elif cena == 'acertorep3':
        acertorep3 = pygame.image.load("acertorep3.png")
        tela.blit(acertorep3, (0, 0))
        pontuacao += 50

    elif cena == 'errorep3':
        errorep3 = pygame.image.load("errorep3.png")
        tela.blit(errorep3, (0, 0))
        pontuacao -= 25

    elif cena == 'repeticao3':
        repeticao3 = pygame.image.load("repeticao3.png")
        tela.blit(repeticao3, (0, 0))

    elif cena == 'acertorep2':
        acertorep2 = pygame.image.load("acertorep2.png")
        tela.blit(acertorep2, (0, 0))
        pontuacao += 50

    elif cena == 'errorep2':
        errorep2 = pygame.image.load("errorep2.png")
        tela.blit(errorep2, (0, 0))
        pontuacao -= 25

    elif cena == 'repeticao2':
        repeticao2 = pygame.image.load("repeticao2.png")
        tela.blit(repeticao2, (0, 0))

    elif cena == 'acertorep1':
        acertorep1 = pygame.image.load("acertorep1.png")
        tela.blit(acertorep1, (0, 0))
        pontuacao += 50

    elif cena == 'errorep1':
        errorep1 = pygame.image.load("errorep1.png")
        tela.blit(errorep1, (0, 0))
        pontuacao -= 25

    elif cena == 'repeticao1':
        repeticao1 = pygame.image.load("repeticao1.png")
        tela.blit(repeticao1, (0, 0))

    elif cena == 'menu12':
        menu12 = pygame.image.load("menu1.2.png")
        tela.blit(menu12, (0, 0))

    elif cena == 'acertofun10':
        acertofun10 = pygame.image.load("acertofun10.png")
        tela.blit(acertofun10, (0, 0))
        pontuacao += 50

    elif cena == 'errofun10':
        errofun10 = pygame.image.load("errofun10.png")
        tela.blit(errofun10, (0, 0))
        pontuacao -= 25

    elif cena == 'funcao10':
        funcao10 = pygame.image.load("funcao10.png")
        tela.blit(funcao10, (0, 0))

    elif cena == 'acertofun9':
        acertofun9 = pygame.image.load("acertofun9.png")
        tela.blit(acertofun9, (0, 0))
        pontuacao += 50

    elif cena == 'errofun9':
        errofun9 = pygame.image.load("errofun9.png")
        tela.blit(errofun9, (0, 0))
        pontuacao -= 25

    elif cena == 'funcao9':
        funcao9 = pygame.image.load("funcao9.png")
        tela.blit(funcao9, (0, 0))

    elif cena == 'acertofun8':
        acertofun8 = pygame.image.load("acertofun8.png")
        tela.blit(acertofun8, (0, 0))
        pontuacao += 50

    elif cena == 'errofun8':
        errofun8 = pygame.image.load("errofun8.png")
        tela.blit(errofun8, (0, 0))
        pontuacao -= 25

    elif cena == 'funcao8':
        funcao8 = pygame.image.load("funcao8.png")
        tela.blit(funcao8, (0, 0))
    
    elif cena == 'acertofun7':
        acertofun7 = pygame.image.load("acertofun7.png")
        tela.blit(acertofun7, (0, 0))
        pontuacao += 50

    elif cena == 'errofun7':
        errofun7 = pygame.image.load("errofun7.png")
        tela.blit(errofun7, (0, 0))
        pontuacao -= 25

    elif cena == 'funcao7':
        funcao7 = pygame.image.load("funcao7.png")
        tela.blit(funcao7, (0, 0))
    
    elif cena == 'acertofun6':
        acertofun6 = pygame.image.load("acertofun6.png")
        tela.blit(acertofun6, (0, 0))
        pontuacao += 50

    elif cena == 'errofun6':
        errofun6 = pygame.image.load("errofun6.png")
        tela.blit(errofun6, (0, 0))
        pontuacao -= 25

    elif cena == 'funcao6':
        funcao6 = pygame.image.load("funcao6.png")
        tela.blit(funcao6, (0, 0))
        
    elif cena == 'acertofun5':
        acertofun5 = pygame.image.load("acertofun5.png")
        tela.blit(acertofun5, (0, 0))
        pontuacao += 50

    elif cena == 'errofun5':
        errofun5 = pygame.image.load("errofun5.png")
        tela.blit(errofun5, (0, 0))
        pontuacao -= 25

    elif cena == 'funcao5':
        funcao5 = pygame.image.load("funcao5.png")
        tela.blit(funcao5, (0, 0))
        
    elif cena == 'acertofun4':
        acertofun4 = pygame.image.load("acertofun4.png")
        tela.blit(acertofun4, (0, 0))
        pontuacao += 50

    elif cena == 'errofun4':
        errofun4 = pygame.image.load("errofun4.png")
        tela.blit(errofun4, (0, 0))
        pontuacao -= 25

    elif cena == 'funcao4':
        funcao4 = pygame.image.load("funcao4.png")
        tela.blit(funcao4, (0, 0))

    elif cena == 'acertofun3':
        acertofun3 = pygame.image.load("acertofun3.png")
        tela.blit(acertofun3, (0, 0))
        pontuacao += 50

    elif cena == 'errofun3':
        errofun3 = pygame.image.load("errofun3.png")
        tela.blit(errofun3, (0, 0))
        pontuacao -= 25

    elif cena == 'funcao3':
        funcao3 = pygame.image.load("funcao3.png")
        tela.blit(funcao3, (0, 0))

    elif cena == 'acertofun2':
        acertofun2 = pygame.image.load("acertofun2.png")
        tela.blit(acertofun2, (0, 0))
        pontuacao += 50

    elif cena == 'errofun2':
        errofun2 = pygame.image.load("errofun2.png")
        tela.blit(errofun2, (0, 0))
        pontuacao -= 25

    elif cena == 'funcao2':
        funcao2 = pygame.image.load("funcao2.png")
        tela.blit(funcao2, (0, 0))

    elif cena == 'acertofun1':
        acertofun1 = pygame.image.load("acertofun1.png")
        tela.blit(acertofun1, (0, 0))
        pontuacao += 50

    elif cena == 'errofun1':
        errofun1 = pygame.image.load("errofun1.png")
        tela.blit(errofun1, (0, 0))
        pontuacao -= 25

    elif cena == 'funcao1':
        funcao1 = pygame.image.load("funcao1.png")
        tela.blit(funcao1, (0, 0))

    elif cena == 'menu11':
        menu11 = pygame.image.load("menu1.1.png")
        tela.blit(menu11, (0, 0))

    elif cena == 'erro10':
        erro10 = pygame.image.load("erro10.png")
        tela.blit(erro10, (0, 0))
        pontuacao -= 25

    elif cena == 'acerto10':
        acerto10 = pygame.image.load("acerto10.png")
        tela.blit(acerto10, (0, 0))
        pontuacao += 50

    elif cena == 'pergunta10':
        pergunta10 = pygame.image.load("pergunta10.png")
        tela.blit(pergunta10, (0, 0))

    elif cena == 'erro9':
        erro9 = pygame.image.load("erro9.png")
        tela.blit(erro9, (0, 0))
        pontuacao -= 25

    elif cena == 'acerto9':
        acerto9 = pygame.image.load("acerto9.png")
        tela.blit(acerto9, (0, 0))
        pontuacao += 50

    elif cena == 'pergunta9':
        pergunta9 = pygame.image.load("pergunta9.png")
        tela.blit(pergunta9, (0, 0))

    elif cena == 'erro8':
        erro8 = pygame.image.load("erro8.png")
        tela.blit(erro8, (0, 0))
        pontuacao -= 25

    elif cena == 'acerto8':
        acerto8 = pygame.image.load("acerto8.png")
        tela.blit(acerto8, (0, 0))
        pontuacao += 50

    elif cena == 'pergunta8':
        pergunta8 = pygame.image.load("pergunta8.png")
        tela.blit(pergunta8, (0, 0))

    elif cena == 'erro7':
        erro7 = pygame.image.load("erro7.png")
        tela.blit(erro7, (0, 0))
        pontuacao -= 25

    elif cena == 'acerto7':
        acerto7 = pygame.image.load("acerto7.png")
        tela.blit(acerto7, (0, 0))
        pontuacao += 50

    elif cena == 'pergunta7':
        pergunta7 = pygame.image.load("pergunta7.png")
        tela.blit(pergunta7, (0, 0))

    elif cena == 'erro6':
        erro6 = pygame.image.load("erro6.png")
        tela.blit(erro6, (0, 0))
        pontuacao -= 25

    elif cena == 'acerto6':
        acerto6 = pygame.image.load("acerto6.png")
        tela.blit(acerto6, (0, 0))
        pontuacao += 50

    elif cena == 'pergunta6':
        pergunta6 = pygame.image.load("pergunta6.png")
        tela.blit(pergunta6, (0, 0))

    elif cena == 'erro5':
        erro5 = pygame.image.load("erro5.png")
        tela.blit(erro5, (0, 0))
        pontuacao -= 25

    elif cena == 'acerto5':
        acerto5 = pygame.image.load("acerto5.png")
        tela.blit(acerto5, (0, 0))
        pontuacao += 50

    elif cena == 'pergunta5':
        pergunta5 = pygame.image.load("pergunta5.png")
        tela.blit(pergunta5, (0, 0))

    elif cena == 'erro4':
        erro4 = pygame.image.load("erro4.png")
        tela.blit(erro4, (0, 0))
        pontuacao -= 25

    elif cena == 'acerto4':
        acerto4 = pygame.image.load("acerto4.png")
        tela.blit(acerto4, (0, 0))
        pontuacao += 50

    elif cena == 'pergunta4':
        pergunta4 = pygame.image.load("pergunta4.png")
        tela.blit(pergunta4, (0, 0))

    elif cena == 'erro3':
        erro3 = pygame.image.load("erro3.png")
        tela.blit(erro3, (0, 0))
        pontuacao -= 25

    elif cena == 'acerto3':
        acerto3 = pygame.image.load("acerto3.png")
        tela.blit(acerto3, (0, 0))
        pontuacao += 50

    elif cena == 'pergunta3':
        pergunta3 = pygame.image.load("pergunta3.png")
        tela.blit(pergunta3, (0, 0))

    elif cena == 'erro2':
        erro2 = pygame.image.load("erro2.png")
        tela.blit(erro2, (0, 0))
        pontuacao -= 25

    elif cena == 'acerto2':
        acerto2 = pygame.image.load("acerto2.png")
        tela.blit(acerto2, (0, 0))
        pontuacao += 50

    elif cena == 'pergunta2':
        pergunta2 = pygame.image.load("pergunta2.png")
        tela.blit(pergunta2, (0, 0))

    elif cena == 'menu':
        menu = pygame.image.load("menu.png")
        tela.blit(menu, (0, 0))

    elif cena == 'tela2':
        tela2 = pygame.image.load("tela2.png")
        tela.blit(tela2, (0, 0))

    elif cena == 'sobre':
        sobre = pygame.image.load("sobre.png")
        tela.blit(sobre, (0, 0))

    elif cena == 'creditos':
        creditos = pygame.image.load("creditos.png")
        tela.blit(creditos, (0, 0))

    elif cena == 'inicio':
        inicio = pygame.image.load("inicio.png")
        tela.blit(inicio, (0, 0))




    pygame.display.flip()
    pygame.display.update()

pygame.quit()