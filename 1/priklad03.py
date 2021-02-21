volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]}

hodina_meetingu = int(input("Napište číslo hodiny mezi 9 a 12, na kterou si chcete zamluvit místnost:"))
if hodina_meetingu in volnePokoje:
    print(len(volnePokoje[hodina_meetingu]))