from mycroft import MycroftSkill, intent_file_handler

class Retail(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_entity_file('item.entity')

    @intent_file_handler('price.intent')
    def handle_price(self, message):
        item=str(message.data.get('item'))

        #TODO customise response
        if type is not None:
            self.speak("price of "+item+" is 30",expect_response=False)
        else:
            self.speak('price')

    @intent_file_handler('product_finder.intent')
    def handle_product_finder_intent(self, message):
        item = str(message.data.get('item'))

        #TODO customise response
        if type is not None:
            self.speak("you can find " + item + " in first floor, 3rd corner", expect_response=False)
        else:
            self.speak('price')

def create_skill():
    return Retail()

