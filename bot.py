import telepot
from produto import Produtos
import time
telegram = telepot.Bot("1318539129:AAEMoKJHN7ZyH40Y3tMNrHS_e0CcngD1lO4")

produto1 = Produtos("LAVA LOUÇAS AZULIM", "Esse produto foi especialmente elaborado para a limpeza de louças, talheres, panelas e demais utensílios de cozinha", "Aplique uma pequena quantidade de LAVA LOUÇAS AZULIM sobre uma esponja umedecida, esfregue sobre a superfície a ser limpa e em seguida, enxágue com água em abundância.", "https://drive.google.com/file/d/1mRIqBf0Cdx24AjrlvTI7z8-H8EnErvfb/view?usp=sharing")
produto2 = Produtos("DESINFETANTE VOREL", "Esse produto possui ação bactericida e germicida que deixa os vasos sanitários, ralos, latas de lixo livres de riscos. ", "\n• O DESINFETANTE VOREL pode ser encontrado nas versões: CITRUS, EUCALIPTO, FLORAL, JASMIM, LAVANDA, PINHO e TALCO; \n• Possui satisfatória ação bactericida frente às cepas de Staphylococcus aureus, Salmonella choleraesuis; \n• Sua formulação deixa um agradável perfume que permanece após a aplicação do produto; \n• Produto biodegradável.","https://drive.google.com/file/d/1DjYbTCKzfGLkua_9wOnbAJHe9Uo-Ronb/view?usp=sharing")
produto3 = Produtos("ÁGUA SANITÁRIA START", "Esse produto é indicado para o alvejamento de roupas, limpeza e desinfecção de superfícies em geral. \n \n Possui excelente ação bactericida na desinfecção dos alimentos. \n Ação bactericida frente às cepas de Salmonella choleraesuis, Escherichia coli, Staphylococcus aureus e Enterococcus faecium.", "*Instruções*: \n\n *Alvejamento de Roupas:* \nDilua 1 copo (200 ml) de ÁGUA SANITÁRIA START para cada 20L de água. \nAdicione as roupas e deixe de molho por 30 minutos antes de iniciar a lavagem no tanque ou na máquina. \n \n*Atenção:* Não utilizar ÁGUA SANITÁRIA START em tecidos de lã, seda, couro, poliuretano (lycra-elastano), roupas coloridas e em roupas com este sinal na etiqueta interna.\n *Desinfecção Geral:* \n Para desinfetar ralos e vasos sanitários: Utilize ÁGUA SANITÁRIA START pura, deixe agir por no mínimo 10 minutos e em seguida, enxague com água em abundância. Para remover incrustações de pisos e azulejos, lavar superfícies encardidas, vidrarias e cerâmicas: Dilua 1 copo (200 ml) de ÁGUA SANITÁRIA START em 5L de água. Aplique a solução diretamente sobre a superfície a ser limpa e esfregue com o auxílio de uma esponja ou pano úmido até que os resíduos sejam removidos. Em seguida, enxágüe com água em abundância. Desinfecção de frutas, hortaliças, verduras e legumes: Dilua em uma bacia plástica 1 colher de sopa (8 ml) de ÁGUA SANITÁRIA START em 1L de água. \n Deixe de molho por 10 minutos e em seguida, enxague com água em abundância. Importante: Use luvas ao manusear o produto e suas diluições. ","https://drive.google.com/file/d/1gU7qrRWN42-S7-XBWELwNlYx6BC19fBN/view?usp=sharing")
produto4 = Produtos("DESINFETANTE VOREL", "Esse produto possui ação bactericida e germicida que deixa os vasos sanitários, ralos, latas de lixo livres de riscos. ", "*Modo de uso:*\n Para desinfecção de vasos sanitários, ralos e latas de lixo: Aplique VOREL puro diretamente sobre as superfícies, deixando agir por 10 minutos. Para limpeza de pisos, pias, azulejos e superfícies laváveis: Use aproximadamente 50 ml de VOREL para cada litro de água, aplique com pano ou esponja, não é necessário enxaguar. *Importante:* É recomendável o uso de luvas ao manusear o produto e suas diluições.","https://drive.google.com/file/d/1DjYbTCKzfGLkua_9wOnbAJHe9Uo-Ronb/view?usp=sharing")
globalProduct = Produtos("Nenhum","Nenhum", "Nenhum", "Nenhum")

selectedProduct = False
lista = []

lista.append(produto1)
lista.append(produto2)
lista.append(produto3)
lista.append(produto4)

def search(name):
    for produto in lista:
        if str(name["text"]).lower() in produto.nome.lower():
          globals()['selectedProduct'] = True
          return produto
    return Produtos("Nenhum","Nenhum","Nenhum","Nenhum")

def recebendoMsg(msg):
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    global globalProduct

    if(globals()['selectedProduct']):    
        if(msg["text"]== "1"):
            telegram.sendMessage(chatID,  "*Produto:* "+  globalProduct.nome, parse_mode= 'Markdown')
            telegram.sendMessage(chatID,  "*Descrição:* \n"+  globalProduct.descricao, parse_mode= 'Markdown')
            time.sleep(10)
        if(msg["text"]== "2"):
            telegram.sendMessage(chatID,  "* Produto: * "+  globalProduct.nome, parse_mode= 'Markdown')
            telegram.sendMessage(chatID,  "* Como usuar:* \n"+  globalProduct.instrucao, parse_mode= 'Markdown')
            time.sleep(10)
        if(msg["text"]== "3"):
            globalProduct = Produtos("Nenhum","Nenhum", "Nenhum", "Nenhum")
            globals()['selectedProduct'] = False
            telegram.sendMessage(chatID,  "Ok, nenhum produto selecionado. \n \n Digite o nome de um produto para saber mais informações: ")
            time.sleep(10)
        else:
            telegram.sendMessage(chatID, "*Produto:*" + globalProduct.nome,  parse_mode= 'Markdown')
            telegram.sendMessage(chatID,  "O que você gostaria de saber sobre esse produto: \n (1) Descrição \n (2) Instrução \n (3) Para selecionar outro produto")
    else: 
        
        globalProduct = search(msg)
        if(globals()['selectedProduct']):
            telegram.sendMessage(chatID, "* Produto: * "+ globalProduct.nome,  parse_mode= 'Markdown')
            telegram.sendPhoto(chatID, globalProduct.url, )
            telegram.sendMessage(chatID,  "O que você gostaria de saber sobre esse produto: \n (1) Descrição \n (2) Instrução \n (3) Para selecionar outro produto")
        else:
            telegram.sendMessage(chatID,  "Me desculpe, não conseguimos encontrar esse produto. Por favor verifique o nome e digite novamente.")

telegram.message_loop(recebendoMsg)
while True:
    pass