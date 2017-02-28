import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition

visual_recognition = VisualRecognition('2016-05-20',api_key='f279b7058ce2af35a49946cfef5d352452c1f34c') #My api
#visual_recognition = VisualRecognition('2016-05-20',api_key='d6106599a7afdca48a99c48e90a8d1c3dc033f32') #Yeshwant Api
def fetchClassification():
    with open(join(dirname(__file__),'C:\\Users\\Kumar\\Desktop\\some wallpapers\\random.jpg'),'rb') as filename:
        return (json.dumps(visual_recognition.classify(images_file=filename,owners='me')))