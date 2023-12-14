import pygame as pg
import random as r
import pickle as pk
import os

#Variavéis "globais" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
valores_sprites = [1, 2, 3, 4, 5]

tlargura = 900
tamL = tlargura - 300
tamA = 400

tamQL = tamL // 6
tamQA = tamA // 6

lin_n = 6

tabuleiro = [[0 for _ in range(lin_n)] for _ in range(lin_n)]#Matriz do tabuleiro
lista_sprites = []#lista que armazena os sprites

arquivo = os.path.join(os.path.dirname(__file__), "./arquivo/file_pont.pkl")
#**********************************************************************************

#Função que importa, calibra o tamanho e adiciona as sprites na lista++++++++++++++
def carregar_sprites():
    for i in range(1, 6):
        imagem = pg.image.load(f"./arquivo/imagem{i}.png")
        imagem = pg.transform.scale(imagem, (tamQL, tamQA))
        lista_sprites.append(imagem)
#**********************************************************************************


#Função que adiciona as spriites iniciis a matriz++++++++++++++++++++++++++++++++++
def criar_matriz():
   
    for _ in range(lin_n):
        linha = []
        for _ in range(lin_n):
            spriten = r.choice(valores_sprites)
            linha.append(spriten)
        tabuleiro.append(linha)

    # loop que garante pelo menos 1/3 das sprites sejam adcionadas a matriz
    for i in range(lin_n):
        for j in range(lin_n):
            while (
                (i < lin_n - 2 and tabuleiro[i][j] == tabuleiro[i + 1][j] == tabuleiro[i + 2][j]) or
                (j < lin_n - 2 and tabuleiro[i][j] == tabuleiro[i][j + 1] == tabuleiro[i][j + 2])
            ):
                tabuleiro[i][j] = r.choice(valores_sprites)
#**********************************************************************************


#função que faz as sprites serem impressas na tela gráfica+++++++++++++++++++++++++
def imprimir(janela):
    for linha in range(lin_n):
        for coluna in range(lin_n):
            xc = coluna * tamQL
            yc = linha * tamQA

            sprite_index = tabuleiro[linha][coluna]
            sprite_surface = lista_sprites[sprite_index - 1]  
            janela.blit(sprite_surface, (xc, yc))
#**********************************************************************************


#Funçção que permite a troca de posição das sprites++++++++++++++++++++++++++++++++
def Tocar_posicao(row1, col1, row2, col2):
    if Validar_Jogadas(tabuleiro, row1, col1, row2, col2):
        tabuleiro[row1][col1], tabuleiro[row2][col2] = tabuleiro[row2][col2], tabuleiro[row1][col1]
#*********************************************************************************


#verifica se as celulas vizinhas são sprites iguais+++++++++++++++++++++++++++++++
def Verificar_celulas():
    global tabuleiro
    celula_encontrada = []

    for linha in range(lin_n):
        for colun in range(lin_n):
            gema = tabuleiro[linha][colun]
            if gema == 0:
                continue

            # Verificar no horizontal
            if colun < lin_n - 2 and tabuleiro[linha][colun + 1] == gema and tabuleiro[linha][colun + 2] == gema:
                celula_encontrada.append((linha, colun))
                celula_encontrada.append((linha, colun + 1))
                celula_encontrada.append((linha, colun + 2))

            # Verificar na vertical
            if linha < lin_n - 2 and tabuleiro[linha + 1][colun] == gema and tabuleiro[linha + 2][colun] == gema:
                celula_encontrada.append((linha, colun))
                celula_encontrada.append((linha + 1, colun))
                celula_encontrada.append((linha + 2, colun))

    for linha, colun in celula_encontrada:
        tabuleiro[linha][colun] = 0

    return celula_encontrada
#*********************************************************************************


#Repõe as gemas destruidas durante o jogo++++++++++++++++++++++++++++++++++++++++++
def Recolocar_gemas():
    global tabuleiro 
    pontuacao = 0
    
    for col in range(lin_n):
        gems = [tabuleiro[row][col] for row in range(lin_n) if tabuleiro[row][col] != 0]

        while len(gems) < lin_n:
            gems.insert(0, r.choice(valores_sprites))
        
        for l in range(lin_n):
            tabuleiro[l][col] = gems[l]

        pontuacao += Pontuaçao([], 0)  # Passando uma lista vazia para quebras

    return pontuacao
#**********************************************************************************

