from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from core.models.chunk import DocumentChunk


class BaseVectorStore(ABC):
    @abstractmethod
    async def store_embeddings(self, chunks: List[DocumentChunk]) -> Tuple[bool, List[str]]:
        """Store document chunks and their embeddings"""
        pass

    @abstractmethod
    async def query_similar(
        self,
        query_embedding: List[float],
        k: int,
        doc_ids: Optional[List[str]] = None,
    ) -> List[DocumentChunk]:
        """Find similar chunks"""
        pass
    
    @abstractmethod
    async def count_number_of_chunks(self, external_id: str) -> int:
        """Count the number of chunks for a given document"""
        pass
    
    @abstractmethod
    async def delete_chunks(self, external_id: str) -> bool:
        """Delete chunks by document ID"""
        pass
