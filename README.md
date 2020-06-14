# Leitor de Código de Barras em python 2.7:

O código barcode.py pega as informações lidas por um leitor de código de barras via USB e envia um Post de um JSON para uma determinada API,
por default, o código está enviando para um servidor local. Esse código pode ser rodado em um pc ou em um hardware com WIFI,
para o projeto, foi escolhido o Raspberry Pi Zero W. Para rodar use o comando:

`python barcode.py`

Já o código api-flask.py roda uma instância local de uma API que irá receber as informações enviadas pelo barcode.py. Este código pode
ser substituído por um servidor que irá receber o JSON enviado pelo barcode.py. Para rodar o servidor:

`python api-flask.py`

# Raspberry Pi Zero W

O Raspberry funciona como um pc normal rodando Linux. Para sua configuração inicial é usado um cartão SD de pelo menos 8GB com o sistema
operacional Raspian. Ele possui duas portas USB: uma para alimentação (fonte) e um para dados (leitor de código de barras), possui ainda 
uma porta micro HDMI. Outra opção simples é fazer uma comunicação via SSH. [Link utilizado para a configuração do sistema operacional,
wifi e comunicação SSH](https://www.filipeflop.com/blog/raspberry-pi-zero-w-para-rede-e-ssh/).

Por fim, foi configurado para que o Raspberry iniciasse automaticamente o programa barcode.py sempre que ele ligasse, para isso foi utilizado
[o tutorial (solução 3)](https://cadernodelaboratorio.com.br/2015/06/10/inicializando-um-programa-automaticamente-no-raspberrypi/#:~:text=O%20programa%20a%20ser%20inicializado,python%20%2C%20ou%20outra%20forma%20qualquer.&text=Para%20executar%20um%20programa%20automaticamente,linha%20com%20o%20%E2%80%9C%23%E2%80%9D.&text=O%20Raspberry%20ir%C3%A1%20iniciar%20j%C3%A1,o%20endere%C3%A7o%20IP%20192.168.1.31.).
