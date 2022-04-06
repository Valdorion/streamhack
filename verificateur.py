import requests
import time
import webbrowser

"""liste des equipes / noms en minuscule(voir l'url de leur chaîne)"""
Les_Macons_du_Cube = ["boitameu","sartar_","roi_Louis","alpzz_","ben1to"]
Lyleeloo_et_co = ["lyleeloo","benjinounours","","","xwiit"]
Les_BGs_Cubiques = ["algrios","thesirgusss","ryuuNyx","skyvex33","jimag4ming"]
Les_inde_si = ["hungergameuryt","keidenn","","goldawn_","d0udi__"]
El_vazytatin = ["valnirlifaen","tanuky_","thetitin_","","elcapette"]
Les_Chomistes = ["altiroh","","","golriver_","elstyos"]
ZxKeirei = ["jxstyann_","r3nkys","myhomoludens","blownupoff","azalaiis"]
Radeau_cubique = ["nyastra","missflamme","ji_bos","uneporteusedegateaux","vkas_le_vkassien"]
Les_Bras_Casses = ["anaximore","","","freud17450",""]
liste_equipes = [Les_Macons_du_Cube,Lyleeloo_et_co,Les_BGs_Cubiques,Les_inde_si,El_vazytatin,Les_Chomistes,ZxKeirei,Radeau_cubique,Les_Bras_Casses]
liste_equipes_a_check = []


"""nom utilisateur"""
utilisateur = str(input("Votre pseudo Twitch : ")) #identifie l'utilisateur du programme
utilisateur = utilisateur.lower()
for i in range(len(liste_equipes)):
    if utilisateur in liste_equipes[i]:
        for j in range(len(liste_equipes)):
            if j != i :
                liste_equipes_a_check.append(liste_equipes[j]) #fait une liste des membres des équipes adverses


"""regarde les viewers toutes les 1min"""
def delai(): #delai d'une minute avant de rechecker les viewers
    print("60sec avant check")
    time.sleep(30)
    print("30sec avant check")
    time.sleep(20)
    print("10sec avant check")
    time.sleep(10)


"""check de streamhack"""
def check_streamhack(liste_equipes_a_check, utilisateur):
    utilisateurs_dans_le_chat = requests.get("https://tmi.twitch.tv/group/user/"+utilisateur+"/chatters") #regarde la liste des chatters
    reponse_serveur = utilisateurs_dans_le_chat.json() #récupere la liste
    chatters = reponse_serveur['chatters'] #garde que les chatters
    viewers = chatters['viewers'] #garde que les viewers
    for i in range(len(viewers)):
        for j in range(len(liste_equipes_a_check)):
            if viewers[i] in liste_equipes_a_check[j]: #regarde si le viewer correspond à un membre d'une autre team
                alert() #lance le son d'alerte
                print(viewers[i])
                break
            elif i == (len(viewers)-1) and j == (len(liste_equipes_a_check)-1):
                print("R.A.S")



"""alerte"""
def alert():
    webbrowser.open("alert.mp3",new=0) #lance le son d'alerte


"""boucle"""
boucle = True
nombre_boucle = 1
while boucle == True: #boocle infinie
    print("=============================================================================================================")
    delai() #lance un delai
    print("=============================================================================================================")
    print("Check n°",nombre_boucle," en cours...")
    nombre_boucle += 1
    check_streamhack(liste_equipes_a_check, utilisateur) #check les viewers
