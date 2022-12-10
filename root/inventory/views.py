from msilib.schema import ListView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, RedirectView, UpdateView, TemplateView, FormView, View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from inventory.models import Brand, Category, Item, Admin
from .forms import BrandForm, CategoryForm, ItemForm, AdminLogin

class AdminLogin(FormView):
    template_name = "login.html"
    form_class = AdminLogin
    success_url = reverse_lazy("inventory:home")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Admin.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Incorrect username or password"})
        return super().form_valid(form)


class AdminMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/login/")
        return super().dispatch(request, *args, **kwargs)



class HomeView(AdminMixin, TemplateView):
    template_name = "index.html"


class AddMixin(AdminMixin, CreateView):
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ItemListView(AdminMixin, ListView):
    template_name = "item_list.html"
    queryset = Item.objects.all()
    paginate_by = 6


class AddItemView(AddMixin):
    template_name = "add_item.html"
    form_class = ItemForm
    success_url = reverse_lazy("inventory:item_list")


class DeleteItemView(AdminMixin, RedirectView):
    template_name = "item_list.html"
    model = Item
    url = "/item-list"

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Item.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs) 


class UpdateItemView(AdminMixin, UpdateView):
    template_name = "add_item.html"
    success_url = reverse_lazy("inventory:item_list")
    queryset = Item.objects.all()
    fields = '__all__'

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Item, id=_id)     


class CategoryListView(AdminMixin, ListView):
    template_name = "category_list.html"
    queryset = Category.objects.all()
    paginate_by = 6


class AddCategoryView(AddMixin):
    template_name = "add_category.html"
    form_class = CategoryForm
    success_url = reverse_lazy("inventory:category_list")


class ValidateCategoryView(View):
    def validate_name(request):
        name = request.GET.get('name', None)
        data = {
            'is_taken': Category.objects.filter(name__iexact=name).exists()
        }
        if data['is_taken']:
            data['error_message'] = 'A user with this username already exists.'
        return JsonResponse(data)


class DeleteCategoryView(AdminMixin, RedirectView):
    template_name = "category_list.html"
    model = Category
    url = "/category-list"

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Category.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


class UpdateCategoryView(AdminMixin, UpdateView):
    template_name = "add_category.html"
    success_url = reverse_lazy("inventory:category_list")
    queryset = Category.objects.all()
    fields = '__all__'

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Category, id=_id) 


class BrandListView(AdminMixin, ListView):
    template_name = "brand_list.html"
    queryset = Brand.objects.all()
    paginate_by = 9


class AddBrandView(AddMixin):
    template_name = "add_brand.html"
    form_class = BrandForm
    success_url = reverse_lazy("inventory:brand_list")


class DeleteBrandView(AdminMixin, RedirectView):
    template_name = "brand_list.html"
    model = Brand
    url = "/brand-list"

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Brand.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


class UpdateBrandView(AdminMixin, UpdateView):
    template_name = "add_brand.html"
    success_url = reverse_lazy("inventory:brand_list")
    queryset = Brand.objects.all()
    fields = '__all__'

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Brand, id=_id) 


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")


    