# FUNÇOES
''' COLETA OS DADOS DO CLIENTE E RETORNA OS DADOS EM SUAS RESPECTIVAS VARIAVEIS '''
def leitura_dos_dados():
    nome_anuncio = str(input('DIGITE O NOME DO ANUNCIO: ')).upper().strip()
    nome_cliente = str(input('DIGITE O NOME DO CLIENTE: ')).upper().strip()
    data_inicio = input('DIGITE A DATA DE INICIO (xx/xx/xxxx): ').split('/')
    data_termino = input('DIGITE A DATA DE TERMINO (xx/xx/xxxx): ').split('/')
    invest_por_dia = int(input('DIGITE O INVESTIMENTO DIARIO: R$ '))
    return nome_anuncio, nome_cliente, data_inicio, data_termino, invest_por_dia

''' A PARTIR DOS DADOS DO CLIENTE SUAS INFORMAÇOES SÂO MOSTRADAS NA TELA SEM NENHUM RETORNO '''
def mostrarDadosNaTela (anuncio, cliente, inicio, termino, investimento):
    print('O NOME DO ANUNCIO É: {}'.format(anuncio))
    print('O NOME DO CLIENTE É: {}'.format(cliente))
    print('A DATA DE INÍCIO DO INVESTIMENTO É: {}/{}/{}'.format(inicio[0], inicio[1], inicio[2]))
    print('A DATA FINAL DO INVESTIMENTO É: {}/{}/{}'.format(termino[0], termino[1], termino[2]))
    print('O INVESTIMENTO DIARIO É DE: R${:.2f}'.format(investimento))
    return None

'''A PARTIR DAS DATAS DE INICIO E FIM SÃO CALCULADOS A QUANTIDADE DE DIAS PARA FAZER O ANUNCIO. ESSE NUMERO
 É RETORNADO PARA FORA DA FUNÇAO'''
def CalcularDias(inicio, fim):
    dias = 0
    if inicio[0] == fim[0] and inicio[1] == fim[1] and inicio[2] == fim[2]:
        print('NAO É POSSIVEL CALCULAR OS DIAS. ENTRE COM NUMEROS VALIDOS!!')
    else:
        if fim[2] < inicio[2]:
            print('NAO É POSSIVEL CALCULAR OS DIAS. ENTRE COM NUMEROS VALIDOS!!')
        else:
            diferenca_anos = int(fim[2]) - int(inicio[2])
            anos_em_dias = int(diferenca_anos) * 360
            if int(fim[1]) >  int(inicio[1]):
                diferenca_meses = int(fim[1]) - int(inicio[1])
                meses_em_dias = int(diferenca_meses) * 30
                dias = meses_em_dias + anos_em_dias
            else:
                diferenca_meses = abs(int(fim[1]) - int(inicio[1]))
                meses_em_dias = anos_em_dias - (diferenca_meses*30)
                dias = meses_em_dias
            if int(fim[0]) >  int(inicio[0]):
                dias_unit = int(fim[0]) - int(inicio[0])
                dias += dias_unit
            else:
                dias_unit = abs(int(fim[0]) - int(inicio[0]))
                dias -= dias_unit
        return dias

''' A PARTIR DO NUMERO DE DIAS E DO VALOR A SER INVESTIDO É POSSIVEL CALCULAR A QUANTIDADE DE VISUALIZAÇOES,
COMPARTILHAMENTOS E CLIQUES FEITOS NO ANUNCIO. ESSES DADOS FICAM ARMAZENADOS EM UMA LISTA E SÃO PASSADOS PARA
FORA DA FUNÇÃO COMO UMA VARIAVEL '''
def calculadoraDeDados(numeroDias, investimentoDia):
    clicam_max = list()
    compartilha_max = list()
    lista = list()
    while numeroDias != 0:
        visualizam = 0
        clicam = 0
        clicam_parcial = 0
        compartilha = 0
        diferenca = 9999
        parcial = 0
        for k in range(0, investimentoDia):
            visualizam += 30
        while diferenca > 100:
            for j in range(visualizam // 100):
                clicam += 12
            clicam_max.append(clicam-clicam_parcial)
            for l in range(clicam // 20):
                compartilha += 3
                clicam -= 20
                clicam_parcial = clicam
            compartilha_max.append(compartilha)
            if compartilha > 4:
                compartilha = 4
            parcial = visualizam
            lista.append(parcial)
            while compartilha != 0:
                visualizam += 40
                compartilha -= 1
            diferenca = visualizam - parcial
            visualizam = diferenca
        numeroDias -= 1
    return lista, clicam_max, compartilha_max

''' COM AS LISTAS COM A QUANTIDADE DE VISUALIZACOES, CLIQUES E COMPARTILHAMENTOS CONSEGUIMOS CHEGAR A UM VALOR INTEIRO
 PARA CADA UM DELES. APÓS ISSO NÓS RETORNAMOS ESSE VALOR PARA UTILIZAR FORA DA FUNÇAO'''
def valoresMaximos(visualizacoes, cliques, compartilhamentos):
    Val_Tot_Compartilha = 0
    Val_Tot_Cliques = 0
    soma = 0
    for numeros in visualizacoes:
        soma += numeros
    for compartilha in compartilhamentos:
        Val_Tot_Compartilha += compartilha
    for clique in cliques:
        Val_Tot_Cliques += clique
    return soma, Val_Tot_Compartilha, Val_Tot_Cliques

''' COM TODOS OS DADOS A JA CALCULADOS E PARAMETRIZADOS SÓ RESTA MOSTRAR NA TELA O RESULTADO FINAL'''
def MostrarRespostaNaTela(dias, investimento, maxVisu, maxCliques, maxCompartilha):
    print(f'Valor total investido:R$ {dias * investimento:.2f}')
    print(f'Quantidade máxima de visualizações: {maxVisu}')
    print(f'Quantidade máxima de cliques: {maxCliques}')
    print(f'Quantidade máxima de compartilhamentos: {maxCompartilha}')
    return None

# PROGRAMA PRINCIPAL
resp = 'S'
while resp[0] == 'S':
    # LER DADOS
    nom_anun, nom_clien, dat_ini, dat_ter, invests = leitura_dos_dados()
    print("#############################################################################")
    # MOSTRAR DADOS NA TELA
    mostrarDadosNaTela(nom_anun, nom_clien, dat_ini, dat_ter, invests)
    print("#############################################################################")
    # CALCULAR A QUANTIDADE DE DIAS
    QtdDias = CalcularDias(dat_ini, dat_ter)
    # ARMAZENAR QUANTIDADE MAXIMA DE VISUALIZAÇOES, CLIQUES E COMPARTILHAMENTOS EM UMA LISTA
    qtd_max_visu, qtd_max_cliques, qtd_max_compartilhamentos = calculadoraDeDados(QtdDias, invests)
    # CALCULAR A QUANTIDADE MAXIMA DE VISUALIZAÇOES, CLIQUES E COMPARTILHAMENTOS
    visu_max,compartilha_max, cliq_max = valoresMaximos(qtd_max_visu, qtd_max_cliques, qtd_max_compartilhamentos)
    # MOSTRAR NA TELA TODOS OS DADOS EXIGIDOS PELO PROGRAMA
    MostrarRespostaNaTela(QtdDias,invests, visu_max,cliq_max,compartilha_max)
    print("#############################################################################")
    # PERGUNTA PARA SABER SE GOSTARIA DE CONTINUAR NO PROGRAMA
    resp = str(input('GOSTARIA DE FAZER UM NOVO CADASTRO [SIM/NAO] ? ')).upper().strip()
print('ATÉ A PROXIMA!!!')

