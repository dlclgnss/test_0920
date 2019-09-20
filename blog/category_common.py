from .models import Category    

def common(request):
    #テンプレートに毎回渡すデータ
    context = {
        'category_list' : Category.objects.all(),
    }

    return context

    #setting에 templates에 저장해줘야 한다.