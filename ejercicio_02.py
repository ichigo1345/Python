class SantoGrial:
    def __init__(self, servants=None, clase_servant=None, master=None, ruler=None):
        self.__servants=[]
        self.__clase_servant=clase_servant
        self.__master=master
        self.__ruler=ruler
    def get_servants(self):
        return self.__servants

    def set_servants(self, servants):
        self.__servants = servants

    def get_clase_servant(self):
        return self.__clase_servant

    def set_clase_servant(self, clase_servant):
        self.__clase_servant = clase_servant

    def get_master(self):
        return self.__master

    def set_master(self, master):
        self.__master = master

    def get_ruler(self):
        return self.__ruler

    def set_ruler(self, ruler):
        self.__ruler = ruler

    def invocar_servant(self, nombre_servant, clase, master):
        invocacion = {
            "servant": nombre_servant,
            "clase": clase,
            "master": master
        }
        self.__servants.append(invocacion)
        return invocacion
    def ganar_guerra(self):
        if len(self.__servants) == 1:
            ganador = self.__servants[0]
            print(f"¡La Guerra ha finalizado! Ganador: {ganador['master']} junto a {ganador['servant']}.")
            return ganador
        elif len(self.__servants) > 1:
            print(f"La Guerra sigue activa. Quedan {len(self.__servants)} Servants en pie.")
            return None
        else:
            print("No quedan Servants en la Guerra.")
            return None
    def pedir_deseo(self, deseo):
        if len(self.__servants) == 1:
            ganador = self.__servants[0]
            print(f"\n[SANTO GRIAL]: Deseo concedido a {ganador['master']}:")
            print(f" \"{deseo}\" ")
        else:
            print(f"\n [ERROR]: El Grial no puede conceder el deseo. Aún hay {len(self.__servants)} Servants combatiendo.")

guerra = SantoGrial(ruler="Jeanne d'Arc")

guerra.invocar_servant("Artoria Pendragon", "Saber", "Kiritsugu Emiya")
guerra.invocar_servant("Gilgamesh", "Archer", "Tokiomi Tohsaka")

guerra.pedir_deseo("Salvar a la humanidad")

print("\n--- ¡Desarrollo de los combates! ---")
guerra.set_servants([
    {"servant": "Artoria Pendragon", "clase": "Saber", "master": "Kiritsugu Emiya"}
])

guerra.ganar_guerra()
guerra.pedir_deseo("Destruir el Santo Grial")