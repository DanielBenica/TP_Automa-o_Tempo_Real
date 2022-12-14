# TP - Automação em TempoReal

A disciplina de Automação em Tempo Real tinha como objetivo proporcionar aos alunos um primeiro contato com os sistemas de tempo real, ensinando desde os conceitos mais básicos que permeiam pelos sistemas de tempo real, até os inúmeros tipos de sistemas. No final da disciplina foi proposto um trabalho prático final, com o objetivo de abordar os conceitos apreendidos durante a disciplina e validar o aprendizado. E esse repositório se refere a esse trabalho prático, desenvolvido por mim e pelo Daniel Benicá. A ideia proposta nesse trabalho é simular o controle em tempo real de um banco de motores. Mais detalhes sobre a proposta do exercício pode ser encontrada no arquivo "Trabalho Final.pdf".

## Pré Requesitos

Para que seja possível executar o programa no dispositivo, é necessário ter instalado alguma versão do compilador Python. Além dsso, é necessário que o dispositivo tenha duas bibliotecas instaladas: a matplotlib num.py. Essas bibliotecas podem ser instaladas usando
o comando:

```
pip install -r requirements.txt
```

## Compilação

Para compilar o programa, é necessário entrar em sua pasta raiz e abrir o terminal. Feito isso é necessário executar o seguinte comando:

```
python_version main.py
```

em que se deve substituir python_version pela versão do compilador python de seu dispositivo. Exemplo:

```
python3 main.py
```

Para executar o synoptco é necessário executar o seguinte comando:

```
python3 synoptic.py
```

Feito isso é necessário imputar no terminal os Ids dos motores separados por espaço e em seguida fornecer a referência de velocidade.

A porta utilizada para fazer conexão TCP/IP é a 51511.

<table>
  <tr>
    <td align="center"><a href="https://www.linkedin.com/in/danielbenica/"><img style="border-radius: 50%;" src="https://media-exp1.licdn.com/dms/image/C4D03AQFHf7R1Ilmq9Q/profile-displayphoto-shrink_400_400/0/1591447156623?e=1675296000&v=beta&t=2DCij1I0uIvFPdGU8y1zP0DTT1Jz_At6lSL2Irr7WoA" width="100px;" alt=""/><br /><sub><b>Daniel Benicá</b></sub></a><br /></td>
    <td align="center"><a href="https://www.linkedin.com/in/paulo-estevao/"><img style="border-radius: 50%;" src="https://media.licdn.com/dms/image/C4D03AQFyfMu22vYrRA/profile-displayphoto-shrink_400_400/0/1622859672972?e=1676505600&v=beta&t=QcZjwgUbnC_Apour2BtlOepPPFUQhoCkCCGIJxlf09I" width="100px;" alt=""/><br /><sub><b>Paulo Estêvão</b></sub></a><br /></td>

  </tr>
</table>
