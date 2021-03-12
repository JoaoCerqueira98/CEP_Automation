import os, datetime

cep = str(input('Qual é o primeiro CEP? '))
cep1 = str(input('Qual é o segundo CEP? '))
testcases = []
statuscase = {}
value = os.system(f'sudo -S sh /Users/joaocerqueira/Desktop/Desafio_SoapUI/testrunner-verifydata_param.sh {cep} {cep1}')
files = os.listdir('/Users/joaocerqueira/Desktop/ResultsCli')
now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


for file in files:
    if file not in '.DS_Store':
        testcase = file.split('-')
        if testcase[1] not in testcases:
            testcases.append(testcase[1])
            statuscase.update({testcase[1]: 'SUCESSO'})
        if statuscase[testcase[1]] == 'SUCESSO':
            if 'FAILED' in file:
                statuscase.update({testcase[1]:['FALHA', file]})


for case in statuscase:
    if 'FALHA' in statuscase[case]:
        print(f'O Testcase {case} teve {statuscase[case][0]} no arquivo {statuscase[case][1]}')
    else:
        print(f'O TestCase {case} teve o status {statuscase[case]}')

os.mkdir(f'/Users/joaocerqueira/Desktop/Repositorio/{now}')
os.system(f'mv /Users/joaocerqueira/Desktop/ResultsCli/* /Users/joaocerqueira/Desktop/Repositorio/{now}')
print(f'Os arquivos de evidencia foram movidos para a pasta /Users/joaocerqueira/Desktop/Repositorio/{now}')