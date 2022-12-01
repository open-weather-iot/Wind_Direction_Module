# MÓDULO DA DIREÇÃO DO VENTO
O subprojeto da Direção do Vento, faz parte do projeto da Estação Meteorológica para Monitoramento Climático e Ambiental.
O subprojeto é composto por um Circuito Integrado de 3 eixos o HMCL5883L, projetado para sensoriamento magnético de baixo campo. O HMC5883L pode medir tanto a direção quanto a magnitude dos campos magnéticos da Terra. O sensor possui uma interface digital I2C para comunicação e geralmente é utilizado para aplicações de Bússolas. 

# DIAGRAMA EM BLOCOS

O diagrama em blocos é composto pelo CI HMC5883L, um HOST (Raspberry Pico Pi) e um display conforme a figura abaixo: 
![Diagrama_Blocos](https://user-images.githubusercontent.com/40901361/202058156-6c2cf4d4-cb75-4f33-9512-aa17b0100968.PNG)


# TESTE

Os testes contam com os arquivos de SW descritos em Micropython. O arquivo HMC5882Lcalibration.py é usado para calibrar o sensor, os valores obtidos são considerados variaveis xs,xb, ys e yb do arquivo hmc5883l.py. No arquivo hmc5883l.py contém  o range do campo do sensor de 0.88 a 8.1 Ga. Nesse arquivo o usuário deverá adicionar o valor local da declinação magnética, através do link  http://www.magnetic-declination.com/ é possivel obter esse ângulo. O modulo é configurado para trabalhar em modo continuo, em que as medidas são coletadas continuamente. A Figura abaixo ilustra a posição em que o sensor precisa estar para realizar as medidas. 

![Direção_Sensor](https://user-images.githubusercontent.com/40901361/202057830-d29dfb14-a627-4d18-9e3d-aeaea10b6909.PNG)


A declinação magnética ou variação magnética,  é o ângulo formado entre o Polo Norte Geográfico e o Polo Norte Magnético, também conhecido como desvio entre o azimute(rumo)  e os correspondentes magnéticos. A declinação no caso deste trabalho ficou em -21º e com inclinação de 38º. No Raspberry Pico Pi os sinais do I2C SCL (pino = 15) e SDA (pino = 14), endereço  0x1e (30 dec), foi adotado um ganho de '1.9', conforme a figura abaixo:

![Declinação](https://user-images.githubusercontent.com/40901361/205069947-b2bb4939-e16b-478f-b868-02f15628b03f.PNG)




Por fim, o arquivo picoHMC5883L.py é usado para obter os dados da direção do vento em graus. Foi dividido em 45 graus cada sentido adotaado (N,L,O,S, SE, SO, NE e NO)
