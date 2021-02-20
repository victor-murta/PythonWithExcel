from openpyxl import Workbook

wb = Workbook()

planilha = wb.worksheets[0]
planilha.title = 'Teste'

planilha['A1'] = 'Victor'
planilha['B1'] = 'Murta'

wb.save("c:/users/vmurt/.vscode/Python/Excel/Testando.xlsx")