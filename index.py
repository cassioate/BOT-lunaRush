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
    reiniciarAPagina()
    while connect == True:
        if contador == 50:
            raise Exception("Erro ao tentar realizar o login")
        if metamaskClick == False and procurarImagemSemRetornarErro("metamask"):
            pyautogui.click(searchForHighConfidenceImage("metamask"), duration = float(os.getenv("DURATION")))
            metamaskClick = True
        if assinarClick == False and metamaskClick == True and procurarImagemSemRetornarErro("assinar"):
            pyautogui.click(searchForHighConfidenceImage("assinar"), duration = float(os.getenv("DURATION")))
            assinarClick = True
        if modoChefeClick == False and assinarClick == True and metamaskClick == True and procurarImagemSemRetornarErro("entrarNoModoCacaAoChefe"):
            pyautogui.click(searchForHighConfidenceImage("entrarNoModoCacaAoChefe"), duration = float(os.getenv("DURATION"))) 
            modoChefeClick = True
        if bossDisponivelClick == False and modoChefeClick == True and assinarClick == True and metamaskClick == True and procurarImagemSemRetornarErro("bossDisponivel"):
            pyautogui.click(searchForHighConfidenceImage("bossDisponivel"), duration = float(os.getenv("DURATION")))
            bossDisponivelClick = True
            connect = False
        contador += 1

# 100%
def searchForHighConfidenceImage(imagem):
    print('Utiliando a func searchForHighConfidenceImage: '+ imagem)
    contadorProcurarImagem = 0
    x, y = None, None
    while x == None:
        x, y = procurarLocalizacaoDaImagemPelosEixos(imagem)
        contadorProcurarImagem += 1
        if contadorProcurarImagem >= 10:
            raise Exception('Erro ao achar a imagem: ' + imagem)
    return x, y

# 100%
def procurarImagemSemRetornarErro(imagem):
    print('Utiliando a func procurarImagemSemRetornarErro: '+ imagem)
    confidence = os.getenv("CONFIDENCE")
    img = None
    contador = 0
    while img == None:
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        if img != None:
            print('Achei a imagem: ' + str(img))
            return True
        contador += 1
        print(contador)
        if contador >= 5:
            img = True
    print('Não consegui encontrar a imagem: ' + imagem)
    return False

def procurarLocalizacaoDaImagemPelosEixos(imagem):
    print('Utiliando a func procurarLocalizacaoDaImagemPelosEixos: ' + imagem)
    contador = 0
    while contador < 10:
###########################################
        if imagem == 'guerreiro' or imagem == 'x':
            if procurarImagemSemRetornarErro(imagem):
                confidence = os.getenv("CONFIDENCE")
                x, y = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
                loop = False
                if x != None:
                    return x, y
                else:
                    print('Erro nas linhas 70-71 do codigo, o X está voltando None, mesmo após ter sido bem sucedido em "procurarImagemSemRetornarErro"')
            else:
                contador += 1
############################################
        if imagem == 'abrirMenuGuerreiro' or imagem == 'fecharMenuGuerreiro':
            if procurarImagemSemRetornarErro(imagem):
                confidence = os.getenv("CONFIDENCE")
                randomVar = random.randint(1, 6)
                x, y = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
                if x != None:
                    x, y = x-(randomVar/2)
                    x, y = x+randomVar, y+randomVar
                    return x, y
                else:
                    print('Erro nas linhas 82-85 do codigo, o X está voltando None, mesmo após ter sido bem sucedido em "procurarImagemSemRetornarErro"')
            else:
                contador += 1
###########################################
        else:        
            if procurarImagemSemRetornarErro(imagem):
                confidence = os.getenv("CONFIDENCE")
                randomVarX = random.randint(1, float(os.getenv("RandomVarEixoX")))
                randomVarY = random.randint(1, float(os.getenv("RandomVarEixoY")))
                x, y = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
                if x != None:
                    x, y = x-(float(os.getenv("RandomVarEixoX"))/2), y-float(os.getenv("RandomVarEixoY"))/2
                    x, y = x+randomVarX, y+randomVarY
                    return x, y
                else:
                    print('Erro nas linhas 82-85 do codigo, o X está voltando None, mesmo após ter sido bem sucedido em "procurarImagemSemRetornarErro"')
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
            pyautogui.click(searchForHighConfidenceImage(boss+i), duration = float(os.getenv("DURATION")))
            if procurarImagemSemRetornarErro("SelecionarHeroina"):
                pyautogui.click(searchForHighConfidenceImage("SetaCinza"), duration = float(os.getenv("DURATION")))
            else:
                contador = i-1
                return contador

