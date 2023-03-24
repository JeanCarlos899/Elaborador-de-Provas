Elaborador de Provas em Django
Este é um projeto de elaboração de provas desenvolvido em Django, uma framework web em Python. Este projeto permite que os usuários criem provas, adicionem questões, respostas e possam visualizá-las posteriormente.

Instalação
Para instalar o Elaborador de Provas em Django, siga os seguintes passos:

Clone o repositório do projeto para o seu computador
bash
Copy code
git clone https://github.com/seu-usuario/elaborador-de-provas-django.git
Crie um ambiente virtual e ative-o
bash
Copy code
python3 -m venv env
source env/bin/activate
Instale as dependências do projeto
bash
Copy code
pip install -r requirements.txt
Execute as migrações do banco de dados
bash
Copy code
python manage.py migrate
Crie um usuário admin
bash
Copy code
python manage.py createsuperuser
Execute o servidor
bash
Copy code
python manage.py runserver
Acesse o Elaborador de Provas no seu navegador, através do endereço http://localhost:8000/
Utilização
Para utilizar o Elaborador de Provas em Django, siga os seguintes passos:

Faça login na plataforma com as credenciais de administrador criadas anteriormente.

Crie uma nova prova, adicionando o título, data de aplicação e duração.

Adicione as questões da prova, especificando o tipo (múltipla escolha ou dissertativa), o enunciado e as alternativas (no caso de múltipla escolha).

Adicione as respostas das questões, especificando o texto da resposta.

Visualize a prova criada para verificar se todas as informações foram adicionadas corretamente.

Contribuição
Se desejar contribuir para o projeto, siga os seguintes passos:

Crie um fork do repositório do projeto.

Clone o repositório do projeto para o seu computador

bash
Copy code
git clone https://github.com/seu-usuario/elaborador-de-provas-django.git
Crie um ambiente virtual e ative-o
bash
Copy code
python3 -m venv env
source env/bin/activate
Instale as dependências do projeto
bash
Copy code
pip install -r requirements.txt
Execute as migrações do banco de dados
bash
Copy code
python manage.py migrate
Faça as suas alterações no código e teste-as localmente.

Faça o commit das suas alterações e crie um pull request no repositório original.

Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
