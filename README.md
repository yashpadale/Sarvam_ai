I have used BERT to get the embeddings of the text in the ncert pdf and used Facebook AI Similarity Search library called  FAISS in short for similarity search in vectors as the pinecone which i explored was not giving any free use so i used the alternative and based on the similarity of the prompt and the different chunks based on the similar vector search using FAISS the chunk with highest similarity is chosen and the the chunk is added to the prompt of the user and given to the Language model , I have used LM studio to inference the language model as it is easy , less resource intensive  and effecient for the use case in place of using hugging face models.

![Screenshot (12)](https://github.com/user-attachments/assets/e773f867-9dc7-4277-80e3-a083752a1ffc)
## This above is the working of the Semantic chunking for Retrieval Augmented Generation task.
####  I am using LM studio in backed to run the Langauge model which is the dolphin from mistral
