from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = int(input("Kolik požadujete v cílové měně?"))
cena_v_korunach = prevodnik.convert(input("Zadejte požadovanou měnu"), 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach)