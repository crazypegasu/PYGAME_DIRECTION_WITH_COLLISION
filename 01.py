import pygame as cerebro
import sys

width = 600 #x
height = 600 #y
tela = "TESTE_01"
BLACK = (000,000,000)
GREEN = (8,72,8)
RED =   (255,000,000)

screen = cerebro.display.set_mode([width,height])
cerebro.display.set_caption(tela)
velocidade = 0.07


def main():
    x = 2
    y = 2
    running = True
    while running:
        for evento in cerebro.event.get():
            if evento.type == cerebro.QUIT:
                running = False
    

        key = cerebro.key.get_pressed()

        if key[cerebro.K_w]:
            y -= velocidade
        if key[cerebro.K_s]:
            y += velocidade
        if key[cerebro.K_a]:
            x -= velocidade
        if key[cerebro.K_d]:
            x += velocidade

        screen.fill(BLACK)

        x = max(0, min(x, width - 25))
        y = max(0, min(y, height - 25))

        cerebro.draw.rect(screen, GREEN, (x,y,25,25))



        cerebro.display.flip()
    cerebro.quit()


if __name__ == "__main__":
    main()

