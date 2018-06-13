import pygame, sys
from pygame.locals import *# serve pra puxar toda a biblioteca do pygame
import random
import time
from random import randint

branco = (255,255,255)

class cavaleiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.guereiro = pygame.image.load("imagens/cavaleironormald.png")

        self.rect = self.guereiro.get_rect()
        self.rect.centerx = 512
        self.rect.centery = 370
        self.JE=0
        self.JD=1
        self.JA=0
        self.velocidade = 20

    def colocar(self,superficie):
        superficie.blit(self.guereiro, self.rect)

class aranhas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.aranha = pygame.image.load("imagens/aranha.png")

        self.rect = self.aranha.get_rect()
        self.rect.centerx = 40
        self.rect.centery = 400
        self.MA=5
        self.EA=1
        self.DA=0
        self.velocidade = self.MA

    def colocar(self,superficie):
        superficie.blit(self.aranha, self.rect)

def iniciando():

    tela=pygame.display.set_mode([1024,512])#TAMANHO DA TELA
    pygame.display.set_caption("Infestação")#NOME QUE IRA APARECER
    relogio=pygame.time.Clock()

    lvl = 5
    c2=0
    inimigos = []

    c=1000
    imagenfundo = pygame.image.load("imagens/fundo.jpg")
    jogador = cavaleiro()
    jogando(c,c2,inimigos,tela,imagenfundo,jogador,relogio,lvl)

def jogando(a,b,c,d,e,f,g,h):
    while True:#WHILE PARA MANTER O LAÇO INFINITO , PARA O JOGO NAO FEHCAR
        pygame.init()
        if pygame.time.get_ticks() > a:
            if b <= h:
                if b%2==0:
                    inimigo = aranhas()
                    c.append(inimigo)
                    c[b].aranha = pygame.image.load("imagens/aranha.png")
                    c[b].rect.centerx = 40
                    b +=1
                    a +=1000
                else:
                    inimigo = aranhas()
                    c.append(inimigo)
                    c[b].aranha = pygame.image.load("imagens/aranha2.png")
                    c[b].rect.centerx = 980
                    b +=1
                    a +=1000
        movaranha(c)
        movjogador(f)
        colisao(c,f)


        d.blit(e, (0,0))#tela
        for n in range(len(c)):#aranha
            c[n].colocar(d)#cavaleiro
        f.colocar(d)
        g.tick(30)
        pygame.display.update()#COMANDO PARA MANTER A TELA ATUALIZADA



def movaranha(a):
    for j in range(len(a)):
        a[j].rect.left+= a[j].MA

    for k in range(len(a)):
        if a[k].rect.left <= 0:
            a[k].MA = a[k].MA*-1
            a[k].aranha = pygame.image.load("imagens/aranha.png")
            a[k].EA =1
            a[k].DA  =0

    for l in range(len(a)):
        if a[l].rect.right >= 1024:
            a[l].MA = a[l].MA*-1
            a[l].aranha = pygame.image.load("imagens/aranha2.png")
            a[l].EA = 0
            a[l].DA = 1

def movjogador(a):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()#COMANDO PARA EVEITAR RPOBLEMAS AO SAIR DO JOGO E ABRIR ELE DENOVO

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                a.guereiro = pygame.image.load("imagens/cavaleironormale.png")
                a.rect.left -= a.velocidade
                a.JE=1
                a.JD=0
                a.JA=0
            if event.key == K_RIGHT:
                a.guereiro = pygame.image.load("imagens/cavaleironormald.png")
                a.rect.left += a.velocidade
                a.JD=1
                a.JE=0
                a.JA=0
            if event.key == K_SPACE:
                if a.JE==1:
                    a.guereiro = pygame.image.load("imagens/cavaleirovivo2.png")
                else:
                    a.guereiro = pygame.image.load("imagens/cavaleirovivo.png")
                a.JA=1

    if a.rect.left <= 0:
        a.rect.left = 0
    if a.rect.right >= 1024:
        a.rect.right = 1024

def colisao(a,b):
    for m in range(len(a)):
        if b.rect.colliderect(a[m].rect):
            if b.JA==1:
                if a[m].EA == 1:
                    a[m].aranha = pygame.image.load("imagens/aranhamortae.png")
                    a[m].MA= 0

                else:
                    a[m].aranha = pygame.image.load("imagens/aranhamortad.png")
                    a[m].MA=0
def menu():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                menu = pygame.image.load("imagens/menu.jpg")
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                inst = pygame.image.load("imagens/instrucoes.jpg")
menu()
iniciando()