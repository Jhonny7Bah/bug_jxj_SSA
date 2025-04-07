import pyautogui
from time import sleep

def InfinitamenteBuscandoImagem(imagem, tempo=2, fidelidade=0.8, tempo_inicial=2):
    while True:
        try:
            IMAGEM = pyautogui.locateCenterOnScreen(f'D:\\jxjproject\\imagens\\{imagem}.png', confidence=fidelidade)
            sleep(tempo_inicial)
            pyautogui.click(IMAGEM)
            print('FUNCINOU O', imagem, '!!!!!!!!!')
            sleep(tempo)
            break
        except pyautogui.ImageNotFoundException:
            print('não encontrei', imagem)


def verificacao_inicial(tempo=2, fidelidade=0.8):
    for __ in range(10):
        sleep(1)
        try:
            IMAGE1 = pyautogui.locateCenterOnScreen(f'D:\\jxjproject\\imagens\\perdeu_3_lose.png', confidence=fidelidade)
            pyautogui.click(IMAGE1)
            sleep(4)
            IMAGE2 = pyautogui.locateCenterOnScreen(f'D:\\jxjproject\\imagens\\perceu_3_fechar.png', confidence=fidelidade)
            pyautogui.click(IMAGE2)
            sleep(1)
            print('FUNCINOU!!!!!!!!!')
            sleep(tempo)
            break
        except pyautogui.ImageNotFoundException:
            print('não encontrei')

def toque_para_fechar():
    while True:
            try:
                FIRST_IMAGE = pyautogui.locateCenterOnScreen(f'D:\\jxjproject\\imagens\\toque_para_fechar_mais_seguro.png', confidence=0.8)
                sleep(2)
                pyautogui.click(FIRST_IMAGE)
                print('FUNCINOU !!!!!!!!!')
                return 0
            except pyautogui.ImageNotFoundException:
                print('não encontrei 1')
                sleep(1.5)
                try:
                    SECOND_IMAGE = pyautogui.locateCenterOnScreen(f'D:\\jxjproject\\imagens\\toque_para_fechar_fechar.png', confidence=0.8)
                    sleep(2)
                    pyautogui.click(SECOND_IMAGE)
                    print('FUNCINOU !!!!!!!!!')
                    return 1
                except pyautogui.ImageNotFoundException:
                    print('não encontrei 2')
                    sleep(1.5)

for Teste in range(50):
    verificacao_inicial()
    InfinitamenteBuscandoImagem('iniciar_partida')
    InfinitamenteBuscandoImagem('comecar_partida')
    toque_para_fechar()
    print(f'joguei {Teste} partidas!')