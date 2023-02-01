import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(text):
    translation = language_translator.translate(
        text= text,
        model_id= "en-fr").get_result()
    jsonTranslation = json.dumps(translation,indent=2, ensure_ascii=False)
    return translation["translations"][0]["translation"]

def frenchToEnglish(text):
    translation = language_translator.translate(
        text= text,
        model_id= "fr-en").get_result()
    jsonTranslation = json.dumps(translation,indent=2, ensure_ascii=False)
    return translation["translations"][0]["translation"]


frenchToEnglish("bonjour")