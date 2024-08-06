temperatura = int(input("informe a temperatura atual (°C): "))

if temperatura<25:
    print ("Frio")
if temperatura>25 and temperatura<30:
    print ("Agradavél")
if temperatura>30:
    print("Calorzão do carai")

furacão = int(input("informe a velocidade do vento (km/h): "))

if furacão<89:
    print ("Velocidade Normal")
if furacão>89 and furacão<103:
    print ("Tempestade")
if furacão>103 and furacão<118:
    print ("Tempestade Violenta")
if furacão>118:
    print ("Furacão parça, corre garai")
