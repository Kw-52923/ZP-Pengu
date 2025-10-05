import pygame
import sys

def menu_inicio(screen, fondo):
    """
    Muestra una pantalla de inicio con un botón 'Start Game' y una bienvenida paraguaya.
    Retorna True si el jugador presiona el botón para empezar.
    """
    fuente_titulo = pygame.font.SysFont(None, 80)
    fuente_texto = pygame.font.SysFont(None, 36)
    fuente_boton = pygame.font.SysFont(None, 50)

    clock = pygame.time.Clock()

    # Texto principal
    titulo = fuente_titulo.render(" Guaraní Invaders ", True, (0, 0, 0))
    subtitulo = fuente_texto.render("¡Oñepyrũ la batalla contra los mosquitos del Chaco!", True, (0, 0, 0))
    frase = fuente_texto.render("Prepárate héroe... ¡ndaipóri karaí ni chipa que te salve!", True, (0, 0, 0))

    # Botón Start Game
    texto_boton = "¡Empezar la batalla!"
    boton_render = fuente_boton.render(texto_boton, True, (255, 255, 255))
    boton_rect = boton_render.get_rect(center=(640, 500))

    anim_color = 0
    anim_direccion = 1

    while True:
        screen.blit(fondo, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # --- Animar color del botón ---
        anim_color += anim_direccion * 3
        if anim_color > 120 or anim_color < 0:
            anim_direccion *= -1
        color_boton = (min(255, max(0, 200 + anim_color)), 0, 0)


        # --- Títulos ---
        rect_titulo = titulo.get_rect(center=(640, 200))
        rect_subtitulo = subtitulo.get_rect(center=(640, 280))
        rect_frase = frase.get_rect(center=(640, 320))
        screen.blit(titulo, rect_titulo)
        screen.blit(subtitulo, rect_subtitulo)
        screen.blit(frase, rect_frase)

        # --- Botón ---
        color = color_boton if boton_rect.collidepoint(mouse_pos) else (100, 0, 0)
        pygame.draw.rect(screen, color, boton_rect.inflate(30, 20), border_radius=15)
        screen.blit(boton_render, boton_rect)

        pygame.display.flip()

        # --- Eventos ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boton_rect.collidepoint(event.pos):
                    return True

        clock.tick(30)
