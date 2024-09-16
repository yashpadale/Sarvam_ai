I have implemented a Retrieval-Augmented Generation (RAG) system for the NCERT dataset by leveraging BERT to generate embeddings from the text within the NCERT PDF. For the similarity search, I opted to use Facebook AI Similarity Search (FAISS)—a highly efficient open-source library for similarity search in dense vectors—due to its performance and resource efficiency.

Initially, I explored Pinecone for vector storage and search; however, its limited free usage led me to select FAISS as a suitable alternative. The system works by computing the similarity between the user's query and various text chunks extracted from the NCERT documents. FAISS identifies the chunk with the highest similarity based on vector distance, and this most relevant chunk is appended to the user’s prompt.

For inference, instead of using Hugging Face models, I have integrated LM Studio, which serves as a lightweight, resource-efficient, and user-friendly alternative. This approach allows for smoother integration and faster inference, making the overall system both scalable and practical for real-world use cases.
I have used gradio for creating the frontend .
![Screenshot (12)](https://github.com/user-attachments/assets/e773f867-9dc7-4277-80e3-a083752a1ffc)
## This above is the working of the Semantic chunking for Retrieval Augmented Generation task.
####  I am using LM studio in backed to run the Langauge model which is the dolphin from mistral
