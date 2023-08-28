from store.helper import get_or_create_knowledge_from_repo

def get_repo_context(query, vdb):
    matched_docs = vdb.similarity_search(query, k=10)
    output = ""
    for idx, docs in enumerate(matched_docs):
        output += f"Context {idx}:\n"
        output += str(docs)
        output += "\n\n"
    return output


class Store:
    def __init__(self, repo):
            self.vdb = get_or_create_knowledge_from_repo(dir_path=repo.repo_root)

    def get(self, query):
        get_repo_context(query, self.vdb)
        pass


