import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
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

def english_to_french(text):
    '''
        Translate from english to french
    '''
    translation = language_translator.translate(
        text= text,
        model_id= "en-fr").get_result()
    return translation["translations"][0]["translation"]

def french_to_english(text):
    '''
        Translate from french to english 
    '''
    translation = language_translator.translate(
        text= text,
        model_id= "fr-en").get_result()
    return translation["translations"][0]["translation"]
    