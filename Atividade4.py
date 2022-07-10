def totalDiarias(x, y):
    total = x * y; 
    return total;
def seguro(x):
    seguro = x * 20;
    return seguro;

def gps(x):
    gps = 0;
    gps = 12 * x;
    return gps;
def bebeConforto(x):
    bebeConforto = 0;
    bebeConforto = 15 * x;
    return bebeConforto;
def cadeira(x):
    cadeira = 0;
    cadeira = 15 * x;
    return cadeira;
def assento(x):
    assento = 0;
    assento = 15 * x;
    return assento;

diarias = int(input("Digite o numero de diarias: "));
print("Qual o tipo de veiculo (economico/sedan/suv)?")
veiculo = input();
valorDiaria = 0;
if veiculo == "economico":
    valorDiaria = 50;
elif veiculo == "sedan":
    valorDiaria = 75;
else:
    valorDiaria = 84.90;
    
if diarias >= 7:
    valorDiaria -= (valorDiaria*0.15);

total = totalDiarias(diarias, valorDiaria);
seguroTotal = seguro(diarias);

print("Deseja adicionar servico de GPS? (s/n)")
resposta = input();
if resposta == "s":
    gpsc = gps(diarias);
else:
    gpsc = gps(0);

print("Deseja adicionar servico de Bebe Conforto? (s/n)")
resposta = input();
if resposta == "s":
    bebeConfortoc = bebeConforto(diarias);
else:
    bebeConfortoc = bebeConforto(0);

print("Deseja adicionar servico de Cadeira de bebe? (s/n)")
resposta = input();
if resposta == "s":
    cadeirac = cadeira(diarias)
else:
    cadeirac = cadeira(0)

print("Deseja adicionar servico de Assento de Elevacao? (s/n)")
resposta = input();
if resposta == "s":
    assentoc = assento(diarias);
else:
    assentoc = assento(0);

taxa = 75;

totalGeral = total + seguroTotal + gpsc + bebeConfortoc + cadeirac + assentoc + taxa;

file = open("gastos.txt", "w")

file.write(f"Tipo do carro: {veiculo}\n");
file.write(f"{diarias} Diarias                    Total\n")
file.write(f"{diarias} x R${valorDiaria}                   R${total}\n")
file.write("----------------------------------------\n")
file.write("Seguro do carro\n")
file.write(f"{diarias} x R$20.00                  R${seguroTotal}\n")
file.write("----------------------------------------\n")
if gpsc != 0:
    file.write(f"GPS - {diarias} x R$12.00            R${gpsc}\n")
if bebeConfortoc != 0:
    file.write(f"Bebe Conforto - {diarias} x R$15.00        R${bebeConfortoc}\n")
if cadeirac != 0:
    file.write(f"Cadeira - {diarias} x R$15.00          R${cadeirac}\n")
if assentoc != 0:
    file.write(f"Assento - {diarias} x R$12.00        R${assentoc}\n")
if (gpsc != 0) or (bebeConfortoc != 0) or (cadeirac != 0) or (assentoc != 0):
    file.write("----------------------------------------\n");
file.write(f"Taxa administrativa          R$ {taxa}\n");
file.write("----------------------------------------\n");
file.write(f"Total do aluguel:            R${totalGeral}\n");

file.close();
















