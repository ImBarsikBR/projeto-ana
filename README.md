Projeto Ana Beatriz - Texto para Voz
Este projeto consiste em uma aplicação web simples, desenvolvida com Flask, que converte texto digitado pelo usuário em voz. A aplicação utiliza a biblioteca gTTS (Google Text-to-Speech) para gerar o áudio e exibi-lo no navegador.

Funcionalidades
O usuário pode digitar um texto e clicar no botão para que a aplicação converta esse texto em voz.

A voz gerada é reproduzida automaticamente no navegador.

A interface do usuário possui um design simples e responsivo, com fundo roxo vinho e imagens florais, tornando-a agradável e fácil de usar.

Tecnologias Utilizadas
Flask: Framework para desenvolvimento web.

gTTS (Google Text-to-Speech): Biblioteca Python para converter texto em fala.

HTML5 & CSS3: Estrutura e estilo da página.

JavaScript: (Opcional) Pode ser utilizado para adicionar interatividade (caso necessário no futuro).

Google Fonts: Para fontes personalizadas (Playfair Display e Great Vibes).

Como Rodar o Projeto Localmente
Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina. Se não tiver, você pode baixá-lo aqui.

Passo a Passo
Clone o repositório para o seu computador:

bash
Copiar
Editar
git clone https://github.com/ImBarsikBR/projeto-ana.git
Navegue até o diretório do projeto:

bash
Copiar
Editar
cd projeto-ana
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar
Editar
python -m venv venv
Ative o ambiente virtual:

No Windows:

bash
Copiar
Editar
.\venv\Scripts\activate
No macOS/Linux:

bash
Copiar
Editar
source venv/bin/activate
Instale as dependências do projeto:

bash
Copiar
Editar
pip install -r requirements.txt
Execute o servidor Flask:

bash
Copiar
Editar
python app.py
Abra o navegador e acesse http://127.0.0.1:5000 para ver a aplicação em funcionamento.

Como Funciona
O usuário insere um texto no campo de entrada.

Ao clicar no botão "Falar", a aplicação gera o áudio usando a biblioteca gTTS.

O áudio gerado é enviado ao navegador e reproduzido automaticamente, permitindo que o usuário ouça o texto falado.

Personalização
Fundo: O fundo da página é um tom de roxo vinho, com uma imagem floral que foi escolhida para dar um toque agradável ao visual.

Texto: O título "Texto para Voz" é exibido com uma fonte personalizada chamada Playfair Display e o subtítulo do projeto usa a fonte Great Vibes.

Layout Responsivo: O design foi feito para ser responsivo, garantindo que o conteúdo seja bem exibido tanto em desktops quanto em dispositivos móveis.

Licença
Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais detalhes.
