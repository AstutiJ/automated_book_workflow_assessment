# chromadb_store/versioning.py

import chromadb
from chromadb.utils import embedding_functions
import uuid
from datetime import datetime
import os

# Setup local persistent ChromaDB
DB_DIR = "chroma_db"
COLLECTION_NAME = "chapter_versions"

client = chromadb.Client(chromadb.config.Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory=DB_DIR
))

# Create or get collection
if COLLECTION_NAME not in [c.name for c in client.list_collections()]:
    collection = client.create_collection(name=COLLECTION_NAME)
else:
    collection = client.get_collection(name=COLLECTION_NAME)

# Use sentence-transformer for embeddings
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")


def save_chapter_version(chapter_text, chapter_id="chapter1", version="ai_written", reward=None):
    """
    Stores a versioned chapter into ChromaDB with metadata
    """
    doc_id = f"{chapter_id}_{version}_{str(uuid.uuid4())[:8]}"
    timestamp = datetime.now().isoformat()

    metadata = {
        "chapter_id": chapter_id,
        "version": version,
        "timestamp": timestamp
    }

    if reward is not None:
        metadata["reward"] = reward

    collection.add(
        documents=[chapter_text],
        ids=[doc_id],
        metadatas=[metadata]
    )

    print(f"✅ Saved version: {doc_id} ({version})")


def list_all_versions():
    """
    Prints all stored version metadata
    """
    results = collection.get(include=['metadatas', 'ids'])
    for idx, meta in enumerate(results['metadatas']):
        print(f"{idx+1}. ID: {results['ids'][idx]}, Meta: {meta}")
