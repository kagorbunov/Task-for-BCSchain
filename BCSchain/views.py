from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import DetailView

from .models import InfBlock


def table(request):
    Block = InfBlock.objects.all()
    paginator = Paginator(Block, 50)

    table_number = request.GET.get('page')
    page_obj = paginator.get_page(table_number)

    return render(request, 'BCSchain/table.html', {'bk': page_obj})


def OneBlocks(request, OneBlock_height):
    OneBlock = InfBlock.objects.get(block_height=OneBlock_height)

    return render(request, 'BCSchain/block_detail.html', {'bk': OneBlock})
