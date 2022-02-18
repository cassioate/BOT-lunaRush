import pyautogui
import random
import time
import dotenv
import os

dotenv.load_dotenv()

# 100%
def conectarFunc():
    contador = 0
    connect = True
    metamaskClick = False
    assinarClick = False
    modoChefeClick = False
    bossDisponivelClick = False
    pyautogui.click(searchForHighConfidenceImage("LunaRushLogo"), duration = durationChoosed())
    time.sleep(2)
    reiniciarAPagina()
    while connect == True:
        if contador == 50:
            raise Exception("Erro ao tentar realizar o login")
        if metamaskClick == False and procurarImagemSemRetornarErro("metamask"):
            pyautogui.click(searchForHighConfidenceImage("metamask"), duration = durationChoosed())
            metamaskClick = True
        if assinarClick == False and metamaskClick == True and (procurarImagemSemRetornarErro("assinar") or procurarImagemSemRetornarErro("metamaskNotification")):
            if procurarImagemSemRetornarErro("assinar"):
                pyautogui.click(searchForHighConfidenceImage("assinar"), duration = durationChoosed())
            elif procurarImagemSemRetornarErro("metamaskNotification"):
                pyautogui.click(searchForHighConfidenceImage("metamaskNotification"), duration = durationChoosed())
                time.sleep(5)
                pyautogui.click(searchForHighConfidenceImage("assinar"), duration = durationChoosed())
            assinarClick = True
        if modoChefeClick == False and assinarClick == True and metamaskClick == True and procurarImagemSemRetornarErro("entrarNoModoCacaAoChefe"):
            pyautogui.click(searchForHighConfidenceImage("entrarNoModoCacaAoChefe"), duration = durationChoosed()) 
            modoChefeClick = True
        if bossDisponivelClick == False and modoChefeClick == True and assinarClick == True and metamaskClick == True and procurarImagemSemRetornarErro("bossDisponivel"):
            pyautogui.click(searchForHighConfidenceImage("bossDisponivel"), duration = durationChoosed())
            bossDisponivelClick = True
            connect = False
        contador += 1

# 100%
def searchForHighConfidenceImage(imagem):
    print('*' + '-' * 50 + '*')
    print('Utiliando a func searchForHighConfidenceImage: '+ imagem)
    contadorProcurarImagem = 0
    x, y = None, None
    while x == None:
        x, y = procurarLocalizacaoDaImagemPelosEixos(imagem)
        contadorProcurarImagem += 1
        if contadorProcurarImagem >= 15:
            raise Exception('Erro ao achar a imagem: ' + imagem)
    print('*' + '-' * 50 + '*')
    return x, y

# 100%
def procurarImagemSemRetornarErro(imagem):
    print('Utiliando a func procurarImagemSemRetornarErro: '+ imagem)
    confidence = os.getenv("CONFIDENCE")
    img = None
    contador = 0
    if (imagem == "metamaskNotification"):
        time.sleep(10)
    while img == None:
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        if img != None:
            print('Achei a imagem: ' + imagem)
            return True
        contador += 1
        if contador >= 5:
            img = True
    print('Não consegui encontrar a imagem: ' + imagem)
    return False

def procurarLocalizacaoDaImagemPelosEixos(imagem):
    print('Utiliando a func procurarLocalizacaoDaImagemPelosEixos: ' + imagem)
    contador = 0
    while contador < 10:
###########################################
        if imagem == 'guerreiro' or imagem == 'metamaskNotification':
            if procurarImagemSemRetornarErro(imagem):
                confidence = os.getenv("CONFIDENCE")
                try:
                    x, y = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
                    loop = False
                    if x != None:
                        print('Clicando em: ' + str(x)+ ', ' + str(y))
                        return x, y
                    else:
                        print('Erro nas linhas 70-71 do codigo, o X está voltando None, mesmo após ter sido bem sucedido em "procurarImagemSemRetornarErro"')
                except:
                    print("Erro ao procurar imagem: " + imagem)            
            else:
                contador += 1
