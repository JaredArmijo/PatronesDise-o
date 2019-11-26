from abc import ABC, abstractmethod

class Controltv(ABC):
    @abstractmethod
    def action(self):
        pass
#--------------------------------------------------
class Play_tv(Controltv):
    def __init__(self, Controltv):
        self.controltv = Controltv

    def action(self):
        self.controltv.Play_tv()

#--------------------------------------------------
class Quitarvolumen(Controltv):
    def __init__(self, Controltv):
        self.controltv = Controltv

    def action(self):
        self.controltv.Quitarvolumen()

#--------------------------------------------------
class Cambiarcanal(Controltv):
    def __init__(self, Controltv):
        self.controltv = Controltv

    def action(self):
        self.controltv.Cambiarcanal()
#--------------------------------------------------
      
class Apagartv(Controltv):
    def __init__(self, Controltv):
        self.controltv = Controltv

    def action(self):
        self.controltv.Apagartv()
#--------------------------------------------------
class ActionMenu:
    def Play_tv(self):
        print("Enciende la tv")
        
    def Quitarvolumen(self):
        print("Pone en modo silencio")
        
    def Cambiarcanal(self):
        print("Cambia de canal")

    def Apagartv(self):
        print("Apaga la tv")
#-----------------------------------------------------
class Action:
    def __init__(self):
        self._actions = []

    def requestActions(self, Controltv):
        self._actions.append(Controltv)
        Controltv.action()

#-------------------------------------------------------
class main():
    menu = ActionMenu()
    controltv_Playtv = Play_tv(menu)
    controltv_Quittv = Quitarvolumen(menu)
    controltv_Cambc = Cambiarcanal(menu)
    controltv_Apatv = Apagartv(menu)

    act = Action()
    act.requestActions(controltv_Playtv)
    act.requestActions(controltv_Quittv)
    act.requestActions(controltv_Cambc)
    act.requestActions(controltv_Apatv)
