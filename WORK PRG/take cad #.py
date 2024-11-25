import openpyxl
import re

# Путь к файлу Excel
file_path = '/Users/vetvy/Desktop/L I S T # 4 - B R E S.xlsx'
# Имя листа и имя столбца для обработки
sheet_name = '- L I S T -'
source_column_letter = 'T'
destination_column_letter = 'AI'


# Обновленное регулярное выражение для поиска кадастрового номера
cadastral_pattern = r'(\d{2}:\d{2}:\d{6}:\d{1,5})'

# Открываем файл Excel
workbook = openpyxl.load_workbook(file_path)
sheet = workbook[sheet_name]

# Проходим по всем ячейкам в заданном столбце
for row in range(1, sheet.max_row + 1):
    cell = sheet[f'{source_column_letter}{row}']
    if cell.value:
        # Поиск всех совпадений в строке
        matches = re.findall(cadastral_pattern, cell.value)
        if matches:
            # Записываем найденные кадастровые номера в указанный столбец
            sheet[f'{destination_column_letter}{row}'] = ', '.join(matches)
        else:
            # Если не найдено, попробуем удалить пробелы и проверить снова
            cleaned_value = re.sub(r'\s+', '', cell.value)
            matches = re.findall(cadastral_pattern, cleaned_value)
            if matches:
                sheet[f'{destination_column_letter}{row}'] = ', '.join(matches)

# Сохраняем изменения в файл
workbook.save(file_path)

print("Кадастровые номера сохранены в столбец", destination_column_letter)