# 100%
def selectHero(x, y):
    pyautogui.click(x, y, duration = float(os.getenv("DURATION")))

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

# 100%
def removeTheTriple(triple):
    if triple == 0:
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(1)), duration = float(os.getenv("DURATION")))
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(2)), duration = float(os.getenv("DURATION")))
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(3)), duration = float(os.getenv("DURATION")))
    elif triple == 1:
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(4)), duration = float(os.getenv("DURATION")))
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(5)), duration = float(os.getenv("DURATION")))
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(6)), duration = float(os.getenv("DURATION")))
    elif triple == 2:
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(7)), duration = float(os.getenv("DURATION")))
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(8)), duration = float(os.getenv("DURATION")))
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(9)), duration = float(os.getenv("DURATION")))
    elif triple == 3:
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(10)), duration = float(os.getenv("DURATION")))
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(11)), duration = float(os.getenv("DURATION")))
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(12)), duration = float(os.getenv("DURATION")))
    elif triple == 4:
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(13)), duration = float(os.getenv("DURATION")))
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(14)), duration = float(os.getenv("DURATION")))
        pyautogui.click(searchForHighConfidenceImage("heroinas/heroinaRemove"+str(15)), duration = float(os.getenv("DURATION")))

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
        dragInTheMenuOfHeros()
    selectTriple(i) 
    time.sleep(1)   

# 100%
def removeVerify():
    while procurarImagemSemRetornarErro("Verificado"):
        pyautogui.click(searchForHighConfidenceImage("Verificado"), duration = float(os.getenv("DURATION")))

# 100%
def toHunt():
    for i in range(5):
        contador = 1
        selectHeroInTheMenu()
        removeAndAddTriple(i)
        closedMenuOfHeroes()
        while contador < 4:
            pyautogui.click(searchForHighConfidenceImage("cacarChefe"), duration = float(os.getenv("DURATION")))
            if procurarImagemSemRetornarErro("AvisoPrevio"):
                pyautogui.click(searchForHighConfidenceImage("x"), duration = float(os.getenv("DURATION")))
                contador = 4               
            time.sleep(5)
            if contador < 4:
                searchForResult()
            contador += 1
            
# 100%
def searchForResult():
    clickAlready = False
    loop = True
    while loop:
        loop = procurarImagemSemRetornarErro("bossLoop")
        if clickAlready == False:
            pyautogui.click(searchForHighConfidenceImage("VS"), duration = float(os.getenv("DURATION")))
            clickAlready = True
        if procurarImagemSemRetornarErro("Derrotado"):
            time.sleep(5)
            pyautogui.click(searchForHighConfidenceImage("Derrotado"), duration = float(os.getenv("DURATION")))   
        elif procurarImagemSemRetornarErro("Vitoria"):
            time.sleep(5)
            if procurarImagemSemRetornarErro("ToqueParaAbrir"):
                pyautogui.click(searchForHighConfidenceImage("ToqueParaAbrir"), duration = float(os.getenv("DURATION")))
                time.sleep(5)
                if procurarImagemSemRetornarErro("Vitoria"):
                    pyautogui.click(searchForHighConfidenceImage("Vitoria"), duration = float(os.getenv("DURATION")))
            time.sleep(10)
            if procurarImagemSemRetornarErro("bossDisponivel"):
                pyautogui.click(searchForHighConfidenceImage("bossDisponivel"), duration = float(os.getenv("DURATION")))

# 100%
def selectHeroInTheMenu():
    pyautogui.click(searchForHighConfidenceImage("abrirMenuGuerreiro"), duration = float(os.getenv("DURATION")))
    time.sleep(4)

# 100%
def closedMenuOfHeroes():
    pyautogui.click(searchForHighConfidenceImage("fecharMenuGuerreiro"), duration = float(os.getenv("DURATION")))
    time.sleep(4)

# 100%
def dragInTheMenuOfHeros():
    x, y = procurarLocalizacaoDaImagemPelosEixos("guerreiro")
    pyautogui.moveTo(x, y+370)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x, y, duration = float(os.getenv("DURATION")))
    pyautogui.mouseUp(button='left')
    time.sleep(2)

def reiniciarAPagina():
    pyautogui.keyDown("ctrl")
    pyautogui.press("f5")
    pyautogui.keyUp("ctrl")

#CONNECT
time.sleep(2)
# 100%
while True:
    try:
        conectarFunc()
        toHunt()
        reiniciarAPagina()
        timeSleep = random.randint(5500, 11000)
        print("Entrando em modo de espera por: "+ str(timeSleep) + " Segundos")
        time.sleep(timeSleep)
    except BaseException as err:
        print("Ocorreu um ERRO: " + str(err))