############################################
        if imagem == 'abrirMenuGuerreiro' or imagem == 'fecharMenuGuerreiro' or imagem == 'x':
            if procurarImagemSemRetornarErro(imagem):
                confidence = os.getenv("CONFIDENCE")
                randomVar = random.randint(0, 10)
                try:
                    x, y = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
                    if x != None:
                        x, y = x-(randomVar/2), y-(randomVar/2)
                        x, y = x+randomVar, y+randomVar
                        print('Clicando em: ' + str(x)+ ', ' + str(y))
                        return x, y
                    else:
                        print('Erro nas linhas 82-85 do codigo, o X está voltando None, mesmo após ter sido bem sucedido em "procurarImagemSemRetornarErro"')
                except:
                    print("Erro ao procurar imagem: " + imagem)                
            else:
                contador += 1
###########################################
        else:        
            if procurarImagemSemRetornarErro(imagem):
                confidence = os.getenv("CONFIDENCE")
                randomVarX = random.randint(0, float(os.getenv("RandomVarEixoX")))
                randomVarY = random.randint(0, float(os.getenv("RandomVarEixoY")))
                try:
                    x, y = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
                    if x != None:
                        x, y = x-(float(os.getenv("RandomVarEixoX"))/2), y-float(os.getenv("RandomVarEixoY"))/2
                        x, y = x+randomVarX, y+randomVarY
                        print('Clicando em: ' + str(x)+ ', ' + str(y))
                        return x, y
                    else:
                        print('Erro nas linhas 82-85 do codigo, o X está voltando None, mesmo após ter sido bem sucedido em "procurarImagemSemRetornarErro"')
                except:
                    print("Erro ao procurar imagem: " + imagem)
            else:
                contador += 1
    return None, None

# LUNA RUSH
#####################################################

# 100%
def selectBoss(boss):
    contador = 0
    for i in range(20):
        if procurarImagemSemRetornarErro(boss+i):
            pyautogui.click(searchForHighConfidenceImage(boss+i), duration = durationChoosed())
            if procurarImagemSemRetornarErro("SelecionarHeroina"):
                pyautogui.click(searchForHighConfidenceImage("SetaCinza"), duration = durationChoosed())
            else:
                contador = i-1
                return contador

# 100%
def selectHero(x, y):
    pyautogui.click(x, y, duration = durationChoosed())

# 100%
def selectTriple(triple):
    randomVar = random.randint(1, float(os.getenv("RandomVarSelectTriple")))
    x, y = procurarLocalizacaoDaImagemPelosEixos("guerreiro")
    x, y = x-(float(os.getenv("RandomVarSelectTriple"))/2), y-(float(os.getenv("RandomVarSelectTriple"))/2)
    x, y = x+randomVar, y+randomVar
    if triple == 0:
        selectHero(x, y+100)
        selectHero(x+100, y+100)
        selectHero(x+200, y+100)     
    elif triple == 1:
        selectHero(x+300, y+100)
        selectHero(x, y+240)
        selectHero(x+100, y+240)      
    elif triple == 2:
        selectHero(x+200, y+240)
        selectHero(x+300, y+240)
        selectHero(x, y+370) 
    elif triple == 3:
        selectHero(x+100, y+370)
        selectHero(x+200, y+370)
        selectHero(x+300, y+370)
    elif triple == 4:
        selectHero(x, y+370)
        selectHero(x+100, y+370)
        selectHero(x+200, y+370)

def clickHeroinaRemove(x, y):
    for i in range(x, y):
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(i)), duration = durationChoosed())
        time.sleep(4)

# 100%
def removeTheTriple(triple):
    if triple == 0:
        clickHeroinaRemove(1, 4)
    elif triple == 1:
        clickHeroinaRemove(4, 7)
    elif triple == 2:
        clickHeroinaRemove(7, 10)
    elif triple == 3:
        clickHeroinaRemove(10, 13)
    elif triple == 4:
        clickHeroinaRemove(13, 15)

# 100%
def removeAndAddTriple(i):
    if i == 0:
        removeVerify()
        dragInTheMenuOfHeros()
        removeVerify()
        closedMenuOfHeroes()
        selectHeroInTheMenu()
        #REMOVENDO TRIPLA ANTERIOR
    if i > 0:
        removeTheTriple(i-1)
    if i == 4:
        time.sleep(2)
        dragInTheMenuOfHeros()
    selectTriple(i) 
    time.sleep(1)   

