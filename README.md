I have implemented a Retrieval-Augmented Generation (RAG) system for the NCERT dataset by leveraging BERT to generate embeddings from the text within the NCERT PDF. For the similarity search, I opted to use Facebook AI Similarity Search (FAISS)—a highly efficient open-source library for similarity search in dense vectors—due to its performance and resource efficiency.

Initially, I explored Pinecone for vector storage and search; however, its limited free usage led me to select FAISS as a suitable alternative. The system works by computing the similarity between the user's query and various text chunks extracted from the NCERT documents. FAISS identifies the chunk with the highest similarity based on vector distance, and this most relevant chunk is appended to the user’s prompt.

For inference, instead of using Hugging Face models, I have integrated LM Studio, which serves as a lightweight, resource-efficient, and user-friendly alternative. This approach allows for smoother integration and faster inference, making the overall system both scalable and practical for real-world use cases.
I have used gradio for creating the frontend .
![Screenshot (12)](https://github.com/user-attachments/assets/e773f867-9dc7-4277-80e3-a083752a1ffc)
## This above is the working of the Semantic chunking for Retrieval Augmented Generation task.
####  I am using LM studio in backed to run the Langauge model which is the dolphin from mistral

### For  deciding whehter for a particular prompt a vector DB needs to be called or not I am going to use classification where there will be two classes - Simple and RAG . If simple is detected no RAG needs to be called and if RAG is detected then we call for the RAG pipeline.


### For this task we can use simple ML models like K-means or naive bayes models but if the model which we have trained gives wrong output it can hamper the quality for our services so I will use a transformer to train the classification model .
## I will use my own code - https://github.com/yashpadale/Transformer_Pytorch which has all necessary code for creating our own custome transformer from scratch .where we can just enter our txt the hyper parameters and we can train our model.
I have limited compuational resources so i have used less data and hyper parameters so i will also test my model for the task with prompts which are similar to ones in the training data which is in the classification.txt.
# The following are the reasons why i am not using a pretrained model for the task - 
#### The pretrained models are trained for complex task than just text classification.
#### The size of the pretrained models is too much if we compare it to the output we are recieving from it.
#### If we quantize small language model for this task  the size is around 100 GB but the performance quality reduces.
#### If we train our own model for this task it will perform well , we know the data it is trained on , the size od the model need not be that high due to simplicity of the task . 


## The action invoking will only be used if the model which classifies whether the vector DB is supposed to be called or not decides that there is no need of vector db then only the action is going to be invoked.
### The actions which I am going to include are as follows - 
###### Email writing- The Language model will write the content to send email to people on my behalf using my email id.
###### Mathematical Calculation- Language models are not always correct at math so the model will just use the python operator for aritmetic calculation and give the correct output.
