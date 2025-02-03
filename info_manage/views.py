from django.shortcuts import render, redirect
from .models import CarModel, HotModel, OrderModel, ItemModel, CategoryModel, UserInfoModel, CommentModel, ItemImageModel
from django.http import JsonResponse


def index(request):
    hots = HotModel.objects.all()
    categories = CategoryModel.objects.all()
    context = {
        'hots': hots,
        'categories': categories
    }
    return render(request, 'index.html', context=context)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 用户登录
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not (username or password):
            return JsonResponse({'code': 400, 'message': '缺少必传的参数'})
        user = UserInfoModel.objects.filter(username=username, password=password).first()
        if not user:
            return JsonResponse({'code': 400, 'message': '账号或密码错误'})
        request.session['login_in'] = True
        request.session['username'] = user.username
        request.session['user_id'] = user.id
        return JsonResponse({'code': 200})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        if not (username or password1 or password2):
            return JsonResponse({'code': 400, 'message': '缺少必传的参数'})

        if password1 != password2:
            return JsonResponse({'code': 400, 'message': '两次输入的密码不一致！'})

        flag = UserInfoModel.objects.filter(username=username).first()
        if flag:
            return JsonResponse({'code': 400, 'message': '该用户名已存在'})
        UserInfoModel.objects.create(
            username=username,
            password=password1,
            address=address,
            phone=phone
        )
        return JsonResponse({'code': 200})


def logout(request):
    # 退出登录
    flag = request.session.clear()
    return redirect('/')


def item_detail(request, item_id):
    if request.method == 'GET':
        # 商品详情界面
        item = ItemModel.objects.filter(
            id=item_id
        ).first()
        comments = CommentModel.objects.filter(
            item_id=item_id
        )
        additional_images = ItemImageModel.objects.filter(
            item_id=item_id
        ).order_by('create_time')
        context = {
            'item': item,
            'comments': comments,
            'additional_images': additional_images
        }
        return render(request, 'item_detail.html', context=context)


def item_list(request, category_id):
    if request.method == 'GET':
        # 商品列表
        items = ItemModel.objects.filter(
            category_id=category_id
        )
        context = {
            'items': items
        }
        return render(request, 'item_list.html', context=context)


def add_car(request):
    if request.method == 'POST':
        # 加入购物车
        item_id = request.POST.get('item_id')
        size = request.POST.get('size')
        number = request.POST.get('number', '1')
        user_id = request.session.get('user_id')
        item = ItemModel.objects.filter(
            id=item_id
        ).first()
        
        # 如果size为空，使用商品的默认尺码
        if not size:
            size = item.size
        
        # 检查库存
            
        CarModel.objects.create(
            item_id=item_id,
            user_id=user_id,
            price=item.price,
            size=size,
        )
        return JsonResponse({'code': 200})


def add_order(request):
    if request.method == 'POST':
        # 商品购买，生成订单
        # import pdb;pdb.set_trace()
        item_id = request.POST.get('item_id')
        size = request.POST.get('size')
        number = request.POST.get('number', '1')
        user_id = request.session.get('user_id')
        car_id = request.POST.get('car_id')
        
        item = ItemModel.objects.filter(
            id=item_id
        ).first()
        

            
        user = UserInfoModel.objects.filter(
            id=user_id
        ).first()
        total_price = item.price 

        # 如果是从购物车购买，获取购物车中的尺码
        if car_id:
            car = CarModel.objects.filter(id=car_id).first()
            size = car.size if car else size

        OrderModel.objects.create(
            item_id=item_id,
            user_id=user_id,
            price=total_price,
            size=size,
        )

        item.save()

        if car_id:
            # 如果是从购物车中点击购买的
            CarModel.objects.filter(
                id=car_id
            ).update(
                is_pay=True
            )
        return JsonResponse({'code': 200})


def my_car(request):
    user_id = request.session.get('user_id')
    if request.method == 'GET':
        # 我的购物车
        cars = CarModel.objects.filter(
            user_id=user_id,
            is_pay=False
        )
        context = {
            'cars': cars
        }
        return render(request, 'my_car.html', context=context)
    else:
        # 删除购物车
        car_id = request.POST.get('car_id')
        CarModel.objects.filter(
            id=car_id
        ).first().delete()
        return JsonResponse({'code': 200})


def my_order(request):
    user_id = request.session.get('user_id')
    if request.method == 'GET':
        # 我的订单
        orders = OrderModel.objects.filter(
            user_id=user_id
        )
        context = {
            'orders': orders
        }
        return render(request, 'my_order.html', context=context)
    else:
        # 删除订单
        order_id = request.POST.get('order_id')
        OrderModel.objects.filter(
            id=order_id
        ).first().delete()
        return JsonResponse({'code': 200})


def my_info(request):
    user_id = request.session.get('user_id')
    if request.method == 'GET':
        # 个人信息界面
        info = UserInfoModel.objects.filter(
            id=user_id
        ).first()
        context = {
            'info': info
        }
        return render(request, 'my_info.html', context=context)
    else:
        # 更新个人信息
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        if not (username or password or phone or address):
            return JsonResponse({'code': 400, 'message': '参数不能为空'})

        UserInfoModel.objects.filter(
            id=user_id
        ).update(
            username=username,
            password=password,
            phone=phone,
            address=address
        )
        return JsonResponse({'code': 200})


def category_count(request):
    if request.method == 'GET':
        categories = CategoryModel.objects.all()
        result = []
        for category in categories:
            items = ItemModel.objects.filter(category=category)
            result.append({
                'value': len(items),
                'name': category.name
            })
        return JsonResponse({'code': 200, 'data': result})


def add_comment(request):
    # 添加评论
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'code': 400, 'message': '请先登录'})
    content = request.POST.get('content')
    item_id = request.POST.get('item_id')
    if not content:
        return JsonResponse({'code': 400, 'message': '内容不能为空'})

    CommentModel.objects.create(
        user_id=user_id,
        content=content,
        item_id=item_id
    )
    return JsonResponse({'code': 200})


def search_items(request):
    query = request.GET.get('query', '')
    if query:
        items = ItemModel.objects.filter(name__icontains=query)
    else:
        items = ItemModel.objects.none()
    
    context = {
        'items': items,
        'query': query,
        'categories': CategoryModel.objects.all()
    }
    return render(request, 'search_results.html', context)
