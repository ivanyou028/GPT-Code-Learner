import requests
from bs4 import BeautifulSoup


def load_urls(urls):
    text_splitter = CharacterTextSplitter(chunk_size=1500, separator="\n")
    docs, metadatas = [], []
    for url in urls:
        html = requests.get(url).text
        soup = BeautifulSoup(html, features="html.parser")
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        page_content = '\n'.join(line for line in lines if line)

        splits = text_splitter.split_text(page_content)
        docs.extend(splits)
        metadatas.extend([{"source": url}] * len(splits))
        print(f"Split {url} into {len(splits)} chunks")
    return docs, metadatas


def load_documents(filenames):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200,
        length_function=len,
    )
    docs = []
    for filename in filenames:
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(filename)
        else:
            loader = TextLoader(filename)
        documents = loader.load()
        splits = text_splitter.split_documents(documents)
        docs.extend(splits)
        print(f"Split {filename} into {len(splits)} chunks")
    return docs


def load_code_chunks(chunks, filepath):
    text_splitter = CharacterTextSplitter(chunk_size=1500, separator="\n")
    docs, metadatas = [], []
    for chunk in chunks:
        splits = text_splitter.split_text(chunk)
        docs.extend(splits)
        metadatas.extend([{"source": filepath}] * len(splits))
    print(f"Split {filepath} into {len(docs)} pieces")
    return docs, metadatas