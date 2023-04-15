import docx2txt

job_des=docx2txt.process(r"C:\Users\HP\Desktop\PYTHON\Job description.docx")

resume=docx2txt.process(r"C:\Users\HP\Desktop\PYTHON\Tulika_Chatterjee_Resume.docx")

content= [job_des,resume]
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
matrix=cv.fit_transform(content)
from sklearn.metrics.pairwise import cosine_similarity
similarity_matrix=cosine_similarity(matrix)

print("Resume matches by "+str(similarity_matrix[1][0] *100)+"%")