# 100%
def removeVerify():
    while procurarImagemSemRetornarErro("Verificado"):
        pyautogui.click(searchForHighConfidenceImage("Verificado"), duration = durationChoosed())
        time.sleep(5)

# 100%
def toHunt():
    for i in range(5):
        contador = 1
        selectHeroInTheMenu()
        removeAndAddTriple(i)
        closedMenuOfHeroes()
        while contador < 4:
            pyautogui.click(searchForHighConfidenceImage("cacarChefe"), duration = durationChoosed())
            time.sleep(10)
            if procurarImagemSemRetornarErro("AvisoPrevio"):
                while procurarImagemSemRetornarErro("AvisoPrevio"):
                    pyautogui.click(searchForHighConfidenceImage("x"), duration = durationChoosed())
                    time.sleep(3)
                    print("cliquei no x")
                contador = 4               
            if contador < 4:
                searchForResult()
            contador += 1
            
# 100%
def searchForResult():
    clickAlready = False
    loop = True
    while loop:
        time.sleep(5)
        loop = procurarImagemSemRetornarErro("bossLoop")
        if clickAlready == False:
            pyautogui.click(searchForHighConfidenceImage("VS"), duration = durationChoosed())
            clickAlready = True
        if procurarImagemSemRetornarErro("Derrotado"):
            time.sleep(5)
            pyautogui.click(searchForHighConfidenceImage("Derrotado"), duration = durationChoosed())   
        elif procurarImagemSemRetornarErro("Vitoria"):
            time.sleep(5)
            if procurarImagemSemRetornarErro("ToqueParaAbrir"):
                pyautogui.click(searchForHighConfidenceImage("ToqueParaAbrir"), duration = durationChoosed())
                time.sleep(5)
                if procurarImagemSemRetornarErro("Vitoria"):
                    pyautogui.click(searchForHighConfidenceImage("Vitoria"), duration = durationChoosed())
            time.sleep(10)
            if procurarImagemSemRetornarErro("bossDisponivel"):
                pyautogui.click(searchForHighConfidenceImage("bossDisponivel"), duration = durationChoosed())

# 100%
def selectHeroInTheMenu():
    pyautogui.click(searchForHighConfidenceImage("abrirMenuGuerreiro"), duration = durationChoosed())
    time.sleep(4)

# 100%
def closedMenuOfHeroes():
    pyautogui.click(searchForHighConfidenceImage("fecharMenuGuerreiro"), duration = durationChoosed())
    time.sleep(4)

# 100%
def dragInTheMenuOfHeros():
    x, y = procurarLocalizacaoDaImagemPelosEixos("guerreiro")
    pyautogui.moveTo(x, y+370)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x, y, duration = durationChoosed())
    pyautogui.mouseUp(button='left')
    time.sleep(2)

def reiniciarAPagina():
    pyautogui.keyDown("ctrl")
    pyautogui.press("f5")
    pyautogui.keyUp("ctrl")
    time.sleep(10)

def durationChoosed():
    durationChoosed = float(os.getenv("DURATION")) + round(random.uniform(0,3), 10)
    return durationChoosed

time.sleep(2)
while True:
    try:
        conectarFunc()
        toHunt()
        reiniciarAPagina()
        timeSleep = random.randint(5500, 11000)
        print("Entrando em modo de espera por: "+ str(timeSleep) + " Segundos")
        for i in range(timeSleep):
            moveRange = round(random.uniform(100,700), 10)
            moveRange2 = round(random.uniform(100,700), 10)
            pyautogui.moveTo(moveRange, moveRange2, duration = 1)
            print(i)
        
        # FAZER O MOUSE MOVER NO TEMPO DE ESPERA
        # contador = 0
        # while contador < timeSleep:
        #     time.sleep(1)
        #     if contador % 30 == 0:
        #         durationRange = random.uniform(1, 10)
        #         timeAcrescimo = durationRange // 1
        #         contador += timeAcrescimo
        #         pyautogui.moveTo(random.uniform(0, 1000), random.uniform(0, 1000), duration = durationRange)
        #     contador += 1
        # 
        # time.sleep(timeSleep)
    except BaseException as err:
        print("Ocorreu um ERRO: " + str(err))