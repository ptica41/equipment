from django.http import HttpResponse
import openpyxl
import decimal
import os
import models
import repository
import utils
from order_804 import equipment_order_804


def parse(file_path: str) -> list[models.Item]:
    """Сбор данных с файла"""
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active
    image_loader = utils.SheetImageLoader(ws)
    data = []

    for row in ws.iter_rows(min_row=8):
        if all([not column.value for column in row[1:]]):
            continue
        name_provider = utils.get_value_from_merged_cell(ws, row[1])
        nums = utils.get_value_from_merged_cell(ws, row[6])
        if not nums:
            # ЗАГЛУШКА ДЛЯ ТЕСТОВ БЕЗ КОЛОНКИ ПРИКАЗА 804
            nums = ['1.1.1']
        else:
            nums = nums.split(';')
        image = utils.get_value_from_merged_image(ws, image_loader, row[2])
        for num in nums:
            data.append(
                models.Item(
                    num=num.strip(),
                    name_804=equipment_order_804.get(num.strip()),
                    provider='СВЕТОЧ',
                    article=utils.get_value_from_merged_cell(ws, row[3]),
                    img=image,
                    name_provider=name_provider,
                    size=utils.get_value_from_merged_cell(ws, row[4]),
                    cost=decimal.Decimal(str(utils.get_value_from_merged_cell(ws, row[5]))),
                )
            )
    return data


def parse_view(request):
    file_path = utils.get_xlsx_file(os.getcwd() + '/SVETOCH')
    repository.ItemsRepository.delete_provider(provider='СВЕТОЧ')
    items = parse(file_path)
    map(repository.ItemsRepository.create, items)

    return HttpResponse('OK')

