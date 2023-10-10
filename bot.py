import telebot
from telebot import types
from settings import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Команды', 'ХЛТВ(в разработке...)']])
    bot.send_message(m.chat.id, 'Выберите действие', reply_markup=keyboard)

@bot.message_handler(commands=['donate']) #создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton( 'Поддержать автора', url='https://oplata.qiwi.com/form?invoiceUid=3454c4c6-c145-4bbb-bbe1-90bcd51a4f15')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и поддержи автора)".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message(message):
    if message.text == 'Команды':
        keyboardgostart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Giants', 'Titan', 'CYBERSHOKE', 'CYBERSHOKE Lite', 'Liquid', 'Cloud9', 'FaZe', 'Insilio', 'G2', 'Vitality', 'Spirit', 'ENCE', 'Astralis', 'Heroic', 'FURIA', 'GamerLegion', 'Evil Geniuses', 'Natus Vincere', 'Into the Breach', 'Ninjas in Pyjamas', 'The Prodigies', '9z', 'BetBoom', 'Falcons', 'OG', 'MOUZ', 'VP', 'Gambit', 'Bad News Eagles', 'Legacy', 'Monte', 'FORZE', 'fnatic', 'Envy', 'Grayhound', 'Apeks', 'EYEBALLERS', 'Aurora', 'TSM', 'TheMongolZ', 'North', 'CYBER', 'B8', '100 Thieves', '9 Pandas', 'Karmine Corp', '500', 'TYLOO', '1WIN', 'SAW', 'VP.Prodigy', 'M80', '9INE', 'HOTU', 'Complexity', 'BIG', 'paiN', 'ECSTATIC', 'MIBR', 'Imperial', 'Movistar Riders', 'AVANGAR', 'HEET', 'Young Ninjas', 'Dignitas', 'Forward', 'ESPADA', 'Nemiga', 'VERTEX', 'sYnck', 'Luminosity', 'IKLA', 'Copenhagen Flames', 'LDLC', 'Slow Brain Good Brain', 'premium', 'Reason', 'Websterz', 'Rare Atom', 'IHC', 'Betera', 'SK', 'HellRaisers', 'HAVU', 'iBUYPOWER', 'The Imperial', 'Eternal Fire', 'Space', 'GODSENT', 'SENTINELS', 'VP Eagles', '500 Academy', 'Gaimin Gladiators', 'Liquid Academy', 'ARCRED', 'xDDDD', 'OneTrickPonies', 'TSM Legion', 'TSM Celine', 'Spirit Youth', 'Imperial Academy', 'FORZA BETERA']])
        bot.send_message(message.chat.id, 'Выберите команду', reply_markup=keyboardgostart)
    elif message.text == 'ХЛТВ(в разработке...)':
        bot.send_message(message.chat.id, 'Тут пока ничего нет')
    elif message.text == 'Giants':
        bot.send_message(message.chat.id, 'Giants: \n hades, danistzz, Sirah, susp, ewjerkz, kAlash (инактив) \n Бюджет:305.500$ \n CEO:@brainzorr')
    elif message.text == 'Titan':
        bot.send_message(message.chat.id, 'Titan: \n ScreaM, KQLY, GeT_RiGhT, f0rest, Ex6TenZ \n Бюджет:920.000$ \n CEO:@ShelbyHell')
    elif message.text == 'CYBERSHOKE':
        bot.send_message(message.chat.id, 'CYBERSHOKE: \n flamie, fen2k, sh1nejezzz, FenomeN, HObbit, Flash_1 (тренер) \n Бюджет:835.000$ \n CEO:@lilkeksikboy')
    elif message.text == 'CYBERSHOKE Lite':
        bot.send_message(message.chat.id, 'CYBERSHOKE Lite: \n Magnojez, FL4MUS, Iceberg, Nevar (тренер) \n Бюджет:835.000$ \n CEO:@lilkeksikboy')
    elif message.text == 'Liquid':
        bot.send_message(message.chat.id, 'Liquid: \n YEKINDAR, flameZ, degster, Twistzz, d1Ledez, innersh1ne (тренер) \n Бюджет:861.000$ \n CEO:@dyrananixe')
    elif message.text == 'Cloud9':
        bot.send_message(message.chat.id, 'Cloud9: \n Perfecto, Ax1Le, sh1ro, electroNic, nafany, groove (тренер) \n Бюджет:3.541.750$ \n CEO:@MedHop')
    elif message.text == 'FaZe':
        bot.send_message(message.chat.id, 'FaZe: \n rain, broky, karrigan, ropz, BOROS, RobbaN (тренер) \n Бюджет:2.294.000$ \n CEO:@ran1l4ikkk')
    elif message.text == 'Insilio':
        bot.send_message(message.chat.id, 'Insilio: \n k4sl-, Polt, Xant3r, DaDte, svyat, fabi (тренер) \n Бюджет:2.292.000$ \n CEO:@Kibokit')
    elif message.text == 'G2':
        bot.send_message(message.chat.id, 'G2: \n huNter-, NiKo, m0NESY, HooXi, jks, Swani (тренер) \n Бюджет:1.783.000$ \n CEO:@dimitriygod')
    elif message.text == 'Vitality':
        bot.send_message(message.chat.id, 'Vitality: \n apEX, ZywOo, Spinx, NAF, REZ, Pipw, zonic (тренер) \n Бюджет:2.782.000$ \n CEO:@coldhesuslawren')
    elif message.text == 'Spirit':
        bot.send_message(message.chat.id, 'Spirit: \n chopper, magixx, donk, zont1x, ArtFr0st, hally (тренер) \n Бюджет:1.817.000$ \n CEO:@emokuash')
    elif message.text == 'ENCE':
        bot.send_message(message.chat.id, 'ENCE: \n dycha, Jerppa, Alxc, mantuu, Patsi, sAw (тренер) \n Бюджет:1.872.500$ \n CEO:@W1el0')
    elif message.text == 'Astralis':
        bot.send_message(message.chat.id, 'Astralis: \n device, Altekz, Peppzor, Bubzkji, Snappi, Magisk, casle (тренер) \n Бюджет:2.938.000$ \n CEO:@Ob1ivi0n')
    elif message.text == 'Heroic':
        bot.send_message(message.chat.id, 'Heroic: \n Buzz, mhL, NBK-, Raijin, kane, Xizt (тренер) \n Бюджет:3.199.000$ \n CEO: сео пока нет')
    elif message.text == 'FURIA':
        bot.send_message(message.chat.id, 'FURIA: \n yuurih, chelo, VINI, skuulz, HEN1, guerri (тренер) \n Бюджет:3.934.000$ \n CEO:@withmusicforever')
    elif message.text == 'GamerLegion':
        bot.send_message(message.chat.id, 'GamerLegion: \n volt, hyped, Fessor, faveN, DickStacy (тренер) \n Бюджет:1.688.500$ \n CEO:@G2huNter')
    elif message.text == 'Evil Geniuses':
        bot.send_message(message.chat.id, 'Evil Geniuses: \n autimatic, junior, bLitz, JOTA, SIXER, maLeK  (тренер) \n Бюджет:1.529.501$ \n CEO:@sbushukaevas')
    elif message.text == 'Natus Vincere':
        bot.send_message(message.chat.id, 'Natus Vincere: \n s1mple, b1t, Aleksib, jL, NickelBack, B1ad3 (тренер) \n Бюджет:2.539.500$ \n CEO:@nani2271 или @Beinggos')
    elif message.text == 'Into the Breach':
        bot.send_message(message.chat.id, 'Into the Breach: \n CRUC1AL, rallen, CYPHER, Thomas, NEOFRAG,  Juve (тренер) \n Бюджет:1.799.500$ \n CEO:@ev3ley')
    elif message.text == 'Ninjas in Pyjamas':
        bot.send_message(message.chat.id, 'Ninjas in Pyjamas: \n Marix, Liazz, podi, zehN, DeathZz, djL (тренер) \n Бюджет:2.730.000$ \n CEO:@SemataryFun')
    elif message.text == 'The Prodigies':
        bot.send_message(message.chat.id, 'The Prodigies: \n fNk, keen, shield, krii, P4TriCK, Independent (тренер) \n Бюджет:2.260.250$ \n CEO:@eliassillaots')
    elif message.text == 'Falcons':
        bot.send_message(message.chat.id, 'Falcons: \n syrsoN, gla1ve, n0rb3r7, stavn, riskyb0b, HUNDEN (тренер) \n Бюджет:1.501.000$ \n CEO:@netetonegustov')
    elif message.text == '9z':
        bot.send_message(message.chat.id, '9z: \n max, dgt, buda, try, leo_drk, tge (тренер) \n Бюджет:2.490.750$ \n CEO:@Daiskeee')
    elif message.text == 'BetBoom':
        bot.send_message(message.chat.id, 'BetBoom: \n interz, zorte, fear, Norwi, RuFire (тренер) \n Бюджет:1.408.500$ \n CEO:@kawoshitk')
    elif message.text == 'OG':
        bot.send_message(message.chat.id, 'OG: \n nexa, F1KU, FASHR, k1to, regali, ruggah (тренер) \n Бюджет:2.047.500$ \n CEO:https://t.me/c/1967671250/18961')
    elif message.text == 'MOUZ':
        bot.send_message(message.chat.id, 'MOUZ: \n frozen, siuhy, Bymas, headtr1ck, KSCERATO, sycrone (тренер) \n Бюджет:1.975.250$ \n CEO:@vamouz')
    elif message.text == 'VP':
        bot.send_message(message.chat.id, 'VP: \n fame, FL1T, Jame, Qikert, KENSI, dastan (тренер) \n Бюджет:3.067.000$ \n CEO:@griskard')
    elif message.text == 'Gambit':
        bot.send_message(message.chat.id, 'Gambit: \n FinigaN, fostar,  KaiR0N-, s1ren, r1nkle \n Бюджет:705.000$ \n CEO:@TrippieSid3') 
    elif message.text == 'Bad News Eagles':
        bot.send_message(message.chat.id, 'Bad News Eagles: \n gxx-, juanflatroo, sinnopsyy, EliGE, roeJ, Devilwalk (тренер) \n Бюджет:960.000$ \n CEO:@theworstinmeee')
    elif message.text == 'Legacy':
        bot.send_message(message.chat.id, 'Legacy: \n coldzera, dumau, latto, nqz, NEKIZ, chucky (тренер), TACO (инактив), n9xtz (инактив) \n Бюджет:1.245.000$ \n CEO:?')
    elif message.text == 'Monte':
        bot.send_message(message.chat.id, 'Monte: \n sdy, acoR, k0nfig, iM, jR, NertZ, lmbt (тренер) \n Бюджет:2.675.000$ \n CEO:@Zel1xo')
    elif message.text == 'FORZE':
        bot.send_message(message.chat.id, 'FORZE: \n Krad, El1an, DemQQ, kRaSnaL, shalfey, Fierce (тренер) \n Бюджет:970.000$ \n CEO:@mamenkoalex')
    elif message.text == 'fnatic':
        bot.send_message(message.chat.id, 'fnatic: \n KRIMZ, mezii, afro, TeSeS, Jimpphat, jabbi, keita (тренер) \n Бюджет:-1.265.000$ \n CEO:@clonnx')
    elif message.text == 'Envy':
        bot.send_message(message.chat.id, 'Envy: \n alpha, blameF, w0nderful, stanislaw (тренер) \n Бюджет:1.366.000$ \n CEO:@angelzzzcs')
    elif message.text == 'Grayhound':
        bot.send_message(message.chat.id, 'Grayhound: \n INS, Vexite, CLASIA, sterling, ADDICT, Kingfisher (тренер), aliStair (инактив) \n Бюджет:1.600.000$ \n CEO:@alistairofficial')
    elif message.text == 'Apeks':
        bot.send_message(message.chat.id, 'Apeks: \n STYKO, jkaem, CacaNito, dexter, oskar, kuben (тренер) \n Бюджет:1.040.000$ \n CEO:@mxwrld')
    elif message.text == 'EYEBALLERS':
        bot.send_message(message.chat.id, 'EYEBALLERS: \n flusha, JW, Sapec, SHiNE, b0RUP, slap (тренер) \n Бюджет:1.300.000$ \n CEO:@Tasim4ik')
    elif message.text == 'Aurora':
        bot.send_message(message.chat.id, 'Aurora: \n Lack1, SELLTER, lattykk, NEO, Snax \n Бюджет:1.650.000$ \n CEO:@dobriy_lis')
    elif message.text == 'TSM':
        bot.send_message(message.chat.id, 'TSM: \n Kjaerbye, Farlig, niko, tiziaN, swag, CyberFocus (тренер), DavCost (инактив) \n Бюджет:116.000$ \n CEO:https://t.me/c/1967671250/18961')
    elif message.text == 'TheMongolZ':
        bot.send_message(message.chat.id, 'TheMongolZ: \n hasteka, Techno, mzinho, yAmi, refrezh, CeRq, maaRaa (тренер) \n Бюджет:855.000$ \n CEO:@Phililu')
    elif message.text == 'North':
        bot.send_message(message.chat.id, 'North: \n Staehr, Zyphon, cadiaN, sjuush, AMANEK (тренер) \n Бюджет:515.000$ \n CEO:@Cringecorexx')
    elif message.text == 'CYBER':
        bot.send_message(message.chat.id, 'CYBER: \n V0R4yn, SoTFiK, N1ghtMan, anscory, sinkie \n Бюджет:1.265.000$ \n CEO:@F4mmyx')
    elif message.text == 'B8':
        bot.send_message(message.chat.id, 'B8: \n cptkurtka023, amster, OWNER, npl, isk, maddened (тренер) \n Бюджет:1.720.000$ \n CEO:https://t.me/c/1967671250/18961')
    elif message.text == '100 Thieves':
        bot.send_message(message.chat.id, '100 Thieves: \n TenZ, oBo, nitrO, Brehze, floppy, zews (тренер) \n Бюджет:1.154.999$ \n CEO:@jxn95')
    elif message.text == '9 Pandas':
        bot.send_message(message.chat.id, '9 Pandas: \n hampus, Jerry, oSee, isak, niki1, es3tag, phzy, Xoma (тренер) \n Бюджет:500.000$ \n CEO:@hikarry')
    elif message.text == 'Karmine Corp':
        bot.send_message(message.chat.id, 'Karmine Corp: \n mwlky, nilo, Grim, REDSTAR, Lekr0, XTQZZZ (тренер) \n Бюджет:1.290.000$ \n CEO:@isareich')
    elif message.text == '500':
        bot.send_message(message.chat.id, '500: \n dennyslaw, Patrick, KalubeR, Pumpkin66, dav1g, SolEk, Grashog (тренер) \n Бюджет:1.191.000$ \n CEO:@fookernya')
    elif message.text == 'TYLOO':
        bot.send_message(message.chat.id, 'TYLOO: \n emi, Freeman, SLOWLY, sk0R, ROGA, LETN1 (тренер) \n Бюджет:1.385.000$ \n CEO:@danisshayh')
    elif message.text == '1WIN':
        bot.send_message(message.chat.id, '1WIN: \n deko, dav1deuS, malbsMd, bodyy, MICHU, hooch (тренер) \n Бюджет:1.770.000$ \n CEO:@matez1k')
    elif message.text == 'SAW':
        bot.send_message(message.chat.id, 'SAW: \n MUTiRiS, roman, arrozdoce, Sonic, Lucky, NABOWOW (тренер) \n Бюджет:1.545.000$ \n CEO:@progaaaa')
    elif message.text == 'VP.Prodigy':
        bot.send_message(message.chat.id, 'VP.Prodigy: \n Sowalio, KusMe, Something, shady, xdENiSZERA \n Бюджет:1.410.000$ \n CEO:@H1llaryyy')
    elif message.text == 'M80':
        bot.send_message(message.chat.id, 'M80: \n Swisher, rech, SLIGHT, Lake, maNkz, dephh (тренер), WolfY (инактив) \n Бюджет:807.500$ \n CEO:@regit99')
    elif message.text == '9INE':
        bot.send_message(message.chat.id, '9INE: \n mynio, Goofy, KEi, Kylar, SaMey, nawrot (тренер) \n Бюджет:1.580.000$ \n CEO:@aquadebil20202021')
    elif message.text == 'HOTU':
        bot.send_message(message.chat.id, 'HOTU: \n nitzie, mizu, gokushima, swiftsteel, casE \n Бюджет:1.340.000$ \n CEO:@CS_Mask1ch')
    elif message.text == 'Complexity':
        bot.send_message(message.chat.id, 'Complexity: \n dennis, hallzerk, cajunb, sstiNiX, valde, T.c (тренер) \n Бюджет:1.370.000$ \n CEO:@unkko')
    elif message.text == 'BIG':
        bot.send_message(message.chat.id, 'BIG: \n tabseN, Krimbo, s1n, kyuubii, kennyS, gob b (тренер) \n Бюджет:1.859.000$ \n CEO:@S1riUzz')
    elif message.text == 'paiN':
        bot.send_message(message.chat.id, 'paiN: \n biguzera, lux, cass1n, JT, Sico, boltz, rikz (тренер) \n Бюджет:1.163.000$ \n CEO:@lodvego')
    elif message.text == 'ECSTATIC':
        bot.send_message(message.chat.id, 'ECSTATIC: \n Nodios, kraghen, Rainwaker, Martinez \n Бюджет:2.071.298$ \n CEO:@SanaevD')
    elif message.text == 'MIBR':
        bot.send_message(message.chat.id, 'MIBR: \n exit, saffee, drop, brnz4n, insani, BIT (тренер) \n Бюджет:1.220.000$ \n CEO:@mn1ray')
    elif message.text == 'Imperial':
        bot.send_message(message.chat.id, 'Imperial: \n venomzera, kauez, FalleN, Azakk (тренер) \n Бюджет:1.174.000$ \n CEO:@ez_4_ence')
    elif message.text == 'Movistar Riders':
        bot.send_message(message.chat.id, 'Movistar Riders: \n alex, mopoz, Patti, Kristou, Maden, bladE (тренер) \n Бюджет:1.145.000$ \n CEO:@fERE43')
    elif message.text == 'AVANGAR':
        bot.send_message(message.chat.id, 'AVANGAR: \n ICY, BLVCKM4GIC, def1zer, AcilioN, Cabbi \n Бюджет:1.028.202$ \n CEO:@Arikyrinkyto')
    elif message.text == 'HEET':
        bot.send_message(message.chat.id, 'HEET: \n Maka, Djoko, ritchiEE, shox, Nivera, HexT, Ex3rcice (инактив) \n Бюджет:1.706.500$ \n CEO:@Vedothy')
    elif message.text == 'Young Ninjas':
        bot.send_message(message.chat.id, 'Young Ninjas: \n lauNX, mir, Brollan, nicoodoz, arT, kyxsan \n Бюджет:152.000$ \n CEO:@sizhn')
    elif message.text == 'Forward':
        bot.send_message(message.chat.id, 'Forward: \n mou, ProbLeM, JIaYm, xiELO, Dosia, TsaGa (тренер) \n Бюджет:1.715.000$ \n CEO:@ktoto30001')
    elif message.text == 'ESPADA':
        bot.send_message(message.chat.id, 'ESPADA: \n speed4k, cheerful, waterfaLLZ, rommi, tr3vl \n Бюджет:1.230.000$ \n CEO:@prodoter777')
    elif message.text == 'Nemiga':
        bot.send_message(message.chat.id, 'Nemiga: \n Jyo, xsepower, Synyx, glowiing, X5G7V, keep3r (тренер) \n Бюджет:1.045.000$ \n CEO:@gocraaaazy')
    elif message.text == 'VERTEX':
        bot.send_message(message.chat.id, 'VERTEX: \n ISSAA, maxster, felps, adamb, eraa, ANGE1, nukkye, seized, Kingfisher (тренер), BRACE (инактив), hazr (инактив) \n Бюджет:955.000$ \n CEO:@lil_mephedronochka')
    elif message.text == 'sYnck':
        bot.send_message(message.chat.id, 'sYnck: \n fejtZ, Wahtzzz, eku, aNdu, consss, Shockwave (тренер) \n Бюджет:1.285.000$ \n CEO:@v1ad1sov')
    elif message.text == 'Luminosity':
        bot.send_message(message.chat.id, 'Luminosity: \n RuStY, spooke, 910, Starry, bobeksde, mimi, NEO (тренер) \n Бюджет:1.010.000$ \n CEO:@MARSIKlmao')
    elif message.text == 'IKLA':
        bot.send_message(message.chat.id, 'IKLA: \n torzsi, Kvem, ALEX, prosus, Keoz, WOLF (тренер) \n Бюджет:1.105.000$ \n CEO:@Jlaytahaha')
    elif message.text == 'Copenhagen Flames':
        bot.send_message(message.chat.id, 'Copenhagen Flames: \n raalz, AZR, story, buster, xertioN, cube (тренер) \n Бюджет:289.000$ \n CEO:@Rod4lf')
    elif message.text == 'LDLC':
        bot.send_message(message.chat.id, 'LDLC: \n kioShiMa, unshaark, Graviti, Brooxsy, Diviiii, Happy (тренер) \n Бюджет:1.010.000$ \n CEO:@Mot99999')
    elif message.text == 'Slow Brain Good Brain':
        bot.send_message(message.chat.id, 'Slow Brain Good Brain: \n salazar, TNDKingg, JUST, friberg, Queenix \n Бюджет:335.000$ \n CEO: не нашел')
    elif message.text == 'premium':
        bot.send_message(message.chat.id, 'premium: \n fANDER, Delight, anastaze, airscape, Aunkere \n Бюджет:1.010.000$ \n CEO:@sonofvertigo')
    elif message.text == 'Reason':
        bot.send_message(message.chat.id, 'Reason: \n SENER1, rigoN, Python, r3salt, pz, Coastal (тренер), Danejoris (инактив), walker (инактив), grape (инактив), JDubs (инактив), BeaKie (инактив) \n Бюджет:315.000$ \n CEO:@sheshsound (я автор бота кстати)')
    elif message.text == 'Websterz':
        bot.send_message(message.chat.id, 'Websterz: \n mds, boX, sugaR, znxxX, tn1r \n Бюджет:1.060.000$ \n CEO:@OCTEV')
    elif message.text == 'iBUYPOWER':
        bot.send_message(message.chat.id, 'iBUYPOWER: \n Zeus, BnTeT, pashaBiceps, Forester, Boombl4, smooya \n Бюджет:135.000$ \n CEO:https://t.me/c/1967671250/18961')
    elif message.text == 'Rare Atom':
        bot.send_message(message.chat.id, 'Rare Atom: \n advent, kaze, JamYoung, Mercury, Moseyuh, k4Mi (тренер) \n Бюджет:1.010.000$ \n CEO:@Ner0137')
    elif message.text == 'IHC':
        bot.send_message(message.chat.id, 'IHC: \n facecrack, Gospadarov, ANNIHILATION, Bart4k, forsaken, zoneR (тренер), H4SAN4TOR (инактив) \n Бюджет:710.000$ \n CEO:@geniusguy43')
    elif message.text == 'Betera':
        bot.send_message(message.chat.id, 'Betera: \n lollipop21k, MaSvAl, Ganginho, sad, nifee, d1maskin (тренер) \n Бюджет:833.000$ \n CEO:@MrDaudfair')
    elif message.text == 'SK':
        bot.send_message(message.chat.id, 'SK: \n fer, fnx, sergej, kNgV-, tarik, draken, xicoz \n Бюджет:1.085.000$ \n CEO:@jongly')
    elif message.text == 'HellRaisers':
        bot.send_message(message.chat.id, 'HellRaisers: \n Dimaoneshot, Porya, AdreN, TRAVIS, SunPayus, F_1N (тренер) \n Бюджет:410.000$ \n CEO:@Sin_Murlicka')
    elif message.text == 'HAVU':
        bot.send_message(message.chat.id, 'HAVU: \n sLowi, uli, ottoNd, Airax, Banjo \n Бюджет:1.010.000$ \n CEO:@r3hubb')
    elif message.text == 'The Imperial':
        bot.send_message(message.chat.id, 'The Imperial: \n mn, mN, mn, mn, rmn \n Бюджет:1.010.000$ \n CEO:не нашел')
    elif message.text == 'Eternal Fire':
        bot.send_message(message.chat.id, 'Eternal Fire: \n XANTARES, Calyx, MAJ3R, woxic, Wicadia, Fabre (тренер), imoRR (инактив) \n Бюджет:1.035.000$ \n CEO:не нашел')
    elif message.text == 'Space':
        bot.send_message(message.chat.id, 'Space: \n enzero, Vert, leri511, fozil, TruNIQ \n Бюджет:1.060.000$ \n CEO:не нашел')
    elif message.text == 'GODSENT':
        bot.send_message(message.chat.id, 'GODSENT: \n Plopski, ztr, joel, Ro1f, nawwk, Golden (тренер), hype (инактив) \n Бюджет:535.000$ \n CEO:не нашел')
    elif message.text == 'SENTINELS':
        bot.send_message(message.chat.id, 'SENTINELS: \n MoDo, nAts, ravenlot, neaLaN, Xeppaa, iDISBALANCE, S0tF1k (тренер) \n Бюджет:575.000$ \n CEO:не нашел')
    elif message.text == 'VP Eagles':
        bot.send_message(message.chat.id, 'VP Eagles: \n SZPERO, ultimate, tudsoN, asran, blacktear5 \n Бюджет:3.067.000$ \n CEO:@griskard')
    elif message.text == '500 Academy':
        bot.send_message(message.chat.id, '500 Academy: \n Danejoris, walker, grape, JDubs, BeaKie, Jeorge \n Бюджет:1.191.000$ \n CEO:@fookernya')
    elif message.text == 'Gaimin Gladiators':
        bot.send_message(message.chat.id, 'Gaimin Gladiators: \n d4rty, kiR, D0cC, br0, JDC, deffo (инактив), BLACKEAGLE (инактив) \n Бюджет:-35.000$ \n CEO:не нашел')
    elif message.text == 'ARCRED':
        bot.send_message(message.chat.id, 'ARCRED: \n Ryujin, hurstlxd, shg, icyvl0ne, frok, Woro2k, iksou (тренер), DSSj (инактив), hurstlxd (инактив), 1NVISIBLEE (инактив) \n Бюджет:230.000$ \n CEO:не нашел')
    elif message.text == 'Liquid Academy':
        bot.send_message(message.chat.id, 'Liquid Academy: \n baz, sFade8, Byrmilov, Malkiss, Topa, Kyivstoner (тренер), Lil Morty (инактив), Zinchenko (инактив), Konoplyanka (инактив) \n Бюджет:861.000$ \n CEO:@dyrananixe')
    elif message.text == 'xDDDD':
        bot.send_message(message.chat.id, 'xDDDD: \n fnyekes, lom1k, God9y, bl1x1, Twiksar, DarkS1de (тренер), hiji (инактив), hutji (инактив), Koshak (инактив) \n Бюджет:935.000$ \n CEO:не нашел')
    elif message.text == 'OneTrickPonies':
        bot.send_message(message.chat.id, 'OneTrickPonies: \n jayzaR, Ludwig, debo, virree, avid \n Бюджет:1.035.000$ \n CEO:не нашел')
    elif message.text == 'TSM Legion':
        bot.send_message(message.chat.id, 'TSM Legion: \n Flarich, Skadoodle, Nifty, shushan, hemzk9 \n Бюджет:116.000$ \n CEO:https://t.me/c/1967671250/18961')
    elif message.text == 'TSM Celine':
        bot.send_message(message.chat.id, 'TSM Celine: \n pauliiee, Nessa, Tynka, kezziwow, Minnie \n Бюджет:116.000$ \n CEO:https://t.me/c/1967671250/18961')
    elif message.text == 'Spirit Youth':
        bot.send_message(message.chat.id, 'Spirit Youth: \n froz1k, Get_Jeka, sorrow, UNBR0KEN, wetfy \n Бюджет:1.817.000$ \n CEO:@emokuash')
    elif message.text == 'FORZA BETERA':
        bot.send_message(message.chat.id, 'FORZA BETERA: \n hAdji, JACKZ, EspiranTo, malta, Infinite \n Бюджет:833.000$ \n CEO:@MrDaudfair')
    elif message.text == 'Imperial Academy':
        bot.send_message(message.chat.id, 'Imperial Academy: \n LNZ, entz, easy, xfl0ud, SLY \n Бюджет:1.174.000$ \n CEO:@ez_4_ence')
    
    

bot.polling(none_stop=True)
