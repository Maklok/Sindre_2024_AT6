class UserInputValidator:

    def __init__(self):
        pass


    def validate_positive_integers(self, item): 
    
        item_list = []
        for x in item:
            if x.isdigit() and int(x) > 0:
                item_list.append(int(x))
    
        return item_list

    def validate_message(self, item):

        valid_item = self.validate_positive_integers(item)
        print(f'Validation complete! Valid integers: {valid_item}')









validator = UserInputValidator()
Y_integer = ["58", "12", "Hello", "House", "46"]
validator.validate_message(Y_integer)