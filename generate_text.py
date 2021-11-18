from random import randint

finish_output = ""





def generate(loc):
    if loc == 1:
        items = [" лесник", " дом", " топор", " загадочное озеро", " изумрудное дерево"]
    elif loc == 2:
        items = [" глава жителей", " житель-мудрец", " мистическая бездонная яма", " центральный дом совета местных", " колодец"]
    elif loc == 3:
        items = [" король демонов", " неизвестная сопутчица", " дочь короля демонов", " тюрьма грешников", " портал в рай"]
    elif loc == 4:
        items = [" капсула, чтобы наблюдать за миром будучи духом", " посох зевса", " собрание жителей рая", " умерший знакомый", " странное сияние сверху"]
    elif loc == 5:
        items = [" главный гном шахтёр", " вагонетка с фиолетовым мешком", " брошенный авантюрист", " сломанный портал", " самовар"]

    sinonims_ryadom = [" рядком", " рядышком", " около тебя", " поблизости", " близко" " невдали", " вплотную", " вблизи", " подле", " возле тебя", " близехонько", " близешенько", " накоротке", " недалеко", " рядом", " близостно", " по соседству", " невдалеке", " невдалече"]
    sinonims_sprava = [" справа", " по правую руку от тебя"]
    spr = [" на "+str(randint(70, 90))+" градусов", " в правой части"]
    spr2 = [" с правой стороны"]
    spr3 = [" по правую сторону"]
    sinonims_sleva = [" слева", " по левую руку от тебя", " по левую сторону", " с левой стороны", " на "+str(randint(260, 290))+" градусов", " в левой части"]
    sinonims_speredy = [" спереди", " впереди", " прямо", " в самом верху карты", " в верхней части карты"]
    sinonims_szady = [" сзади", " позади"]
    sin_sz = [" за спиной", " на задах"]
    sin_sz2 = [" сзаду", " в тылу"]
    sin_sz3 = [" на задней части"]
    sinonims_daleko = [" далеко", " вдалеке"]
    sin_dal2 = [" далеконько", " на почтительном расстоянии"]
    sin_dal3 = [" неблизко", " далековато"]
    sin_dal4 = [" вдали", " далеко-далеко"]
    slovar_polochenia = [" находится", " располагается", " пребывает", " размещается"]
    second_sloy_phrases = [", подальше", ", поближе", ", в "+str(randint(10, 20))+" метрах", ", а рядом", " и", ", чуть дальше", ", чуть ближе", ", а в противоположной стороне", ", намного правее", ", намного левее", ", чуть левее", ", в "+str(randint(5, 14))+" метрах"]
    all_kit_words = [sinonims_ryadom ,sinonims_daleko, sin_dal2, sin_dal3, sin_dal4]
    all_kit_words2 = [sinonims_sprava, sinonims_sleva, spr, spr2, spr3]
    all_kit_words3 = [sinonims_speredy, sinonims_szady, sin_sz, sin_sz2, sin_sz3]
    list_random_items = [[], [], [], [], []]
    s = 0
    f = 5
    l = []
    while s < f:

        l.append("o")
        if len(l) > 50:
            break
        rand = randint(0, 4)
        rd = randint(0, 4)
        g = False
        for i in list_random_items:
            if items[rand] in i:
                g = True
                break
        if g:
            continue
        else:
        
            list_random_items[s].append(items[rand])
            if rd != 3:
                s += 1
    try:
        
        for h in list_random_items[3]:
            num = randint(0, 2)
            list_random_items[num].append(h)
        del list_random_items[3]
    except IndexError:
        None
    try:
        
        for h in list_random_items[3]:
            num = randint(0, 2)
            list_random_items[num].append(h)
        del list_random_items[3]
    except IndexError:
        None
    kl = False
    for hj in list_random_items:
        if len(hj) > 3:
            raise IndexError


    s = 0
    while s < len(list_random_items):
        if list_random_items[s] == []:
            del list_random_items[s]
        else:
            s += 1
    print(list_random_items)

    fn = ""
    g = []
    g2 = []
    g3 = []
    for i in list_random_items:
        
        if len(i) == 1:
            
            while True:
                rand_gen = randint(0, 2)
                

                if rand_gen == 0:
                    if len(all_kit_words) == 0 or len(all_kit_words2) == 0:
                        continue
                        
                    else:
                        g.append(0)
                        break
                elif rand_gen == 1:
                    if len(all_kit_words3) == 0 or len(all_kit_words2) == 0:
                        continue
                    else:
                        g.append(1)
                        break
                elif rand_gen == 2:
                    if len(all_kit_words3) == 0 or len(all_kit_words) == 0:
                        continue
                    else:
                        g.append(2)
                        break
                elif rand_gen in g:
                    continue


            if rand_gen == 0:

                words = []

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                del all_kit_words[rand_num_for_all_kit_words]

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words2[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words2[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                while len(words) != 0:
                    gj = randint(0, len(words)-1)
                    fn += words[gj]
                    del words[gj]
                fn += i[0]+"."
                del all_kit_words2[rand_num_for_all_kit_words]

            elif rand_gen == 1:

                words = []

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words2[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words2[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                del all_kit_words2[rand_num_for_all_kit_words]

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words3[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words3[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                while len(words) != 0:
                    gj = randint(0, len(words)-1)
                    fn += words[gj]
                    del words[gj]
                fn += i[0]+"."
                del all_kit_words3[rand_num_for_all_kit_words]

            elif rand_gen == 2:

                words = []

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                del all_kit_words[rand_num_for_all_kit_words]

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words3[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words3[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                while len(words) != 0:
                    gj = randint(0, len(words)-1)
                    fn += words[gj]
                    del words[gj]
                fn += i[0]+"."
                del all_kit_words3[rand_num_for_all_kit_words]

        elif len(i) == 2:

            while True:
                
                rand_gen = randint(0, 2)

                if rand_gen == 0:
                    if len(all_kit_words) == 0 or len(all_kit_words2) == 0:
                        continue
                    else:
                        g2.append(rand_gen)
                        break
                elif rand_gen == 1:
                    if len(all_kit_words3) == 0 or len(all_kit_words2) == 0:
                        continue
                    else:
                        g2.append(rand_gen)
                        break
                elif rand_gen == 2:
                    if len(all_kit_words3) == 0 or len(all_kit_words) == 0:
                        continue
                    else:
                        g2.append(rand_gen)
                        break
                elif rand_gen in g2:
                    continue
                

            if rand_gen == 0:

                words = []

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                del all_kit_words[rand_num_for_all_kit_words]

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words2[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words2[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                while len(words) != 0:
                    gj = randint(0, len(words)-1)

                    fn += words[gj]

                    del words[gj]
                
                fn += i[0]

                if i[0] == " лесник" and i[1] == " топор":
                    ford = [" , а его топор "+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)]), " со своим топором", " с топором"]
                    fn += ford[randint(0, len(ford)-1)]+"."
                elif i[0] == " топор" and i[1] == " лесник":
                    ford = [" , а сам лесник "+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)]), " его хозяин"+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)])]
                    fn += ford[randint(0, len(ford)-1)]+"."
                else:
                    r_word_sec = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[r_word_sec]+ i[1] + "."
                    del second_sloy_phrases[r_word_sec]
                del all_kit_words2[rand_num_for_all_kit_words]

            elif rand_gen == 1:

                words = []

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words2[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words2[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                del all_kit_words2[rand_num_for_all_kit_words]

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words3[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words3[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                while len(words) != 0:
                    gj = randint(0, len(words)-1)

                    fn += words[gj]

                    del words[gj]
            
                fn += i[0]
                if i[0] == " лесник" and i[1] == " топор":
                    ford = [" , а его топор "+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)]), " со своим топором", " с топором"]
                    fn += ford[randint(0, len(ford)-1)]+"."
                elif i[0] == " топор" and i[1] == " лесник":
                    ford = [" , а сам лесник "+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)]), " его хозяин"+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)])]
                    fn += ford[randint(0, len(ford)-1)]+"."
                else:
                    r_word_sec = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[r_word_sec]+ i[1] + "."
                    del second_sloy_phrases[r_word_sec]
                del all_kit_words3[rand_num_for_all_kit_words]

            elif rand_gen == 2:

                words = []

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                del all_kit_words[rand_num_for_all_kit_words]

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words3[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words3[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                while len(words) != 0:
                    gj = randint(0, len(words)-1)
                    fn += words[gj]

                    del words[gj]
                
                fn += i[0]
                if i[0] == " лесник" and i[1] == " топор":
                    ford = [" , а его топор "+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)]), " со своим топором", " с топором"]
                    fn += ford[randint(0, len(ford)-1)]
                elif i[0] == " топор" and i[1] == " лесник":
                    ford = [" , а сам лесник "+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)]), " его хозяин"+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)])]
                    fn += ford[randint(0, len(ford)-1)]
                else:
                    r_word_sec = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[r_word_sec]+ i[1] + "."
                    del second_sloy_phrases[r_word_sec]
                del all_kit_words3[rand_num_for_all_kit_words]

        elif len(i) == 3:

            while True:
                
                rand_gen = randint(0, 2)

                if rand_gen == 0:
                    if len(all_kit_words) == 0 or len(all_kit_words2) == 0:
                        continue
                    else:
                        g3.append(rand_gen)
                        break
                elif rand_gen == 1:
                    if len(all_kit_words3) == 0 or len(all_kit_words2) == 0:
                        continue
                    else:
                        g3.append(rand_gen)
                        break
                elif rand_gen == 2:
                    if len(all_kit_words3) == 0 or len(all_kit_words) == 0:
                        continue
                    else:
                        g3.append(rand_gen)
                        break
                elif rand_gen in g3:
                    continue
                

            if rand_gen == 0:

                words = []

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                del all_kit_words[rand_num_for_all_kit_words]

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words2[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words2[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                while len(words) != 0:
                    gj = randint(0, len(words)-1)

                    fn += words[gj]

                    del words[gj]
                
                fn += i[0]

                if i[0] == " лесник" and i[1] == " топор":
                    ford = [" , а его топор "+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)]), " со своим топором", " с топором"]
                    fn += ford[randint(0, len(ford)-1)]
                    l = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[l] + i[2]+"."
                    del second_sloy_phrases[l]
                elif i[0] == " топор" and i[1] == " лесник":
                    ford = [" , а сам лесник "+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)]), " его хозяин"+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)])]
                    fn += ford[randint(0, len(ford)-1)]
                    l = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[l] + i[2]+"."
                    del second_sloy_phrases[l]
                else:
                    r_word_sec = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[r_word_sec]+ i[1]
                    l = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[l] + i[2]+"."
                    del second_sloy_phrases[l]
                    del second_sloy_phrases[r_word_sec]
                del all_kit_words2[rand_num_for_all_kit_words]

            elif rand_gen == 1:

                words = []

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words2[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words2[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                del all_kit_words2[rand_num_for_all_kit_words]

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words3[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words3[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                while len(words) != 0:
                    gj = randint(0, len(words)-1)

                    fn += words[gj]

                    del words[gj]
            
                fn += i[0]
                if i[0] == " лесник" and i[1] == " топор":
                    ford = [" , а его топор "+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)]), " со своим топором", " с топором"]
                    fn += ford[randint(0, len(ford)-1)]
                    l = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[l] + i[2]+"."
                    del second_sloy_phrases[l]
                elif i[0] == " топор" and i[1] == " лесник":
                    ford = [" , а сам лесник "+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)]), " его хозяин"+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)])]
                    fn += ford[randint(0, len(ford)-1)]
                    l = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[l] + i[2]+"."
                    del second_sloy_phrases[l]
                else:
                    r_word_sec = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[r_word_sec]+ i[1] 
                    l = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[l] + i[2]+"."
                    del second_sloy_phrases[l]
                    del second_sloy_phrases[r_word_sec]
                del all_kit_words3[rand_num_for_all_kit_words]

            elif rand_gen == 2:

                words = []

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                del all_kit_words[rand_num_for_all_kit_words]

                rand_num_for_all_kit_words = 0
                rand_num_for_kit_in_words = randint(0, len(all_kit_words3[rand_num_for_all_kit_words])-1)

                words.append(all_kit_words3[rand_num_for_all_kit_words][rand_num_for_kit_in_words])
                while len(words) != 0:
                    gj = randint(0, len(words)-1)
                    fn += words[gj]

                    del words[gj]
                
                fn += i[0]
                if i[0] == " лесник" and i[1] == " топор":
                    ford = [" , а его топор "+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)]), " со своим топором", " с топором"]
                    fn += ford[randint(0, len(ford)-1)]
                    l = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[l] + i[2]+"."
                    del second_sloy_phrases[l]
                elif i[0] == " топор" and i[1] == " лесник":
                    ford = [" , а сам лесник "+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)]), " его хозяин"+str(second_sloy_phrases[randint(0, len(second_sloy_phrases)-1)])]
                    fn += ford[randint(0, len(ford)-1)]
                    l = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[l] + i[2]+"."
                    del second_sloy_phrases[l]
                else:
                    r_word_sec = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[r_word_sec]+ i[1]
                    l = randint(0, len(second_sloy_phrases)-1)
                    fn += second_sloy_phrases[l] + i[2]+"."
                    del second_sloy_phrases[l]
                    del second_sloy_phrases[r_word_sec]
                del all_kit_words3[rand_num_for_all_kit_words]
    
    print(fn)
    return fn

