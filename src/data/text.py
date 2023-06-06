from langchain.text_splitter import CharacterTextSplitter

class TextManager:
    def __init__(self):
        pass

    def get_chunks_from_text(self, text: str) -> list[str]:
        splitter = CharacterTextSplitter(
            separator="\n", chunk_size=512, chunk_overlap=200, length_function=len)
        return splitter.split_text(text)