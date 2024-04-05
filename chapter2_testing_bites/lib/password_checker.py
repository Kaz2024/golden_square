class PasswordChecker:

    def check(self, password):
        if len(password) >= 8:
            return True
        else:
            raise Exception("Invaild password, must be 8+ characters.")