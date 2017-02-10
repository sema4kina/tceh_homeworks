class Printer(object):
	def log(*values):
		for i in values:
		print(i)

class FormattedPrinter(object):             # Здесь можно бы было пойти через наследование, но подумала, что незачем... Зря, наверно
    def log(*values):
        for i in values:
            print((10 * '*') + str(i) + (10 * '*'))

Printer.log(1, 3, 5, 'sf')
FormattedPrinter.log(1, 3, 5, 'sf')