#Funçao que caucula a pontiuaçao das gemas+++++++++++++++++++++++++++++++++++++++++
def Pontuaçao(quebras,pontuacao):
    pontua = 0
    
    for cadeia in quebras:
        pontua += len(cadeia) * 10#faz com que cada gema possua o valor de dez pontos
        
    return pontua
#**********************************************************************************


#Descobre se as sprites formam cadeias de tres ou mais*++++++++++++++++++++++++++++
def Validar_Jogadas(tabuleiro, linha1, coluna1,linha2, coluna2):
    if linha1 < 0 or linha1 >= lin_n or coluna1 < 0 or coluna1 >= lin_n:
        return False
    
    if linha2 < 0 or linha2 >= lin_n or coluna2 < 0 or coluna2 >= lin_n:
        return False
    if (abs(linha1 - linha2) == abs(coluna1-coluna2)):
        return True
    #Verifica a direaçao da linha
    return (abs(linha1 - linha2) == 1 and coluna1 == coluna2) or (linha1 == linha2 and abs(coluna1 - coluna2) == 1)
#**********************************************************************************


#Verificar se tem jogadaas disponivel para ajuda+++++++++++++++++++++++++++++++++++
def Dicas_disponivel(tabuleiro):
    for linha in range(lin_n):
        for coluna in range(lin_n):
            gema = tabuleiro[linha][coluna]
            # horizontal
            if coluna < lin_n - 2 and tabuleiro[linha][coluna + 1] == gema and tabuleiro[linha][coluna + 2] == gema:
                return True
            # vertical
            if linha < lin_n - 2 and tabuleiro[linha + 1][coluna] == gema and tabuleiro[linha + 2][coluna] == gema:
                return True
    return False
#**********************************************************************************


#encontra gemas vizinhas que podem formar cadeias++++++++++++++++++++++++++++++++++
def Dicas_encontrar(tabuleiro):
    dicas = []

    for linha in range(lin_n):
        for coluna in range(lin_n):
           
            if coluna < lin_n - 1:
                tabuleiro[linha][coluna], tabuleiro[linha][coluna + 1] = tabuleiro[linha][coluna + 1], tabuleiro[linha][coluna]
                if Dicas_disponivel(tabuleiro):
                    dicas.append(((linha, coluna), (linha, coluna + 1)))
                tabuleiro[linha][coluna], tabuleiro[linha][coluna + 1] = tabuleiro[linha][coluna + 1], tabuleiro[linha][coluna]  

           
            if linha < lin_n - 1:
                tabuleiro[linha][coluna], tabuleiro[linha + 1][coluna] = tabuleiro[linha + 1][coluna], tabuleiro[linha][coluna]
                if Dicas_disponivel(tabuleiro):
                    dicas.append(((linha, coluna), (linha + 1, coluna)))
                tabuleiro[linha][coluna], tabuleiro[linha + 1][coluna] = tabuleiro[linha + 1][coluna], tabuleiro[linha][coluna]  

    return dicas
#**********************************************************************************

#avisa que nao tem ajuda disponivel++++++++++++++++++++++++++++++++++++++++++++++++
def Aviso_sem_ajuda(janela, ajudaqt):
    font = pg.font.Font(None, 36)
    if ajudaqt <= 0:
        sem_ajuda = font.render(f'SEM DICAS DISPONIVEIS!!!',False, (255, 0, 0))
        janela.blit(sem_ajuda, (10,10))
#**********************************************************************************


#abre o arquivo com a pontuação salva++++++++++++++++++++++++++++++++++++++++++++++
def Arquivo_Abrir():
    if os.path.exists(arquivo):
        try:
            with open(arquivo, 'rb') as file:
                return pk.load(file)
        except (FileNotFoundError, EOFError, pk.UnpicklingError) as e:
            #print(f"Aviso: {e}")
            return 0 
    else:
        #print("Aviso: O arquivo não existe.")
        return 0 
#**********************************************************************************


#salva a pontuação em arquivo binario++++++++++++++++++++++++++++++++++++++++++++++
def Arquivo_Salvar(pontuacao):
    pontuacao_ofc = Arquivo_Abrir()
    pont = pontuacao_ofc + pontuacao
    diretorio = os.path.dirname(arquivo)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    with open(arquivo, 'wb') as file:
        pk.dump(pont, file)
#**********************************************************************************


