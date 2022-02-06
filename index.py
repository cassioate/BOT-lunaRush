import pyautogui
import time
import dotenv
import os

dotenv.load_dotenv()

def conectarFunc():
    connect = True
    pyautogui.keyDown("ctrl")
    pyautogui.press("f5")
    pyautogui.keyUp("ctrl")
    while connect == True:
        if procurarImagemSemRetornarErro("metamask"):
            pyautogui.click(searchForHighConfidenceImage("metamask"), duration = float(os.getenv("DURATION")))
        if procurarImagemSemRetornarErro("assinar"):
            pyautogui.click(searchForHighConfidenceImage("assinar"), duration = float(os.getenv("DURATION")))
        if procurarImagemSemRetornarErro("entrarNoModoCacaAoChefe"):
            pyautogui.click(searchForHighConfidenceImage("entrarNoModoCacaAoChefe"), duration = float(os.getenv("DURATION"))) 
        if procurarImagemSemRetornarErro("1de10"):
            pyautogui.click(searchForHighConfidenceImage("1de10"), duration = float(os.getenv("DURATION")))
            connect = False

def searchForHighConfidenceImage(imagem):
    print("Procurando imagem em searchForHighConfidenceImage: "+ imagem)
    contadorProcurarImagem = 0
    img = None
    confidence = os.getenv("CONFIDENCE")
    loading = True
    while img == None:
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        contadorProcurarImagem += 1
        if contadorProcurarImagem >= 200:
            raise Exception('Erro ao achar a imagem: ' + imagem)
    return img

def procurarImagemSemRetornarErro(imagem):
    loop = True
    contador = 0
    time.sleep(3)
    confidence = os.getenv("CONFIDENCE")
    print("Procurando imagem em procurarImagemSemRetornarErro: "+ imagem)
    img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
    print(img)
    if img != None:
        return True
    return False

def procurarLocalizacaoDaImagemPelosEixos(imagem):
    if procurarImagemSemRetornarErro(imagem):
        confidence = os.getenv("CONFIDENCE")
        x, y = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        return x, y
    else:
        return None, None

# LUNA RUSH
#####################################################

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

def selectHero(x, y):
    pyautogui.click(x, y, duration = float(os.getenv("DURATION")))

def selectTriple(triple):
    x, y = procurarLocalizacaoDaImagemPelosEixos("guerreiro")
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

def removeAndAddTriple(i):
    if i == 0:
        dragInTheMenuOfHeros()
        if procurarImagemSemRetornarErro("heroinas/heroinaRemove15"):
            removeTheTriple(4)
            closedMenuOfHeroes()
            selectHeroInTheMenu()
        else:
            closedMenuOfHeroes()
            selectHeroInTheMenu()
        #REMOVENDO TRIPLA ANTERIOR
    if i > 0:
        removeTheTriple(i-1)
    if i == 4:
        dragInTheMenuOfHeros()
    selectTriple(i) 
    time.sleep(1)   

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
            if procurarImagemSemRetornarErro("1de10"):
                pyautogui.click(searchForHighConfidenceImage("1de10"), duration = float(os.getenv("DURATION")))


def selectHeroInTheMenu():
    pyautogui.click(searchForHighConfidenceImage("abrirMenuGuerreiro"), duration = float(os.getenv("DURATION")))
    time.sleep(4)

def closedMenuOfHeroes():
    pyautogui.click(searchForHighConfidenceImage("fecharMenuGuerreiro"), duration = float(os.getenv("DURATION")))
    time.sleep(4)

def dragInTheMenuOfHeros():
    x, y = procurarLocalizacaoDaImagemPelosEixos("guerreiro")
    pyautogui.moveTo(x, y+370)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x, y, duration = float(os.getenv("DURATION")))
    pyautogui.mouseUp(button='left')
    time.sleep(2)

#CONNECT
time.sleep(2)
while True:
    try:
        conectarFunc()
        toHunt()
        time.sleep(5500)
    except BaseException as err:
        print("Ocorreu um ERRO:")
        print(err)