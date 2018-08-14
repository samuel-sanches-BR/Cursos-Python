import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura
    a ser comparada com os textos fornecidos'''

    print("Bem-vindo ao detector automático de COH-PIAH.\n\n")
    
    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    as_a = [wal, ttr, hlr, sal, sac, pal]

    textos = le_textos()
    compara = []
    
    for texto in textos:
        as_b = calcula_assinatura(texto)
        compara.append(compara_assinatura(as_a, as_b))
        
    print("\nO autor do texto",avalia_textos(textos, compara),"está infectado com COH-PIAH")
    return avalia_textos(textos, compara)

###################################################################################

def le_textos():
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair): ")
    while (texto):
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

###################################################################################

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''

    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

###################################################################################

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    frases = re.split(r'[,:;.]+', sentenca)

    if frases[-1] == '':
        del frases[-1]
    
    return frases

###################################################################################

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''

    return frase.split()

###################################################################################

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que
    aparecem uma unica vez'''

    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

###################################################################################            

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras
    diferentes utilizadas'''

    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

###################################################################################

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de
    similaridade nas assinaturas.'''

    a = 0
    b = 0
    somaAB = 0
    
    while (a < 6 and b < 6):
        somaAB = somaAB + abs((as_a[a] - as_b[b])) / 6
        a += 1
        b += 1
    
    return somaAB

###################################################################################

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    '''calcula a qtd de caracteres'''
    texto_sem_pontua1 = texto
    pontuacao = '.!?,;:'
    for i in range(0, len(pontuacao)):
        texto_sem_pontua1 = texto_sem_pontua1.replace(pontuacao[i]," ")
       
    
    n_Caract = 0
    for x in texto_sem_pontua1:
        if (x == " " or x == "." or x == "," or x == ";" or x == ":" or x == "!" or x == "?"
            or x == ' " ' '''or x == "[" or x == "]" or x == "(" or x == ")"'''):
            pass
        else:
            n_Caract += 1

    '''divide o TEXTO em palavras e conta as palavras no len(----)'''
    n_Tot_palavras = texto_sem_pontua1.split()
    taman_Medio = n_Caract / len(n_Tot_palavras)

    '''for remove as vírgulas, pontos para que a funçao nao confunda coisas do tp "comer" e
    "comer,"chama função para calcular palavras diferentes e divide pelo total de palavras'''
    n_pala_dif = n_palavras_diferentes(separa_palavras(texto_sem_pontua1))
    rel_Typ_Tok = n_pala_dif / len(n_Tot_palavras)

    '''chama func para calc palavras unicas e divide pelo total de palavras'''
    n_pala_uni = n_palavras_unicas(separa_palavras(texto_sem_pontua1))
    rel_Hapax_lego = n_pala_uni / len(n_Tot_palavras)

    '''chama função para separar texto em sentenças e faz divisão
    # caracteres pelo # sentença'''
    n_Caract_com_pont = 0
    for x in texto:
        if (x == "."):
            pass
        else:
            n_Caract_com_pont += 1

    n_sentenca = separa_sentencas(texto)
    rel_Carac_Sent = n_Caract_com_pont / len(n_sentenca)

    '''chama func separa frase e divide pela func separa sentenca'''
    n_frase = separa_frases(texto)
    rel_Senten_Fras = len(n_frase) / len(n_sentenca)

    '''chama func separa frase e faz divisão total caract pelo total frases'''
    n_Caract_com_pont2 = 0
    for x in texto:
        if (x == "," or x == ";" or x == ":" or x == "."):
            pass
        else:
            n_Caract_com_pont2 += 1
    rel_Carac_Fras = n_Caract_com_pont2 / len(n_frase)

    return taman_Medio, rel_Typ_Tok, rel_Hapax_lego, rel_Carac_Sent, rel_Senten_Fras, rel_Carac_Fras
    
###################################################################################

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero
    (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    copiah = ass_cp.index(min(ass_cp)) + 1
        
    return copiah
