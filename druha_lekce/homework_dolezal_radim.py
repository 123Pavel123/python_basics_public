def oprava_sedacky_automobilu(does_it_move, should_it_move):
    if does_it_move and not should_it_move:
        return "Použij lepicí pásku."
    elif not does_it_move and should_it_move:
        return "Použij WD-40."
    else:
        return "Vše je v pořádku."

# Příklad
does_it_move = False  # Změním na True, pokud se sedačka pohybuje
should_it_move = True  # Změním na False, pokud by se sedačka nehýbe
print(oprava_sedacky_automobilu(does_it_move, should_it_move))



# Jak vykopat díru URL chart https://1drv.ms/b/s!AgHAOiSZveaNoZsuQ1xTQJqA6hrCgg?e=8Dxvku

# def vykopat_diru(mam_lopatu):
#     if mam_lopatu:
#         return "Kopu díru s lopatou."
#     else:
#         return "Používám vlastní ruce."
#
# # Příklad použití
# mam_lopatu = True  # Změň na False, pokud nemáš lopatu
# print(vykopat_diru(mam_lopatu))