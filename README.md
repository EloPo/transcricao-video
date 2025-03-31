# Transcrição de Vídeo para Texto

Este projeto permite a transcrição de vídeos para texto usando o modelo **Whisper** da OpenAI. O objetivo é extrair o áudio do vídeo e, em seguida, transcrevê-lo para texto, salvando o resultado em um arquivo `.txt`.

## Funcionalidades

- Extração de áudio de arquivos de vídeo.
- Transcrição do áudio usando o modelo Whisper.
- Geração de arquivo de texto com a transcrição.

## Tecnologias Utilizadas

- **Python 3.x**
- **OpenAI Whisper**: Modelo para transcrição de áudio.
- **FFmpeg**: Ferramenta para extrair áudio de vídeos.

## Pré-requisitos

- **Python 3.x** instalado em sua máquina.
- **FFmpeg** instalado. Se não tiver, pode ser instalado via Homebrew no macOS ou via outras formas dependendo do seu sistema operacional.
- **Pip** para instalação das dependências Python.

## Passos de Instalação

### 1. **Clone o repositório**

Clone este repositório para sua máquina local usando o comando:

```bash
git clone https://github.com/seu-usuario/transcricao-de-video.git
cd transcricao-de-video
```

### 2. **Instale as dependências**

Certifique-se de ter o `pip` atualizado. Se não tiver, execute:

```bash
python3 -m pip install --upgrade pip
```

Agora, instale as dependências necessárias para rodar o projeto:

```bash
pip3 install -r requirements.txt
```

O arquivo `requirements.txt` contém as bibliotecas que são necessárias para o projeto, como `openai-whisper`, `ffmpeg-python`, entre outras.

### 3. **Instale o FFmpeg**

O FFmpeg é necessário para extrair o áudio dos vídeos. Se você estiver no macOS, pode instalar via Homebrew:

```bash
brew install ffmpeg
```

Se você estiver em outro sistema operacional, siga as instruções de instalação do [FFmpeg](https://ffmpeg.org/download.html).

### 4. **Execute a transcrição**

Agora que todas as dependências estão instaladas, você pode rodar o script de transcrição com o seguinte comando:

```bash
python3 transcricao.py caminho/do/seu/video.mp4 caminho/para/salvar/transcricao.txt
```

Isso irá:

1. Extrair o áudio do vídeo.
2. Transcrever o áudio usando o modelo Whisper.
3. Salvar a transcrição no arquivo `.txt` especificado.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
/transcricao-de-video/
  ├── transcricao.py           # Código principal para transcrição de vídeo
  ├── requirements.txt         # Dependências do projeto
  ├── /uploads/                # (Opcional) Pasta para armazenar vídeos enviados (caso queira usar)
  └── transcricao.txt          # Arquivo gerado com a transcrição (salvo após o processamento)
```

## Contribuições

Se você quiser contribuir com o projeto, fique à vontade! Crie um fork do repositório, faça suas alterações e envie um pull request com suas modificações.

---

### **Licença**
Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
