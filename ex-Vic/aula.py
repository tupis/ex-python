## variáveis
## uma variavel pode receber um valor de qualquer tipo, porém ainda é tipada

isso_e_uma_variavel_tipo_string = 'Ola mundo!'
isso_e_uma_variavel_tipo_integer = 54
isso_e_uma_variavel_tipo_float = 5.7
isso_e_uma_variavel_tipo_boolean = True

## é possivel definir um tipo de variável ao declara-la

integer = int(5)
string = str('Ola Mundo')
floatNumber = float(4.9)

## os inputs servem para perguntar ao usuário algum valor, geralmente são utilizados junto com variaveis

pergunta_inteiro = int(input("Qual o inteiro você deseja inserir? "))
pergunta_float = float(input("Qual o float você deseja inserir? "))
pergunt_string = str(input("Qual cadeia de caractere você deseja inserir? "))

## Operadores
    ## Operadores Aritméticos
        ## "+" representa adição
        ## "-" representa subtração
        ## "*" representa mutiplicação
        ## "/" representa divisão
        ## "//" representa divisão inteira
        ## "%" representa o resto da divisão
        ## "**" representa exponenciação

            dez = 10
            dois = 2

            soma = dez + dois ## saida == 12
            subtracao = dez - dois ## saida == 8
            multipicacao = dez * dois ## saida == 20
            divisao = dez / dois ## saida == 5.0
            divisao_inteira = dez // dois ## saida == 5
                #nota-se a diferencia de uma divisão inteira pra uma divisão comum, uma o valor vem em int, na outra vem em float
            resto_divisao = dez % dois #saida == 0
            exponenciacao = dez ** dois #saida == 100

    ## Operadores de comparação
        ## "==" representa IGUAL A
        ## "!=" representa DIFERENTE DE
        ## "<" representa MAIOR QUE
        ## "<=" representa MAIOR OU IGUAL A
        ## ">" representa MENOR QUE
        ## ">=" representa MENOR OU IGUAL A

            if dez == 10:
                ## retorna uma verdadeiro
            if dez != 9:
                ## retorna verdadeiro
            if dez < 5:
                ## retorna falso
            if dez <= 10:
                ## retorna verdadeiro
            if dez > 15:
                ## retorna falso
            if dez >= 11:
                ## retorna falso

    ## Operadores Lógicos
        ## os mais usados são: (and), (or) e (not)
            ## no AND retorna verdadeiro se todas as afirmaçãoes forem verdadeiras
                if dez > 0 and dois > 0:
                    ## retorna verdadeiro
                if dez < 0 and dois > 0:
                    ## retorna falso
                            ## no OR retorna verdadeiro se pelo menos uma afirmação for verdadeira
                if dez > 0 or 2 < 0:
                    #retorna verdadeiro
                if dez < 0 or dois < 0:
                    ## retorna falso
                            ## no NOT ele inverte o valor entra true e false
                if not(dez > 0 and dois > 0):
                    ## retorna falso
                if not(dez > 0 or dois < 0):
                    ## retorna falso

## If..Else
    ## o if..else é um loop condicional
    ## como visto anteriormente ele aceita operadores lógicos e de comparação
    ## o if :é a primeira condição a ser executada, caso não seja verdadeira, ele procura a proxima condição
    ## existe o elif : que geralmente é usada quando tem que verificar mais de uma condição
    ## o elif : significa que, se a condição anterior não for verdadeira, tente essa condição
    ## o else : é usado caso ele não consiga achar nenhuma condição verdadeira durante o laço, ele executa os blocos de comandos dentro do else :

        ## exemplo apenas com if

            if dez == dez:
                ## retorna verdadeiro

        ## exemplo com elif
            if dez == 11:
                ## retorna falso, então ele vai pra proxima condição
            elif dez > 15:
                ## retorna falso, então ele vai pra proxima condição
            elif dez >= dez
                ## retorna verdadeiro, e encerra o laço

        ## exemplo com else
            if dez == 11:
                ## retorna falso, então ele vai pra proxima condição
            elif dez > 15:
                ## retorna falso, então ele vai pra proxima condição
            elif dez < dez:
                ## retorna falso, então ele vai pra proxima condição
            else:
                ## execua o bloco de comandos que tiver aqui

## While loop
    ## while em português siginfica ENQUANTO
    ## seguindo a lógica, podemos pensar assim, enquanto a condição for verdadeira execute os seguintes comandos

        ## primeiro irei declarar uma variavel, na qual sera trabalhado a minha condição
            i = 0
        ## segundo chamar o laço while pra executar a condição deseja, no meu caso, a minha condição será enquanto a minha variavel "i" for menor que 10
            while i < 10:
                i = i + 1
        ## ao terminar esse loop minha variavel terá o valor igual a 10