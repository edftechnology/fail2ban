# Como configurar/instalar/usar o `fail2ban` no `Linux Ubuntu`

## Resumo

Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `fail2ban` no `Linux Ubuntu`.

## _Abstract_

_In this document are contained the main commands and settings to set up/install/use the `fail2ban` on `Linux Ubuntu`._

## Descrição [2]

### `fail2ban`

O `Fail2ban` é uma ferramenta de segurança para sistemas baseados em `Linux` que protege contra ataques de força bruta e tentativas de intrusão. Ele monitora os _logs_ do sistema em busca de padrões de comportamento suspeitos, como tentativas repetidas e falhas de login, e bloqueia automaticamente os endereços IP associados a essas atividades por um período determinado. Isso ajuda a proteger o sistema contra ataques de hackers e garante uma maior segurança ao restringir o acesso de potenciais invasores.


## 1. Como configurar/instalar/usar o `fail2ban` no `Linux Ubuntu` [1][3]

Para configurar/instalar/usar o `fail2ban` no `Linux Ubuntu`, você pode seguir estes passos:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`    

2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 

    2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`

    2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 

    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`


Para configurar/instalar/usar o `fail2ban` no `Linux Ubuntu`, você seguirá estes passos:

1. **Instalar o `Fail2Ban`**: Instale o pacote `fail2ban` utilizando o comando: `sudo apt install fail2ban -y`

2. **Habilitar o `Fail2Ban` para iniciar na inicialização**: Para que o `fail2ban` inicie automaticamente na inicialização do sistema, habilite-o com: `sudo systemctl enable fail2ban`

3. **Iniciar o serviço `Fail2Ban`**: Se o serviço não estiver rodando, inicie-o com: `sudo systemctl start fail2ban`

4. **Verificar o _status_ do serviço**: Após a instalação, verifique se o serviço `fail2ban` está ativo e rodando: `sudo systemctl status fail2ban`


### 1.1 Recebendo notificações (**NÃO** fazer isso para o `Kali Linux`)

Para configurar notificações sobre esses eventos de auditoria, uma abordagem simples pode ser usar um _script_ que monitora os _logs_ de auditoria e envia notificações quando eventos específicos ocorrem. Vou te guiar na criação de um script básico que faz isso e envia um e-mail como notificação.

#### 1.1.1 Pré-requisitos

1. **Enviar e-mails:** Para este exemplo, usaremos o `mail` para enviar e-mails. Certifique-se de que você tem um cliente de e-mail de linha de comando instalado. Se não tiver, você pode instalar o `mailutils` (que inclui o comando `mail`) no Ubuntu: `sudo apt install mailutils postfix -y`

    1.1 **Configurar `Postfix`**: Se a tela de configuração do `Postfix` não aparecer automaticamente, você pode forçar a reconfiguração com o seguinte comando: `sudo dpkg-reconfigure postfix`

    Isso abrirá a tela de configuração do `Postfix`.

1.2 **Seguir as etapas de configuração**:

- **Selecione `Internet Site`**: Quando solicitado, escolha a opção Internet Site e pressione `Enter`.

- **`Nome do host`**: Quando solicitado, insira o nome do `host` desejado (por exemplo, `yourdomain.com` ou `localhost` se você estiver testando localmente) e pressione `Enter`.

#### 1.2.2 Configurar o `fail2ban` para enviar notificações por _e-mail_

Edite o arquivo de configuração do `fail2ban` para definir o endereço de _e-mail_ para o qual as notificações devem ser enviadas e ativar as ações de _e-mail_.

1. **Verificar ou criar o arquivo `jail.local`**: O arquivo de configuração principal do `Fail2Ban` é o `jail.conf`, mas você não deve editar esse arquivo diretamente, pois ele pode ser sobrescrito durante atualizações. Em vez disso, você deve criar um arquivo `jail.local` com suas configurações personalizadas.

    1.1 Primeiro, veja se o arquivo `jail.local` já existe: `ls /etc/fail2ban/jail.local`

    Se o arquivo não existir, você pode criá-lo a partir do `jail.conf`: `sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local`

    2.1 **Configurar o destinatário dos _e-mails_**: Você precisa editar o arquivo `jail.local` ou o arquivo de configuração específico para a prisão (`jail`) que você configurou. Se `jail.local` não existir, crie-o a partir de `jail.conf`: `sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local`

3. **Editar o arquivo `jail.local`**: Abra o arquivo jail.local para edição: `sudo nano /etc/fail2ban/jail.local`

4. **Configurar o destinatário do _e-mail_ e ativar as ações de _e-mail_**: Dentro do arquivo `jail.local`, você precisará configurar o endereço de _e-mail_ para o qual as notificações devem ser enviadas e ativar a ação de _e-mail_. Procure as seguintes linhas no arquivo (ou adicione-as se não estiverem presentes), pois elas podem **NÃO** estão na sequência:

    ```
    destemail = edendenis@gmail.com
    sendername = Fail2Ban
    action = %(action_mwl)s
    ```

    - **`destemail`**: O endereço de _e-mail_ para onde as notificações de banimentos serão enviadas.

    - **`sendername`**: O nome que aparecerá no campo "De" dos _e-mails_ que você receber.

    - **`action = %(action_mwl)s`**: Esta linha ativa o envio de _e-mails_ com as informações do banimento (incluindo o _log_ e o `whois`).

5. **Configurar a seção `sshd`**: Dentro do arquivo `jail.local`, você precisará configurar a seção `sshd`. Procure as seguintes linhas no arquivo (ou adicione-as se não estiverem presentes), pois elas podem **NÃO** estão na sequência:   

    ```
    [sshd]
    enabled = true
    port = ssh
    logpath = /var/log/auth.log
    maxretry = 5
    ```
    
6. **Salvar e sair do editor**: Após configurar o arquivo, salve-o e saia do editor (em `nano`, use `Ctrl + O` para salvar e `Ctrl + X` para sair).

7. **Reiniciar o `Fail2Ban`**: Depois de editar o arquivo, você precisa reiniciar o serviço `Fail2Ban` para que as alterações entrem em vigor: `sudo systemctl restart fail2ban`

8. **Verificar o _status_ do serviço**: Após a instalação, verifique se o serviço `fail2ban` está ativo e rodando: `sudo systemctl status fail2ban`


#### 1.2.3 Testar as configurações de notificação

Depois de configurar o `fail2ban` e o Postfix, você pode testar se as notificações por _e-mail_ estão funcionando corretamente. Você pode forçar um banimento manualmente ou realizar uma ação que dispare um banimento para testar se o `fail2ban` envia o _e-mail_.

1. Agora, o `Fail2Ban` deve enviar notificações por _e-mail_ sempre que um IP for banido. Para testar, você pode forçar um banimento manualmente:

    ```
    sudo fail2ban-client set sshd banip 127.0.0.2
    ```

    Verifique se você recebeu um _e-mail_ com as informações do banimento no endereço configurado.

2. **Verificar se o IP foi banido**: Após executar o comando, você pode verificar se o IP foi banido com o seguinte comando:

    ```
    sudo fail2ban-client status sshd
    ```

    Isso listará o número de IPs banidos e o próprio IP banido.

3. **Reiniciar o `fail2ban`:** Não se esqueça de reiniciar o serviço `fail2ban` após fazer alterações nas configurações:

    ```
    sudo systemctl restart fail2ban
    ```

4. **Verifique o _status_ do serviço:** Após tentar reiniciar, verifique o _status_ novamente para ver se o serviço está rodando:

    ```
    sudo systemctl status fail2ban
    ```

Com essas configurações, o `fail2ban` enviará automaticamente um _e-mail_ de notificação sempre que realizar uma ação de banimento, sem a necessidade de um _script_ adicional ou configurações do `cron`. Isso torna o `fail2ban` uma ferramenta poderosa e conveniente para monitorar a segurança do seu servidor em tempo real.


## 2. Banir ou desbanir um IP manualmente

### 2.1 Banir um IP manualmente

1. Se você quiser banir manualmente um endereço IP específico usando o `Fail2Ban`, o comando que você usaria é:

    ```
    sudo fail2ban-client set <nome-da-prisao> banip <endereço-ip>
    ```

    **Exemplo**: Se você quiser banir o IP `192.168.1.100` na prisão `sshd` (usada para monitorar o SSH), o comando seria:
    
    ```
    sudo fail2ban-client set sshd banip 192.168.1.100
    ```

    **Explicação**:

    - **<nome-da-prisao>**: O nome da prisão na qual você quer banir o IP. Exemplo: `sshd` para a prisão que monitora tentativas de _login_ SSH.

    - **<endereço-ip>**: O endereço IP que você quer banir. Exemplo: `192.168.1.100`.

2. **Verificar se o IP foi banido**: Após executar o comando, você pode verificar se o IP foi banido com o seguinte comando:

    ```
    sudo fail2ban-client status sshd
    ```

    Isso listará o número de IPs banidos e o próprio IP banido.


### 2.1 Desbanir um IP manualmente

1. **Desbanir um IP**: Se você quiser desbanir o IP depois, o comando é: `sudo fail2ban-client set <nome-da-prisao> unbanip <endereço-ip>`

    Por exemplo, para desbanir `192.168.1.100` na prisão `sshd`: `sudo fail2ban-client set sshd unbanip 192.168.1.100`

**Conclusão**:

- Para banir um IP manualmente, use sudo `fail2ban-client set <nome-da-prisao> banip <endereço-ip>`.

- Verifique o _status_ da prisão com `sudo fail2ban-client status <nome-da-prisao>`.

- Para desbanir um IP, use `sudo fail2ban-client set <nome-da-prisao> unbanip <endereço-ip>`.


### Configurar o `Fail2Ban` para banir todos os IPs, exceto o seu

1. **Identifique o seu IP**:

    - Antes de fazer qualquer alteração, certifique-se de que você conhece o seu endereço IP. Você pode encontrar o seu IP com o comando: `ip a`

    - Ou, se você está atrás de um roteador e deseja banir os IPs externos (da internet), use: `curl ifconfig.me`

    Anote o IP que você deseja "ignorar" no banimento.

2. **Edite o arquivo `jail.local`**:

    2.1 Você deve fazer essa configuração no arquivo `jail.local`. Se ele não existir, crie uma cópia do `jail.conf` para `jail.local`: `sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local`

    2.2 **Agora edite o `jail.local`**: `sudo nano /etc/fail2ban/jail.local`

3. **Adicione ou ajuste a configuração `ignoreip`**: No arquivo `jail.local`, dentro da seção `[DEFAULT]` ou na seção específica para a prisão `sshd`, adicione a linha `ignoreip` com o seu endereço IP. Se você quiser garantir que seu IP nunca será banido, adicione a configuração na seção [DEFAULT]:

    ```
    [DEFAULT]
    ignoreip = 127.0.0.1/8 ::1 192.168.37.244 192.168.37.213
    bantime = 10m
    findtime = 10m
    maxretry = 3
    ```

    Onde `SEU_IP` é o seu endereço IP (por exemplo, 192.168.1.100 ou o IP público, dependendo do que deseja proteger). Se quiser ignorar múltiplos IPs, você pode separá-los por espaços.

4. **Reinicie o `Fail2Ban`**: Após adicionar a configuração, reinicie o `Fail2Ban` para aplicar as mudanças: `sudo systemctl restart fail2ban`

5. **Verifique a configuração**: Para garantir que a configuração foi aplicada corretamente, verifique o _status_ do `Fail2Ban` e se ele está ignorando seu IP: `sudo fail2ban-client status sshd`

**Como funciona**:

-**`ignoreip`**: Define uma lista de endereços IP que o `Fail2Ban` nunca banirá. Isso inclui o seu próprio IP ou qualquer outro IP que você deseja proteger.

-**`bantime`**: Define o tempo de banimento para os IPs que falharem repetidamente nas tentativas de _login_.

-**`findtime`**: Define o intervalo de tempo dentro do qual as tentativas de _login_ falhas serão contadas.

-**`maxretry`**: Define o número máximo de tentativas falhas antes de banir um IP.


## 1.2. Código completo para configurar/instalar/usar

Para configurar/instalar/usar o `fail2ban` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Digite o seguinte comando e pressione `Enter`:

    ```
    sudo apt clean
    sudo apt autoclean
    sudo apt autoremove -y
    sudo apt update
    sudo apt --fix-broken install
    sudo apt clean
    sudo apt list --upgradable
    sudo apt full-upgrade -y
    sudo apt install fail2ban -y
    sudo systemctl enable fail2ban
    sudo systemctl start fail2ban
    sudo systemctl status fail2ban
    ```
    

## 2. Notificação de acesso pelo `Telegram`

### 2.1 Obter um token do _bot_ do `Telegram`

1. **Abrir o `Telegram` e Procurar por `@BotFather`**:

    1.1 Abra o aplicativo `Telegram` no seu celular ou no _desktop_.

    1.2 Na barra de busca, digite `@BotFather` e abra a conversa com ele. O @`BotFather` é um _bot_ oficial do `Telegram` responsável pela criação e gerenciamento de outros _bots_.

2. **Criar um Novo Bot**:

    2.1 Envie o comando `/newbot` para o `@BotFather`.

    2.2 Ele vai te pedir um nome para o _bot_. Este nome pode ser qualquer coisa, como `"MeuBotDeNotificacoes"`.

    2.3 Em seguida, ele vai te pedir um `username` para o _bot_. Este nome deve ser único e terminar em `"bot"`. Por exemplo, `meubotdenotificacoes_bot`.

3. **Receber o Token do _Bot_**:

    3.1 Assim que o _bot_ for criado, o `@BotFather` fornecerá uma mensagem contendo um _token_ de acesso. Este _token_ é um identificador exclusivo que você usará para enviar mensagens usando a API do `Telegram`.

    3.2 O _token_ terá um formato parecido com:

    ```
    7550358484:AAHQ8KRYfbQ1r7ZV7FgbsmDub3Ypnd0xcPM
    ```

4. **Anotar o Token**:

    4.1 Copie e guarde esse _token_ com segurança, pois ele será necessário para enviar notificações a partir do bot que você acabou de criar.
    

### 2.2 Obter o `chat_id` do Usuário ou Grupo

Além do token, você precisará do `chat_id`, que identifica para qual usuário ou grupo a mensagem deve ser enviada. Veja como obter isso:

1. **Enviar uma Mensagem para o Bot**:

    1.1 Vá até o bot que você criou e clique em `"Iniciar"` para abrir a conversa.

    1.2 Envie uma mensagem qualquer para o bot (por exemplo, `"Oi"`).

2. **Obter o `chat_id`**:

    2.1 Para obter o `chat_id`, você pode usar a API do Telegram:

    2.1.2 Abra um navegador e acesse o seguinte link (substituindo 7550358484:AAHQ8KRYfbQ1r7ZV7FgbsmDub3Ypnd0xcPM pelo seu token):
    
    ```
    https://api.telegram.org/bot7550358484:AAHQ8KRYfbQ1r7ZV7FgbsmDub3Ypnd0xcPM/getUpdates
    ```

    2.1.3 Você verá um JSON de resposta contendo informações sobre as últimas mensagens enviadas ao bot. Procure pelo campo `"chat"`, que terá um `"id"`, este é o `chat_id` que você precisará usar:

    ```
    475891890
    ```

Com essas informações, você conseguirá configurar o bot do Telegram para enviar alertas sempre que houver uma tentativa de login não autorizada no seu servidor.

### 2.3 Script de Notificação

Com o `token` e o `chat_id` em mãos, você pode criar o seguinte _script_ para enviar notificações ao `Telegram`:

#### 2.3.1 Utilizar o Diretório `/etc/secret`

Caso queira um nível extra de segurança, você pode salvar o arquivo de configuração em um diretório seguro, por exemplo, `/etc/secret`.

1. Crie um diretório seguro:

    ```
    sudo mkdir /etc/secret
    sudo chmod 700 /etc/secret
    ```

2. Crie o arquivo para armazenar os detalhes do bot:

    ```
    sudo nano /etc/secret/telegram_bot.conf
    ```

3. Adicione `TOKEN` e `CHAT_ID`:

    ```
    #!/bin/bash
    TOKEN="7550358484:AAHQ8KRYfbQ1r7ZV7FgbsmDub3Ypnd0xcPM"
    CHAT_ID="475891890"
    MESSAGE="Tentativa de login detectada no servidor $(hostname) de IP $1"

    curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
        -d chat_id=$CHAT_ID \
        -d text="$MESSAGE"
     ```

4. Altere as permissões do arquivo para garantir que apenas usuários autorizados possam lê-lo:

    ```
    sudo chmod 600 /etc/secret/telegram_bot.conf
    ```

5. Depois, escrever _script_ do `Fail2Ban` conforme Seção a segui.

### 2.4  Script do `Fail2Ban` para notificar pelo `Telegram`

Você deve colocar esse _script_ em um local onde possa ser executado pelo `Fail2Ban` ou pela aplicação responsável por monitorar as tentativas de _login_. Uma boa prática é salvá-lo em um diretório como `/usr/local/bin/` ou outro diretório acessível para _scripts_ executáveis.

1. Crie o script no diretório adequado:

    ```
    sudo nano /usr/local/bin/telegram_notify.sh
    ```

2. Cole o conteúdo do _script_:

    ```
    #!/bin/bash
    source /etc/secret/telegram_bot.conf

    MESSAGE="Login attempt on server $(hostname) of IP $1"

    curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
        -d chat_id=$CHAT_ID \
        -d text="$MESSAGE"
    ```

3. Torne o _script_ executável:

    ```
    sudo chmod +x /usr/local/bin/telegram_notify.sh
    ```

4. Testar para verificar se **NÃO** há nenhum problema e se todos os acessos estão corretos. Execute no `Terminal Emulator`:

    ```
    !/bin/bash

    # Carregar as variáveis do arquivo de configuração
    source /etc/secret/telegram_bot.conf

    # Mensagem de teste
    MESSAGE="Tentativa de login detectada no servidor $(hostname) de IP $1"

    # Exibir mensagem para garantir que as variáveis foram carregadas
    echo "TOKEN: $TOKEN"
    echo "CHAT_ID: $CHAT_ID"
    echo "MESSAGE: $MESSAGE"

    # Enviar a mensagem para o Telegram
    curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
        -d chat_id=$CHAT_ID \
        -d text="$MESSAGE" -v
    ```

5. Configure o `Fail2Ban` (ou outra aplicação) para acionar o _script_ `/usr/local/bin/telegram_notify.sh` quando houver uma tentativa de _login_.

Isso garantirá que o _script_ seja acionado automaticamente para enviar uma mensagem ao `Telegram` sempre que necessário.


## 3. Como desinstalar o `fail2ban`

Para desinstalar o `Fail2Ban` no seu sistema, siga as instruções abaixo, dependendo da distribuição que você está usando:

1. **Desinstalar no Ubuntu/Debian**: Use o comando abaixo para remover o `Fail2Ban`:

    ```
    sudo apt remove --purge fail2ban -y
    ```

    Este comando irá remover o `Fail2Ba`n e limpar as configurações associadas.
    
2. Caso deseje remover também pacotes dependentes que não estão mais em uso, execute:

    ```
    sudo apt autoremove -y
    ```

3. **Verificar se foi Removido**: Você pode confirmar se o `Fail2Ban` foi desinstalado corretamente verificando o _status_ do serviço:

    ```
    sudo systemctl status fail2ban
    ```

Este comando deve retornar algo como `"Unit fail2ban.service could not be found"`, indicando que o serviço foi removido.

4. **Remover Arquivos Residuais**: Se houverem arquivos residuais de configuração, como os arquivos `jail.local` que foram editados, você pode removê-los manualmente:

    ```
    sudo rm -rf /etc/fail2ban
    ```

Isso vai garantir que todos os arquivos de configuração que você modificou ou criou sejam excluídos.

Após esses passos, o `Fail2Ban` estará totalmente desinstalado do seu sistema.

## Referências

[1] OPENAI. ***Monitoramento de acesso no linux.*** Disponível em: <https://chat.openai.com/c/7772a507-88e7-46c8-ad7a-64a2d9011843> (texto adaptado). ChatGPT. Acessado em: 21/02/2024 12:00.

[2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 21/02/2024 12:00.

