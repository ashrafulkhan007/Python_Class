class Customer():
    __customers = []  # List to store all customer objects

    # constructor: constructs objects with values
    def __init__(self, customerName, email, address: dict = None, creditCardInfo: dict = None, accountBalance: float = 0.0) -> None:
        # Default values for address and credit card info
        if address is None:
            address = {
                "Street": "",
                "House Number": "",
                "City": "",
                "State": "",
                "Zip Code": "",
                "Country": ""
            }
        if creditCardInfo is None:
            creditCardInfo = {
                "Type": "",
                "Card Number": "",
                "CVV": "",
                "Expiry": "",
                "Currency": ""
            }
        # Assigning instance variables
        self.__customerName = customerName
        self.__email = email
        self.__address = address
        self.__creditCardInfo = creditCardInfo
        self.__accountBalance = accountBalance

    def signup(self) -> None:
        # Check if the email is already in use
        for customer in Customer.__customers:
            if customer.__email == self.__email:
                raise ValueError("Email already in use.")
        # Add the customer to the list
        Customer.__customers.append(self)
        print("Signup successful!")

    def signin(self, email):
        # Searching for the customer with the provided email
        for customer in Customer.__customers:
            if customer.__email == email:
                print("Signin successful!")
                return customer
        # If no customer found with the provided email
        print("No customer found with the provided email.")
        return None

    def updateProfile(self, newCustomerName=None, newEmail=None, newAddress=None, newCreditCardInfo=None,):
        # Updating profile attributes if new values are provided
        if newCustomerName:
            self.__customerName = newCustomerName
        if newEmail:
            # Checking if the new email is already in use
            for customer in Customer.__customers:
                if customer.__email == newEmail:
                    raise ValueError("Email already in use.")
            self.__email = newEmail
        if newAddress:
            self.__address = newAddress
        if newCreditCardInfo:
            self.__creditCardInfo = newCreditCardInfo
        print("Profile updated successfully!")

    def getCustomerDetails(self):
        print("Name:", self.__customerName)
        print("Email:", self.__email)
        print("Address:", self.__address)
        print("Card Details:", self.__creditCardInfo)
        print("Account Balance:", self.__accountBalance)


# Example
customer1 = Customer(
    customerName="John Doe",
    email="john@example.com",
    address={
        "Street": "123 Main St",
        "House Number": "007",
        "City": "Berlin",
        "State": "Berlin",
        "Zip Code": "12345",
        "Country": "Germany"
    },
    creditCardInfo={
        "Type": "Visa",
        "Card Number": "4111111111111111",
        "CVV": "123",
        "Expiry": "12/25",
        "Currency": "EURO"
    },
    accountBalance=100.0
)
customer1.signup()
customer1.signin("john@example.com")
customer1.getCustomerDetails()

customer1.updateProfile(newCustomerName="John A. Doe", newEmail="john.a.doe@example.com")
customer1.getCustomerDetails()