#imprime os textos com suas funcionalidades++++++++++++++++++++++++++++++++++++++++
def Textos(janela, pontuacao, ajudaqt, temp_inic):
    pontuacao_ofc = Arquivo_Abrir()
    font = pg.font.Font(None, 36)
#score
    texto = font.render(f'Score: {pontuacao}', True, (255, 0, 0))
#tempo
    textot = font.render(f'Tempo: {temp_inic}', True, (255, 0,0))
#Dicas
    textoa = font.render(f'Dicas Disponiveis:{ajudaqt}', True, (200,10,10))
# pontuação 
    text = font.render(f'Pontuação:{pontuacao_ofc}', True, (255, 50, 100))

    janela.blit(texto, ((tamL +6), 10))
    janela.blit(textoa, ((tamL + 6), (tamA - 30)))
    janela.blit(text, ((tamL + 6), 30))
    janela.blit(textot, ((tamL + 6), (tamA - 50)))
#**********************************************************************************


# Dicas para jogadores+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Ajuda(janela):
    dicas = Dicas_encontrar(tabuleiro)
    for d in dicas:
        (linha1, coluna1), (linha2, coluna2) = d
        pg.draw.rect(janela, (0, 0, 0), (coluna1 * tamQL, linha1 * tamQA,  tamQL, tamQA), 3)
        pg.draw.rect(janela, (0, 0, 0), (coluna2 * tamQL, linha2 * tamQA, tamQL, tamQA), 3)
#**********************************************************************************


#imagem de BackGround+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def imagem_de_fundo(janela):
    bg = pg.image.load("./arquivo/fazendeiro_fundo2.PNG")
    bg = pg.transform.scale(bg, (300, tamA))
    janela.blit(bg, (tamL, 0))
#**********************************************************************************


#Função Princippal+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Main():
    #chama as funçãos e variaveis ecenciais
    pg.init()
    janela = pg.display.set_mode((tlargura, tamA))

    pontuacao = 0

    ajudaqt = 10
    rodar = True
    carregar_sprites()
    criar_matriz()

    temp_inic = 0
    temp_alvo = r.randint(1000, 10000)
    temp_inic += temp_alvo
    
    gem_select = None
    gem_select_pos = None  
     
    while rodar:#loop princiopal
        temp_inic -= 1
        janela.fill((50, 50, 50))
        #loop para evento das teclas
        for evento in pg.event.get():
            if evento.type == pg.QUIT or (evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                rodar = False
            if evento.type == pg.KEYDOWN and evento.key == pg.K_h:
                ajudaqt -= 1
            
            #condição para funcionamento do mouse
            if evento.type == pg.MOUSEBUTTONDOWN:
                
                px, py = pg.mouse.get_pos()
                posx = px // tamQL
                posy = py // tamQA

                if gem_select is None:
                    gem_select = tabuleiro[posy][posx]
                    gem_select_pos = (posy, posx)
                else:
                    posx2, posy2 = posx, posy
                    #troca de posição conforme o botao do mouse
                    if (abs(posy2 - gem_select_pos[0]) == 1 and posx2 == gem_select_pos[1]) or (
                            abs(posx2 - gem_select_pos[1]) == 1 and posy2 == gem_select_pos[0]):
                        Tocar_posicao(gem_select_pos[0], gem_select_pos[1], posy, posx)

                        # Verifica e atualiza a pontuação
                        quebras = Verificar_celulas()
                        if quebras:
                            Recolocar_gemas()
                            pontuacao += Pontuaçao( quebras, pontuacao)
                            jvk = (pontuacao // 100) * 5
                            Arquivo_Salvar(jvk)
                            
                        gem_select = None
        
        if temp_inic <= 0:#verifica o tempo e para o jogo
            rodar = False

        imagem_de_fundo(janela)
        imprimir(janela)
        
        if pg.key.get_pressed()[pg.K_h] or pg.key.get_pressed()[pg.K_PRINT]:#chama a ajuda
            ativar_ajuda = True
            Aviso_sem_ajuda(janela, ajudaqt)
            if ajudaqt <= 0:
                ativar_ajuda = False
        else:
            ativar_ajuda = False

        if ativar_ajuda:
            Ajuda(janela)

        pg.draw.line(janela, (0,0,50), (tamL -2, 0), (tamL -2, tamA), 10)
        Textos(janela, pontuacao, ajudaqt, temp_inic)
   
        pg.display.flip()

    pg.quit()
  
beM = Main#chama a funçao para o arquivo Tela_Entrada
