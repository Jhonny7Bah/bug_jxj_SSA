import pyautogui
from time import sleep

def InfinitamenteBuscandoImagem(imagem, tempo=2, fidelidade=0.8, tempo_inicial=2):
    #o intuito dessa função é buscar por uma imagem específica até encontrar.
    #caso não encontre a imagem, a função continuará buscando infinitamente!
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

def decorator(funcao):
    def interna(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        for __ in range(10):
            sleep(1)
            try:
                IMAGE1 = pyautogui.locateCenterOnScreen(f'D:\\jxjproject\\imagens\\perdeu_3_lose.png', confidence=0.8)
                sleep(2)
                IMAGE2 = pyautogui.locateCenterOnScreen(f'D:\\jxjproject\\imagens\\perceu_3_fechar', confidence=0.8)
                pyautogui.click(IMAGE1, duration=0.5)
                sleep(1)
                pyautogui.click(IMAGE2, duration=0.5)
                print('pronto para iniciar uma nova partida!')
                sleep(2)
                return resultado
            except pyautogui.ImageNotFoundException():
                print('não perdeu ainda!')
    return interna

garantindo_iniciar_partida = decorator(InfinitamenteBuscandoImagem)
for Teste in range(2):
    garantindo_iniciar_partida('iniciar_partida')
    InfinitamenteBuscandoImagem('comecar_partida')
    InfinitamenteBuscandoImagem('toque_para_fechar_mais_seguro')