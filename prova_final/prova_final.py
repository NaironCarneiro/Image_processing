import cv2
count1 = 0
count2=0 
count3=0
count4=0
counter=0
menCount = 0
womenCount = 0

detections = [(0,0)]
detectionsAge = [(0,0)]
detectionsGender = [(0,0)]

def countAge(x,y, g, list):
    lm, ln = detectionsAge[-1] # identifica se é a mesma pessoa na imagem
    m = abs(lm-x)
    n = abs(ln-y)
    i = 10  # verifica a quantidade de x e y se moveu

    if (m<i or n<i):
        detectionsAge[-1] = (x, y)  
    else:
        detectionsAge.append((x, y))
        if g == list[0] or g == list[1] or  g == list[2]:
            return 0
        if g == list[3] or g == list[4]:
            return 1
        if g == list[5] or g == list[6]:
            return 2
        if g == list[7]:
            return 3


def countGender(x,y, s, listG):
    lm, ln = detectionsGender[-1] # identifica se é a mesma pessoa na imagem
    m = abs(lm-x)
    n = abs(ln-y)
    i = 10  # verifica a quantidade de x e y se moveu

    if (m<i or n<i):
        detectionsGender[-1] = (x, y)  
    else:
        detectionsGender.append((x, y))
        if s == listG[0]:
            return 0
        if s == listG[1]:
            return 1

def countPeople(x, y):
    lm, ln = detections[-1] # identifica se é a mesma pessoa na imagem
    m = abs(lm-x)
    n = abs(ln-y)
    i = 10  # verifica a quantidade de x e y se moveu

    if (m<i or n<i):
        detections[-1] = (x, y)        
        return 0
    else:
        detections.append((x, y))
        return 1


def resize_image(image):
    image = cv2.resize(image, (640, 400), interpolation=cv2.INTER_AREA)
    return image

face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')
ageProto = "classifiersAgeGender/age_deploy.prototxt"
ageModel = "classifiersAgeGender/age_net.caffemodel"
genderProto = "classifiersAgeGender/gender_deploy.prototxt"
genderModel = "classifiersAgeGender/gender_net.caffemodel"

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList=['(0 - 2 anos)', '(4 - 6 anos)', '(8 - 12 anos)', '(15 - 20 anos)', '(25 - 32 anos)', '(38 - 43 anos)', 
'(48 - 53 anos)', '(60 - 100 anos)']
genderList = ['Homem', 'Mulher']

ageNet = cv2.dnn.readNet(ageModel, ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto)

video = cv2.VideoCapture(0)

while cv2.waitKey(1) < 0:
    hasFrame, frame = video.read()
    if not hasFrame:
        cv2.waitKey()
        break

    img = resize_image(frame)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=19,  minSize=(20,20))
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_color = img[y:y+h, x:x+w]

        blob = cv2.dnn.blobFromImage(roi_color, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)
        genderPreds = genderNet.forward()
        gender = genderList[genderPreds[0].argmax()]

        ageNet.setInput(blob)   
        agePreds = ageNet.forward()
        age = ageList[agePreds[0].argmax()]

        center=(int(w/2), int(h/2)) # calcula o centro da face
        ax, by = center   # recebe as duas coordenadas do centro
        
        counter += countPeople(ax, by) # conta mais uma face encontrada
        n = countGender(ax,by,gender, genderList)
        if n == 0:
            menCount += 1
        if n == 1:
            womenCount =+ 1
            
        a = countAge(ax,by,age,ageList)
        if a == 0:
            count1 += 1
        if a == 1:
            count2 += 1
        if a == 2:
            count3 += 1
        if a == 3:
            count4 += 1
        
        cv2.putText(img, f'{gender}, {age}', (x-30, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 255), 2, cv2.LINE_AA)
        
    cv2.putText(img, f"Quantidade de pessoas: {str(counter)}", (10 , 20), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 2, cv2.LINE_AA) 
    cv2.putText(img, f"Homens: {str(menCount)} Mulheres: {str(womenCount)}", (10 , 40), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, f"Pessoas entre 0 e 12 anos: {str(count1)}", (10 , 60), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, f"Pessoas entre 15 e 32 anos: {str(count2)}", (10 , 80), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 2, cv2.LINE_AA)               
    cv2.putText(img, f"Pessoas entre 38 e 53 anos: {str(count3)}", (10 , 100), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 2, cv2.LINE_AA)               
    cv2.putText(img, f"Pessoas maiores  que 60 anos: {str(count4)}", (10 , 120), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 2, cv2.LINE_AA)               
    cv2.imshow("Detecting age and gender", img)
# print("Quantidade de homens: [ " +str(menCount),"]", "\nQuantidade de mulheres: [ " +str(womenCount),"]")
# print("Pessoas entre 0 e 12 anos : [ " +str(count1),"] \nPessoas entre 15 e 32 anos : [ " +str(count2),
# "] \nPessoas entre 38 e 53 anos : [ " +str(count4),"] \nPessoas maiores que 60 anos : [ " +str(count4),"]")
# print("Total de pessoas no video: [ "+ str(counter),"]")