from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']
    from captcha.image import ImageCaptcha
    #Create an instance of ImageCaptcha.
    image_captcha = ImageCaptcha()
    #Call ImageCaptcha.generate_image method to create the image object.
    image = image_captcha.generate_image("231321321321321")

    #If you want to add some noise curve or dots, you can call create_noise_curve or create_noise_dots method.Call 
    ImageCaptcha.write
    image

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [Contribute, ResultsWaitPage, Results]

