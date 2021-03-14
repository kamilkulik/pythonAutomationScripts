class UserInputs:
    def __init__(self):
        self.original_extension_msg = 'What extension do you want to change? '
        self.new_extension_msg = 'What extension do you wan change to? '
        self.root_dir_msg = 'Please provide root directory you want checked '

    def input_template(self, user_message):
        return input(user_message)

    def root_dir(self):
        return self.input_template(self.root_dir_msg)

    def original_extension(self):
        return self.input_template(self.original_extension_msg)

    def new_extension(self):
        return self.input_template(self.new_extension_msg)
