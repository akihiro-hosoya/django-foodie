from .models import Pref, Category


def common(request):
    context = {
        'pref_list': Pref.objects.all().order_by('pref'), # 全ての都道府県データ
        'category_list': Category.objects.all().order_by('category_l'), # 全てのカテゴリーデータ
    }
    return context