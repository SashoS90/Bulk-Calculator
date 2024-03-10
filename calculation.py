class Calculator:
    def __init__(self, data: str):
        self.data = data
        self.currency = None

    def cleaning_data(self):
        cleaned_data = []

        for element in self.data:
            if element not in ['$', '£']:
                if element == 'x':
                    cleaned_data.append('*')
                else:
                    cleaned_data.append(element)

        return ''.join(cleaned_data)

    def calculating(self):
        data = self.cleaning_data()

        try:
            result = eval(data)
            rounded_result = f"{round(result, 2):.2f}"
        except Exception as e:
            rounded_result = f"NaN"

        return f"{rounded_result}"
