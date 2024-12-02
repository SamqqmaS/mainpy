dict = {
            "BACANO": "Referirse a algo como bueno",
            "PARCHADO": "Relajado",
            "LOCHA": "Hacer pereza",
            "GUACHAFITA": "Recocha",
            "CAMELLAR": "Referirse al trabajo",
            "VAINA": "Una Palabra usada para designar cualquier cosa u objeto del cual no recuerdas el nombre",
            "CAER": "Palabra para describir cuando alguien está conquistando a uno persona. También significa llegar a un lugar",
            "CHIMBO":"Se refiere a algo que es de mala calidad, una réplica o algo falso."
            }
palabra = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if palabra in dict.keys():
    print(palabra, "es" , dict[palabra] )
  
else:
    print("La palabra no se encuentra")
